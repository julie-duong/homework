# 25atseq.py

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

# Note: set random.seed() if you want repeatable random numbers

import random 

length = 30
AT_fraction = 0
seq = ''

for i in range(length):
	r = random.randint(1,100)
	if r <= 60:
		seq = seq + random.choice('AT')
		AT_fraction += 1 
	else:
		seq = seq + random.choice('GC')
		
print(length, AT_fraction/length, seq)


	


"""
python3 25atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
