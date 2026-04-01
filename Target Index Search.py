#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'binarySearch' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER target
#

def binarySearch(nums, target):
    # binary searsh algorithm
    left = 0
    right = len(nums) - 1
    # main iteration
    while left <= right:
        middle = (left + right) // 2

        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    return -1

if __name__ == '__main__':
    nums_count = int(input().strip())

    nums = []

    for _ in range(nums_count):
        nums_item = int(input().strip())
        nums.append(nums_item)

    target = int(input().strip())

    result = binarySearch(nums, target)

    print(result)
