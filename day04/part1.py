file = open('day4/input.txt')
lines = [l.strip() for l in file.readlines()]

def has_subsets(line: str):
    pairs = line.split(',')
    ranges = [range(int(p[0]), int(p[1]) + 1) for p in (pair.split('-') for pair in pairs)]
    
    return all(r in ranges[0] for r in ranges[1]) or all(r in ranges[1] for r in ranges[0])

overlaps = [l for l in lines if has_subsets(l)]

print(len(overlaps))