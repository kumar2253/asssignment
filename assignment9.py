#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


# Question 1: Python - Replace multiple words with K

def replace_multiple_words(string, words, k):
    replaced_string = string
    for word in words:
        replaced_string = replaced_string.replace(word, k)
    return replaced_string

# Example usage
my_string = "Python is a great programming language"
words_to_replace = ["Python", "language"]
replacement = "K"
replaced_string = replace_multiple_words(my_string, words_to_replace, replacement)
print("Replaced string:", replaced_string)


# In[3]:


# Question 2: Python | Permutation of a given string using the inbuilt function

from itertools import permutations

def string_permutations(string):
    perms = permutations(string)
    perm_list = [''.join(perm) for perm in perms]
    return perm_list

# Example usage
my_string = "ABC"
permutations_list = string_permutations(my_string)
print("Permutations:", permutations_list)


# In[4]:


# Question 3: Python | Check for URL in a String

import re

def check_for_url(string):
    pattern = re.compile(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+')
    match = re.search(pattern, string)
    if match:
        return True
    else:
        return False

# Example usage
my_string = "Visit my website at https://www.example.com"
if check_for_url(my_string):
    print("URL found in the string.")
else:
    print("URL not found in the string.")


# In[5]:


# Question 4: Execute a String of Code in Python

def execute_code(code_string):
    exec(code_string)

# Example usage
code = '''
for i in range(5):
    print(i)
'''
execute_code(code)


# In[6]:


# Question 5: String slicing in Python to rotate a string

def rotate_string(string, k):
    rotated_string = string[k:] + string[:k]
    return rotated_string

# Example usage
my_string = "Hello, World!"
rotation_index = 4
rotated_string = rotate_string(my_string, rotation_index)
print("Rotated string:", rotated_string)


# In[7]:


# Question 6: String slicing in Python to check if a string can become empty by recursive deletion

def is_empty_string(string):
    if len(string) == 0:
        return True
    for i in range(len(string)):
        new_string = string[:i] + string[i+1:]
        if is_empty_string(new_string):
            return True
    return False

# Example usage
my_string = "abcde"
if is_empty_string(my_string):
    print("String can become empty by recursive deletion.")
else:
    print("String cannot become empty by recursive deletion.")


# In[8]:


# Question 7: Python Counter | Find all duplicate characters in a string

from collections import Counter

def find_duplicate_characters(string):
    frequency = Counter(string)
    duplicate_chars = [char for char, count in frequency.items() if count > 1]
    return duplicate_chars

# Example usage
my_string = "Hello, World!"
duplicate_chars = find_duplicate_characters(my_string)


# In[9]:


# Question 8: Python - Replace all occurrences of a substring in a string

def replace_all_occurrences(string, substring, replacement):
    replaced_string = string.replace(substring, replacement)
    return replaced_string

# Example usage
my_string = "Hello, World!"
substring = "o"
replacement = "a"
replaced_string = replace_all_occurrences(my_string, substring, replacement)
print("Replaced string:", replaced_string)


# In[10]:


# Question 9: Python - Extract unique values from dictionary values

def extract_unique_values(dictionary):
    values = dictionary.values()
    unique_values = set(values)
    return unique_values

# Example usage
my_dict = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}
unique_values = extract_unique_values(my_dict)
print("Unique values:", unique_values)


# In[11]:


# Question 10: Python program to find the sum of all items in a dictionary

def sum_dictionary_items(dictionary):
    sum_of_items = sum(dictionary.values())
    return sum_of_items

# Example usage
my_dict = {"a": 5, "b": 3, "c": 8, "d": 2}
sum_of_items = sum_dictionary_items(my_dict)
print("Sum of dictionary items:", sum_of_items)


# In[ ]:




