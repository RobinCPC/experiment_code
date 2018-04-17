# -*- coding: utf-8 -*-
"""
Example of using unittest.TestSuite
"""

import unittest
from test_mathfunc import TestMathFunc

if __name__ == '__main__':
    suite = unittest.TestSuite()

    tests = [TestMathFunc("test_add"), TestMathFunc("test_minus"),
             TestMathFunc("test_divide")]

    # add multiple testing cases in suite
    suite.addTests(tests)

    # add single case in suite
    suite.addTest(TestMathFunc("test_multi"))

    '''
    # using addTests + TestLoader
    # loadTestsFromName(), input 'module.TestCase'
    suite.addTests(unittest.TestLoader().loadTestsFromName('test_mathfunc.TestMathFunc'))
    suite.addTests(unittest.TestLoader().loadTestsFromNames(['test_mathfunc.TestMathFunc']))  # loadTestsFromNames()

    # loadTestsFromTestCase(), input TestCase
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))

    '''

    # running test suite
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

