import sys
import numpy as np 

def main(args):
	file = str(args[1])
	with open(file) as f:
		lines = list(map(int,f.read().split()))
		K,N = lines[0],lines[1]
		arr = np.reshape(lines[2:],(K,N))
	target = 0	
	for row in arr:
		two_sum(row,target)
				
def two_sum(nums, target):

    sum_dict = {}
    for i in range(len(nums)):
        if nums[i] in sum_dict:
            print('%d %d'%(sum_dict[nums[i]]+1, i+1))
            return
        else:
            sum_dict[target - nums[i]] = i
    print('-1')        

if '__main()__':
	main(sys.argv)	