Перегрузка методов и функций для Python.

# Как это работает?

Перегрузка PyMultiFunc работает аналогично языкам,с предоставлением перегрузки из "коробки".

Рассмотрим базовый пример:
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

# Анализ наследования

Нужно указать типом абстрактный класс? Пожалйста, простой пример с машинами:
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

# Перегрузка по количеству

Вы также можете перегружать ваши функции по количеству аргументов:
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

# Перегрузка со значениями по умолчанию

Вместо того, чтобы передавать аргумент напрямую, вы можете использовать класс `DEFAULT_ARG`, для использования значения по умолчанию.
> [!IMPORTANT]
> Чтобы класс и его замена на аргумент по умолчанию работал корректно, нужно соблюдать несколько правил:
> 1. В конструктор `DEFAULT_ARG` требуется передать тип, который стоит на месте аргумента со значением по умолчанию
> 2. `DEFAULT_ARG` требует позиционирования в том месте, где у аргумента есть значение по умолчаню, например нельзя делать так!
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
> 3. Инициализированный `DEFAULT_ARG` нельзя передать, из-за специфики работы декоратора, если вам это требуется, то используйте `FAKE_DEFAULT_ARG`, он индентичен `DEFAULT_ARG`, но не заменяется на значение по умолчанию

```python
from py_multi_func.override import overload
from py_multi_func.defaults_arg import DEFAULT_ARG


@overload()
def foo(a: str, b: str = "default"):
    print(a, b)


foo("shprot", "oli")             # shprot oli
foo("this", DEFAULT_ARG(str))    # this default
```
