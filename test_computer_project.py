"Testing module"
import unittest
import computer_project as cp

class TestFunctions(unittest.TestCase):
    """Test class."""

    def test_count(self):
        """Count test."""
        gens = [cp.count(2), cp.count(-2), cp.count(2, 3)]
        self.assertEqual([next(gens[0]) for _ in range(3)], [2, 3, 4])
        self.assertEqual([next(gens[1]) for _ in range(3)], [-2, -1, 0])
        self.assertEqual([next(gens[2]) for _ in range(3)], [2, 5, 8])

        # Errors
        self.assertRaises(TypeError, list, cp.count('a'))
        self.assertRaises(TypeError, list, cp.count([1, 2]))
        self.assertRaises(TypeError, list, cp.count((1, 2)))
        self.assertRaises(TypeError, list, cp.count({1, 2}))

    def test_cycle(self):
        """Count test."""
        iter_obj = [cp.cycle([1, 2]), cp.cycle({1, 2}), cp.cycle((1, 2)),
                    cp.cycle('AB'), cp.cycle(range(2))]
        self.assertEqual([next(iter_obj[0]) for _ in range(3)], [1, 2, 1])
        # self.assertEqual([next(iter_obj[1]) for _ in range(3)], [1, 2, 1])
        self.assertEqual([next(iter_obj[2]) for _ in range(3)], [1, 2, 1])
        self.assertEqual([next(iter_obj[3]) for _ in range(3)], ['A', 'B', 'A'])
        self.assertEqual([next(iter_obj[4]) for _ in range(5)], [0, 1, 0, 1, 0])

        # Errors
        self.assertRaises(TypeError, list, cp.cycle(2))

    def test_repeat(self):
        """Repeat test."""
        self.assertEqual([next(cp.repeat(3)) for _ in range(3)], [3, 3, 3])
        self.assertEqual([next(cp.repeat('a')) for _ in range(3)], ['a', 'a', 'a'])
        self.assertEqual([next(cp.repeat([1, 2])) for _ in range(3)], [[1, 2], [1, 2], [1, 2]])
        self.assertEqual([next(cp.repeat((1, 2))) for _ in range(3)], [(1, 2), (1, 2), (1, 2)])
        self.assertEqual([next(cp.repeat({1, 2})) for _ in range(3)], [{1, 2}, {1, 2}, {1, 2}])

        # self.assertEqual(list(cp.repeat(3, 3)), [3, 3, 3])
        # self.assertEqual(list(cp.repeat('a', 3)), ['a', 'a', 'a'])
        # self.assertEqual(list(cp.repeat([1, 2], 3)), [[1, 2], [1, 2], [1, 2]])
        # self.assertEqual(list(cp.repeat((1, 2), 3)), [(1, 2), (1, 2), (1, 2)])
        # self.assertEqual(list(cp.repeat({1, 2}, 3)), [{1, 2}, {1, 2}, {1, 2}])

        # Errors
        # self.assertRaises(TypeError, list, cp.repeat(1, '1'))
        # self.assertRaises(TypeError, list, cp.repeat([1, 2], 'a'))

    def test_product(self):
        """Product test."""
        data = [[1], [1, 2], (1, 2), {1, 2}, range(3)]
        self.assertEqual(list(cp.product(data[0])), [(1,)])
        # self.assertEqual(list(cp.product(data[0], repeat=3)), [(1, 1, 1)])
        self.assertEqual(list(cp.product(data[1])), [(1,), (2,)])
        self.assertEqual(list(cp.product(data[2])), [(1,), (2,)])
        # self.assertEqual(list(cp.product(data[2], repeat=2)), [(1, 1), (1, 2), (2, 1), (2, 2)])
        self.assertEqual(list(cp.product(data[3])), [(1,), (2,)])
        self.assertEqual(list(cp.product(data[4])), [(0,), (1,), (2,)])
        self.assertEqual(list(cp.product('ABC', 'x')), [('A', 'x'), ('B', 'x'), ('C', 'x')])

        # Errors
        # self.assertRaises(TypeError, list, cp.product(2))
        # self.assertRaises(TypeError, list, cp.product(data[1], repeat='1'))

    def test_permutations(self):
        """Permutations test."""
        data = [[1], [1, 2], (1, 2), {1, 2}, range(3), 'ABB', 'ABC', [1, [2], 'a']]
        self.assertEqual(list(cp.permutations(data[0])), [(1,)])
        self.assertEqual(list(cp.permutations(data[1])), [(1, 2), (2, 1)])
        self.assertEqual(list(cp.permutations(data[2])), [(1, 2), (2, 1)])
        self.assertEqual(list(cp.permutations(data[3])), [(1, 2), (2, 1)])
        self.assertEqual(list(cp.permutations(data[4])), [(0, 1, 2), (0, 2, 1), (1, 0, 2),
                                                         (1, 2, 0), (2, 0, 1), (2, 1, 0)])
        self.assertEqual(list(cp.permutations(data[5])), [('A', 'B', 'B'), ('A', 'B', 'B'),
                                                         ('B', 'A', 'B'), ('B', 'B', 'A'),
                                                         ('B', 'A', 'B'), ('B', 'B', 'A')])
        self.assertEqual(list(cp.permutations(data[6])), [('A', 'B', 'C'), ('A', 'C', 'B'),
                                                         ('B', 'A', 'C'), ('B', 'C', 'A'),
                                                         ('C', 'A', 'B'), ('C', 'B', 'A')])
        self.assertEqual(list(cp.permutations(data[6], 2)), [('A', 'B'), ('A', 'C'), ('B', 'A'),
                                                            ('B', 'C'), ('C', 'A'), ('C', 'B')])
        self.assertEqual(list(cp.permutations(data[7])), [(1, [2], 'a'), (1, 'a', [2]),
                                                         ([2], 1, 'a'), ([2], 'a', 1),
                                                         ('a', 1, [2]), ('a', [2], 1)])
        self.assertEqual(list(cp.permutations(data[6], 1)), [('A',), ('B',), ('C',)])

        # Errors
        self.assertRaises(TypeError, list, cp.permutations(2))


    def test_combinations(self):
        """Combinations test."""
        data = [[1, 2], (1, 2), [1, 'a'], range(3), 'ABB', 'ABC', [1, [2], 'a', 'b']]
        self.assertEqual(list(cp.combinations(data[0], 0)), [()])
        self.assertEqual(list(cp.combinations(data[0], 1)), [(1,), (2,)])
        self.assertEqual(list(cp.combinations(data[1], 2)), [(1, 2)])
        self.assertEqual(list(cp.combinations(data[2], 2)), [(1, 'a')])
        self.assertEqual(list(cp.combinations(data[3], 2)), [(0, 1), (0, 2), (1, 2)])
        self.assertEqual(list(cp.combinations(data[4], 2)), [('A', 'B'), ('A', 'B'), ('B', 'B')])
        self.assertEqual(list(cp.combinations(data[5], 2)), [('A', 'B'), ('A', 'C'), ('B', 'C')])
        self.assertEqual(list(cp.combinations(data[6], 2)), [(1, [2]), (1, 'a'), (1, 'b'),
        ([2], 'a'), ([2], 'b'), ('a', 'b')])
        self.assertEqual(list(cp.combinations(data[6], 6)), [])

        # Errors
        self.assertRaises(ValueError, list, cp.combinations(data[0], -1))
        self.assertRaises(TypeError, list, cp.combinations(data[0], 'a'))
        self.assertRaises(TypeError, list, cp.combinations(data[0], [1, 2]))
        self.assertRaises(TypeError, list, cp.combinations(0, 1))


    def test_combinations_with_replacement(self):
        """Combinations with replacement test."""
        data = [[1, 2], (1, 2), [1, 'a'], range(3), 'ABB', 'ABC', [1, [2]]]
        # self.assertEqual(list(cp.combinations_with_replacement(data[0], 1)), [(1,), (2,)])
        self.assertEqual(list(cp.combinations_with_replacement(data[1], 2)),
        [(1, 1), (1, 2), (2, 2)])
        # self.assertEqual(list(cp.combinations_with_replacement(data[2], 2)),
        # [(1, 1), (1, 'a'), ('a', 'a')])
        self.assertEqual(list(cp.combinations_with_replacement(data[3], 2)),
        [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)])
        self.assertEqual(list(cp.combinations_with_replacement(data[4], 2)),
        [('A', 'A'), ('A', 'B'), ('A', 'B'), ('B', 'B'), ('B', 'B'), ('B', 'B')])
        self.assertEqual(list(cp.combinations_with_replacement(data[5], 2)),
        [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')])
        # self.assertEqual(list(cp.combinations_with_replacement(data[6], 2)),
        # [(1, 1), (1, [2]), ([2], [2])])
        # self.assertEqual(list(cp.combinations_with_replacement(data[0], 0)), [()])

        # Error
        self.assertRaises(TypeError, list, cp.combinations_with_replacement(data[0], 'a'))
        self.assertRaises(TypeError, list, cp.combinations_with_replacement(data[0], [1, 2]))
        self.assertRaises(TypeError, list, cp.combinations_with_replacement(data[0], (1, 2)))
        self.assertRaises(TypeError, list, cp.combinations_with_replacement(data[0], {1, 2}))
        self.assertRaises(TypeError, list, cp.combinations_with_replacement(data[0][0], 2))
        self.assertRaises(ValueError, list, cp.combinations_with_replacement(data[0], -1))


if __name__ == '__main__':
    unittest.main()
