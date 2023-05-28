#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


def find_remainder(arr, n):
    """
    Function to find the remainder of the multiplication of array elements divided by n.
    """
    result = 1

    # Calculate the product of array elements
    for num in arr:
        result = (result * num) % n

    return result


# Take input from the user for the array elements
array = input("Enter the array elements (space-separated): ").split()

# Convert the array elements to integers
array = [int(num) for num in array]

# Take input from the user for the divisor
divisor = int(input("Enter the divisor: "))

# Find the remainder of the multiplication of array elements divided by the divisor
remainder = find_remainder(array, divisor)

# Display the remainder
print("Remainder of the multiplication of array elements divided by", divisor, "is", remainder)


# In[3]:


def is_monotonic(arr):
    """
    Function to check if an array is monotonic.
    """
    increasing = decreasing = True

    # Check if the array is increasing or decreasing
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            increasing = False
        if arr[i] > arr[i - 1]:
            decreasing = False

    # Return True if the array is either increasing or decreasing
    return increasing or decreasing


# Take input from the user for the array elements
array = input("Enter the array elements (space-separated): ").split()

# Convert the array elements to integers
array = [int(num) for num in array]

# Check if the array is monotonic
if is_monotonic(array):
    print("The array is monotonic.")
else:
    print("The array is not monotonic.")


# In[4]:


def interchange_first_last(lst):
    """
    Function to interchange the first and last elements in a list.
    """
    if len(lst) >= 2:
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst


# Take input from the user for the list elements
lst = input("Enter the list elements (space-separated): ").split()

# Interchange the first and last elements in the list
interchanged_lst = interchange_first_last(lst)

# Display the list after interchange
print("List after interchange:", interchanged_lst)


# In[5]:


def swap_elements(lst, index1, index2):
    """
    Function to swap two elements in a list given their indices.
    """
    lst[index1], lst[index2] = lst[index2], lst[index1]
    return lst


# Take input from the user for the list elements
lst = input("Enter the list elements (space-separated): ").split()

# Take input from the user for the indices of elements to swap
index1 = int(input("Enter the index of the first element: "))
index2 = int(input("Enter the index of the second element: "))

# Swap the elements in the list
swapped_lst = swap_elements(lst, index1, index2)

# Display the list after swapping
print("List after swapping:", swapped_lst)


# In[6]:


def find_list_length(lst):
    """
    Function to find the length of a list.
    """
    length = len(lst)
    return length


# Take input from the user for the list elements
lst = input("Enter the list elements (space-separated): ").split()

# Find the length of the list
list_length = find_list_length(lst)

# Display the length of the list
print("Length of the list:", list_length)


# In[7]:


def check_element_in_list(lst, element):
    """
    Function to check if an element exists in a list.
    """
    if element in lst:
        return True
    else:
        return False


# Take input from the user for the list elements
lst = input("Enter the list elements (space-separated): ").split()

# Take input from the user for the element to check
element = input("Enter the element to check: ")

# Check if the element exists in the list
if check_element_in_list(lst, element):
    print("Element", element, "exists in the list.")
else:
    print("Element", element, "does not exist in the list.")


# In[8]:


def clear_list(lst):
    """
    Function to clear a list.
    """
    lst.clear()


# Take input from the user for the list elements
lst = input("Enter the list elements (space-separated): ").split()

# Clear the list
clear_list(lst)

# Display the cleared list
print("List after clearing:", lst)


# In[9]:


def reverse_list(lst):
    """
    Function to reverse a list.
    """
    reversed_lst = lst[::-1]
    return reversed_lst


# Take input from the user for the list elements
lst = input("Enter the list elements (space-separated): ").split()

# Reverse the list
reversed_list = reverse_list(lst)

# Display the reversed list
print("Reversed list:", reversed_list)


# In[10]:


def find_sum(lst):
    """
    Function to find the sum of elements in a list.
    """
    total = sum(lst)
    return total


# Take input from the user for the list elements
lst = input("Enter the list elements (space-separated): ").split()

# Convert the list elements to integers
lst = [int(num) for num in lst]

# Find the sum of elements in the list
sum_of_elements = find_sum(lst)

# Display the sum of elements
print("Sum of elements in the list:", sum_of_elements)


# In[11]:


def multiply_list(lst):
    """
    Function to multiply all numbers in a list.
    """
    result = 1
    for num in lst:
        result *= num
    return result


# Take input from the user for the list elements
lst = input("Enter the list elements (space-separated): ").split()

# Convert the list elements to integers
lst = [int(num) for num in lst]

# Multiply all numbers in the list
product = multiply_list(lst)

# Display the product
print("Product of numbers in the list:", product)


# In[ ]:




