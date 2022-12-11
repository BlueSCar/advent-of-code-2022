import numpy as np

def vectorize_step(direction):
    if direction == 'U':
        return [0,1]
    elif direction == 'D':
        return [0,-1]
    elif direction == 'R':
        return [1,0]
    elif direction == 'L':
        return [-1,0]
    
def calculate_next_position(knot, next_knot):
    movement = [0,0]
    diff = np.subtract(knot, next_knot)
    
    if abs(diff[0]) < 2 and abs(diff[1]) < 2:
        movement = [0,0]
    elif abs(diff[0]) > 1:
        movement[0] = diff[0]/abs(diff[0])
        if abs(diff[1]) > 0:
            movement[1] = diff[1]/abs(diff[1])
    elif abs(diff[1]) > 1:
        movement[1] = diff[1]/abs(diff[1])
        if abs(diff[0]) > 0:
            movement[0] = diff[0]/abs(diff[0])
            
    return np.add(next_knot, movement)

def process_positions(positions, initial_step):
    positions[0] = np.add(positions[0], initial_step)
    for i in range(1, len(positions)):
        positions[i] = calculate_next_position(positions[i-1], positions[i])

file = open('day9/input.txt')
directions = [dict(direction=l[0], steps=int(l[1])) for l in (line.strip().split(' ') for line in file.readlines())]

positions = [[0,0]]*10
tail_history = {(0,0)}

for dir in directions:
    step_vector = vectorize_step(dir['direction'])
    for step in range(dir['steps']):
        process_positions(positions, step_vector)
        tail_history.add((positions[-1][0], positions[-1][1]))

print(len(tail_history))