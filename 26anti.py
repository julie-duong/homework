# 26anti.py

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

# Variation: try this with the range() function and slice syntax

dna = 'ACTGAAAAAAAAAAA'

for i in range(len(dna), 0, -1):

	if dna[i-1] == 'A':
		print('T', end='')
	elif dna[i-1] == 'T':
		print('A', end='')
	elif dna[i-1] == 'G':
		print('C', end='')
	else:
		print('G', end='')


	

"""
python3 26anti.py
TTTTTTTTTTTCAGT
"""
