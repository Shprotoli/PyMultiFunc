from .config import DEFAULT_ARG_TYPE, KEY_LIST_TYPE_FUNC
from .exception import (
    NoDefaultsArgsError,
    NoDefaultValueForThisArgError,
    NoOverideError,
)



def overload(*, __overload_list__: dict = {}):
    def decorate(func):
        # __overload_list__.setdefault(func.__name__, [])
        if not __overload_list__.get(func.__name__):
            __overload_list__[func.__name__] = {}
            __overload_list__[func.__name__][KEY_LIST_TYPE_FUNC] = set()

        """Генерация строки, которая служит, как ключ для вызова нужной функции"""
        informations_arg_func = ""
        list_types_arg_func = []
        for type_arg in func.__annotations__.values():
            if "<class " not in str(type_arg):
                type_arg = f"<class '__multi_func__.{type_arg}'>"
            elif "." in str(type_arg):
                name_class = str(type_arg).split(".")[-1]
                type_arg = f"<class '__multi_func__.{name_class}"
            informations_arg_func += f"({type_arg})"
            list_types_arg_func.append(str(type_arg))

        """Запись нашей функции, в словарь типа: __overload_list__[Название функции][Сгенерированные аргументы]"""
        __overload_list__[func.__name__][informations_arg_func] = func
        __overload_list__[func.__name__][KEY_LIST_TYPE_FUNC].add(tuple(list_types_arg_func))

        def wrapper(*args, **kwargs):
            """Генерация строки, с которая будет является ключем"""
            index_arg_default = []
            informations_arg_func_call = ""

            for index_arg, value_arg in enumerate([*args, *(kwargs.values())]):
                if str(type(value_arg)) == DEFAULT_ARG_TYPE:
                    index_arg_default.append(index_arg)

                type_arg = value_arg.__class__
                if "." in str(type_arg):
                    name_class = str(type_arg).split(".")[-1]
                    type_arg = f"<class '__multi_func__.{name_class}"

                information_arg = f"({type_arg})"
                informations_arg_func_call += information_arg
            # print(informations_arg_func_call)

            """Переменные для хранения аргументов по умолчанию и переданных аргументов"""
            args_for_called_function = [*args, *kwargs.values()]


            """Проверка, что аргументы являются дочерними от требующихся"""
            currect_arg_for_called_function = __overload_list__[func.__name__][KEY_LIST_TYPE_FUNC]

            mro_types_transmitted_type = [type(arg).__mro__ for arg in args_for_called_function]
            mro_types_transmitted_type_string = [str(arg) for arg in mro_types_transmitted_type]

            name_file = str(mro_types_transmitted_type[0][0])[8:].split(".")[0]

            for currect_type in currect_arg_for_called_function:
                for index_type, need_type in enumerate(currect_type):
                    need_type_with_currect_name_file = need_type.replace("__multi_func__", name_file)

                    if len(mro_types_transmitted_type_string) <= index_type:
                        break
                    if not (need_type_with_currect_name_file in mro_types_transmitted_type_string[index_type]):
                        break
                else:
                    informations_arg_func_call = "".join(list(map(lambda arg: f"({arg})", currect_type)))
                    break

            if not __overload_list__[func.__name__].get(informations_arg_func_call):
                raise NoOverideError("You are trying to cause an overload that does not exist")
            called_function = __overload_list__[func.__name__][informations_arg_func_call]

            if not called_function.__defaults__ and index_arg_default:
                raise NoDefaultsArgsError(
                    "You are trying to pass (DEFAULT_ARG) although the function has no default arguments."
                )

            if called_function.__defaults__ and index_arg_default:
                default_args_for_called_function = (*(index_arg_default[0] * [None]), *called_function.__defaults__)
                if called_function.__code__.co_argcount != len(default_args_for_called_function):
                    error_default_arg = called_function.__code__.co_varnames[index_arg_default[0]]
                    raise NoDefaultValueForThisArgError(
                        f"The argument [{error_default_arg}] marked as (DEFAULT_ARG) does not have a default value."
                    )

                """Цикл замены аргументов DEFAULT_ARG на указанные дефолтные"""
                for index_arg, value_arg in enumerate(args_for_called_function):
                    if str(type(value_arg)) == DEFAULT_ARG_TYPE:
                        args_for_called_function[index_arg] = default_args_for_called_function[index_arg]

            return called_function(*args_for_called_function)
        return wrapper
    return decorate