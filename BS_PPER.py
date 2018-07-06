import sys

def main(args):
	N = int(args[1])
	k = int(args[2])
	print(calc_part_perm(N,k)%pow(10,6))

def calc_part_perm(N,K):
	res = 1
	for i in range(K):
		res *= (N - i)	
	return res	

if '__main()__':
	main(sys.argv)	