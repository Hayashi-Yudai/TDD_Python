import sys
sys.path.append('../src')

import unittest
from dollar import Dollar

class MoneyTest(unittest.TestCase):
    def testMultiplication(self):
        five = Dollar(5)
        product = five.times(2)
        self.assertEqual(10, product.amount)
        product = five.times(3)
        self.assertEqual(15, product.amount)

if __name__ == '__main__':
    unittest.main()
