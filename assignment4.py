#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


def find_smallest_number(lst):
    """
    Function to find the smallest number in a list.
    """
    smallest = min(lst)
    return smallest

# Take input from the user for the list elements
lst = input("Enter the list elements (space-separated): ").split()

# Convert the list elements to integers
lst = [int(num) for num in lst]

# Find the smallest number in the list
smallest_number = find_smallest_number(lst)

# Display the smallest number
print("Smallest number in the list:", smallest_number)


# In[3]:


def find_largest_number(lst):
    """
    Function to find the largest number in a list.
    """
    largest = max(lst)
    return largest

# Take input from the user for the list elements
lst = input("Enter the list elements (space-separated): ").split()

# Convert the list elements to integers
lst = [int(num) for num in lst]

# Find the largest number in the list
largest_number = find_largest_number(lst)

# Display the largest number
print("Largest number in the list:", largest_number)


# In[ ]:


def find_second_largest_number(lst):
    """
    Function to find the second largest number in a list.
    """
    sorted_list = sorted(lst)
    second_largest = sorted_list[-2]
    return second_largest

# Take input from the user for the list elements
lst = input("Enter the list elements (space-separated): ").split()

# Convert the list elements to integers
lst = [int(num) for num in lst]

# Find the second largest number in the list
second_largest_number = find_second_largest_number(lst)

# Display the second largest number
print("Second largest number in the list:", second_largest_number)


# In[1]:


def find_n_largest_elements(lst, n):
    """
    Function to find N largest elements from a list.
    """
    sorted_list = sorted(lst, reverse=True)
    n_largest = sorted_list[:n]
    return n_largest

# Take input from the user for the list elements
lst = input("Enter the list elements (space-separated): ").split()

# Convert the list elements to integers
lst = [int(num) for num in lst]

# Take input from the user for N
n = int(input("Enter the value of N: "))

# Find the N largest elements in the list
n_largest_elements = find_n_largest_elements(lst, n)

# Display the N largest elements
print("N largest elements in the list:", n_largest_elements)


# In[2]:


def print_even_numbers(lst):
    """
    Function to print even numbers in a list.
    """
    even_numbers = [num for num in lst if num % 2 == 0]
    return even_numbers

# Take input from the user for the list elements
lst = input("Enter the list elements (space-separated): ").split()

# Convert the list elements to integers
lst = [int(num) for num in lst]

# Print even numbers in the list
even_numbers = print_even_numbers(lst)

# Display the even numbers
print("Even numbers in the list:", even_numbers)


# In[3]:


def print_odd_numbers(lst):
    """
    Function to print odd numbers in a list.
    """
    odd_numbers = [num for num in lst if num % 2 != 0]
    return odd_numbers

# Take input from the user for the list elements
lst = input("Enter the list elements (space-separated): ").split()

# Convert the list elements to integers
lst = [int(num) for num in lst]

# Print odd numbers in the list
odd_numbers = print_odd_numbers(lst)

# Display the odd numbers
print("Odd numbers in the list:", odd_numbers)


# In[4]:


start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Print even numbers in the range
even_numbers = [num for num in range(start, end+1) if num % 2 == 0]

# Display the even numbers
print("Even numbers in the range:", even_numbers)


# In[5]:


start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Print odd numbers in the range
odd_numbers = [num for num in range(start, end+1) if num % 2 != 0]

# Display the odd numbers
print("Odd numbers in the range:", odd_numbers)


# In[6]:


def print_positive_numbers(lst):
    """
    Function to print positive numbers in a list.
    """
    positive_numbers = [num for num in lst if num > 0]
    return positive_numbers

# Take input from the user for the list elements
lst = input("Enter the list elements (space-separated): ").split()

# Convert the list elements to integers
lst = [int(num) for num in lst]

# Print positive numbers in the list
positive_numbers = print_positive_numbers(lst)

# Display the positive numbers
print("Positive numbers in the list:", positive_numbers)


# In[7]:


def print_negative_numbers(lst):
    """
    Function to print negative numbers in a list.
    """
    negative_numbers = [num for num in lst if num < 0]
    return negative_numbers

# Take input from the user for the list elements
lst = input("Enter the list elements (space-separated): ").split()

# Convert the list elements to integers
lst = [int(num) for num in lst]

# Print negative numbers in the list
negative_numbers = print_negative_numbers(lst)

# Display the negative numbers
print("Negative numbers in the list:", negative_numbers)


# In[8]:


start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Print positive numbers in the range
positive_numbers = [num for num in range(start, end+1) if num > 0]

# Display the positive numbers
print("Positive numbers in the range:", positive_numbers)


# In[ ]:


|

