#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


numbers = []
for num in range(1500, 2701):
    if num % 7 == 0 and num % 5 == 0:
        numbers.append(num)
print("Numbers divisible by 7 and multiple of 5 between 1500 and 2700:")
print(numbers)


# In[3]:


word = input("Enter a word: ")
reversed_word = word[::-1]
print("Reversed word:", reversed_word)


# In[4]:


human_years = int(input("Enter the dog's age in human years: "))
if human_years < 0:
    print("Invalid input. Age must be a positive number.")
elif human_years <= 2:
    dog_years = human_years * 10.5
else:
    dog_years = 21 + (human_years - 2) * 4
print("The dog's age in dog's years is:", dog_years)


# In[5]:


import inspect

def get_local_variables(func):
    _, _, _, locals_dict = inspect.getargvalues(inspect.currentframe().f_back)
    return len(locals_dict)

def example_function():
    variable1 = 10
    variable2 = "Hello"
    variable3 = [1, 2, 3]
    print("Number of local variables:", get_local_variables(example_function))

example_function()


# In[6]:


code_string = '''
def hello_world():
    print("Hello, World!")

hello_world()
'''

exec(code_string)


# In[7]:


list_of_tuples = [('apple', 'banana'), ('orange', 'grape'), ('watermelon', 'kiwi')]
list_of_strings = list(map(lambda x: ' '.join(x), list_of_tuples))
print("List of strings:", list_of_strings)


# In[8]:


dictionary_of_lists = {
    'name': ['John', 'Alice', 'Bob'],
    'age': [25, 30, 35],
    'city': ['New York', 'London', 'Paris']
}
list_of_dictionaries = list(map(lambda x: {key: value for key, value in zip(dictionary_of_lists.keys(), x)},
                               zip(*dictionary_of_lists.values())))
print("List of dictionaries:")
for dictionary in list_of_dictionaries:
    print(dictionary)


# In[ ]:


import os

def scan_directory(directory_path):
    subdirectories = []
    files = []
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        if os.path.isdir(item_path):
            subdirectories.append(item)
        else:
            files.append(item)
    print("Subdirectories:", subdirectories)
    print("Files:", files)

directory_path = input("Enter the directory path: ")
scan_directory(directory_path)


# In[ ]:


import time

time_string = input("Enter the time string (e.g., 10:30 PM): ")
structured_time = time.strptime(time_string, "%I:%M %p")
print("Structured Time:")
print("Hour:", structured_time.tm_hour)
print("Minute:", structured_time.tm_min)
print("Second:", structured_time.tm_sec)


# In[ ]:


import urllib.parse
import urllib.request

data = {'key1': 'value1', 'key2': 'value2'}
query_string = urllib.parse.urlencode(data)
url = 'http://www.example.com/?' + query_string
response = urllib.request.urlopen(url)
print(response.read())


# In[ ]:


import urllib.request

url = input("Enter the URL: ")
response = urllib.request.urlopen(url)
headers = response.headers
print("Header Information:")
for key, value in headers.items():
    print(key, ":", value)

parsed_headers = dict(headers._headers)
print("Parsed Headers:")
for key, value in parsed_headers.items():
    print(key, ":", value)


# In[ ]:


import csv

dictionary = {'Name': 'John', 'Age': 25, 'City': 'New York'}

file_path = 'data.csv'
with open(file_path, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=dictionary.keys())
    writer.writeheader()
    writer.writerow(dictionary)

print("Dictionary written to CSV file.")

with open(file_path, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


# In[ ]:


import csv

file_path = 'data.csv'
with open(file_path, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    data = list(reader)

print("Number of Rows:", len(data))
print("Field Names:", header)


# In[ ]:


import re

string = input("Enter a string: ")
if re.match(r'^[a-zA-Z0-9]+$', string):
    print("The string contains only a-z, A-Z, and 0-9.")
else:
    print("The string contains other characters as well.")


# In[ ]:




