# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 15:43:06 2023

@author: collin

program to generate random numbers for mega millions

"""

import random

# define range
min_white = 1
max_white = 70

# set of numbers, list of numbers
nums_set = set()
nums_list = []

# generate 5 numbers
while len(nums_set) < 5:
    num = random.randint(min_white, max_white)
    nums_set.add(num)

# set to list
for num in nums_set:
    nums_list.append(num)
    
# sort numbers
nums_list.sort()

# print numbers to console  
print()  
print("***Your Mega Millions numbers***")
for num in nums_list:
    print(str(num) + " ", end="")
    
print()
print()
print("***MEGABALL***")
print(random.randint(1, 25))