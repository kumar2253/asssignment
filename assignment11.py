#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


# Question 1: Python - Sort Dictionary key and values List

def sort_dict_key_values(dictionary):
    sorted_dict = dict(sorted(dictionary.items()))
    sorted_values = [value for _, value in sorted_dict.items()]
    return sorted_values

# Example usage
my_dict = {'c': [4, 2, 3], 'a': [1, 5, 6], 'b': [7, 8, 9]}
sorted_values = sort_dict_key_values(my_dict)
print("Sorted values:", sorted_values)


# In[3]:


# Question 2: Handling missing keys in Python dictionaries

def get_value(dictionary, key, default=None):
    try:
        return dictionary[key]
    except KeyError:
        return default

# Example usage
my_dict = {'a': 1, 'b': 2, 'c': 3}
value = get_value(my_dict, 'd', default='Key not found')
print("Value:", value)


# In[4]:


# Question 3: Python dictionary with keys having multiple inputs

def create_dict(keys, values):
    my_dict = {}
    for key, value in zip(keys, values):
        if key in my_dict:
            my_dict[key].append(value)
        else:
            my_dict[key] = [value]
    return my_dict

# Example usage
keys = ['a', 'b', 'a', 'c', 'b']
values = [1, 2, 3, 4, 5]
my_dict = create_dict(keys, values)
print("Dictionary:", my_dict)


# In[5]:


# Question 4: Print anagrams together in Python using List and Dictionary

def group_anagrams(words):
    anagram_dict = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    grouped_anagrams = list(anagram_dict.values())
    return grouped_anagrams

# Example usage
word_list = ['cat', 'dog', 'tac', 'god', 'act']
anagram_groups = group_anagrams(word_list)
print("Anagram groups:", anagram_groups)


# In[6]:


# Question 5: K'th Non-repeating Character in Python using List Comprehension and OrderedDict

from collections import OrderedDict

def get_kth_non_repeating_char(string, k):
    char_count = OrderedDict()
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1
    non_repeating_chars = [char for char, count in char_count.items() if count == 1]
    if len(non_repeating_chars) >= k:
        return non_repeating_chars[k - 1]
    return None

# Example usage
my_string = 'hello world'
k = 2
kth_non_repeating_char = get_kth_non_repeating_char(my_string, k)
print("K'th non-repeating character:", kth_non_repeating_char)


# In[7]:


# Question 6: String slicing in Python to check if a string can become empty by recursive deletion

def check_empty_string(string):
    if len(string) == 0:
        return True
    for i in range(len(string)):
        modified_string = string[:i] + string[i+1:]
        if check_empty_string(modified_string):
            return True
    return False

# Example usage
my_string = "abcde"
is_empty = check_empty_string(my_string)
print("Can the string become empty?", is_empty)


# In[8]:


# Question 7: Python Counter to find the size of the largest subset of anagram words

from collections import Counter

def largest_anagram_subset(words):
    word_counts = [Counter(word) for word in words]
    max_subset_size = 0
    for i in range(len(words)):
        subset_size = 0
        for j in range(i+1, len(words)):
            if word_counts[i] == word_counts[j]:
                subset_size += 1
        if subset_size > max_subset_size:
            max_subset_size = subset_size
    return max_subset_size + 1

# Example usage
word_list = ['cat', 'dog', 'tac', 'god', 'act', 'good']
subset_size = largest_anagram_subset(word_list)
print("Largest subset size:", subset_size)


# In[9]:


# Question 8: Python | Remove all duplicate words from a given sentence

def remove_duplicate_words(sentence):
    words = sentence.split()
    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    return ' '.join(unique_words)

# Example usage
my_sentence = 'Python is great and Python is easy to learn'
unique_sentence = remove_duplicate_words(my_sentence)
print("Sentence without duplicate words:", unique_sentence)


# In[10]:


# Question 9: Python Dictionary to find mirror characters in a string

def find_mirror_characters(string):
    mirror_dict = {'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p'}
    mirrored_chars = []
    for char in string:
        if char in mirror_dict:
            mirrored_chars.append(mirror_dict[char])
    return mirrored_chars

# Example usage
my_string = 'bdpq'
mirrored_chars = find_mirror_characters(my_string)
print("Mirrored characters:", mirrored_chars)


# In[11]:


# Question 10: Counting the frequencies in a list using a dictionary in Python

def count_frequencies(my_list):
    freq_dict = {}
    for item in my_list:
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1
    return freq_dict

# Example usage
my_list = [1, 2, 3, 2, 1, 3, 4, 5, 1]
frequencies = count_frequencies(my_list)
print("Frequencies:", frequencies)


# In[ ]:




