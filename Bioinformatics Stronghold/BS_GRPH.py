import sys
import itertools

def main(args):
	k = int(args[1])
	file_cont = open('rosalind_grph.txt').read().split()
	start_indices = [i for i,val in enumerate(file_cont) if '>' in val]
	content = []
	for i in range(len(start_indices)):
		start = start_indices[i]
		if i == len(start_indices) - 1:
			end = -1
		else:
			end = start_indices[i + 1]
		content.append(file_cont[start])
		content.append(''.join(file_cont[start+1:end]))
		
	itr = iter(content)
	dna_dict = dict(zip(itr, itr))
	for edge in edges(dna_dict, k):
		print(edge[0], edge[1])

def is_k_overlap(s, t, k):
	return s[-k:] == t[:k]

def edges(data, k):
	results = []
	for u in data.keys():
		for v in data.keys():
			if u != v and is_k_overlap(data[u],data[v],k):
				results.append((u[1:], v[1:]))
	return results

if __name__ == "__main__":
   main(sys.argv)