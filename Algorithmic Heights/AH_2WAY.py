import sys

def main(args):
	file = str(args[1])
	with open(file) as f:
		N = int(f.readline())
		A = list(map(int,f.read().split()))

	threshold = A[0]
	start = i = 0
	end = N-1

	while i <= end:
		if A[i] < threshold:
			A[i],A[start] = A[start],A[i]
			start += 1
			i += 1
		elif A[i] > threshold:
			A[i],A[end] = A[end],A[i]
			end -= 1
		else:
			i+=1

	with open('rosalind_par_res.txt','w') as f:
		f.write(' '.join(map(str,A)))

if '__main()__':
	main(sys.argv)