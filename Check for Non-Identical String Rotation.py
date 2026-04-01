#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'isNonTrivialRotation' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def isNonTrivialRotation(s1, s2):
    # they must have the same length
    if len(s1) != len(s2):
        return 0

    # the strings should be simillars
    if s1 == s2:
        return 0

    # the s2 must be a substring of s1 + s2
    if s2 in (s1 + s1):
        return 1

    return 0
if __name__ == '__main__':
    s1 = input()

    s2 = input()

    result = isNonTrivialRotation(s1, s2)

    print(int(result))
