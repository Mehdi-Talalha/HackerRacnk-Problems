#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'isAlphabeticPalindrome' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING code as parameter.
#

def isAlphabeticPalindrome(code):
    # keep in the variable only alphabitics and convert them to lowercase.
    letters = ''.join(ch.lower() for ch in code if ch.isalpha())
    # compare the code and the reversed string.
    return letters == letters[::-1]
    
if __name__ == '__main__':
    code = input()

    result = isAlphabeticPalindrome(code)

    print(int(result))
