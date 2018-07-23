import sys

class BinMaxHeap:
    def __init__(self,N):
        self.heap = [0]*(N+1)
        self.size = 0

    def get_heap(self):
    	return self.heap[1:]

    def insert(self,k):
    	self.size += 1
    	self.heap[self.size] = k
    	self.decrease_key(self.size)

    def decrease_key(self,index):
	    parent = index // 2
	    while parent > 0:
	    	if self.heap[index] > self.heap[parent]:
	    		self.heap[index],self.heap[parent] = \
	    		self.heap[parent],self.heap[index]
	    	index,parent = parent, parent // 2
    
    def build_heap(self,alist):
	    for elm in alist:
	    	self.insert(elm)		


def main(args):
	file = str(args[1])
	with open(file) as f:
		N = int(f.readline())
		A = list(map(int,f.readline().split()))

	bin_heap = BinMaxHeap(N)
	bin_heap.build_heap(A)
	with open('rosalind_res_hea.txt','w') as f:
		f.write(' '.join(map(str,bin_heap.get_heap())))

if '__main()__':
	main(sys.argv)	
