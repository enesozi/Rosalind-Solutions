import sys

def main(args):
	n = int(args[1])
	m = int(args[2])
	
	print(fibd(n,m))

def fibd(n,m=1):
	ages = [1] + [0]*(m-1)
	for i in range(n-1):
		ages = [sum(ages[1:])] + ages[:-1]
	return sum(ages)

if __name__ == "__main__":
   main(sys.argv)