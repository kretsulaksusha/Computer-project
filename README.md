# Recreated itertools library

## Functions:
- ### count()
Description: Count from a `number` by `step` forever

In an infinite loop yield `number` and increase it by 1

Made by: Natalia
```python
def count(firstval: int | float = 0, step: int | float = 1):
    number = firstval
    while True:
        yield number
        number += step
```

- ### cycle()
Description: Cycle through an iterable forever

Infinitely cycle through a list, tuple, string or anything else iterable

Made by: Sviatoslav
```python
def cycle(iterable):
    index = 0
    while 1:
        yield iterable[index]
        index += 1
        if index >= len(iterable):
            index -= len(iterable)
```

- ### repeat()
Description: Return value forever

Repeatedly yield the same value

Made by: Yulia
```python
def repeat(value):
    while True:
        yield value
```

- ### product()
Description: Generate a cartesian product of input iterables

Get a cartesian product of some iterables

Made by: Radomyr
```python
def product(*iterables):
    if len(iterables) == 0:
        yield ()
    if len(iterables) == 1:
        for element in iterables[0]:
            yield (element,)
    if len(iterables) > 1:
        for element in iterables[0]:
            for element2 in product(*iterables[1:]):
                yield (element, *element2)
```

- ### permutations()
Description: Generate all permutations of length `number` of elements in `iterable`

Get permutations of an iterable of length `number`

Made by: Sviatoslav
Helped: Ksenia, Radomyr
```python
def permutations(iterable, number: int = None):
    if not hasattr(iterable, "__iter__"):
        raise TypeError(f"'{type(iterable)}' object is not iterable")
    iterable = list(iterable)
    if number is None:
        number = len(iterable)
    if number < 0:
        raise ValueError("r must be non-negative")
    if number > len(iterable):
        return None
    history = set()

    to_compare = list(range(len(iterable)))

    yield tuple(iterable[:number])
    history.add(tuple(to_compare[:number]))

    for _ in range(int(factorial(len(iterable)) - 1)):
        n = len(iterable) - 1
        j = n - 1
        while to_compare[j] > to_compare[j + 1]:
            j -= 1
        k = n
        while to_compare[j] > to_compare[k]:
            k -= 1
        iterable[j], iterable[k] = iterable[k], iterable[j]
        to_compare[j], to_compare[k] = to_compare[k], to_compare[j]
        r = n
        s = j + 1
        while r > s:
            iterable[r], iterable[s] = iterable[s], iterable[r]
            to_compare[r], to_compare[s] = to_compare[s], to_compare[r]
            r -= 1
            s += 1
        if tuple(to_compare[:number]) not in history:
            history.add(tuple(to_compare[:number]))
            yield tuple(iterable[:number])
```

- ### combinations()
Description

Made by: Natalia
Helped: Ksenia
```python
def combinations(iterable, number=None):
    pass
```

- ### combinations_with_replacement()
Description

Made by: Yulia
Helped: Ksenia
```python
def combinations_with_replacement():
    pass
```

- ### Unittests
Test all functions

Made by: Ksenia
