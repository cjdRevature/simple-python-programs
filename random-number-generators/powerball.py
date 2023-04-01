# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 16:47:18 2023

@author: collin

program to generate random numbers for powerball

"""
import random

# define range
min_white = 1
max_white = 69

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
print("***Your Powerball numbers***")
for num in nums_list:
    print(str(num) + " ", end="")
    
print()
print()
print("***POWERBALL***")
print(random.randint(1, 26))
