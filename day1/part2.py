file = open("day1/input.txt", "r")
contents = file.read()

elves = [e.split('\n') for e in contents.split('\n\n')]

calories_counts = []

for e in elves:
    calories = sum([int(c) for c in e])
    calories_counts.append(calories)
    
sum = sum(sorted(calories_counts, reverse=True)[:3])

print(sum)