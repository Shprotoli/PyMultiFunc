from unittest import TestCase
from py_multi_func.override import overload


@overload()
def test_eq_types_foo(a: int, b: int):
    return (type(a).__name__, type(b).__name__)


@overload()
def test_eq_types_foo(a: bool, b: bool):
    return (type(a).__name__, type(b).__name__)


@overload()
def test_eq_types_foo(a: str, b: str):
    return (type(a).__name__, type(b).__name__)


@overload()
def test_nq_types_foo(a: int, b: str):
    return (type(a).__name__, type(b).__name__)


@overload()
def test_nq_types_foo(a: int, b: float):
    return (type(a).__name__, type(b).__name__)


@overload()
def test_nq_types_foo(a: bool, b: float):
    return (type(a).__name__, type(b).__name__)


class SimpleTypeTest(TestCase):
    """
    Тест проверяющий перегрузку класса с простыми типами данных
    """

    def test_eq_types(self):
        result_1 = test_eq_types_foo(5, 5)
        self.assertEqual(result_1, ("int", "int"))

        result_2 = test_eq_types_foo(False, True)
        self.assertEqual(result_2, ("bool", "bool"))

        result_3 = test_eq_types_foo("shprot", "oil")
        self.assertEqual(result_3, ("str", "str"))

    def test_nq_types(self):
        result_1 = test_nq_types_foo(5, "string")
        self.assertEqual(result_1, ("int", "str"))

        result_2 = test_nq_types_foo(5, 5.5)
        self.assertEqual(result_2, ("int", "float"))

        result_3 = test_nq_types_foo(False, 5.5)
        self.assertEqual(result_3, ("bool", "float"))


@overload()
def test_eq_types_foo(a: list):
    return type(a).__name__


@overload()
def test_eq_types_foo(a: dict):
    return type(a).__name__


@overload()
def test_eq_types_foo(a: tuple):
    return type(a).__name__


@overload()
def test_nq_types_foo(a: list, b: dict):
    return (type(a).__name__, type(b).__name__)


@overload()
def test_nq_types_foo(a: list, b: list):
    return (type(a).__name__, type(b).__name__)

class ContainersTypeTest(TestCase):
    """
    Тесты проверяющие перегрузку типов для контейнеров
    """

    def test_eq_types(self):
        result_1 = test_eq_types_foo([])
        self.assertEqual(result_1, "list")

        result_2 = test_eq_types_foo({})
        self.assertEqual(result_2, "dict")

        result_3 = test_eq_types_foo(())
        self.assertEqual(result_3, "tuple")

    def test_nq_types(self):
        result_1 = test_nq_types_foo(list(), dict())
        self.assertEqual(result_1, ("list", "dict"))

        result_2 = test_nq_types_foo(list(), list())
        self.assertEqual(result_2, ("list", "list"))
