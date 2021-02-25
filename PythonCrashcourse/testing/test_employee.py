import unittest
from unittest import TestCase

from employee import Employee

class TestEmployee(unittest.TestCase): #notice that it is a dot here. It is unittest module Test case class
    def setUp(self):
        ''' create a survey and a set of responses for use in all test methods '''
        # setUp() create a survey instance and a set of responses that
        # can be used in later functions
        self.new_employee = Employee('Hanwei', 'Li', 10000)

    def test_give_default_raise(self):
        new_salary = self.new_employee.annual_salary + 5000  # if you do not need this variable
        # somewhere else, do not need to store in self.xxx
        self.new_employee.give_raise()
        self.assertEqual(self.new_employee.annual_salary, new_salary) # assertIn verify that item is in list

    def test_give_custom_raise(self):
        new_raise = 3000 # give a new variable to the raise amount so
        # you don't have to type it all the time, have random number.
        new_salary = self.new_employee.annual_salary + new_raise
        self.new_employee.give_raise(new_raise)
        self.assertEqual(self.new_employee.annual_salary,new_salary)


