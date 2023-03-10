# 50dust.py

# Write a better version of your 42dust.py program
# Your program must have the following properties

# 1. has option and default value for window size
# 2. has option and default value for entropy threshold
# 3. has a switch for N-based or lowercase (soft) masking
# 4. works with uppercase or lowercase input files
# 5. works as an executable
# 6. outputs a FASTA file wrapped at 60 characters

# Optional: make the algorithm faster (see 29gcwin.py for inspiration)
# Optional: benchmark your programs with different window sizes using time

# Hint: make a smaller file for testing (e.g. e.coli.fna in the CLI below)


import argparse 
import math
import mcb185 

parser = argparse.ArgumentParser(description='Entropy filtering on fasta files')
parser.add_argument('-w', '--window', required=False, type= int, 
	default=11, metavar='window', help='window size [%(default)i]')
parser.add_argument('-t', '--threshold', required=False, type=float,
	default=1.4, metavar='threshold', help='entropy threshold [%%(default).3f]')
parser.add_argument('file', type=str, metavar='file', help='fasta file')
parser.add_argument('-l', '--lowercase', action='store_true',
	help='switch for lowercase masking')
arg = parser.parse_args()

def probabilities(seq):
	l = len(seq)
	prob = [seq.count('A')/l, seq.count('C')/l, seq.count('T')/l, seq.count('G')/l]
	return prob

def entropy(prob):
	entropy = 0.0
	for p in prob:
		if p > 0:
			entropy += -(p * math.log2(p))
	return entropy

for defline, seq in mcb185.read_fasta(arg.file):
	seq = seq.upper()
	finalseq = list(seq)
	# Switch for lowercase masking
	for i in range(len(finalseq)-arg.window+1):
		frequency = probabilities(seq[i:arg.window+i])
		if not arg.lowercase:
			if entropy(frequency) < arg.threshold:
				for j in range(i, i+ arg.window):
					finalseq[j]='N'
		else:
			if entropy(frequency) < arg.threshold:
				for j in range(i, i+ arg.window):
					finalseq[j]= finalseq[j].lower()
	seq = "".join(finalseq)
	print(f'>{defline}')
	for i in range(0, len(seq), 60):
		print(seq[i:i+60])



"""
python3 50dust.py -w 11 -t 1.4 -s e.coli.fna  | head
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGcttttcattctGACTGCAACGGGCAATATGTCTCTGTGTggattaaaaaaagagtgTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGagtaaattaaaattttattgaCTTAGG
TCACtaaatactttaaCCAATATAGGCATAGCGCACAGacagataaaaattacaGAGTac
acaacatccaTGAAACGCATTAGCACCACCATtaccaccaccatcaccaTTACCACAGGT
AACggtgcgggctgACGCGTACAGgaaacacagaaaaaagccCGCACCTGACAGTGCggg
ctttttttttcgaCCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
AggcaggggcaggtggCCAccgtcctctctgcccccgccaaaatcaccaaccacctGGTG
GCGATgattgaaaaaaccattaGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA
"""
