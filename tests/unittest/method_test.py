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
