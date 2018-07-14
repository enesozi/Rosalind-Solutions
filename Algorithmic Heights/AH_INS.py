import sys

def main(args):
	file = str(args[1])
	with open(file) as f:
		numbers = f.read().split()

	n = int(numbers[0])
	A = list(map(int,numbers[1:]))
	print(ins_sort_inv_num(A,n))

def ins_sort_inv_num(A,n):
	inv = 0
	for i in range(1,n):
		k = i
		while k>0 and A[k] < A[k-1]:
			A[k],A[k-1] = A[k-1],A[k]
			inv += 1
			k -= 1
	return inv

if '__main()__':
	main(sys.argv)