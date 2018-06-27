import sys
from scipy.misc import comb

def main(args):
	k = int(args[1])
	N = int(args[2])
	tot = 2**k
	prob = 0

	# Since the prob of having AaBb genome for an organism is 0.25 at each generation
	for i in range(N,tot+1):
		prob += comb(tot,i)*(0.25**i)*(0.75**(tot-i))	

	print(round(prob,3))

if __name__ == "__main__":
   main(sys.argv)	