"Recreated Itertools library"
from math import factorial

from math import factorial

def count(firstval=0, step=1):
    """
    Documentation
    """
    number = firstval
    while True:
        yield number
        number += step


def cycle(iterable):
    """
    Documentation
    """
    index = 0
    while 1:
        yield iterable[index]
        index += 1
        if index >= len(iterable):
            index -= len(iterable)


def repeat(value):
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
    while True:
        yield value


def product(*iterables):
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
    if len(iterables) == 0:
        yield ()
    if len(iterables) == 1:
        for element in iterables[0]:
            yield (element,)
    if len(iterables) > 1:
        for element in iterables[0]:
            for element2 in product(*iterables[1:]):
                yield (element, *element2)



def permutation(iterable, number=None):
    """
    Documentation
    """
    if not hasattr(iterable, '__iter__'):
        raise TypeError(f"'{type(iterable)}' object is not iterable")
    iterable = list(iterable)
    if number is None:
        number = len(iterable)
    if number < 0:
        raise ValueError("r must be non-negative")
    if number > len(iterable):
        return None
    if number is None:
        number = len(iterable)
    history = set()
    elements_counts = {}
    result_iterable = []
    for element in iterable:
        if isinstance(element, list):
            element = tuple(element)
            if element not in elements_counts:
                result_iterable.append((element, -1, 0))
            else:
                result_iterable.append(
                    (element, "was_list", elements_counts[element]))
        elif element not in elements_counts:
            result_iterable.append((element, 0))
        else:
            result_iterable.append((element, elements_counts[element]))
        elements_counts[element] = elements_counts.get(element, 0) + 1
    history.add(tuple(i[0] for i in result_iterable)[:number])
    yield tuple(
        list(i[0]) if isinstance(i, tuple) and i[1] == -1 else i[0]
        for i in result_iterable[:number]
    )

    to_compare = list(range(len(result_iterable)))

    for _ in range(int(factorial(len(result_iterable)) - 1)):
        n = len(result_iterable) - 1
        j = n - 1
        while to_compare[j] > to_compare[j + 1]:
            j -= 1
        k = n
        while to_compare[j] > to_compare[k]:
            k -= 1
        result_iterable[j], result_iterable[k] = result_iterable[k], result_iterable[j]
        to_compare[j], to_compare[k] = to_compare[k], to_compare[j]
        r = n
        s = j + 1
        while r > s:
            result_iterable[r], result_iterable[s] = (
                result_iterable[s],
                result_iterable[r],
            )
            to_compare[r], to_compare[s] = to_compare[s], to_compare[r]
            r -= 1
            s += 1
        if tuple(result_iterable)[:number] not in history:
            history.add(tuple(result_iterable)[:number])
            yield tuple(
                list(i[0]) if isinstance(
                    i, tuple) and i[1] == -1 else i[0]
                for i in result_iterable
            )[:number]


def combinations():
    """
    Documentation
    """


def combinations_with_replacement():
    """
    Documentation
    """
