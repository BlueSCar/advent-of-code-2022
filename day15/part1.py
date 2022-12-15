import re

pattern = r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"

def get_distance(a: tuple, b: tuple):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_uncovered(name, row):
    file = open("day15/{0}.txt".format(name))
    inputs = [re.findall(pattern, l)[0] for l in file.readlines()]

    beacon_cover = set()
    sensors = [tuple([int(j) for j in i]) for i in inputs]
    row_sensors = set([s[0] for s in sensors if s[1] == row])
    row_beacons = set([s[2] for s in sensors if s[3] == row])

    for sensor in sensors:
        distance = get_distance((sensor[0], sensor[1]), (sensor[2], sensor[3]))
        
        if sensor[1] == row:
            beacon_cover.update(range(sensor[0] - distance, sensor[0] + distance + 1))
        elif abs(row - sensor[1]) <= distance:
            diff = distance - abs(row - sensor[1])
            x = list(range(sensor[0] - diff, sensor[0] + diff + 1))
            beacon_cover.update(x)
            
    uncovered = [i for i in beacon_cover if i not in row_sensors and i not in row_beacons]
    
    return len(uncovered)

count = get_uncovered('input', 2000000)

print(count)
