file = open('day8/input.txt')

trees = [[int(tree) for tree in list(line.strip())] for line in file.readlines()]
scores = [[0 for tree in row] for row in trees]

rows = len(trees)
columns = len(trees[0])

def get_view(height, trees):
    count = 0
    for tree in trees:
        count += 1
        if tree >= height:
            break;
    
    return count

def get_score(row, column):
    if row == 0 or column == 0 or row == (rows - 1) or column == (columns -1):
        return 0
    
    height = trees[row][column]
    
    tree_row = trees[row]
    tree_column = [row[column] for row in trees]
    
    left_score = get_view(height, reversed(tree_row[:column]))
    right_score = get_view(height, tree_row[column+1:])
    up_score = get_view(height,  reversed(tree_column[:row]))
    down_score = get_view(height, tree_column[row+1:])
        
    return left_score * right_score * up_score * down_score
      
for k in range(len(scores)):
    for l in range(len(scores[k])):
        scores[k][l] = get_score(k,l)
   
max_score = max([score for row in scores for score in row]) 

print(max_score)