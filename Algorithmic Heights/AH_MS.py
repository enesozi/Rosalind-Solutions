import sys

def main(args):
	file = str(args[1])
	with open(file) as f:
		N = int(f.readline())
		A = list(map(int,f.readline().split()))

	merge_sort(A,0,N-1)
	with open('rosalind_ms_res.txt','w') as f:
		f.write(' '.join(map(str,A)))

def merge(arr,l,m,r):
    n1 = m-l+1
    n2 = r-m
    L = [0]*(n1)
    R = [0]*(n2)
    
    for i in range(n1):
        L[i] = arr[i+l]
    
    for i in range(n2):
        R[i] = arr[m+i+1]
    
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
    
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr,l,r):
    if l < r:
        m = (l+r-1)//2
        merge_sort(arr,l,m)
        merge_sort(arr,m+1,r)
        merge(arr,l,m,r)

if '__main()__':
	main(sys.argv)        