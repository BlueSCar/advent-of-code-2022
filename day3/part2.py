import numpy as np

inputs = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

file = open("day3/input.txt", "r")
lines = [l.strip() for l in file.readlines()]

groups = np.array_split(lines, len(lines) / 3)

def get_priority(group):
    common = [e for e in group[0] if e in group[1] and e in group[2]]
    
    return inputs.index(common[0]) + 1

total = sum([get_priority(g) for g in groups])

print(total)