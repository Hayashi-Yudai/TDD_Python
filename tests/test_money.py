import sys
sys.path.append('../src')

import unittest
from dollar import Dollar
from franc import Franc

class MoneyTest(unittest.TestCase):
    def testMultiplication(self):
        five = Dollar(5)
        self.assertEqual(Dollar(10), five.times(2))
        self.assertEqual(Dollar(15), five.times(3))

    def testFrancMultiplication(self):
        five = Franc(5)
        self.assertEqual(Franc(10), five.times(2))
        self.assertEqual(Franc(15), five.times(3))

    def testEquality(self):
        self.assertNotEqual(Franc(5), Dollar(5))

if __name__ == '__main__':
    unittest.main()
