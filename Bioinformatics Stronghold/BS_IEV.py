import sys

def main(args):
	geno_probs = {1:1,2:1,3:1,4:.75,5:.5,6:0}
	geno_nums = {i:int(args[i]) for i in range(1,7)}
	offs_gen = 2
	print(sum([offs_gen*geno_nums[key]*geno_probs[key] for key in geno_nums]))

if __name__ == "__main__":
   main(sys.argv)	