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
    
def calculate_tail_position(head_position, tail_position):
    movement = [0,0]
    diff = np.subtract(head_position, tail_position)
    
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
            
    return np.add(tail_position, movement)

file = open('day9/input.txt')
directions = [dict(direction=l[0], steps=int(l[1])) for l in (line.strip().split(' ') for line in file.readlines())]

head_position = [0,0]
tail_position = [0,0]
tail_history = {(0,0)}

for dir in directions:
    step_vector = vectorize_step(dir['direction'])
    for step in range(dir['steps']):
        head_position = np.add(head_position, step_vector)
        tail_position = calculate_tail_position(head_position, tail_position)
        tail_history.add((tail_position[0], tail_position[1]))

print(len(tail_history))