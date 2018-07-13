import sys
from math import log10
from collections import Counter

def main(args):
	s = str(args[1])
	A = args[2:]
	A = list(map(float,A))
	base_dict = Counter(s)
	for gc_c in A:
		gc_prob = gc_c/2
		at_prob = (1-gc_c)/2
		res = (base_dict['G']+base_dict['C'])*log10(gc_prob) + \
			  (base_dict['A']+base_dict['T'])*log10(at_prob)
		print('%.3f'%res)	  


if '__main()__':
	main(sys.argv)	