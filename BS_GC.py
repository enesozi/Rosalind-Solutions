from collections import Counter

def main():
	with open('rosalind_gc.txt', 'r') as file:
		content = file.readlines()

	content = [x.strip() for x in content]
	indices = [i for i, s in enumerate(content) if '>' in s]
	
	max_ratio = 0
	max_id = ''
	for i in range(len(indices)):
		start_ind = indices[i]
		if i < len(indices)-1:
			end_ind = indices[i+1]
		else:
			end_ind = len(content)
		dna_strand = ''.join(content[start_ind+1:end_ind])
		c = Counter(dna_strand)
		ratio =  float("%2.6f" % (100*(c['C']+c['G'])/len(dna_strand)))
		if ratio > max_ratio:
			max_ratio = ratio
			max_id = content[start_ind][1:]		
	
	print(max_id)
	print(max_ratio)	

if __name__ == "__main__":
   main()