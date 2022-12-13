import json

def compare(left, right):
    leftType = type(left)
    rightType = type(right)
    
    if leftType == int and rightType == int:
        return left - right
    elif leftType == list and rightType == int:
        return compare(left, [right])
    elif leftType == int and rightType == list:
        return compare([left], right)
    else:
        if len(left) > 0 and len(right) > 0:
            diff = compare(left[0], right[0])
            
            if diff != 0:
                return diff
            else:
                return compare(left[1:], right[1:])
        else:
            return len(left) - len(right)

file = open('day13/input.txt')
inputs = file.read().split('\n\n')

pairs = [[json.loads(p.strip()) for p in l.split('\n')] for l in inputs]

comparisons = sum(i + 1 for i in range(len(pairs)) if compare(pairs[i][0], pairs[i][1]) < 0)
    
print(comparisons)
