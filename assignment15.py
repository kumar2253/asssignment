#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


# Question 1: Python Program for Topological Sorting

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort_util(self, v, visited, stack):
        visited[v] = True

        for neighbor in self.graph[v]:
            if visited[neighbor] == False:
                self.topological_sort_util(neighbor, visited, stack)

        stack.insert(0, v)

    def topological_sort(self):
        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            if visited[i] == False:
                self.topological_sort_util(i, visited, stack)

        print("Topological Sorting:")
        for vertex in stack:
            print(vertex, end=" ")

# Example usage
g = Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

g.topological_sort()


# In[3]:


# Question 2: Python Program for Radix Sort

def counting_sort(arr, exp):
    n = len(arr)
    count = [0] * 10
    output = [0] * n

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_value = max(arr)
    exp = 1

    while max_value // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Example usage
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print("Sorted array:", arr)


# In[4]:


# Question 3: Python Program for Binary Insertion Sort

def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        low = 0
        high = i - 1

        while low <= high:
            mid = (low + high) // 2
            if arr[mid] < key:
                low = mid + 1
            else:
                high = mid - 1

        for j in range(i, low, -1):
            arr[j] = arr[j - 1]

        arr[low] = key

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
binary_insertion_sort(arr)
print("Sorted array:", arr)


# In[5]:


# Question 4: Python Program for Bitonic Sort

def bitonic_sort(arr, up=True):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        first_half = bitonic_sort(arr[:mid], True)
        second_half = bitonic_sort(arr[mid:], False)
        return bitonic_merge(first_half + second_half, up)

def bitonic_merge(arr, up=True):
    if len(arr) <= 1:
        return arr
    else:
        bitonic_compare(arr, up)
        mid = len(arr) // 2
        first_half = bitonic_merge(arr[:mid], up)
        second_half = bitonic_merge(arr[mid:], up)
        return first_half + second_half

def bitonic_compare(arr, up):
    distance = len(arr) // 2
    for i in range(distance):
        if (arr[i] > arr[i + distance]) == up:
            arr[i], arr[i + distance] = arr[i + distance], arr[i]

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bitonic_sort(arr)
print("Sorted array:", sorted_arr)


# In[6]:


# Question 5: Python Program for Comb Sort

def comb_sort(arr):
    n = len(arr)
    gap = n
    shrink_factor = 1.3
    sorted = False

    while not sorted:
        gap = int(gap / shrink_factor)
        if gap <= 1:
            gap = 1
            sorted = True

        i = 0
        while i + gap < n:
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted = False
            i += 1

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
comb_sort(arr)
print("Sorted array:", arr)


# In[7]:


# Question 6: Python Program for Pigeonhole Sort

def pigeonhole_sort(arr):
    min_val = min(arr)
    max_val = max(arr)
    size = max_val - min_val + 1
    holes = [0] * size

    for x in arr:
        holes[x - min_val] += 1

    i = 0
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1
            arr[i] = count + min_val
            i += 1

# Example usage
arr = [8, 3, 2, 7, 4, 6, 8]
pigeonhole_sort(arr)
print("Sorted array:", arr)


# In[8]:


# Question 7: Python Program for Cocktail Sort

def cocktail_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False

        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        end -= 1

        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        start += 1

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
cocktail_sort(arr)
print("Sorted array:", arr)


# In[9]:


# Question 8: Python Program for Gnome Sort

def gnome_sort(arr):
    n = len(arr)
    i = 0

    while i < n:
        if i == 0 or arr[i - 1] <= arr[i]:
            i += 1
        else:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
gnome_sort(arr)
print("Sorted array:", arr)


# In[10]:


# Question 9: Python Program for Odd-Even Sort / Brick Sort

def odd_even_sort(arr):
    n = len(arr)
    sorted = False

    while not sorted:
        sorted = True

        for i in range(1, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted = False

        for i in range(0, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted = False

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
odd_even_sort(arr)
print("Sorted array:", arr)


# In[11]:


# Question 10: Python Program for BogoSort or Permutation Sort

import random

def is_sorted(arr):
    n = len(arr)
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            return False
    return True

def bogo_sort(arr):
    while not is_sorted(arr):
        random.shuffle(arr)

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
bogo_sort(arr)
print("Sorted array:", arr)


# In[ ]:




