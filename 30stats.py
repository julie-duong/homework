# 30stats.py

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median

# Hint: use sys.argv to get the values from the command line

# Note: you are not allowed to import any library except sys

import sys 

#print(sys.argv)

vals = []

for thing in sys.argv[1:]:
	vals.append(float(thing))

vals.sort()

# count
count = len(vals)
print("Count:", count)

# minimum 
print("Minimum:", min(vals))

# maximum
print("Maximum:", max(vals))

# Mean 
mean = sum(vals)/count
print("Mean:", "%.3f"%mean)

# Standard Deviation
variance = 0.0
for x in vals:
	variance += (x-mean)**2
std = (variance/(count))**0.5
print("Standard Deviation:", "%.3f"%std)

# Median
median = vals[int(count/2)]
print("Median:", "%.3f"%median)



"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
