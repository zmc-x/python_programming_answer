import unittest
from city_functions import city

class Test(unittest.TestCase):
    def test_city_country(self):
        sen=city('santiago','Chile')
        self.assertEqual(sen,'santiago,Chile')

if __name__=='__main__':
    unittest.main()

