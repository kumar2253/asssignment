#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[ ]:


def find_word_line_number(file_path, word):
    with open(file_path, 'r') as file:
        for line_num, line in enumerate(file, 1):
            if word in line:
                return line_num
    return -1

file_path = input("Enter the file path: ")
word = input("Enter the word to search: ")
line_number = find_word_line_number(file_path, word)
if line_number != -1:
    print("The word '{}' is found in line number: {}".format(word, line_number))
else:
    print("The word '{}' is not found in the file.".format(word))


# In[ ]:


def count_lines(file_path):
    with open(file_path, 'r') as file:
        line_count = sum(1 for line in file)
    return line_count

file_path = input("Enter the file path: ")
line_count = count_lines(file_path)
print("Number of lines in the file:", line_count)


# In[ ]:


def remove_lines_with_prefix(file_path, prefix):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    with open(file_path, 'w') as file:
        for line in lines:
            if not line.startswith(prefix):
                file.write(line)

file_path = input("Enter the file path: ")
prefix = input("Enter the prefix to remove: ")
remove_lines_with_prefix(file_path, prefix)
print("Lines starting with prefix '{}' removed from the file.".format(prefix))


# In[ ]:


def eliminate_repeated_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    lines = list(set(lines))
    with open(file_path, 'w') as file:
        file.writelines(lines)

file_path = input("Enter the file path: ")
eliminate_repeated_lines(file_path)
print("Repeated lines eliminated from the file.")


# In[ ]:


import ast

def read_list_of_dictionaries(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    dictionaries = ast.literal_eval(content)
    return dictionaries

file_path = input("Enter the file path: ")
list_of_dictionaries = read_list_of_dictionaries(file_path)
print("List of dictionaries:", list_of_dictionaries)


# In[ ]:


def append_file_content(source_file_path, destination_file_path):
    with open(source_file_path, 'r') as source_file:
        content = source_file.read()
    with open(destination_file_path, 'a') as destination_file:
        destination_file.write(content)

source_file_path = input("Enter the source file path: ")
destination_file_path = input("Enter the destination file path: ")
append_file_content(source_file_path, destination_file_path)
print("Content appended successfully.")


# In[ ]:


def copy_odd_lines(source_file_path, destination_file_path):
    with open(source_file_path, 'r') as source_file:
        lines = source_file.readlines()
    odd_lines = lines[::2]
    with open(destination_file_path, 'w') as destination_file:
        destination_file.writelines(odd_lines)

source_file_path = input("Enter the source file path: ")
destination_file_path = input("Enter the destination file path: ")
copy_odd_lines(source_file_path, destination_file_path)
print("Odd lines copied successfully.")


# In[ ]:


def merge_files(file1_path, file2_path, merged_file_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        content1 = file1.read()
        content2 = file2.read()
    with open(merged_file_path, 'w') as merged_file:
        merged_file.write(content1)
        merged_file.write(content2)

file1_path = input("Enter the path of the first file: ")
file2_path = input("Enter the path of the second file: ")
merged_file_path = input("Enter the path of the merged file: ")
merge_files(file1_path, file2_path, merged_file_path)
print("Files merged successfully.")


# In[ ]:


def reverse_line(file_path, line_number):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    if line_number <= len(lines):
        lines[line_number - 1] = lines[line_number - 1][::-1]
        with open(file_path, 'w') as file:
            file.writelines(lines)
        print("Line {} reversed successfully.".format(line_number))
    else:
        print("Line number out of range.")

file_path = input("Enter the file path: ")
line_number = int(input("Enter the line number to reverse: "))
reverse_line(file_path, line_number)


# In[ ]:


def reverse_content(file_path, reversed_file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    reversed_content = content[::-1]
    with open(reversed_file_path, 'w') as reversed_file:
        reversed_file.write(reversed_content)

file_path = input("Enter the file path: ")
reversed_file_path = input("Enter the reversed file path: ")
reverse_content(file_path, reversed_file_path)
print("Content reversed and stored in the file.")


# In[ ]:


def reverse_content_stack(file_path, reversed_file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    reversed_lines = list(reversed(lines))
    with open(reversed_file_path, 'w') as reversed_file:
        reversed_file.writelines(reversed_lines)

file_path = input("Enter the file path: ")
reversed_file_path = input("Enter the reversed file path: ")
reverse_content_stack(file_path, reversed_file_path)
print("Content reversed using stack and stored in the file.")


# In[ ]:




