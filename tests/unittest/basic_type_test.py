from unittest import TestCase
from py_multi_func.override import overload


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

        self.assertEqual(foo(list(), dict()), "(<class 'list'>, <class 'dict'>)")
        self.assertEqual(foo(list(), list()), "(<class 'list'>, <class 'list'>)")
