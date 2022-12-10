import re

addx_pattern = r"addx (-?\d+)"

file = open('day10/input.txt')
lines = file.readlines()

cycles = [1]

def add_cycle(register):
    previous = cycles[-1]
    cycles.append(previous + register)
    
def get_cycle_power(cycle):
    return cycle * cycles[cycle - 1]

def get_marker(cycle, position):
    if abs((cycle % 40) - position) < 2:
        return '#'
    else:
        return '.'

for line in lines:
    add_cycle(0)
    
    addx_match = re.match(addx_pattern, line)
    if addx_match:
        add_cycle(int(addx_match.groups()[0]))

signal_sums = sum([get_cycle_power(i) for i in range(20, 221, 40)])

print(signal_sums)

for cycle in range(0, 240, 40):
    print(''.join([get_marker(i, cycles[i]) for i in range(cycle, cycle + 40)]))