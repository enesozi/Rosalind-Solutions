import sys
import numpy as np

def main(args):
	file = str(args[1])
	with open(file) as f:
		lines = list(map(int,f.read().split()))
	
	n = lines[0]
	m = lines[1]
	edges = lines[2:]
	deg_arr = np.zeros([n+1,n+1],dtype=int)

	for i in range(0,len(edges),2):
		deg_arr[edges[i],edges[i+1]],deg_arr[edges[i+1],edges[i]] = 1,1

	print(' '.join(map(str,np.sum(deg_arr[1:],1))))
	



if '__main()__':
	main(sys.argv)