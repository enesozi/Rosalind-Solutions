import sys

def main(args):
	prot_str = str(args[1])
	content = open("codon_table.txt").read().split()
	rna_codon_table = {content[i]: content[i+1] for i in range(0, len(content), 2)}
	freq_table = get_freq_table(rna_codon_table)
	
	res = freq_table['Stop']
	for aa in prot_str:
		res *= freq_table[aa]
	print(res%pow(10,6))	

def get_freq_table(codon_table):
	freq = {}
	for k,v in codon_table.items():
		if not v in freq:
			freq[v] = 1
		else:
			freq[v] += 1

	return freq			

if __name__ == "__main__":
   main(sys.argv)	