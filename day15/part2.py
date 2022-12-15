import re
import z3

pattern = r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"

class Sensor:
    def __init__(self, inputs: tuple):
        self.sx = inputs[0]
        self.sy = inputs[1]
        self.bx = inputs[2]
        self.by = inputs[3]
        self.radius = abs(self.sx - self.bx) + abs(self.sy - self.by)

def parse_input(name):
    file = open("day15/{0}.txt".format(name))
    inputs = [re.findall(pattern, l)[0] for l in file.readlines()]

    sensors = [Sensor(tuple([int(j) for j in i])) for i in inputs]
    
    return sensors

# def get_line_coverage(sensors: Sensor, row: int, width: int):
#     beacon_cover = set()
    
#     for sensor in sensors:
#         range_start = 0
#         range_end = -1
        
#         if sensor.sy == row:
#             range_start = sensor.sx - sensor.radius
#             range_end = sensor.sx + sensor.radius
#         elif abs(row - sensor.sy) <= sensor.radius:
#             diff = sensor.radius - abs(row - sensor.sy)
            
#             range_start = sensor.sx - diff
#             range_end = sensor.sx + diff
#         else:
#             continue
        
#         if range_start < 0:
#             range_start = 0
        
#         if range_end > width:
#             range_end = width
            
#         coverage = list(range(range_start, range_end + 1))
#         beacon_cover.update(coverage)
            
#     return beacon_cover

# def find_distress_beacon(sensors, width):
#     for row in range(width + 1):
#         if row % 100000 == 0:
#             print(row)
            
#         coverage = get_line_coverage(sensors, row, width)
        
#         if len(coverage) < width + 1:
#             missing = [i for i in range(width + 1) if i not in coverage]
#             return (missing[0], row)
        
# def find_distress_beacon2(sensors, width):
#     beacon_map = [set() for _ in range(width + 1)]
    
#     for sensor in sensors:
#         row_start = sensor.sy - sensor.radius
#         if row_start < 0:
#             row_start = 0
            
#         row_end = sensor.sy + sensor.radius
#         if row_end > width:
#             row_end = width
        
#         for row in range(row_start, row_end + 1):
#             range_start = 0
#             range_end = -1
            
#             if sensor.sy == row:
#                 range_start = sensor.sx - sensor.radius
#                 range_end = sensor.sx + sensor.radius
#             elif abs(row - sensor.sy) <= sensor.radius:
#                 diff = sensor.radius - abs(row - sensor.sy)
                
#                 range_start = sensor.sx - diff
#                 range_end = sensor.sx + diff
#             else:
#                 continue
            
#             if range_start < 0:
#                 range_start = 0
            
#             if range_end > width:
#                 range_end = width
                
#             coverage = list(range(range_start, range_end + 1))
#             beacon_map[row].update(coverage)
            
#     missing_row = [r for r in range(width + 1) if len(beacon_map[r]) <= width][0]
#     missing_col = [c for c in range(width + 1) if c not in beacon_map[missing_row]][0]
    
#     return [missing_col, missing_row]

width = 4000000
sensors = parse_input("input")

x = z3.Int("x")
y = z3.Int("y")
solver = z3.Solver()

solver.add(x >= 0, x <= width, y > 0, y <= width)

for sensor in sensors:
    solver.add(z3.Abs(sensor.sx - x) + z3.Abs(sensor.sy - y) > sensor.radius)

solver.check()
solution = solver.model()

distress_signal = 4000000 * solution[x].as_long() + solution[y].as_long()

print(distress_signal)
