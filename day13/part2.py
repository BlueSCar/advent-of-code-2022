import json
from functools import cmp_to_key
from math import prod

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
inputs = file.readlines()

packets = [json.loads(i.strip()) for i in inputs if i != '\n']
packets.append([[2]])
packets.append([[6]])

ordered_packets = sorted(packets, key=cmp_to_key(compare))
product = prod([(i + 1) for i in range(len(ordered_packets)) if ordered_packets[i] == [[2]] or ordered_packets[i] == [[6]]])
    
print(product)
