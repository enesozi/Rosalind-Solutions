import sys

def main(args):
	n = int(args[1])
	f_t = 0
	f_t_1 = 1
	for i in range(n-1):
		f_t_1,f_t = f_t_1+f_t,f_t_1

	print(f_t_1)	


if '__main()__':
	main(sys.argv)
