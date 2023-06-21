#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False

email_address = input("Enter an email address: ")
if is_valid_email(email_address):
    print("Valid email address")
else:
    print("Invalid email address")


# In[3]:


import re
import os

def find_files_with_extension(directory, extension):
    pattern = r'.*\.' + re.escape(extension) + '$'
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            if re.match(pattern, filename):
                files.append(os.path.join(root, filename))
    return files

directory = input("Enter the directory path: ")
extension = input("Enter the file extension: ")
result = find_files_with_extension(directory, extension)
if result:
    print("Files with the extension '{}' found:".format(extension))
    for file_path in result:
        print(file_path)
else:
    print("No files with the extension '{}' found.".format(extension))


# In[ ]:


import re

def extract_ip_addresses(file_path):
    pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    ip_addresses = []
    with open(file_path, 'r') as file:
        for line in file:
            matches = re.findall(pattern, line)
            ip_addresses.extend(matches)
    return ip_addresses

file_path = input("Enter the file path: ")
ip_addresses = extract_ip_addresses(file_path)
if ip_addresses:
    print("IP addresses found in the file:")
    for ip_address in ip_addresses:
        print(ip_address)
else:
    print("No IP addresses found in the file.")


# In[ ]:


import re

def is_valid_password(password):
    pattern = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'
    if re.match(pattern, password):
        return True
    else:
        return False

password = input("Enter a password: ")
if is_valid_password(password):
    print("Valid password")
else:
    print("Invalid password")


# In[ ]:


file_path = input("Enter the file path: ")
with open(file_path, 'r') as file:
    for line in file:
        words = line.split()
        for word in words:
            print(word)


# In[ ]:


file_path = input("Enter the file path: ")
with open(file_path, 'r') as file:
    while True:
        char = file.read(1)
        if not char:
            break
        print(char)


# In[ ]:


file_path = input("Enter the file path: ")
with open(file_path, 'r') as file:
    text = file.read()
    character_count = len(text)
    word_count = len(text.split())
    space_count = text.count(' ')
    line_count = text.count('\n')
    print("Number of characters:", character_count)
    print("Number of words:", word_count)
    print("Number of spaces:", space_count)
    print("Number of lines:", line_count)


# In[ ]:


def count_key_value_pairs(file_path, key, value):
    count = 0
    with open(file_path, 'r') as file:
        for line in file:
            if key in line and value in line:
                count += 1
    return count

file_path = input("Enter the file path: ")
key = input("Enter the key: ")
value = input("Enter the value: ")
count = count_key_value_pairs(file_path, key, value)
print("Number of occurrences:", count)


# In[ ]:


import re

def find_n_character_words(file_path, n):
    pattern = r'\b\w{' + str(n) + r'}\b'
    words = set()
    with open(file_path, 'r') as file:
        for line in file:
            matches = re.findall(pattern, line)
            words.update(matches)
    return words

file_path = input("Enter the file path: ")
n = int(input("Enter the number of characters: "))
result = find_n_character_words(file_path, n)
if result:
    print("Words with {} characters found in the file:".format(n))
    for word in result:
        print(word)
else:
    print("No words with {} characters found in the file.".format(n))


# In[ ]:




