import sys
import numpy as np

def main(args):
	file = str(args[1])
	with open(file) as f:
		lines = f.read().split()
		k,n = lines[0],lines[1]
		arr = np.reshape(lines[2:],(int(k),int(n)))

		freq_dict = dict()
		for row in arr:
			freq_dict.clear()
			for num in row:
				if num in freq_dict:
					freq_dict[num] += 1
				else:
					freq_dict[num] = 1

			elm_found = False

			for k,v in freq_dict.items():
				if int(v) > int(n)//2:
					elm_found = True
					print(k)
					break

			if not elm_found:
				print('-1')		

	



		





if '__main()__':
	main(sys.argv)	