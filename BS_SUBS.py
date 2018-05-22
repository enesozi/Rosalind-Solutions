
def main():
	s,t = open('rosalind_subs.txt').read().split()
	start = 0
	indices = []
	while True:
		start = s.find(t, start)
		if start == -1:
			break
		indices.append(start+1)	
		start += 1 

	print(' '.join(map(str,indices)))
		
if __name__ == "__main__":
   main()	