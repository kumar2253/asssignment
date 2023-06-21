#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


import re
from datetime import datetime

# 1. Python program to find the difference between the current time and a given time
def time_difference(given_time):
    current_time = datetime.now().time()
    given_time = datetime.strptime(given_time, "%H:%M:%S").time()
    difference = datetime.combine(datetime.today(), current_time) - datetime.combine(datetime.today(), given_time)
    return difference.total_seconds()



# In[3]:






# 2. Python program to create a lap timer
import time

def lap_timer():
    start_time = time.time()
    while True:
        input("Press Enter to record lap time.")
        lap_time = time.time() - start_time
        print("Lap time:", lap_time, "seconds")



# In[4]:



# 3. Convert date string to timestamp in Python
def date_to_timestamp(date_string, format):
    timestamp = datetime.strptime(date_string, format).timestamp()
    return int(timestamp)







# In[5]:


# 4. How to convert timestamp string to datetime object in Python?
def timestamp_to_datetime(timestamp):
    dt_object = datetime.fromtimestamp(timestamp)
    return dt_object



# In[6]:


# 5. Find number of times every day occurs in a year
import calendar

def count_days_in_year(year):
    days_count = [0] * 7
    for month in range(1, 13):
        for day in range(1, calendar.monthrange(year, month)[1] + 1):
            weekday = calendar.weekday(year, month, day)
            days_count[weekday] += 1
    return days_count



# In[7]:


# 6. Python Program to Check if String Contains Only Defined Characters using Regex
def check_string(pattern, input_string):
    if re.match(pattern, input_string):
        return True
    else:
        return False










# In[8]:



# 7. Python program to Count Uppercase, Lowercase, special character, and numeric values using Regex
def count_characters(input_string):
    uppercase_count = len(re.findall(r'[A-Z]', input_string))
    lowercase_count = len(re.findall(r'[a-z]', input_string))
    special_char_count = len(re.findall(r'[^A-Za-z0-9]', input_string))
    numeric_count = len(re.findall(r'[0-9]', input_string))
    return uppercase_count, lowercase_count, special_char_count, numeric_count


# In[9]:


# 8. Python Program to find the most occurring number in a string using Regex
def find_most_occurring_number(input_string):
    numbers = re.findall(r'\d+', input_string)
    if numbers:
        count_dict = {}
        for number in numbers:
            count_dict[number] = count_dict.get(number, 0) + 1
        most_occurring_number = max(count_dict, key=count_dict.get)
        return int(most_occurring_number)
    else:
        return None


# In[10]:


# 9. Python Regex to extract the maximum numeric value from a string
def extract_maximum_numeric_value(input_string):
    numbers = re.findall(r'\d+', input_string)
    if numbers:
        max_numeric_value = max(map(int, numbers))
        return max_numeric_value
    else:
        return None


# In[11]:



# 10. Python Program to put spaces between words starting with capital letters using Regex
def put_spaces(input_string):
    output_string = re.sub(r"(\w)([A-Z])", r"\1 \2", input_string)
    return output_string


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




