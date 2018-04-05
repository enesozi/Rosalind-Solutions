from collections import Counter
import sys

def main(dna_string):
	dna_molecules = ['A','C','G','T']
	counts=Counter(dna_string)
	result = ""
	for d_m in dna_molecules:
		result += str(counts[d_m])+" "
	print(result[:-1])	

if __name__ == "__main__":
   main(sys.argv[1])	