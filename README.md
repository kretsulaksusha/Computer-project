# Recreated itertools library

## Functions:
- ### count()
Description: Count from a `number` by `step` forever

In an infinite loop yield `number` and increase it by 1

Made by: Natalia
```python
def count(firstval: int | float = 0, step: int | float = 1):
    if not isinstance(firstval, int) or not isinstance(step, int):
        raise TypeError("a number is required")
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
    if not hasattr(iterable, "__iter__"):
        raise TypeError(f"'{type(iterable)}' object is not iterable")
    index = 0
    if isinstance(iterable, set):
        iterable = list(iterable)
    while 1:
        yield iterable[index]
        index += 1
        if index >= len(iterable):
            index -= len(iterable)
```

- ### repeat()
Description: Yield same value

Repeatedly yield the same value

Made by: Yulia
```python
def repeat(value, repeat_obj=None):
    if repeat_obj is not None and not isinstance(repeat_obj, int):
        raise TypeError(
            f"'{type(repeat_obj)}' object cannot be interpreted as an integer"
        )
    if repeat_obj is not None and repeat_obj <= 0:
        return []
    if repeat_obj:
        for _ in range(repeat_obj):
            yield value
    else:
        while True:
            yield value
```

- ### product()
Description: Generate a cartesian product of input iterables

Get a cartesian product of some iterables

Made by: Radomyr
```python
def product(*iterables, repeat_obj=1):
    if not hasattr(iterables, "__iter__"):
        raise TypeError(f"'{type(iterables)}' object is not iterable")
    if not isinstance(repeat_obj, int):
        raise TypeError(
            f"'{type(repeat_obj)}' object cannot be interpreted as an integer"
        )
    iterables = iterables * repeat_obj
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
        raise ValueError("number must be non-negative")
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
Description: Generate all combinations of length `number` of elements in `iterable`


Made by: Natalia

Helped: Ksenia
```python
def combinations(iterable, number: int):
    if not hasattr(iterable, "__iter__"):
        raise TypeError(f"'{type(iterable)}' object is not iterable")
    if not isinstance(number, int):
        raise TypeError(
            f'number "{type(number)}" object cannot be interpreted as an integer'
        )
    if number < 0:
        raise ValueError("number must be non-negative")
    if number > len(iterable):
        return None
    if number == 0:
        return []
    indexes = list(range(number))
    n = len(iterable) - 1
    index_to_change = indexes[-1]
    history = []
    while True:
        if tuple([iterable[i] for i in indexes]) not in history:
            history.append(tuple([iterable[i] for i in indexes]))
            yield tuple([iterable[i] for i in indexes])
        else:
            break
        if indexes[index_to_change] < n:
            indexes[index_to_change] += 1
        else:
            counter = 0
            for i in reversed(range(len(indexes))):
                if indexes[i] != n - counter:
                    index_to_change = i
                    indexes[index_to_change] += 1
                    break
                counter += 1
            for i in range(index_to_change + 1, number):
                indexes[i] = indexes[i - 1] + 1
            index_to_change = len(indexes) - 1

        if indexes == list(range(len(iterable) - number, len(iterable))):
            temp = []
            for i in range(len(iterable) - number, len(iterable)):
                temp.append(iterable[i])
            if tuple(temp) not in history:
                history.append(tuple(temp))
                yield tuple(temp)
            else:
                break
```

- ### combinations_with_replacement()
Description: Generate all combinations with replacement of length number of elements in iterable


Made by: Yulia

Helped: Ksenia
```python
def combinations_with_replacement(iterable, number: int):
    if not hasattr(iterable, "__iter__"):
        raise TypeError(f"'{type(iterable)}' object is not iterable")
    if not isinstance(number, int):
        raise TypeError(
            f'number "{type(number)}" object cannot be interpreted as an integer'
        )
    if number < 0:
        raise ValueError("number must be non-negative")
    if number == 0:
        return []
    el_lst = []
    counter = 2

    if number < 2:
        for el in iterable:
            yield tuple([el])
        return None
    for el in range(len(iterable)):
        for subel in range(el, len(iterable)):
            el_lst.append([iterable[el], iterable[subel]])
    while counter != number:
        new_lst = []
        for subel in iterable:
            for ind in range(len(el_lst)):
                part = sorted(el_lst[ind] + [subel])
                if part in new_lst:
                    continue
                new_lst.append(part)
        el_lst = new_lst
        counter += 1
    for el in el_lst:
        yield tuple(el)
```

- ### Unittests
Test all functions

Made by: Ksenia


- ### Presentation

