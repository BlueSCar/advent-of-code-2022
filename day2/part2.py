inputs = ['A', 'B', 'C']
outcomes = ['X', 'Y', 'Z']

file = open("day2/input.txt", "r")
lines = file.readlines()

matches = [l.strip().split(' ') for l in lines]

def get_match_points(match):
    opp_index = inputs.index(match[0])
    match_points = outcomes.index(match[1]) * 3
    
    player_points = 0
    if match_points == 0:
        player_points = ((opp_index - 1) % 3) + 1
    elif match_points == 3:
        player_points = opp_index + 1
    elif match_points == 6:
        player_points = ((opp_index + 1) % 3) + 1
    
    return match_points + player_points

total_points = sum([get_match_points(match) for match in matches])

print(total_points)