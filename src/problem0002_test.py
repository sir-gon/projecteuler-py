###############################################################################
# Even Fibonacci numbers
#
# https://projecteuler.net/problem=2
#
# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.
###############################################################################

import unittest
from .problem0002 import problem0002


class TestProblem0002(unittest.TestCase):

    def test_problem0002(self):

        tests = [
          {'input': 4000000, 'answer': 4613732}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual( problem0002(_tt['input']), _tt['answer'],
              f"{_} | problem0002({_tt['input']}) must be "\
              f"=> {_tt['answer']}")
