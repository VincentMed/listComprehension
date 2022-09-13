# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 17:50:52 2022

@author: Vincent Medrano
"""

# writes a list comprehension that prints a list of cubes from 1 to 10
cubed_numbers = [i **3 for i in range(11)]

print(cubed_numbers)

# write a list comprehension that prints put possible results of two coin flips
coin_flips = [x + y for x in ["h", "t"] for y in ["h", "t"]]

print(coin_flips)

# write a function that takes in a string.
# Use list comprehension to return all vowels in the string.
def vowel_checker(string, vowels):
    vowel_list = [x for x in string if x in vowels]
    print("Number of vowels in your string: ")
    print(len(vowel_list))
    print(vowel_list)


string = input("Hello, enter a string")
vowels = ["a", "e", "i", "o", "u"]
vowel_checker(string, vowels)

# run code below from Canvas (Incomplete)
print([x+y for x in [10,20,30] for y in [1,2,3]])

print("~~~~~~~~~~~BreakPoint~~~~~~~~~~~~~~~~~")

#creates a nested for loop and adds results to result []
result = []

for x in [10, 20, 30]:
    for y in [1, 2, 3]:
        result.append(x + y)
        
print(result)

