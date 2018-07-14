import sys

def main(args):
	file = str(args[1])
	with open(file) as f:
		numbers = f.read().split()

	n = int(numbers[0])
	m = int(numbers[1])
	A = list(map(int,numbers[2:n+2]))
	K = list(map(int,numbers[n+2:]))
	res = []
	for k in K:
		res.append(search_value(A,k,0,len(A)))
	with open('bins_res.txt','w') as f:
		f.write(' '.join(map(str,res)))	

def search_value(arr,n,l,h):
	while l <= h:

		m = l+(h-l)//2
		
		if arr[m] == n:
			return m+1
		if arr[m] > n:
			h = m - 1
		else:
			l = m + 1

	return -1


if '__main()__':
	main(sys.argv)