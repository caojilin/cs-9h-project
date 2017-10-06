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

new_state30 = {"111": '0', "110": '0', "101": '0', "000": '0',
             "100": '1', "011": '1', "010": '1', "001": '1'}
new_state139 = {"110": '0', "101": '0', "100": '0', "010": '0',
             "111": '1', "011": '1', "001": '1', "000": '1'}

if rule == 30:
    new_state = new_state30
else:
    new_state = new_state139
print('P1',1+2*half_size, rows)
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
