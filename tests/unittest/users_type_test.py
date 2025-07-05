from unittest import TestCase
from py_multi_func.override import overload


class B:
    ...


class A:
    ...


@overload()
def test_eq_type_foo(a: A):
    return type(a).__name__


@overload()
def test_eq_type_foo(a: B):
    return type(a).__name__


@overload()
def test_nq_type_foo(a: A, b: B):
    return (type(a).__name__, type(b).__name__)


@overload()
def test_nq_type_foo(a: A, b: A):
    return (type(a).__name__, type(b).__name__)


class UsersTypeTest(TestCase):
    """
    Тесты проверяющие пользовательские типы данных
    """

    @classmethod
    def setUpClass(cls):
        cls.B_class = B()
        cls.A_class = A()

    def test_eq_type(self):
        result_1 = test_eq_type_foo(self.A_class)
        self.assertEqual(result_1, "A")

        result_2 = test_eq_type_foo(self.B_class)
        self.assertEqual(result_2, "B")

    def test_nq_type(self):
        result_1 = test_nq_type_foo(self.A_class, self.B_class)
        self.assertEqual(result_1, ("A", "B"))

        result_2 = test_nq_type_foo(self.A_class, self.A_class)
        self.assertEqual(result_2, ("A", "A"))


class Parent:
    ...


class Children(Parent):
    ...


@overload()
def test_inheritance_foo(a: Parent):
    return type(a).__name__


class InheritanceTypeTest(TestCase):
    def test_inheritance(self):
        result_1 = test_inheritance_foo(Parent())
        self.assertEqual(result_1, "Parent")

        result_2 = test_inheritance_foo(Children())
        self.assertEqual(result_2, "Children")


class Parent:
    ...


class Children(Parent):
    ...


@overload()
def test_analyz_foo(a: Parent):
    return type(a).__name__


@overload()
def test_analyz_foo(a: Children):
    return type(a).__name__


class CurrectAnalyzTypeTest(TestCase):
    def test_analyz(self):
        result_1 = test_analyz_foo(Parent())
        self.assertEqual(result_1, "Parent")

        result_1 = test_analyz_foo(Children())
        self.assertEqual(result_1, "Children")