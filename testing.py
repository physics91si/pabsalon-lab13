#!/usr/bin/python

# Lab 13
# Physics 91SI
# Spring 2016

import unittest
import calc

class CalcTest(unittest.TestCase):
    # TODO implement tests here to verify that your functions work!
    def testAddition(self):
        self.assertEqual(calc.calc('102+1'), 103)

    def testSubtraction(self):
        self.assertEqual(calc.calc('10-2'), 8)

    def testMultiplciation(self):
        self.assertEqual(calc.calc('3*2'), 6)
 
    def testDivision(self):
        self.assertEqual(calc.calc('10/2'), 5)

if __name__ == '__main__':
    unittest.main()

