# -*- coding: utf-8 -*-
"""
Example of using unittest.TestSuite and output to txt
"""

import unittest
from test_mathfunc import TestMathFunc

if __name__ == '__main__':
    suite = unittest.TestSuite()

    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))

    # running test suite
    with open('UnittestTextReport.txt', 'a') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suite)
