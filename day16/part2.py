import networkx as nx
import re

from typing import List

input_pattern = r"Valve ([A-Z]{2}) has flow rate=(\d+); tunnels? leads? to valves? ([A-Z, ]+)"

class Valve:
    def __init__(self, inputs):
        self.name = inputs[0]
        self.flow_rate = int(inputs[1])
        self.tunnels = inputs[2].split(', ')
        
        self.distances = dict()
        
def calculate_pressure(valves: List[Valve], possible_moves):
    pressures = []
    
    if len(possible_moves) > 0:
        current_time, starting_released, path = possible_moves.pop()
        current_valve = path[-1]
        next_moves = []
        
        for valve, distance in valves[current_valve].distances.items():
            if distance <= current_time - 2 and valve not in path:
                time_left = current_time - distance - 1
                pressure_released = starting_released + valves[valve].flow_rate * time_left
                
                next_moves.append((time_left, pressure_released, path + [valve]))
                
    else:
        return pressures
    
def calculate_next(valves, current_time, starting_released, path):
    current_valve = path[-1]
    next_moves = []
    
    for valve, distance in valves[current_valve].distances.items():
        if distance <= current_time - 2 and valve not in path:
            time_left = current_time - distance - 1
            pressure_released = starting_released + valves[valve].flow_rate * time_left
            
            next_moves.append((time_left, pressure_released, path + [valve]))
            
    return next_moves

def calculate_pressures(valves: List[Valve]):
    paths = []
    possible_moves = [(26, 0, ['AA'])]
    
    while possible_moves:
        current_time, starting_released, path = possible_moves.pop()
        next_moves = calculate_next(valves, current_time, starting_released, path)
        
        if len(next_moves) > 0:
            possible_moves.extend(next_moves)
        else:
            paths.append(dict(path=path[1:], released=starting_released))
            
    return paths
    

def get_valves(name):
    file = open("day16/{0}.txt".format(name))
    inputs = [re.findall(input_pattern, line.strip())[0] for line in file.readlines()]
    
    G = nx.Graph()
    G.add_nodes_from([i[0] for i in inputs])
    
    valves = dict()
    for input in inputs:
        valve = Valve(input)
        valves[input[0]] = valve
        
        for node in valve.tunnels:
            G.add_edge(valve.name, node)
            
    nontrivials = [key for key in valves if valves[key].flow_rate > 0]
    
    for v in ['AA'] + nontrivials:
        for nt in nontrivials:
            if v != nt:
                valves[v].distances[nt] = nx.shortest_path_length(G, v, nt)
                
    return valves

valves = get_valves('input')
paths = sorted(calculate_pressures(valves), key=lambda x: x['released'], reverse=True)

index1 = 0
index2 = 1

for i in range(1, len(paths)):
    if not any(x in paths[i]['path'] for x in paths[0]['path']):
        index2 = i
        break
    
max_released = paths[index1]['released'] + paths[index2]['released']
    
for i in range(1, index2):
    for j in range(i + 1, index2):
        if not any(x in paths[j]['path'] for x in paths[i]['path']):
            released = paths[i]['released'] + paths[j]['released']
            if released > max_released:
                max_released = released
                index2 = j
                break

print(max_released)
