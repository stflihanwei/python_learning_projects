# module unittest provides tools for testing your code
# unit test verifies that one specific aspect of a function'' behavior is correct
# a test case is a collection of unit tests that together prove that a function behaves as it's
# supposed to, within the full range of situations you expect it to handle.
# a test case with full coverage includes a full range of unit tests covering all the possible
# ways you can use a function.

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase): # create a class called NTC, which will contain
    # a series of unit tests for get_formatted_name(). It must INHERIT from the
    # class unittest.Testcase.
    # NTC contains a single method that tests one aspect of get_formatted_name()
    # any method that starts with test_ will be run automatically when we run test_name_function.py
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?'"""
        formatted_name = get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name, 'Janis Joplin') # unittest'' most useful features:
        # an assert method.
        # assert methods verify that a result you received matches the result you
        # expected to receive. Because we know get_formatted_name() is supposed to return a capitalized,
        # properly spaced full name, we expect the value in formatted_name to be Janis Joplin.

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('gang','mozart','amadeus')
        self.assertEqual(formatted_name,'Gang Amadeus Mozart')




