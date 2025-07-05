# [PyMultiFunc – Your Assistant for Function Overloading](https://github.com/Shprotoli/PyMultiFunc)

Method and Function Overloading in Python

# How Does It Work? (🇺🇸)

PyMultiFunc overloading works similarly to languages that provide overloading "out of the box".

Let’s look at a basic example:
```python
from py_multi_func.override import overload

@overload()
def foo(a: int):
    print("called func `int`")

@overload()
def foo(a: str):
    print("called func `str`")

foo(5)      # called func `int`
foo("str")  # called func `str`
```



### Inheritance Analysis

Do we need to specify the type as an abstract class?
Here’s a simple example with cars:
```python
from py_multi_func.override import overload
from abc import ABC


class Car(ABC):
    """Somethink code for car class..."""
    ...


class BMW(Car):
    """I think it could be I8"""
    ...


class Tesla(Car):
    """Tesla Roa..., no Tesla X, yes, of course X"""
    ...


class Lada(Car):
    """I don't care which model is going to be here."""
    ...


@overload()
def foo(car: Car):
    print("called with `Car` or children `Car`")


@overload()
def foo(car: BMW):
    print("called with `BMW`")


@overload()
def foo(car: Tesla):
    print("called with `Tesla`")


foo(Lada())     # called with `Car` or children `Car`
foo(BMW())      # called with `BMW`
foo(Tesla())    # called with `Tesla`
```



### Overloading by Number of Arguments

You can also overload your functions based on the number of arguments:
```python
from py_multi_func.override import overload


@overload()
def foo(a: int):
    print("a = int")


@overload()
def foo(a: int, b: int):
    print("a = int, b = int")


foo(5)        # a = int
foo(5, 5)     # a = int, b = int
```



### Overloading with Default Values

Instead of passing an argument directly, you can use the `DEFAULT_ARG` class to represent a default value.
> [!WARNING]
> To ensure the class and its replacement as a default argument work correctly, you must follow several rules:
> 1. The constructor of `DEFAULT_ARG` must be given the type that corresponds to the argument with the default value.
> 2. `DEFAULT_ARG` must be positioned exactly where the argument has a default value — for example, you cannot do this:
> ```python
> from py_multi_func.override import overload
> from py_multi_func.defaults_arg import DEFAULT_ARG
>
>
> @overload()
> def foo(a: str, b: str = "default"):
>     print(a, b)
>
> 
> # NoDefaultValueForThisArgError: The argument [a] marked as (DEFAULT_ARG) does not have a default value.
> # A good error that tells you where the `DEFAULT_ARG` is passed incorrectly
> foo(DEFAULT_ARG(str), "somethink") 
> ```
> 3. An initialized `DEFAULT_ARG` cannot be passed due to the specifics of how the decorator works.
> If you need to pass such a value explicitly, use `FAKE_DEFAULT_ARG` instead — it is identical to `DEFAULT_ARG`, but it is not replaced with the default value.

```python
from py_multi_func.override import overload
from py_multi_func.defaults_arg import DEFAULT_ARG


@overload()
def foo(a: str, b: str = "default"):
    print(a, b)


foo("shprot", "oli")             # shprot oli
foo("this", DEFAULT_ARG(str))    # this default
```


# Brief Overview of the Project Structure
> [!NOTE]
> - [📄(🐍)] `override.py` - Contains the main logic of the decorato
> - [📄(🐍)] `exception.py` - Contains all exceptions that may occur when working with PyMultiFunc
> - [📄(🐍)] `config.py` - Contains constants and other static arguments for analysis during decorator execution
> - [📄(🐍)] `defaults_arg.py` - Contains classes (`DEFAULT_ARG` and others) that provide access to overriding arguments with default values
> - [📁] `tests` - Contains tests for the decorator
> - └── [📁] `unittest` - Unittest for decorater
