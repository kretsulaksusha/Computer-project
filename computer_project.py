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


def repeat():
    """
    Documentation
    """
    pass


def product():
    """
    Documentation
    """
    pass


def permutations(iterable, number=None):
    """
    Documenatation
    """
    if number is None:
        number = len(iterable)

    def make_all_permutations(to_iterate):
        if len(to_iterate) <= 1:
            return [to_iterate] if len(to_iterate) == 1 else []
        result = []
        length = len(to_iterate)

        for index in range(length):
            first = to_iterate[index]
            other_elements = to_iterate[:index] + to_iterate[index+1:]
            for permutation in make_all_permutations(other_elements):
                if ([first, *permutation])[:number] not in result:
                    result.append(([first, *permutation])[:number])
        return result

    all_permutations = make_all_permutations(iterable)
    for element in all_permutations:
        yield tuple(element)


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
