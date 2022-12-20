"Recreated Itertools library"
from math import factorial


def count(firstval: int | float = 0, step: int | float = 1):
    """
    Count from a number by step forever

    Parameters
    ----------
    firstval : int | float, optional
        Number to start counting from, by default 0
    step : int | float, optional
        Step to count by, by default 1

    Yields
    ------
    int | float
    """
    if not isinstance(firstval, int) or not isinstance(step, int):
        raise TypeError('a number is required')
    number = firstval
    while True:
        yield number
        number += step


def cycle(iterable):
    """
    Cycle through an iterable forever

    Parameters
    ----------
    iterable : iterable
        Iterable to cycle through

    Yields
    ------
    any
    """
    if not hasattr(iterable, "__iter__"):
        raise TypeError(f"'{type(iterable)}' object is not iterable")
    index = 0
    while 1:
        yield iterable[index]
        index += 1
        if index >= len(iterable):
            index -= len(iterable)


def repeat(value, repeat=None):
    """
    Return value forever

    Parameters
    ----------
    value : any
        Value to repeat

    Yields
    ------
    value : any
        Value to repeat
    """
    if repeat is not None and not isinstance(repeat, int):
        raise TypeError(f"'{type(repeat)}' object cannot be interpreted as an integer")
    while True:
        yield value


def product(*iterables, repeat=1):
    """
    Generate a cartesian product of input iterables

    Parameters
    ----------
    *iterables : iterable
        Iterables to generate a cartesian product of

    Yields
    ------
    tuple
        Tuple of elements from each iterable
    """
    if not hasattr(iterables, "__iter__"):
        raise TypeError(f"'{type(iterables)}' object is not iterable")
    if not isinstance(repeat, int):
        raise TypeError(f"'{type(iterables)}' object cannot be interpreted as an integer")
    if len(iterables) == 0:
        yield ()
    if len(iterables) == 1:
        for element in iterables[0]:
            yield (element,)
    if len(iterables) > 1:
        for element in iterables[0]:
            for element2 in product(*iterables[1:]):
                yield (element, *element2)


def permutations(iterable, number: int = None):
    """
    Generate all permutations of length number of elements in iterable

    Parameters
    ----------
    iterable : iterable
        Iterable to generate permutations of
    number : int, optional
        Length of permutations, by default will be length of iterable

    Yields
    ------
    tuple
        Tuple of elements from iterable
    """
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


def combinations(iterable, number: int):
    """
    Documentation
    """
    if not hasattr(iterable, '__iter__'):
        raise TypeError(f"'{type(iterable)}' object is not iterable")
    iterable = list(iterable)
    if not isinstance(number, int):
        raise TypeError(f'number "{type(number)}" object cannot be interpreted as an integer')
    if number < 0:
        raise ValueError("number must be non-negative")
    if number > len(iterable):
        return None
    history = set()

    to_compare = list(range(len(iterable)))

    yield tuple(iterable[:number])
    history.add(tuple(sorted(to_compare[:number])))


    for _ in range(int(factorial(len(iterable))-1)):
        n = len(iterable)-1
        j = n-1
        while to_compare[j]>to_compare[j+1]:
            j-=1
        k = n
        while to_compare[j]>to_compare[k]:
            k-=1
        iterable[j], iterable[k] = iterable[k], iterable[j]
        to_compare[j], to_compare[k] = to_compare[k], to_compare[j]
        r = n
        s = j+1
        while r>s:
            iterable[r], iterable[s] = iterable[s], iterable[r]
            to_compare[r], to_compare[s] = to_compare[s], to_compare[r]
            r-=1
            s+=1
        if tuple(sorted(to_compare[:number])) not in history:
            history.add(tuple(sorted(to_compare[:number])))
            yield tuple(iterable[:number])


def combinations_with_replacement(iterable, number: int):
    """
    Documentation
    """
    if not hasattr(iterable, '__iter__'):
        raise TypeError(f"'{type(iterable)}' object is not iterable")
    if not isinstance(number, int):
        raise TypeError(f'number "{type(number)}" object cannot be interpreted as an integer')
