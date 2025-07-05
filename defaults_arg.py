class DEFAULT_ARG:
    """
    Класс-заглушка, который требуется для того, чтобы в функции был использован аргумент по умолчанию,
    а не тот, который был передан
    """
    def __init__(self, type):
        self.__type__ = type

    def __getattribute__(self, name):
        if name == "__class__":
            return self.__type__
        return object.__getattribute__(self, name)

class FAKE_DEFAULT_ARG:
    """
    Класс-заглушка, который индентичен классу `DEFUALT_ARG`,
    но его можно передавать в качестве аргумента без получения ошибки,
    также данный аргумент не будет заменен на дефолтный из вашей функции
    """
    def __init__(self, type):
        self.__type__ = type
        self.__defualt_arg__ = None

    def __getattribute__(self, name):
        if name == "__class__":
            return self.__type__
        return object.__getattribute__(self, name)

    def get_defualt_arg(self) -> DEFAULT_ARG:
        if not self.__defualt_arg__:
            self.__defualt_arg__ = DEFAULT_ARG(self.__type__)
        return self.__defualt_arg__