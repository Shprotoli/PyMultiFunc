from unittest import TestCase, main

from ..override import overload

class SimpleTypeTest(TestCase):
    """
    Тест проверяющий перегрузку класса с простыми типами данных
    """
    def test_eq_types(self):
        @overload()
        def foo(a: int, b: int):
            return f"({type(a)}, {type(b)})"

        @overload()
        def foo(a: bool, b: bool):
            return f"({type(a)}, {type(b)})"

        @overload()
        def foo(a: str, b: str):
            return f"({type(a)}, {type(b)})"

        self.assertEqual(foo(5, 5), "(<class 'int'>, <class 'int'>)")
        self.assertEqual(foo(False, True), "(<class 'bool'>, <class 'bool'>)")
        self.assertEqual(foo("shprot", "oil"), "(<class 'str'>, <class 'str'>)")


    def test_nq_types(self):
        @overload()
        def foo(a: int, b: str):
            return f"({type(a)}, {type(b)})"

        @overload()
        def foo(a: int, b: float):
            return f"({type(a)}, {type(b)})"

        @overload()
        def foo(a: bool, b: float):
            return f"({type(a)}, {type(b)})"

        self.assertEqual(foo(5, "string"), "(<class 'int'>, <class 'str'>)")
        self.assertEqual(foo(5, 5.5), "(<class 'int'>, <class 'float'>)")
        self.assertEqual(foo(False, 5.5), "(<class 'bool'>, <class 'float'>)")

class ContainersTypeTest(TestCase):
    """
    Тесты проверяющие перегрузку типов для контейнеров
    """
    def test_eq_types(self):
        @overload()
        def foo(a: list):
            return f"({type(a)})"

        @overload()
        def foo(a: dict):
            return f"({type(a)})"

        @overload()
        def foo(a: tuple):
            return f"({type(a)})"

        self.assertEqual(foo([]), "(<class 'list'>)")
        self.assertEqual(foo({}), "(<class 'dict'>)")
        self.assertEqual(foo(()), "(<class 'tuple'>)")


    def test_nq_types(self):
        @overload()
        def foo(a: list, b: dict):
            return f"({type(a)}, {type(b)})"

        @overload()
        def foo(a: list, b: list):
            return f"({type(a)}, {type(b)})"

        self.assertEqual(foo([], {}), "(<class 'list'>, <class 'dict'>)")
        self.assertEqual(foo([], []), "(<class 'list'>, <class 'list'>)")




# ============================================================================================================================

class B:
    ...

class A:
    ...

class UsersTypeTest(TestCase):
    """
    Тесты проверяющие пользовательские типы данных
    """
    @classmethod
    def setUpClass(cls):
        cls.B_class = B()
        cls.A_class = A()


    def test_eq_type(self):
        @overload()
        def foo(a: A):
            return A.__name__

        @overload()
        def foo(a: B):
            return B.__name__

        self.assertEqual(foo(self.A_class), "A")
        self.assertEqual(foo(self.B_class), "B")

    def test_nq_type(self):
        @overload()
        def foo(a: A, b: B):
            return (A.__name__, B.__name__)

        @overload()
        def foo(a: A, b: A):
            return (A.__name__, A.__name__)

        self.assertEqual(foo(self.A_class, self.B_class), ("A", "B"))
        self.assertEqual(foo(self.A_class, self.A_class), ("A", "A"))

class B:
    @overload()
    def foo(self: "B", a: int):
        return "B int"

    @overload()
    def foo(self: "B", a: str):
        return "B str"

class A:
    @overload()
    def foo(self: "A", a: int):
        return "A int"

    @overload()
    def foo(self: "A", a: str):
        return "A str"

class MethodOverloadTest(TestCase):
    """
    Тесты, которые перегружают методы класса
    """
    @classmethod
    def setUpClass(cls):
        cls.B_class = B()
        cls.A_class = A()

    def test_currect_find(self):
        self.assertEqual(self.A_class.foo("str"), "A str")
        self.assertEqual(self.B_class.foo("str"), "B str")
        self.assertEqual(self.A_class.foo(5), "A int")
        self.assertEqual(self.B_class.foo(5), "B int")

class WrapB:
    @overload()
    def __init__(self: "WrapB", a: int):
        print("B int")

    @overload()
    def __init__(self: "WrapB", a: str):
        print("B str")

class WrapA:
    @overload()
    def __init__(self: "WrapA", a: int):
        print("A int")

    @overload()
    def __init__(self: "WrapA", a: str):
        print("A str")

class WrapperOverloadTest(TestCase):
    """
    Тесты, которые проверяют корректную работу при вложенности
    """
    def test_wrapper(self):
        @overload()
        def print(obj: WrapA):
            return "print A"

        @overload()
        def print(obj: WrapB):
            return "print B"

        self.assertEqual(print(WrapA(5)), "print A")
        self.assertEqual(print(WrapA("str")), "print A")
        self.assertEqual(print(WrapB(5)), "print B")
        self.assertEqual(print(WrapB("str")), "print B")

if __name__ == '__main__':
    main()