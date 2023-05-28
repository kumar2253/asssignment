#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:



for num in range(1500, 2701):
    if num % 7 == 0 and num % 5 == 0:
        # Print the number
        print(num)


# In[ ]:


# Take input from the user for the first number
num1 = float(input("Enter the first number: "))

# Take input from the user for the second number
num2 = float(input("Enter the second number: "))

# Add the two numbers
sum = num1 + num2

# Display the result
print("The sum of", num1, "and", num2, "is", sum)


# In[ ]:


# Take input from the user for the first number
num1 = float(input("Enter the first number: "))

# Take input from the user for the second number
num2 = float(input("Enter the second number: "))

# Find the maximum of the two numbers
maximum = max(num1, num2)

# Display the result
print("The maximum of", num1, "and", num2, "is", maximum)


# In[ ]:


# Take input from the user for the number
num = int(input("Enter a number: "))

# Initialize the factorial variable
factorial = 1

# Check if the number is negative, zero, or positive
if num < 0:
    print("Factorial cannot be calculated for a negative number.")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    # Calculate the factorial of the number
    for i in range(1, num + 1):
        factorial *= i

    # Display the result
    print("Factorial of", num, "is", factorial)


# In[ ]:


# Take input from the user for the principal amount
principal = float(input("Enter the principal amount: "))

# Take input from the user for the rate of interest
rate = float(input("Enter the rate of interest (in percentage): "))

# Take input from the user for the time period
time = float(input("Enter the time period (in years): "))

# Calculate the simple interest
simple_interest = (principal * rate * time) / 100

# Display the result
print("Simple Interest:", simple_interest)


# In[ ]:


# Take input from the user for the principal amount
principal = float(input("Enter the principal amount: "))

# Take input from the user for the rate of interest
rate = float(input("Enter the rate of interest (in percentage): "))

# Take input from the user for the time period
time = float(input("Enter the time period (in years): "))

# Take input from the user for the compounding frequency
frequency = int(input("Enter the compounding frequency per year: "))

# Calculate the compound interest
amount = principal * (1 + (rate / (100 * frequency))) ** (frequency * time)
compound_interest = amount - principal

# Display the result
print("Compound Interest:", compound_interest)


# In[ ]:


# Take input from the user for the number
number = int(input("Enter a number: "))

# Calculate the number of digits in the number
num_of_digits = len(str(number))

# Initialize the sum variable
sum = 0

# Temporary variable to store the original number
temp = number

# Calculate the sum of the cubes of each digit
while temp > 0:
    digit = temp % 10
    sum += digit ** num_of_digits
    temp //= 10

# Check if the number is an Armstrong number
if number == sum:
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")


# In[ ]:


# Take input from the user for the radius of the circle
radius = float(input("Enter the radius of the circle: "))

# Calculate the area of the circle
area = 3.14159 * (radius ** 2)

# Display the result
print("The area of the circle with radius", radius, "is", area)


# In[ ]:


# Take input from the user for the lower and upper limits of the interval
lower_limit = int(input("Enter the lower limit of the interval: "))
upper_limit = int(input("Enter the upper limit of the interval: "))

print("Prime numbers between", lower_limit, "and", upper_limit, "are:")

# Iterate through the numbers in the interval
for num in range(lower_limit, upper_limit + 1):
    # Prime numbers are greater than 1
    if num > 1:
        # Check if the number is divisible by any number from 2 to the square root of the number
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            # If the number is not divisible by any number, it is prime
            print(num)


# In[ ]:


# Take input from the user for the number
number = int(input("Enter a number: "))

# Prime numbers are greater than 1
if number > 1:
    # Check if the number is divisible by any number from 2 to the square root of the number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")
else:
    print(number, "is not a prime number")


# In[ ]:





# In[ ]:





# In[ ]:




