file = open('day8/input.txt')

trees = [[int(tree) for tree in list(line.strip())] for line in file.readlines()]

rows = len(trees)
columns = len(trees[0])

def is_visible(row, column):
    if row == 0 or column == 0 or row == (rows - 1) or column == (columns - 1):
        return True
    
    height = trees[row][column]
    if height > max(trees[row][:column]) or height > max(trees[row][column+1:]):
        return True
    
    if height > max([row[column] for row in trees[:row]]) or height > max([row[column] for row in trees[row+1:]]):
        return True

visible_trees = 0
for row in range(rows):
    for col in range(columns):
        if is_visible(row, col):
            visible_trees += 1
        

print(visible_trees)