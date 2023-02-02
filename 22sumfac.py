# 22sumfac.py

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# Use the same loop for both calculations

# Note: you may not import math or any other library

i = 1
n = 5 
running_sum = 0
factorial = 1

while i <= n:
	running_sum += i
	factorial = factorial*i
	i += 1 


print(n, running_sum, factorial)



"""
python3 22sumfac.py
5 15 120
"""
