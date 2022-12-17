"Recreated Itertools library"


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
    if len(iterables) == 2:
        for element in iterables[0]:
            for element2 in iterables[1]:
                yield (element, element2)
    if len(iterables) > 2:
        for element in iterables[0]:
            for element2 in product(*iterables[1:]):
                yield (element, *element2)


def permutations(iterable, number=None):
    """
    Documenatation
    """
    if number is None:
        number = len(iterable)
    elif number == 1:
        for element in iterable:
            yield (element,)
    if number > 1:
        for element in iterable:
            for element2 in permutations(iterable, number-1):
                if element not in element2:
                    yield (element, *element2)


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
