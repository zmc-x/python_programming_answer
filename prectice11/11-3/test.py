import unittest
import employee

class Test(unittest.TestCase):
    def setUp(self):
        self.object=employee.Employee('helloworld',1)

    def test_default(self):
        x=self.object.give_raise()
        self.assertEqual(x,5001)
    def test_increase_people(self):
        x=self.object.give_raise(1)
        self.assertEqual(x,2)

if __name__=='__main__':
    unittest.main()