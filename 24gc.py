# 24gc.py

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT'

gc_content = 0

for nt in dna:
	if nt == 'G' or nt == 'C':
		gc_content += 1
		
print('{:.2f}'.format(gc_content/len(dna)))


"""
python3 24gc.py
0.42
"""
