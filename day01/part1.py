file = open("day1/input.txt", "r")
contents = file.read()

elves = [e.split('\n') for e in contents.split('\n\n')]

max_calories = 0

for e in elves:
    calories = sum([int(c) for c in e])
    if calories > max_calories:
        max_calories = calories

print(max_calories)