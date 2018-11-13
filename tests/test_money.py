import sys
sys.path.append('../src')

import unittest
from money import Money

class MoneyTest(unittest.TestCase):
    def testMultiplication(self):
        five = Money.dollar(5)
        self.assertEqual(Money.dollar(10), five * 2)
        self.assertEqual(Money.dollar(15), five * 3)

    def testEquality(self):
        self.assertNotEqual(Money.franc(5), Money.dollar(5))

    def testSimpleAddition(self):
        sum_ = Money.dollar(5) + Money.dollar(5)
        self.assertEqual(sum_, Money.dollar(10))

if __name__ == '__main__':
    unittest.main()
