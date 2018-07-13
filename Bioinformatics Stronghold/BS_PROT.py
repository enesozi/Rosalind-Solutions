
def main():
	rna_str = open('rosalind_prot.txt').read().strip()
	content = open('codon_table.txt').read().split()
	rna_codon_table = {content[i]: content[i+1] for i in range(0, len(content), 2)}
	result = [rna_codon_table[rna_str[i:i+3]] for i in range(0,len(rna_str),3)]
	print(''.join(result[:-1]))

if __name__ == "__main__":
   main()	