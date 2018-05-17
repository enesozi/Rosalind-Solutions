import sys

def main(args):
	s = str(args[1])
	t = str(args[2])
	print(sum(c1 != c2 for c1, c2 in zip(s, t)))

if __name__ == "__main__":
   main(sys.argv)