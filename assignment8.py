#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


# Question 1: Python - Least frequent character in a string

from collections import Counter

def least_frequent_character(string):
    frequency = Counter(string)
    least_frequent_char = min(frequency, key=frequency.get)
    return least_frequent_char

# Example usage
my_string = "Hello, World!"
least_frequent = least_frequent_character(my_string)
print("Least frequent character:", least_frequent)


# In[3]:


# Question 2: Python | Maximum frequency character in a string

from collections import Counter

def maximum_frequency_character(string):
    frequency = Counter(string)
    max_frequency = max(frequency.values())
    max_frequency_chars = [char for char, count in frequency.items() if count == max_frequency]
    return max_frequency_chars

# Example usage
my_string = "Hello, World!"
max_frequency_chars = maximum_frequency_character(my_string)
print("Maximum frequency character(s):", max_frequency_chars)


# In[4]:


# Question 3: Python | Program to check if a string contains any special character

import re

def contains_special_character(string):
    special_chars = re.compile(r'[@_!#$%^&*()<>?/\|}{~:]')
    if special_chars.search(string) is None:
        return False
    else:
        return True

# Example usage
my_string = "Hello, World!"
if contains_special_character(my_string):
    print("String contains special character(s).")
else:
    print("String does not contain any special character.")


# In[ ]:


# Question 4: Generating random strings until a given string is generated

import random
import string

def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string

def generate_until_match(target_string):
    generated_string = ""
    while generated_string != target_string:
        generated_string = generate_random_string(len(target_string))
        print(generated_string)

# Example usage
target_string = "hello"
generate_until_match(target_string)


# In[ ]:


# Question 5: Find words which are greater than a given length k

def find_words_greater_than_length(string, k):
    words = string.split()
    result = [word for word in words if len(word) > k]
    return result

# Example usage
my_string = "Python is a great programming language"
k = 4
words_greater_than_k = find_words_greater_than_length(my_string, k)
print("Words greater than length", k, ":", words_greater_than_k)


# In[1]:


# Question 6: Python program for removing i-th character from a string

def remove_ith_character(string, i):
    new_string = string[:i] + string[i+1:]
    return new_string

# Example usage
my_string = "Hello, World!"
index_to_remove = 7
new_string = remove_ith_character(my_string, index_to_remove)
print("New string:", new_string)


# In[2]:


# Question 7: Python program to split and join a string

def split_and_join(string):
    words = string.split()
    joined_string = '-'.join(words)
    return joined_string

# Example usage
my_string = "Python is a great programming language"
joined_string = split_and_join(my_string)
print("Joined string:", joined_string)


# In[3]:


# Question 8: Python | Check if a given string is a binary string or not

def is_binary_string(string):
    binary_chars = {'0', '1'}
    for char in string:
        if char not in binary_chars:
            return False
    return True

# Example usage
my_string = "10101010"
if is_binary_string(my_string):
    print("String is a binary string.")
else:
    print("String is not a binary string.")


# In[4]:


# Question 9: Python program to find uncommon words from two strings

def find_uncommon_words(string1, string2):
    words1 = string1.split()
    words2 = string2.split()
    uncommon_words = [word for word in words1 + words2 if word not in words1 or word not in words2]
    return uncommon_words

# Example usage
string1 = "Python is a great programming language"
string2 = "Python is used for various applications"
uncommon_words = find_uncommon_words(string1, string2)
print("Uncommon words:", uncommon_words)


# In[5]:


# Question 10: Python - Replace duplicate occurrence in a string

from collections import Counter

def replace_duplicate_occurrence(string):
    frequency = Counter(string.split())
    replaced_string = ' '.join([word if count == 1 else '$' for word, count in frequency.items()])
    return replaced_string

# Example usage
my_string = "Python is great and Python is easy to learn"
replaced_string = replace_duplicate_occurrence(my_string)
print("Replaced string:", replaced_string)


# In[ ]:




