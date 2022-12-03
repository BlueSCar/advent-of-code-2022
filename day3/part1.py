inputs = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

file = open("day3/input.txt", "r")
lines = file.readlines()


def get_priority(line):
    size = len(line)
    half = int(size / 2)
    
    first = set(line[:half])
    second = set(line[half:])
    
    common = [f for f in first if f in second]
    
    return inputs.index(common[0]) + 1

total = sum([get_priority(l.strip()) for l in lines])

print(total)