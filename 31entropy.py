# 31entropy.py

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# Store the values in a new list

# Note: make sure the command line values contain numbers
# Note: make sure the probabilities sum to 1.0
# Note: import math and use the math.log2()

# Hint: try breaking your program with erroneous input

import sys
import math

new_list = []
entropy = 0.0

for thing in sys.argv[1:]:
	new_list.append(float(thing))

for thing in new_list:
	entropy += -(thing * math.log2(thing))



print("%.3f"%entropy)


"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
