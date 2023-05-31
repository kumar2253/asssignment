#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


# Question 1: Python Program for Cycle Sort

def cycle_sort(arr):
    n = len(arr)
    for cycle_start in range(n - 1):
        item = arr[cycle_start]
        pos = cycle_start
        for i in range(cycle_start + 1, n):
            if arr[i] < item:
                pos += 1
        if pos == cycle_start:
            continue
        while item == arr[pos]:
            pos += 1
        arr[pos], item = item, arr[pos]
        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start + 1, n):
                if arr[i] < item:
                    pos += 1
            while item == arr[pos]:
                pos += 1
            arr[pos], item = item, arr[pos]

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
cycle_sort(arr)
print("Sorted array:", arr)


# In[3]:


# Question 2: Python Program for Stooge Sort

def stooge_sort(arr, low, high):
    if low >= high:
        return
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if high - low + 1 > 2:
        third = (high - low + 1) // 3
        stooge_sort(arr, low, high - third)
        stooge_sort(arr, low + third, high)
        stooge_sort(arr, low, high - third)

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
stooge_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)


# In[4]:


# Question 3: Python Program to print the pattern 'G'

def print_pattern_G():
    pattern = [
        "  *****",
        " *      ",
        "*       ",
        "*   *** ",
        "*     * ",
        " *   *  ",
        "  ***   "
    ]
    for line in pattern:
        print(line)

# Example usage
print_pattern_G()


# In[5]:


# Question 4: Python Program to print an Inverted Star Pattern

def print_inverted_star_pattern(rows):
    for i in range(rows, 0, -1):
        print("*" * i)

# Example usage
print_inverted_star_pattern(5)


# In[7]:


# Question 6: Python Program to print with your own font

def print_with_custom_font(text):
    font = {
        'A': ['  A  ', ' A A ', 'AAAAA', 'A   A', 'A   A'],
        'B': ['BBBB ', 'B   B', 'BBBB ', 'B   B', 'BBBB '],
        'C': [' CCCC', 'C    ', 'C    ', 'C    ', ' CCCC'],
        # Add more letters and their corresponding font representation here
    }

    for row in range(5):
        for char in text.upper():
            if char in font:
                print(font[char][row], end=' ')
            else:
                print('     ', end=' ')
        print()

# Example usage
input_text = input("Enter a string: ")
print_with_custom_font(input_text)


# In[8]:


# Question 7: Get Current Date and Time using Python

import datetime

def get_current_date_time():
    current_date_time = datetime.datetime.now()
    print("Current Date and Time:", current_date_time)

# Example usage
get_current_date_time()


# In[9]:


# Question 8: Python | Find yesterday's, today's and tomorrow's date

import datetime

def get_dates():
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    tomorrow = today + datetime.timedelta(days=1)
    
    print("Yesterday's date:", yesterday)
    print("Today's date:", today)
    print("Tomorrow's date:", tomorrow)

# Example usage
get_dates()


# In[ ]:


# Question 9: Python program to convert time from 12-hour to 24-hour format

def convert_to_24_hour_format(time):
    # Split the time into hours, minutes, and period (AM/PM)
    hours, minutes, period = time.split(':')
    
    # Check if the period is AM and adjust the hours accordingly
    if period.lower() == 'am':
        if hours == '12':
            hours = '00'
    # Check if the period is PM and adjust the hours accordingly
    elif period.lower() == 'pm':
        if hours != '12':
            hours = str(int(hours) + 12)
    
    # Return the time in 24-hour format
    return hours + ':' + minutes

# Example usage
time_12_hour = input("Enter time in 12-hour format (HH:MM AM/PM): ")
time_24_hour = convert_to_24_hour_format(time_12_hour)
print("Time in 24-hour format:", time_24_hour)


# In[ ]:


# Question 10: Python program to find the sum of all items in a dictionary

def sum_dictionary_items(dictionary):
    total_sum = sum(dictionary.values())
    return total_sum

# Example usage
my_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
result = sum_dictionary_items(my_dict)
print("Sum of dictionary items:", result)


# In[ ]:




