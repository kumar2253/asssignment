#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np


# In[2]:


# Take input from the user for the value of n
n = int(input("Enter the value of n: "))

# Initialize the first two numbers in the Fibonacci sequence
fibonacci = [0, 1]

# Calculate the Fibonacci sequence up to the n-th number
for i in range(2, n+1):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

# Display the n-th Fibonacci number
print("The", n, "th Fibonacci number is", fibonacci[n])


# In[3]:


# Take input from the user for the number
number = int(input("Enter a number: "))

# Function to check if a number is a perfect square
def isPerfectSquare(num):
    sqrt = int(num ** 0.5)
    return sqrt * sqrt == num

# Function to check if a number is a Fibonacci number
def isFibonacciNumber(num):
    return isPerfectSquare(5 * num * num + 4) or isPerfectSquare(5 * num * num - 4)

# Check if the given number is a Fibonacci number
if isFibonacciNumber(number):
    print(number, "is a Fibonacci number")
else:
    print(number, "is not a Fibonacci number")


# In[4]:


# Take input from the user for the number and the value of n
number = int(input("Enter a number: "))
n = int(input("Enter the value of n: "))

# Function to check if a number is a perfect square
def isPerfectSquare(num):
    sqrt = int(num ** 0.5)
    return sqrt * sqrt == num

# Function to check if a number is a Fibonacci number
def isFibonacciNumber(num):
    return isPerfectSquare(5 * num * num + 4) or isPerfectSquare(5 * num * num - 4)

# Find the n-th multiple of the given number in the Fibonacci series
count = 0
i = 1
fibonacci_number = 0

while count < n:
    if isFibonacciNumber(i):
        fibonacci_number = i
        count += 1
    i += 1

result = fibonacci_number * number

# Display the result
print("The", n, "th multiple of", number, "in the Fibonacci series is", result)


# In[5]:


# Take input from the user for the character
character = input("Enter a character: ")

# Convert the character to its ASCII value
ascii_value = ord(character)

# Display the ASCII value
print("The ASCII value of", character, "is", ascii_value)


# In[6]:


# Take input from the user for the value of n
n = int(input("Enter the value of n: "))

# Calculate the sum of the squares
sum_of_squares = (n * (n + 1) * (2 * n + 1)) // 6

# Display the result
print("The sum of the squares of the first", n, "natural numbers is", sum_of_squares)


# In[7]:


# Take input from the user for the value of n
n = int(input("Enter the value of n: "))

# Calculate the sum of the cubes
sum_of_cubes = (n * (n + 1) // 2) ** 2

# Display the result
print("The sum of the cubes of the first", n, "natural numbers is", sum_of_cubes)


# In[8]:


# Take input from the user for the array elements
array = input("Enter the array elements (space-separated): ").split()

# Convert the array elements to integers
array = [int(num) for num in array]

# Calculate the sum of the array elements
sum_of_array = sum(array)

# Display the result
print("The sum of the array elements is", sum_of_array)


# In[9]:


# Take input from the user for the array elements
array = input("Enter the array elements (space-separated): ").split()

# Convert the array elements to integers
array = [int(num) for num in array]

# Find the largest element in the array
largest_element = max(array)

# Display the result
print("The largest element in the array is", largest_element)


# In[10]:


def rotate_array(arr, k):
    """
    Function to rotate an array by k positions to the right.
    """
    n = len(arr)
    k = k % n  # Adjust k if it is larger than the array size

    # Rotate the array using slicing
    rotated_arr = arr[-k:] + arr[:-k]

    return rotated_arr


# Take input from the user for the array elements
array = input("Enter the array elements (space-separated): ").split()

# Convert the array elements to integers
array = [int(num) for num in array]

# Take input from the user for the rotation amount
rotation = int(input("Enter the number of positions to rotate: "))

# Perform array rotation
rotated_array = rotate_array(array, rotation)

# Display the rotated array
print("Array after rotation:", rotated_array)


# In[11]:


def reverse_array(arr, start, end):
    """
    Function to reverse an array from index start to end.
    """
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_array(arr, rotation):
    """
    Function to rotate an array by rotation positions using the reversal algorithm.
    """
    n = len(arr)
    rotation = rotation % n  # Adjust rotation if it is larger than the array size

    # Reverse the first part of the array
    reverse_array(arr, 0, rotation - 1)

    # Reverse the second part of the array
    reverse_array(arr, rotation, n - 1)

    # Reverse the entire array
    reverse_array(arr, 0, n - 1)

    return arr


# Take input from the user for the array elements
array = input("Enter the array elements (space-separated): ").split()

# Convert the array elements to integers
array = [int(num) for num in array]

# Take input from the user for the rotation amount
rotation = int(input("Enter the number of positions to rotate: "))

# Perform array rotation using the reversal algorithm
rotated_array = rotate_array(array, rotation)

# Display the rotated array
print("Array after rotation:", rotated_array)


# In[ ]:




