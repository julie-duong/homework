# 32xcoverage.py

# Write a program that simulates a shotgun resequencing project
# How uniformly do the reads "pile up" on a chromosome?
# How much of that depends on sequencing depth?

# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line

# Hint: make the problem smaller, so it's easier to visualize and debug
# Hint: if you don't understand the context of the problem, ask for help
# Hint: if you are undersampling the ends, do something about it

# Note: you will not get exactly the same results as the command line below


import sys
import random

genome_size = sys.argv[1]
read_num = sys.argv[2]
read_len = sys.argv[3]

random_num = []

# generate random starting points to imitate fragments 
for thing in range(int(read_num)):
	random_num.append(random.randint(0, int(genome_size)-int(read_len)))

# set coverage to zero for the whole genome
coverage = []
for thing in range(int(genome_size)):
	coverage.append(0)

# add coverage when starting point matches 
for num in random_num:
	for i in range(num, num + int(read_len)):
		coverage[i] += 1


average = sum(coverage)/int(genome_size)
print(min(coverage), max(coverage), "%.5f"%average)


#print(coverage)

	


"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
