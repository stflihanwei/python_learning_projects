import unittest
from city_functions import city_country

class test_city_country(unittest.TestCase):
    def test_name(self):
        city_country_name = city_country('beijing','china')
        self.assertEqual(city_country_name,'Beijing China')

    def test_name_2(self): # the second test name must be different from the first one
        city_country_name = city_country('beijing','china', '10000')
        self.assertEqual(city_country_name, 'Beijing China -Population 10000')

# Assert methods available from the unittest.TestCase module
# assertEqual(a,b)  Verify that a == b
# assertNotEqual(a,b)  verify that a != b
# assertTrue(x)   verify that x is True
# assertFalse(x)   verify that x is False
# assertIn(item,list)  verify that item is in list
# assertNotIn(item,list)  verify that item is not in list

