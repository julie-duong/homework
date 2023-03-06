# 50dust.py

# Write a better version of your 42dust.py program
# Your program must have the following properties

# 1. the entropy of each window is centered (N's in the middle of windows)
# 2. has option and default value for window size
# 3. has option and default value for entropy threshold
# 4. has a switch for N-based or lowercase (soft) masking
# 5. works with uppercase or lowercase input files
# 6. works as an executable

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
parser.add_argument('-s', '--switch', action='store_true',
	help='switch for N=based masking')
arg = parser.parse_args()

for defline, seq in mcb185.read_fasta(arg.file):
	words = defline.split()
	name = words[0]

seq = seq.upper()
	
def probabilities(seq):
	l = len(seq)
	prob = [seq.count('A')/l, seq.count('C')/l, seq.count('T')/l, seq.count('G/')/l]
	return prob

def entropy(prob):
	entropy = 0.0
	for p in prob:
		if p > 0:
			entropy -= p * math.log2(p)
	return entropy

# Switch for N-based masking
finalseq = ''
if arg.switch:
	for i in range(len(seq)-1):
		probs = probabilities(seq[i:arg.window+i-1])
		if (entropy(probs) < arg.threshold):
			finalseq += 'N'
		else:
			finalseq += seq[i]
else:
	for i in range(len(seq)-1):
		probs = probabilities(seq[i:arg.window+i-1])
		if (entropy(probs) < arg.threshold):
			finalseq += seq[i].lower()
		else:
			finalseq += seq[i]
segments = [finalseq[i:i+59] for i in range(0, len(finalseq), 60)]

for seq_60 in segments:
	print(seq_60)

"""
python3 50dust.py -w 11 -t 1.4 -s e.coli.fna  | head
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGCTTTTcATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTaaaaaaaGAGTGTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAattaaaattttATTGACTTAGG
TCACTAAATacTTTAACCAATATAGGCATAGCGCACAGACAGAtAaaaaTTACAGAGTAC
ACAacATCCATGAAACGCATTAGCACCACCATTACCAccaccatCACCATTACCACAGGT
AACGGTGCgGGCTGACGCGTACAGGAAACacagaaaaAAGCCCGCACCTGACAGTGCGGG
CTttttttTTCGACCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
AGGCAGggGCaGGTGGCCACCGTCcTCtctgcccCcgcCAAAatcaccaacCACCTGGTG
GCGATGATTGaAAAAacCATTAGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA

Timings
win alg1 alg2
11  28.7 25.8
25  30.4 26.1
100 33.2 26.1
200 37.4 25.9
"""
