import sys

def main():
	with open('rosalind_lcsm.txt') as f:
		dna_arr = []
		content = f.read().split()
		ind = [i for i,val in enumerate(content) if '>' in val]
		for i in range(len(ind)-1):
			dna_arr.append("".join(content[ind[i]+1:ind[i+1]]))
		dna_arr.append("".join(content[ind[len(ind)-1]+1:]))	

	dna_1 = dna_arr[0]
	l = len(dna_1)
	m = len(dna_arr)
	lcs = ""
	for i in range(l):
		for j in range(i+1,l+1):
			sub_dna = dna_1[i:j]
			is_contained = True
			for k in range(1,m):
				if not sub_dna in dna_arr[k]:
					is_contained = False
					break
			if is_contained and len(lcs) < len(sub_dna):
				lcs = sub_dna
	print(lcs) 

if __name__ == "__main__":
   main()	