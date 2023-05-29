#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 
import numpy as np


# In[3]:


def print_negative_numbers(start, end):
    negative_numbers = [num for num in range(start, end+1) if num < 0]
    print("Negative numbers:", negative_numbers)

print_negative_numbers(-5, 5)


# In[4]:


def remove_elements(lst, elements):
    lst = [x for x in lst if x not in elements]
    return lst

my_list = [1, 2, 3, 4, 5]
elements_to_remove = [2, 4]
updated_list = remove_elements(my_list, elements_to_remove)
print("Updated list:", updated_list)


# In[5]:


def remove_empty_lists(lst):
    lst = [sublist for sublist in lst if sublist]
    return lst

my_list = [1, [], [2, 3], [], [4, 5, 6], []]
updated_list = remove_empty_lists(my_list)
print("Updated list:", updated_list)


# In[6]:


def clone_list(lst):
    cloned_list = lst.copy()
    return cloned_list

my_list = [1, 2, 3, 4, 5]
cloned_list = clone_list(my_list)
print("Cloned list:", cloned_list)


# In[7]:


def count_occurrences(lst, element):
    count = lst.count(element)
    return count

my_list = [1, 2, 3, 4, 2, 2, 5, 2]
element_to_count = 2
occurrences = count_occurrences(my_list, element_to_count)
print("Occurrences of", element_to_count, "in the list:", occurrences)


# In[8]:


# Question 6: Python program to remove empty tuples from a list

def remove_empty_tuples(lst):
    lst = [tup for tup in lst if tup]
    return lst

# Example usage
my_list = [(1, 2), (), (3, 4), (), (5, 6, 7), ()]
updated_list = remove_empty_tuples(my_list)
print("Updated list:", updated_list)


# In[9]:


# Question 7: Python program to print duplicates from a list of integers

def find_duplicates(lst):
    duplicates = []
    for num in lst:
        if lst.count(num) > 1 and num not in duplicates:
            duplicates.append(num)
    return duplicates

# Example usage
my_list = [1, 2, 3, 4, 2, 5, 6, 3, 4]
duplicate_values = find_duplicates(my_list)
print("Duplicate values:", duplicate_values)


# In[10]:


# Question 8: Python program to find cumulative sum of a list

def cumulative_sum(lst):
    cumulative_sum = []
    total = 0
    for num in lst:
        total += num
        cumulative_sum.append(total)
    return cumulative_sum

# Example usage
my_list = [1, 2, 3, 4, 5]
cumulative_sum_list = cumulative_sum(my_list)
print("Cumulative sum list:", cumulative_sum_list)


# In[11]:


# Question 8: Python program to find cumulative sum of a list

def cumulative_sum(lst):
    cumulative_sum = []
    total = 0
    for num in lst:
        total += num
        cumulative_sum.append(total)
    return cumulative_sum

# Example usage
my_list = [1, 2, 3, 4, 5]
cumulative_sum_list = cumulative_sum(my_list)
print("Cumulative sum list:", cumulative_sum_list)


# In[12]:


# Question 9: Python program to find sum of number digits in a list

def sum_of_digits(lst):
    total_sum = 0
    for num in lst:
        total_sum += sum([int(digit) for digit in str(num)])
    return total_sum

# Example usage
my_list = [123, 456, 789]
digits_sum = sum_of_digits(my_list)
print("Sum of digits:", digits_sum)


# In[13]:


# Question 10: Python program to break a list into chunks of size N

def break_into_chunks(lst, chunk_size):
    chunked_list = [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]
    return chunked_list

# Example usage
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
chunk_size = 3
chunked_list = break_into_chunks(my_list, chunk_size)
print("Chunked list:", chunked_list)


# In[14]:


# Question 11: Python program to sort the values of the first list using the second list

def sort_first_list_using_second(first_list, second_list):
    zipped_lists = zip(second_list, first_list)
    sorted_list = [x for _, x in sorted(zipped_lists)]
    return sorted_list

# Example usage
first_list = [4, 2, 1, 3]
second_list = ['d', 'b', 'a', 'c']
sorted_first_list = sort_first_list_using_second(first_list, second_list)
print("Sorted first list:", sorted_first_list)


# In[ ]:




