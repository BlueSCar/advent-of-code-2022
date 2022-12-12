def get_height(letter):
    heights = 'abcdefghijklmnopqrstuvwxyz'

    if letter == 'S':
        return 0
    elif letter == 'E':
        return 25
    else:
        return heights.index(letter)

def parse_input(file):
    file = open('day12/{0}.txt'.format(file))
    content = file.read()
    heightmap = [[get_height(i) for i in row.strip()] for row in content.split('\n')]
    
    stripped = content.replace('\n', '')
    row_length = content.index('\n')
    
    start_index = stripped.index('S')
    start_row = start_index // row_length
    start_column = start_index % row_length
    
    end_index = stripped.index('E')
    end_row = end_index // row_length
    end_column = end_index % row_length
    
    return heightmap, (start_row, start_column), (end_row, end_column)

def get_neighbors(position, heightmap):
    neighbors = []
    height = heightmap[position[0]][position[1]]
    
    if position[0] > 0:
        neighbors.append((position[0] - 1, position[1]))
        
    if position[0] < (len(heightmap) - 1):
        neighbors.append((position[0] + 1, position[1]))
    
    if position[1] > 0:
        neighbors.append((position[0], position[1] - 1))
        
    if position[1] < (len(heightmap[0]) - 1):
        neighbors.append((position[0], position[1] + 1))
            
    return [n for n in neighbors if heightmap[n[0]][n[1]] <= (height + 1)]

def set_distances(current_distance, visited, distances, heightmap):
    
    positions = [(i,j) for i in range(len(heightmap)) for j in range(len(heightmap[i])) if (i,j) not in visited and distances[i][j] == current_distance]
    if len(positions) == 0:
        return
    
    new_distance = current_distance + 1
    
    for current_position in positions:
    
        neighbors = [n for n in get_neighbors(current_position, heightmap) if n not in visited]
        
        for n in neighbors:
            neighbor_distance = distances[n[0]][n[1]]
            if neighbor_distance is None or neighbor_distance > new_distance:
                distances[n[0]][n[1]] = new_distance
    
        visited.add(current_position)
    
    set_distances(new_distance, visited, distances, heightmap)
    

def find_distance(start_position, end_position, heightmap):
    visited = set()
    distances = [[None for _ in row] for row in heightmap]
    distances[start_position[0]][start_position[1]] = 0
    
    set_distances(0, visited, distances, heightmap)
    
    end_distance = distances[end_position[0]][end_position[1]]
    
    return end_distance
    


heightmap, start_position, end_position = parse_input('test')
end_distance = find_distance(start_position, end_position, heightmap)

print(end_distance)
