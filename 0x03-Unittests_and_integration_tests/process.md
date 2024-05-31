access_nested_map

    This is the function from the `utils` module that we are going to test. This function retrieves a value from a nested dictionary based on a given path (a sequence of keys).

@parameterized.expand Decorator

    >>Decorates the test_access_nested_map method to run it with different sets of inputs.
    >>The decorator takes a list of tuples, each containing the parameters for one test case (nested_map, path, expected).

**@parameterized.expand**:

    This decorator allows the `test_access_nested_map` method to be run multiple times with different sets of parameters. Each tuple in the list passed to `expand` represents a set of parameters for one test case:
    - `({"a": 1}, ("a",), 1)`: Tests that accessing the key `"a"` in the dictionary `{"a": 1}` returns `1`.
    - `({"a": {"b": 2}}, ("a",), {"b": 2})`: Tests that accessing the key `"a"` in the dictionary `{"a": {"b": 2}}` returns the nested dictionary `{"b": 2}`.
    - `({"a": {"b": 2}}, ("a", "b"), 2)`: Tests that accessing the path `("a", "b")` in the dictionary `{"a": {"b": 2}}` returns `2`.

def test_access_nested_map(self, nested_map, path, result):
    self.assertEqual(access_nested_map(nested_map, path), result)

    >> Calls access_nested_map with nested_map and path
    >> Asserts that the result is equal to the expected value using self.assertEqual.


     **test_access_nested_map**: This is the actual test method that will be run with the different sets of parameters. It takes three arguments:
    - `nested_map`: The nested dictionary to be accessed.
    - `path`: The sequence of keys to follow in the nested dictionary.
    - `expected`: The expected result of accessing the nested dictionary with the given path.

=================================