#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countResponseTimeRegressions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY responseTimes as parameter.
#

def countResponseTimeRegressions(responseTimes):
    # create the function the calculate the average of the list
    def average(previous_list):
        return sum(previous_list) / len(previous_list)

    count = 0
    # iterate over the list
    for i in range(1, len(responseTimes)):
        # store the previous items in a list
        previous_list = responseTimes[:i]
        # calcualte the average number of the previous list
        average_number = average(previous_list)
        # check if their average greater than the current item
        if average_number < responseTimes[i]:
            count += 1
    return count

if __name__ == '__main__':
    responseTimes_count = int(input().strip())

    responseTimes = []

    for _ in range(responseTimes_count):
        responseTimes_item = int(input().strip())
        responseTimes.append(responseTimes_item)

    result = countResponseTimeRegressions(responseTimes)

    print(result)
