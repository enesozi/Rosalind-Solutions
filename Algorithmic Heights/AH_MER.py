import sys

def main(args):
	file = str(args[1])
	with open(file) as f:
		N = int(f.readline())
		A = list(map(int,f.readline().split()))
		M = int(f.readline())
		B = list(map(int,f.readline().split()))

	res = [0] * (N+M)
	j,k,i = 0,0,0

	while j < N and k < M:
		if A[j] <= B[k]:
			res[i] = A[j]
			j += 1
		else:
			res[i] = B[k]
			k += 1
		i += 1

	while j < N:
		res[i] = A[j]
		j += 1
		i += 1

	while k < M:
		res[i] = A[k]
		k += 1
		i += 1				

	with open('rosalind_mer_res.txt','w') as f:
		f.write(' '.join(list(map(str,res))))


if '__main()__':
	main(sys.argv)	