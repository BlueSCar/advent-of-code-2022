import re
from enum import Enum
import numpy as np

point_pattern = r"\d+,\d+"

class Matter(Enum):
    Air = 1
    Sand = 2
    Rock = 3
    
def generate_map(file):
    file = open("day14/{0}.txt".format(file))
    lines = file.readlines()
    matches = [[[int(n) for n in m.split(',')] for m in re.findall(point_pattern, line.strip())] for line in lines]
    
    max_x = max([i[0] for m in matches for i in m])
    max_y = max([i[1] for m in matches for i in m])
    
    map = [np.repeat(Matter.Air, max_x + 500) for y in range(max_y + 2)]
    map.append(np.repeat(Matter.Rock, max_x + 500))
    
    for match in matches:
        for i in range(1, len(match)):
            start = match[i - 1]
            end = match[i]
            
            if start[0] == end[0]:
                if start[1] < end[1]:
                    for j in range(start[1], end[1] + 1):
                        map[j][start[0]] = Matter.Rock
                else:
                    for j in range(end[1], start[1]):
                        map[j][start[0]] = Matter.Rock
            elif start[1] == end[1]:
                if start[0] < end[0]:
                    for j in range(start[0], end[0] + 1):
                        map[start[1]][j] = Matter.Rock
                else:
                    for j in range(end[0], start[0]):
                        map[start[1]][j] = Matter.Rock
    
    return map

def drop_sand(x, y, max_depth):
    if map[y + 1][x] == Matter.Air:
        return drop_sand(x, y + 1, max_depth)
    elif map[y + 1][x - 1] == Matter.Air:
        return drop_sand(x - 1, y + 1, max_depth)
    elif map[y + 1][x + 1] == Matter.Air:
        return drop_sand(x + 1, y + 1, max_depth)
    elif x == 500 and y == 0:
        return False
    else:
        map[y][x] = Matter.Sand
        return True
            
    
map = generate_map('test')

keep_dropping = True
while keep_dropping:
    keep_dropping = drop_sand(500, 0, len(map))
    
units = [col for row in map for col in row if col == Matter.Sand]

print(len(units))
