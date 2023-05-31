#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[ ]:


# Question 1: Python Program for Recursive Insertion Sort

def recursive_insertion_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        sorted_arr = recursive_insertion_sort(arr[1:])
        key = arr[0]
        i = len(sorted_arr) - 1
        while i >= 0 and sorted_arr[i] > key:
            sorted_arr[i + 1] = sorted_arr[i]
            i -= 1
        sorted_arr[i + 1] = key
        return sorted_arr

# Example usage
arr = [5, 2, 8, 12, 3]
sorted_arr = recursive_insertion_sort(arr)
print("Sorted array:", sorted_arr)


# In[3]:


# Question 2: Python Program for QuickSort

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Example usage
arr = [5, 2, 8, 12, 3]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)


# In[4]:


# Question 3: Python Program for Iterative Quick Sort

def iterative_quick_sort(arr):
    stack = [(0, len(arr) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot = partition(arr, low, high)
            stack.append((low, pivot - 1))
            stack.append((pivot + 1, high))
    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Example usage
arr = [5, 2, 8, 12, 3]
sorted_arr = iterative_quick_sort(arr)
print("Sorted array:", sorted_arr)


# In[5]:


# Question 4: Python Program for Selection Sort

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Example usage
arr = [5, 2, 8, 12, 3]
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)


# In[6]:


# Question 5: Python Program for Bubble Sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage
arr = [5, 2, 8, 12, 3]
bubble_sort(arr)
print("Sorted array:", arr)


# In[7]:


# Question 6: Python Program for Merge Sort

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    while i < len(left):
        result.append(left[i])
        i += 1
    
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result

# Example usage
arr = [5, 2, 8, 12, 3]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)


# In[8]:


# Question 7: Python Program for Iterative Merge Sort

def merge_sort(arr):
    current_size = 1
    while current_size < len(arr) - 1:
        left = 0
        while left < len(arr) - 1:
            mid = min((left + current_size - 1), (len(arr) - 1))
            right = ((2 * current_size + left - 1,
                     len(arr) - 1)[2 * current_size + left - 1 > len(arr)-1])
            merge(arr, left, mid, right)
            left = left + current_size * 2
        current_size = 2 * current_size

def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    L = [0] * n1
    R = [0] * n2

    for i in range(0, n1):
        L[i] = arr[left + i]
    for i in range(0, n2):
        R[i] = arr[mid + i + 1]

    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# Example usage
arr = [5, 2, 8, 12, 3]
merge_sort(arr)
print("Sorted array:", arr)


# In[9]:


# Question 8: Python Program for Heap Sort

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr


# In[10]:


# Question 9: Python Program for Counting Sort

def counting_sort(arr):
    max_value = max(arr)
    count = [0] * (max_value + 1)
    sorted_arr = [0] * len(arr)

    for num in arr:
        count[num] += 1

    for i in range(1, max_value + 1):
        count[i] += count[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        sorted_arr[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    return sorted_arr

# Example usage
arr = [5, 2, 8, 12, 3]
sorted_arr = counting_sort(arr)
print("Sorted array:", sorted_arr)


# In[11]:


# Question 10: Python Program for ShellSort

def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        gap //= 2

# Example usage
arr = [5, 2, 8, 12, 3]
shell_sort(arr)
print("Sorted array:", arr)


# In[ ]:




