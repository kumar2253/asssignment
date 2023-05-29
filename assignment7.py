#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


# Question 1: Reverse words in a given string in Python

def reverse_words(string):
    words = string.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words

# Example usage
my_string = "Hello, World!"
reversed_string = reverse_words(my_string)
print("Reversed string:", reversed_string)


# In[3]:


# Question 2: Ways to remove i'th character from a string in Python

def remove_ith_character(string, i):
    new_string = string[:i] + string[i+1:]
    return new_string

# Example usage
my_string = "Hello, World!"
index_to_remove = 7
new_string = remove_ith_character(my_string, index_to_remove)
print("New string:", new_string)


# In[4]:


# Question 3: Python | Check if a substring is present in a given string

def is_substring_present(string, substring):
    if substring in string:
        return True
    else:
        return False

# Example usage
my_string = "Hello, World!"
my_substring = "World"
if is_substring_present(my_string, my_substring):
    print("Substring is present in the string.")
else:
    print("Substring is not present in the string.")


# In[5]:


# Question 4: Python - Words frequency in string shorthands

from collections import Counter

def word_frequency(string):
    word_count = Counter(string.split())
    return word_count

# Example usage
my_string = "I love Python programming. Python is my favorite language."
frequency = word_frequency(my_string)
print("Word frequency:")
for word, count in frequency.items():
    print(word, ":", count)


# In[6]:


# Question 5: Python - Convert snake case to Pascal case

def snake_to_pascal_case(snake_case_string):
    words = snake_case_string.split('_')
    pascal_case_string = ''.join(word.capitalize() for word in words)
    return pascal_case_string

# Example usage
my_string = "hello_world"
pascal_case_string = snake_to_pascal_case(my_string)
print("Pascal case string:", pascal_case_string)


# In[7]:


# Question 6: Find length of a string in Python (4 ways)

# Method 1: Using the len() function
def find_length1(string):
    return len(string)

# Method 2: Using a loop to count characters
def find_length2(string):
    count = 0
    for char in string:
        count += 1
    return count

# Method 3: Using recursion
def find_length3(string):
    if string == '':
        return 0
    else:
        return 1 + find_length3(string[1:])

# Method 4: Using the str.__len__() magic method
def find_length4(string):
    return string.__len__()

# Example usage
my_string = "Hello, World!"
print("Length using Method 1:", find_length1(my_string))
print("Length using Method 2:", find_length2(my_string))
print("Length using Method 3:", find_length3(my_string))
print("Length using Method 4:", find_length4(my_string))


# In[8]:


# Question 7: Python program to print even-length words in a string

def print_even_length_words(string):
    words = string.split()
    for word in words:
        if len(word) % 2 == 0:
            print(word)

# Example usage
my_string = "Python is a great programming language"
print("Even-length words:")
print_even_length_words(my_string)


# In[9]:


# Question 8: Python program to accept strings that contain all vowels

def has_all_vowels(string):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for vowel in vowels:
        if vowel not in string.lower():
            return False
    return True

# Example usage
my_string = "The quick brown fox jumps over the lazy dog"
if has_all_vowels(my_string):
    print("String contains all vowels.")
else:
    print("String does not contain all vowels.")


# In[10]:


# Question 9: Python | Count the number of matching characters in a pair of strings

def count_matching_characters(string1, string2):
    count = 0
    for char1, char2 in zip(string1, string2):
        if char1 == char2:
            count += 1
    return count

# Example usage
string1 = "hello"
string2 = "bello"
matching_count = count_matching_characters(string1, string2)
print("Number of matching characters:", matching_count)


# In[11]:


# Question 10: Remove all duplicates from a given string in Python

def remove_duplicates(string):
    result = ""
    for char in string:
        if char not in result:
            result += char
    return result

# Example usage
my_string = "Hello, World!"
unique_string = remove_duplicates(my_string)
print("String with duplicates removed:", unique_string)


# In[ ]:




