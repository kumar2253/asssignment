#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


# Question 1: Python | Convert a list of Tuples into Dictionary

def convert_to_dictionary(tuple_list):
    dictionary = dict(tuple_list)
    return dictionary

# Example usage
my_tuple_list = [('a', 1), ('b', 2), ('c', 3)]
my_dictionary = convert_to_dictionary(my_tuple_list)
print("Dictionary:", my_dictionary)


# In[3]:


# Question 2: Python counter and dictionary intersection example (Make a string using deletion and rearrangement)

from collections import Counter

def make_string(deleted, rearranged):
    deleted_counter = Counter(deleted)
    rearranged_counter = Counter(rearranged)
    intersection = deleted_counter & rearranged_counter
    result = ''.join(sorted(intersection.elements()))
    return result

# Example usage
deleted = "apple"
rearranged = "plape"
result_string = make_string(deleted, rearranged)
print("Result string:", result_string)


# In[4]:


# Question 3: Python dictionary, set, and counter to check if frequencies can become the same

from collections import Counter

def check_same_frequencies(my_list):
    frequency_counter = Counter(my_list)
    frequency_values = set(frequency_counter.values())
    return len(frequency_values) == 1

# Example usage
my_list = [1, 1, 2, 2, 2, 3]
same_frequencies = check_same_frequencies(my_list)
print("Do the frequencies match?", same_frequencies)


# In[5]:


# Question 4: Scraping And Finding Ordered Words In A Dictionary using Python
# This question involves web scraping and dictionary manipulation. It requires external libraries like BeautifulSoup and requests.

import requests
from bs4 import BeautifulSoup

def scrape_ordered_words(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Parse the HTML response
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the dictionary words on the page
    words = soup.find_all('li')
    
    ordered_words = []
    
    # Iterate through the words and check if they are in alphabetical order
    for word in words:
        word_text = word.text.strip()
        if is_ordered_word(word_text):
            ordered_words.append(word_text)
    
    return ordered_words

def is_ordered_word(word):
    # Check if the characters in the word are in ascending order
    return list(word) == sorted(word)

# Example usage
url = 'https://www.example.com/dictionary'
ordered_words = scrape_ordered_words(url)
print("Ordered words:", ordered_words)


# In[6]:


# Question 5: Possible Words using given characters in Python

from itertools import permutations

def get_possible_words(characters):
    character_list = list(characters)
    possible_words = []
    for r in range(1, len(character_list) + 1):
        permutations_list = permutations(character_list, r)
        possible_words += [''.join(word) for word in permutations_list]
    return possible_words

# Example usage
given_characters = "abc"
words = get_possible_words(given_characters)
print("Possible words:", words)


# In[7]:


# Question 7: Python program to Find the size of a Tuple

def get_tuple_size(my_tuple):
    return len(my_tuple)

# Example usage
my_tuple = (1, 2, 3, 4, 5)
tuple_size = get_tuple_size(my_tuple)
print("Tuple size:", tuple_size)


# In[8]:


# Question 8: Python - Maximum and Minimum K elements in Tuple

def find_k_maximum_minimum_elements(my_tuple, k):
    sorted_tuple = sorted(my_tuple)
    maximum_elements = sorted_tuple[-k:]
    minimum_elements = sorted_tuple[:k]
    return maximum_elements, minimum_elements

# Example usage
my_tuple = (5, 3, 9, 1, 7, 2, 8, 4, 6)
k = 3
max_elements, min_elements = find_k_maximum_minimum_elements(my_tuple, k)
print("Maximum elements:", max_elements)
print("Minimum elements:", min_elements)


# In[9]:


# Question 9: Create a list of tuples from the given list having a number and its cube in each tuple

def create_tuple_list(numbers):
    tuple_list = [(num, num ** 3) for num in numbers]
    return tuple_list

# Example usage
numbers = [1, 2, 3, 4, 5]
tuple_list = create_tuple_list(numbers)
print("Tuple list:", tuple_list)


# In[10]:


# Question 10: Python - Adding Tuple to List and vice versa

def add_tuple_to_list(my_tuple, my_list):
    new_list = my_list + list(my_tuple)
    return new_list

def add_list_to_tuple(my_list, my_tuple):
    new_tuple = tuple(my_tuple) + tuple(my_list)
    return new_tuple

# Example usage
my_tuple = (1, 2, 3)
my_list = [4, 5, 6]
updated_list = add_tuple_to_list(my_tuple, my_list)
updated_tuple = add_list_to_tuple(my_list, my_tuple)
print("Updated list:", updated_list)
print("Updated tuple:", updated_tuple)


# In[11]:


# Question 11: Python - Closest Pair to Kth index element in Tuple

def find_closest_pair(tuple_list, k):
    closest_pair = None
    min_distance = float('inf')
    for i, pair in enumerate(tuple_list):
        distance = abs(pair[0] - pair[1])
        if distance < min_distance:
            min_distance = distance
            closest_pair = pair
    return closest_pair

# Example usage
my_tuple_list = [(2, 5), (8, 10), (4, 6), (1, 9)]
k = 2
closest_pair = find_closest_pair(my_tuple_list, k)
print("Closest pair to kth index element:", closest_pair)


# In[ ]:




