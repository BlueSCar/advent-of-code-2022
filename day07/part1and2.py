import re

cd_pattern = r"\$ cd (.+)"
file_pattern = r"(\d+) .+"

file = open("day7/input.txt")
lines = [l.strip() for l in file.readlines()]

current_dirs = []
dirs = {}

for line in lines:
    if re.match(cd_pattern, line):
        dir = re.match(cd_pattern, line).groups()[0]
        
        if dir == '/':
            current_dirs = []
        elif dir == '..':
            current_dirs.pop()
        else:
            current_dirs.append(dir)
            
        key = '/'.join(current_dirs)
        if key not in dirs.keys():
            dirs[key] = 0
    elif re.match(file_pattern, line):
        file_size = int(re.match(file_pattern, line).groups()[0])
        
        for i in range(len(current_dirs) + 1):
            key = '/'.join(current_dirs[:i])
            dirs[key] = dirs[key] + file_size
            
sums = sum([d[1] for d in dirs.items() if d[1] <= 100000])

total_free = 70000000 - dirs['']
needed = 30000000 - total_free

to_delete = sorted([d[1] for d in dirs.items() if d[1] >= needed])[0]
        
print(sums)
print(to_delete)