# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 16:50:31 2023

@author: collin

program to generate random numbers based on user input

"""

import random

# define range
print("********************************")
print("**Define range for white balls**")
min_white = int(input("Enter minimum number: "))
max_white = int(input("Enter maximum number: "))
num_balls = int(input("Enter number of balls: "))


# define range for gold ball
print()
print("******************************")
print("**Define range for gold ball**")
min_gold = int(input("Enter minimum number: "))
max_gold = int(input("Enter maximum number: "))

# set of numbers, list of numbers
nums_set = set()
nums_list = []

# generate 5 numbers
while len(nums_set) < num_balls:
    num = random.randint(min_white, max_white)
    nums_set.add(num)

# set to list
for num in nums_set:
    nums_list.append(num)
    
# sort numbers
nums_list.sort()

# print numbers to console  
print()  
print("***Your numbers***")
for num in nums_list:
    print(str(num) + " ", end="")
    
print()
print()
print("***GOLDBALL***")
print(random.randint(min_gold, max_gold))