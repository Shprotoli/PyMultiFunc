from unittest import TestCase
from py_multi_func.override import overload


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
        result_1 = self.A_class.foo("str")
        self.assertEqual(result_1, "A str")

        result_2 = self.B_class.foo("str")
        self.assertEqual(result_2, "B str")

        result_3 = self.A_class.foo(5)
        self.assertEqual(result_3, "A int")

        result_4 = self.B_class.foo(5)
        self.assertEqual(result_4, "B int")


class WrapB:
    @overload()
    def __init__(self: "WrapB", a: int):
        ...

    @overload()
    def __init__(self: "WrapB", a: str):
        ...


class WrapA:
    @overload()
    def __init__(self: "WrapA", a: int):
        ...

    @overload()
    def __init__(self: "WrapA", a: str):
        ...


@overload()
def test_wrapper_print(obj: WrapA):
    return type(obj).__name__


@overload()
def test_wrapper_print(obj: WrapB):
    return type(obj).__name__


class WrapperOverloadTest(TestCase):
    """
    Тесты, которые проверяют корректную работу при вложенности
    """

    def test_wrapper(self):
        result_1 = test_wrapper_print(WrapA(5))
        self.assertEqual(result_1, "WrapA")

        result_2 = test_wrapper_print(WrapA("str"))
        self.assertEqual(result_2, "WrapA")

        result_3 = test_wrapper_print(WrapB(5))
        self.assertEqual(result_3, "WrapB")

        result_4 = test_wrapper_print(WrapB("str"))
        self.assertEqual(result_4, "WrapB")
