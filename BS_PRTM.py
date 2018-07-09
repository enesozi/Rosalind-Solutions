import sys

def main(args):
	f_dir = str(args[1])
	P = str(args[2])
	with open(f_dir) as file:
		mass_table = file.read().split()

	m_t_dict = {str(mass_table[i]):float(mass_table[i+1]) for i in range(0,len(mass_table),2)}
	p_mass = 0
	for symb in P:
		p_mass += m_t_dict[symb]

	print('%.3f'%p_mass)	


if '__main()__':
	main(sys.argv)	