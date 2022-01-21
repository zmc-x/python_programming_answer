import unittest
from city_function import city

class Test(unittest.TestCase):
    def test_city_county(self):
        sen=city('santiago','chile')
        self.assertEqual(sen,'santiago,chile')
    def test_city_county_population(self):
        sen=city('shanghai','China','more people')
        self.assertEqual(sen,'shanghai,China-more people')
if __name__=='__main__':
    unittest.main()