"Recreated Itertools library"

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
    if isinstance(iterable, str):
        iterable = [*iterable]
    if number is None:
        number = len(iterable)
    history = set()
    yield tuple(iterable)[:number]
    history.add(tuple(iterable)[:number])

    to_compare = list(range(len(iterable)))

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
        if tuple(iterable)[:number] not in history:
            history.add(tuple(iterable)[:number])
            yield tuple(iterable)[:number]


def combinations():
    """
    Documentation
    """
    pass


def combinations_with_replacement():
    """
    Documentation
    """
    pass
