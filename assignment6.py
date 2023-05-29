#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np


# In[2]:


# Question 1: Python program to add two matrices

def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result


matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
result_matrix = add_matrices(matrix1, matrix2)
print("Result matrix:")
for row in result_matrix:
    print(row)


# In[3]:


# Question 2: Python program to multiply two matrices

def multiply_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            cell = 0
            for k in range(len(matrix2)):
                cell += matrix1[i][k] * matrix2[k][j]
            row.append(cell)
        result.append(row)
    return result

# Example usage
matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8], [9, 10], [11, 12]]
result_matrix = multiply_matrices(matrix1, matrix2)
print("Result matrix:")
for row in result_matrix:
    print(row)


# In[4]:


# Question 3: Python program for matrix product

def matrix_product(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            cell = 0
            for k in range(len(matrix2)):
                cell += matrix1[i][k] * matrix2[k][j]
            row.append(cell)
        result.append(row)
    return result

# Example usage
matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8], [9, 10], [11, 12]]
result_matrix = matrix_product(matrix1, matrix2)
print("Result matrix:")
for row in result_matrix:
    print(row)


# In[5]:


# Question 4: Adding and Subtracting Matrices in Python

def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def subtract_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)
    return result

# Example usage
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
addition_result = add_matrices


# In[6]:


# Question 5: Transpose a matrix in a single line in Python

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print("Transposed matrix:")
for row in transpose_matrix:
    print(row)


# In[7]:


# Question 6: Python | Matrix creation of n*n

n = 3
matrix = [[0] * n for _ in range(n)]
print("Matrix of size", n, "x", n)
for row in matrix:
    print(row)


# In[8]:


# Question 7: Python | Get Kth Column of Matrix

def get_kth_column(matrix, k):
    column = [row[k] for row in matrix]
    return column

# Example usage
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k = 1
column_k = get_kth_column(matrix, k)
print("Column", k, "of the matrix:", column_k)


# In[9]:


# Question 8: Python - Vertical Concatenation in Matrix

def vertical_concatenation(matrix1, matrix2):
    result = matrix1 + matrix2
    return result

# Example usage
matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8, 9], [10, 11, 12]]
concatenated_matrix = vertical_concatenation(matrix1, matrix2)
print("Concatenated matrix:")
for row in concatenated_matrix:
    print(row)


# In[10]:


# Question 9: Python program to check if a string is a palindrome or not

def is_palindrome(string):
    reversed_string = string[::-1]
    if string == reversed_string:
        return True
    else:
        return False

# Example usage
my_string = "madam"
if is_palindrome(my_string):
    print(my_string, "is a palindrome.")
else:
    print(my_string, "is not a palindrome.")


# In[11]:


# Question 10: Python program to check whether a string is symmetrical or a palindrome

def is_symmetrical(string):
    reversed_string = string[::-1]
    if string == reversed_string:
        return True
    else:
        return False

# Example usage
my_string = "level"
if is_symmetrical(my_string):
    print(my_string, "is symmetrical.")
else:
    print(my_string, "is not symmetrical.")


# In[ ]:




