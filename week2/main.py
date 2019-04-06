""" Week 2"""

import re

nums = []

with open("regex_sum_136538.txt", 'r') as text:
    for line in text:
        nums += re.findall('[0-9]+', line)

nums = [int(num) for num in nums]

print(sum(nums))