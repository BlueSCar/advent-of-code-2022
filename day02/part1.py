opp_inputs = ['A', 'B', 'C']
player_inputs = ['X', 'Y', 'Z']

file = open("day2/input.txt", "r")
lines = file.readlines()

matches = [l.strip().split(' ') for l in lines]

def get_match_points(match):
    opp_points = opp_inputs.index(match[0]) + 1
    player_points = player_inputs.index(match[1]) + 1
    
    total = 0
    diff = player_points - opp_points
    if diff in [1,-2]:
        total = player_points + 6
    elif diff == 0:
        total = player_points + 3
    else:
        total = player_points
        
    return total

total_points = sum([get_match_points(match) for match in matches])

print(total_points)