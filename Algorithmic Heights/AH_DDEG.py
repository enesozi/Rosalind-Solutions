import sys
import numpy as np

def main(args):
	file = str(args[1])
	with open(file) as f:
		N,E = list(map(int,f.readline().split()))
		adj_mat = np.zeros([N+1,N+1])
		while True:
			line = f.readline()
			if not line:
				break
			u,v = list(map(int,line.split()))
			adj_mat[u][v],adj_mat[v][u] = 1,1

	tot_deg_arr = np.sum(adj_mat,1,dtype=int)
	res = []
	for u in range(1,N+1):
		deg = 0
		for v in range(1,N+1):
			if adj_mat[u][v] == 1:
				deg += tot_deg_arr[v]
		res.append(deg)		

	with open('rosalind_ddeg_res.txt','w') as f:
		f.write(' '.join(list(map(str,res))))


if '__main()__':
	main(sys.argv)	