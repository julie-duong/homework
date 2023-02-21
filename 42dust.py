# 42dust.py

# Write a program that performs entropy filtering on nucleotide fasta files
# Windows that are below the entropy threshold are replaced by N

# Program arguments include file, window size, and entropy threshold

# Output should be a fasta file with sequence wrapped at 60 characters

# Hint: use the mcb185 library
# Hint: make up some fake sequences for testing

# Note: don't worry about "centering" the entropy on the window (yet)

import mcb185
import sys
import math 

filename = sys.argv[1]
window = int(sys.argv[2])
threshold = float(sys.argv[3])

def entropy(prob):
	entropy = 0.0
	for p in prob:
		if p > 0:
			entropy -= p * math.log2(p)
	return entropy
	
def probabilities(seq):
	l = len(seq)
	prob = [seq.count('A')/l, seq.count('C')/l, seq.count('T')/l, seq.count('G/')/l]
	return prob 

for defline, seq in mcb185.read_fasta(filename):
	words = defline.split()
	name = words[0]

finalseq = ''
for i in range(len(seq)-1):
	probs = probabilities(seq[i:window+i-1])
	if (entropy(probs) < threshold):
		finalseq += 'N'
	else:
		finalseq += seq[i]

print(name)

segments = [finalseq[i:i+59] for i in range(0, len(finalseq), 60)]

for seg60 in segments:
	print(seg60)
"""
python3 42dust.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz 11 1.4
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGNTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTNNNNNNNAAAAAGAGTGTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGNNNNNNNNNNNATTTTATTGACTTAGG
TCACNNAATACTTTAACCAATATAGGCATAGCGCACAGNCNNNNAAAAATTACAGAGTNN
ACAACATCCATGAAACGCATTAGCACCACCATNNNNNNNACCATCACCATTACCACAGGT
AACNGTGCGGGCTGACGCGTACAGNNNNNNNNGAAAAAAGCCCGCACCTGACAGTGCNNN
NNNTTTTTTTCGACCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
ANNCANGGGCAGGTGGCCANCGNNNNNNNTNNNCCCGNNNNNNNNNCCAACCACCTGGTG
GCGATNATTGNNAAAACCATTAGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA
...
"""
