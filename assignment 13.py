#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


# Question 1: Python - Join Tuples if similar initial element

def join_tuples(tuples_list):
    result = []
    current_tuple = ()
    for tuple_item in tuples_list:
        if not current_tuple:
            current_tuple = tuple_item
        elif current_tuple[0] == tuple_item[0]:
            current_tuple += tuple_item[1:]
        else:
            result.append(current_tuple)
            current_tuple = tuple_item
    result.append(current_tuple)
    return result

# Example usage
tuples_list = [(1, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (3, 'e')]
joined_tuples = join_tuples(tuples_list)
print("Joined tuples:", joined_tuples)


# In[3]:


# Question 2: Python - Extract digits from Tuple list

def extract_digits(tuples_list):
    digits = []
    for tuple_item in tuples_list:
        for item in tuple_item:
            if isinstance(item, int):
                digits.append(item)
    return digits

# Example usage
tuples_list = [(1, 'a', 2), ('b', 3, 'c'), (4, 5, 'd')]
extracted_digits = extract_digits(tuples_list)
print("Extracted digits:", extracted_digits)


# In[4]:


# Question 3: Python - All pair combinations of 2 tuples

def get_all_pairs(tuple1, tuple2):
    pairs = []
    for item1 in tuple1:
        for item2 in tuple2:
            pairs.append((item1, item2))
    return pairs

# Example usage
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
all_pairs = get_all_pairs(tuple1, tuple2)
print("All pairs:", all_pairs)


# In[5]:


# Question 4: Python - Remove Tuples of Length K

def remove_tuples_of_length_k(tuples_list, k):
    filtered_list = [tuple_item for tuple_item in tuples_list if len(tuple_item) != k]
    return filtered_list

# Example usage
tuples_list = [(1, 2), (3, 4, 5), (6,), (7, 8, 9, 10), (11,)]
k = 2
filtered_tuples = remove_tuples_of_length_k(tuples_list, k)
print("Filtered tuples:", filtered_tuples)


# In[6]:


# Question 5: Sort a list of tuples by second Item

def sort_by_second_item(tuples_list):
    sorted_list = sorted(tuples_list, key=lambda x: x[1])
    return sorted_list

# Example usage
tuples_list = [(3, 'b'), (1, 'a'), (2, 'c'), (4, 'd')]
sorted_tuples = sort_by_second_item(tuples_list)
print("Sorted tuples:", sorted_tuples)


# In[7]:


# Question 6: Python - Keys associated with Values in Dictionary

def get_keys_by_value(dictionary, value):
    keys = []
    for key, val in dictionary.items():
        if val == value:
            keys.append(key)
    return keys

# Example usage
my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
value = 1
keys = get_keys_by_value(my_dict, value)
print("Keys associated with value", value, ":", keys)


# In[8]:


# Question 7: Python program to Find the size of a Tuple

def get_tuple_size(tuple_obj):
    return len(tuple_obj)

# Example usage
my_tuple = (1, 2, 3, 'a', 'b', 'c')
tuple_size = get_tuple_size(my_tuple)
print("Size of the tuple:", tuple_size)


# In[9]:


# Question 8: Python - Maximum and Minimum K elements in Tuple

def get_max_min_k_elements(tuple_obj, k):
    max_k = sorted(tuple_obj)[-k:]
    min_k = sorted(tuple_obj)[:k]
    return max_k, min_k

# Example usage
my_tuple = (9, 1, 5, 2, 8, 3, 7, 6, 4)
k = 3
max_k_elements, min_k_elements = get_max_min_k_elements(my_tuple, k)
print("Maximum", k, "elements:", max_k_elements)
print("Minimum", k, "elements:", min_k_elements)


# In[10]:


# Question 9: Create a list of tuples from a given list, with each tuple containing a number and its cube

def create_tuple_list(numbers):
    tuple_list = [(num, num ** 3) for num in numbers]
    return tuple_list

# Example usage
numbers = [1, 2, 3, 4, 5]
tuple_list = create_tuple_list(numbers)
print("List of tuples:", tuple_list)


# In[11]:


# Question 10: Python - Adding Tuple to List and vice versa

def add_tuple_to_list(tuple_obj, list_obj):
    list_obj.append(tuple_obj)
    return list_obj

def add_list_to_tuple(list_obj, tuple_obj):
    return tuple_obj + tuple(list_obj)

# Example usage
tuple_obj = (1, 2)
list_obj = [3, 4, 5]
updated_list = add_tuple_to_list(tuple_obj, list_obj)
print("Updated list:", updated_list)

list_obj = [6, 7, 8]
tuple_obj = (9, 10)
updated_tuple = add_list_to_tuple(list_obj, tuple_obj)
print("Updated tuple:", updated_tuple)


# In[12]:


# Question 11: Python - Closest Pair to Kth index element in Tuple

def closest_pair_to_kth_index(tuples_list, k):
    kth_element = tuples_list[k]
    closest_pair = None
    closest_distance = float('inf')
    for tuple_item in tuples_list:
        if tuple_item != kth_element:
            distance = abs(kth_element - tuple_item)
            if distance < closest_distance:
                closest_distance = distance
                closest_pair = tuple_item
    return closest_pair

# Example usage
tuples_list = (1, 3, 5, 7, 9)
k = 2
closest_pair = closest_pair_to_kth_index(tuples_list, k)
print("Closest pair to kth index element:", closest_pair)


# In[ ]:




