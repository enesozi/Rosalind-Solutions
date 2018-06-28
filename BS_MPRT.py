import sys
import requests
import re

def main(args):
	file_name = str(args[1])
	regex = r"(?=(N[^P][ST][^P]))"
	uni_prot_ids = open(file_name).read().split()
	for p_id in uni_prot_ids:
		r = requests.get('https://www.uniprot.org/uniprot/%s.fasta'%p_id)
		prot_str = ''.join(r.text.split('\n')[1:-1])
		matches = re.finditer(regex, prot_str)
		result = ' '.join([str(m.start(0)+1) for m in matches])
		if len(result) > 0:
			print(p_id)
			print(result)
			

if __name__ == "__main__":
   main(sys.argv)	