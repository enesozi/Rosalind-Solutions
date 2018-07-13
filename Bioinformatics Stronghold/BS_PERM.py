import sys
from itertools import permutations
from math import factorial

def main(args):
	N = int(args[1])
	perm_list = list(permutations(range(1,N+1)))
	print(factorial(N))
	for p in perm_list:
		print(' '.join(map(str,p)))

if '__main()__':
	main(sys.argv)	