import sys

def main(args):
	n = int(args[1])
	k = int(args[2])
	p_0 = (1,0)
	p_t = (1,0)
	for i in range(2,n):
		a,b = p_t
		p_t_1 = (a+b,k*a)
		p_t = p_t_1

	print(sum(p_t_1))	

if __name__ == "__main__":
   main(sys.argv)