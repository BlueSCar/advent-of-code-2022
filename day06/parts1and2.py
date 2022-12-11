file = open('day6/input.txt')
buffer = file.read()

def get_first_unique(length):
    for i in range(length, len(buffer)):
        section = buffer[i-length:i]
        if len(section) == len(set(section)):
            return i

print(get_first_unique(4))
print(get_first_unique(14))