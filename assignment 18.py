#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


def starts_ends_same(string):
    return string[0] == string[-1]

# Example usage:
print(starts_ends_same("hello"))  # False
print(starts_ends_same("level"))  # True


# In[3]:


def starts_ends_same(string):
    return string[0] == string[-1]

# Example usage:
print(starts_ends_same("hello"))  # False
print(starts_ends_same("level"))  # True


# In[4]:


def remove_duplicates(sentence):
    words = sentence.split()
    unique_words = list(set(words))
    return ' '.join(unique_words)

# Example usage:
sentence = "This is is a sample sentence with duplicate words"
result = remove_duplicates(sentence)
print(result)  # "This is a sample sentence with duplicate words"


# In[5]:


import re

def remove_special_chars(string):
    pattern = r'[^a-zA-Z0-9]'
    cleaned_string = re.sub(pattern, '', string)
    return cleaned_string

# Example usage:
text = "Th1s !s @n ex#mpl3"
cleaned_text = remove_special_chars(text)
print(cleaned_text)  # "Th1s s n exmpl3"


# In[6]:


import re

def ends_with_alphanumeric(string):
    pattern = r'^.*[a-zA-Z0-9]$'
    match = re.match(pattern, string)
    return match is not None

# Example usage:
print(ends_with_alphanumeric("Hello123"))  # True
print(ends_with_alphanumeric("abc@123"))  # False


# In[7]:


import re

def starts_with_vowel(string):
    pattern = r'^[aeiouAEIOU].*'
    match = re.match(pattern, string)
    return match is not None

# Example usage:
print(starts_with_vowel("apple"))  # True
print(starts_with_vowel("banana"))  # False


# In[8]:


import re

def starts_with_substring(string, substring):
    pattern = r'^' + re.escape(substring)
    match = re.match(pattern, string)
    return match is not None

# Example usage:
print(starts_with_substring("Hello, World!", "Hello"))  # True
print(starts_with_substring("Goodbye, World!", "Hello"))  # False


# In[9]:


import re

def is_valid_url(url):
    pattern = r'^(http|https)://[^\s/$.?#].[^\s]*$'
    match = re.match(pattern, url)
    return match is not None

# Example usage:
print(is_valid_url("http://www.example.com"))  # True
print(is_valid_url("invalid-url"))  # False


# In[10]:


from urllib.parse import urlparse

url = "http://www.example.com/path?param=value#fragment"
parsed_url = urlparse(url)

print(parsed_url.scheme)  # "http"
print(parsed_url.netloc)  # "www.example.com"
print(parsed_url.path)  # "/path"
print(parsed_url.query)  # "param=value"
print(parsed_url.fragment)  # "fragment"


# In[11]:


import re

def is_valid_ip_address(ip_address):
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    match = re.match(pattern, ip_address)
    if match is not None:
        octets = ip_address.split('.')
        if all(0 <= int(octet) <= 255 for octet in octets):
            return True
    return False

# Example usage:
print(is_valid_ip_address("192.168.0.1"))  # True
print(is_valid_ip_address("10.0.0.256"))  # False


# In[ ]:




