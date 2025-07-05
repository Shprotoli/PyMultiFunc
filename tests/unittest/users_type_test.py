from unittest import TestCase
from py_multi_func.override import overload


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
