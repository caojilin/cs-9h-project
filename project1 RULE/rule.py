import sys
rule = int(sys.argv[1])
rows = int(sys.argv[2])
half_size = rows
indices = range(-half_size,half_size+1)
# initial condition
cells = {i: '0' for i in indices}
cells[0] = '1'
# set both ends
cells[-half_size-1] = '0'
cells[ half_size+1] = '0'

# current outcome:              111 110 101 100 011 010 001 000
# new state:                     0   0   0   1   1   1   1   0
# new_state30 = {"111": '0', "110": '0', "101": '0', "000": '0',
#              "100": '1', "011": '1', "010": '1', "001": '1'}

def new_rule_pattern(rule):
	"""
	>>>new_rule_pattern(30)
	{"111": '0', "110": '0', "101": '0', "000": '0', "100": '1', "011": '1', "010": '1', "001": '1'}
	"""
	myList = []
	pattern = _init_pattern()
	for i in pattern:
		input = int(bin(i)[2:],2)
		binary = bin(rule)[2:][::-1]
		if len(binary) <= input:
			num = '0'
			myList.append(num)
		else:
			num = str(binary[input])
			myList.append(num)
	
	new_state = {"111": str(myList[7]), "110": str(myList[6]), "101": str(myList[5]), "000": str(myList[0]),
            	 "100": str(myList[4]), "011": str(myList[3]), "010": str(myList[2]), "001": str(myList[1])}

	return new_state

def _init_pattern():
	"""
	>>>_init_pattern()
	{0,1,2,3,4,5,6,7}
	"""
	pattern={0,1,2,3,4,5,6,7} 
	return pattern

print('P1',1+2*half_size, rows)
def print_pattern(rule):
	"""
	>>> print_pattern(31)
	P1 7 3
	0001000
	0011100
	0110010
	>>> print_pattern(33)
	P1 7 3
	0001000
	1100011
	0001000
	"""
	half_size = rows
	indices = range(-half_size,half_size+1)
	# initial condition
	cells = {i: '0' for i in indices}
	cells[0] = '1'
	# set both ends
	cells[-half_size-1] = '0'
	cells[ half_size+1] = '0'

	new_state = new_rule_pattern(rule)
	for row in range(0, rows):
	    #current state

	    for i in indices:
	        if cells[i] == '1':
	            # sys.stdout.write(u'\u0031')
	            print('1', end='')
	        else:
	            # sys.stdout.write(u'\u0030')
	            print('0', end='')
	    # sys.stdout.write('\n')
	    print()
	    #next state
	    patterns = {i: cells[i-1] + cells[i] + cells[i+1] for i in indices}
	    cells = {i: new_state[patterns[i]] for i in indices}
	    cells[-half_size-1] = '0'
	    cells[ half_size+1] = '0'

print_pattern(rule)
