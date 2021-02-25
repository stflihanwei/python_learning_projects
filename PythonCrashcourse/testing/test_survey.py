import unittest
from unittest import TestCase

from survey import AnonymousSurvey

# test_survey.py we created a new instance of AnonymousSurvey in each test method,
# and created new responses in each method.


class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        '''create a survey and a set of responses for use in all test methods'''
        # setUp() create a survey instance and a set of responses that
        # can be used/accessed in later functions
        question = "what language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question) # create an instance of AnonymousSurvey,
        # pass a question string goes to AS class init function, as it is required.
        # then store the instance of AnonymousSurvey to my_survey attribute.
        self.responses = ['English','Spainish','Mandarin'] # array of strings
        # stored as a instance attribute



    def test_store_single_response(self):
        # question = "what language did you first learn to speak?"
        # my_survey = AnonymousSurvey(question)
        # my_survey.store_response('English')
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses) # assertIn verify that item is in list
        # verify that the response was stored correctly by asserting that English is in the list
        # my_survey.responses


    def test_store_three_responses(self): # create a new method
        # question = "What language did you first learn to speak?"
        # my_survey = AnonymousSurvey(question) # create my_survey instance of AMS class
        # responses = ['English', 'Spanish', 'Mandarin']
        for response in self.responses:
            self.my_survey.store_response(response) # call my_survey.store_response function
            # giving response variable as a parameter to be stored in this function
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)





