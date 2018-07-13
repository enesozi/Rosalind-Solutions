import numpy as np
import sys

def main():

	content = open('rosalind_cons.txt').read().split()
	start_indices = [i for i,val in enumerate(content) if '>' in val]
	row_num = len(start_indices)
	if len(start_indices) > 1:
		col_num = len(''.join(content[start_indices[0]+1:start_indices[1]]))
	else:
		col_num = len(''.join(content[start_indices[0]+1:-1]))

	dna_arr = np.empty([row_num,col_num],dtype='str')

	for i in range(len(start_indices)-1):
		start = start_indices[i]
		end = start_indices[i + 1]
		dna_arr[i] = [base for base in ''.join(content[start+1:end])]		

	dna_arr[-1] = [base for base in ''.join(content[start_indices[-1]+1:])]
	profile_arr = np.zeros([4,col_num],dtype='int')
	base_dict = {0:'A',1:'C',2:'G',3:'T'}

	for col in range(col_num):
		col_list = list(dna_arr[:,col])		
		profile_arr[:,col] = [col_list.count(base) for base in base_dict.values()]

	max_val_indices = profile_arr.argmax(axis=0)
	
	consensus = ''
	for ind in max_val_indices:
		consensus += base_dict[ind]
	print(consensus)

	for row in range(4):
		print('%s: %s'%(base_dict[row],' '.join(map(str,profile_arr[row,:]))))


if __name__ == "__main__":
   main()	