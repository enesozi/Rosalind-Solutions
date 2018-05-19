import sys
from scipy.special import comb


def main(args):
	k = int(args[1])
	m = int(args[2])
	n = int(args[3])

	pop_total = 4 * comb(k + m + n, 2)
       
	pop_dom = 4*comb(k,2) + 4*k*m + 4*k*n + 3*comb(m,2) + 2*m*n

	prob_dom = pop_dom/pop_total
								  
	print(prob_dom)

if __name__ == "__main__":
   main(sys.argv)	