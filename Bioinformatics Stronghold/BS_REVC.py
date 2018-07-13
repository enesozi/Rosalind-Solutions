import sys

def main(dna_string):
	dna_string_reverse = dna_string[::-1]
	result = ""
	for ch in dna_string_reverse:
		if ch == 'A':
			result += 'T'
		elif ch == 'T':
			result += 'A'
		elif ch == 'G':
			result += 'C'
		else:
			result += 'G'
	print(result)					

if __name__ == "__main__":
   main(sys.argv[1])	