#!/usr/bin/env python3
'''
Unit test for access_nested_map function using parameterized testing.
'''

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    '''
    Unit test class for access_nested_map function.
    '''

    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2),
    ])
    def test_access_nested_map(self, nested_map, path, result):
        '''
        Test access_nested_map function with various inputs.

        Args:
            nested_map (dict): The nested dictionary to access.
            path (tuple): The sequence of keys
            to follow in the nested dictionary.
            result: The expected result when
            accessing the nested dictionary with the given path.
        '''
        self.assertEqual(access_nested_map(nested_map, path), result)


if __name__ == '__main__':
    unittest.main()
