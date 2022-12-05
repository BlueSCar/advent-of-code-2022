import re

state_pattern = r"[\[ ]([ A-Z])[\] ] [\[ ]([ A-Z])[\] ] [\[ ]([ A-Z])[\] ] [\[ ]([ A-Z])[\] ] [\[ ]([ A-Z])[\] ] [\[ ]([ A-Z])[\] ] [\[ ]([ A-Z])[\] ] [\[ ]([ A-Z])[\] ] [\[ ]([ A-Z])[\] ]"
instruction_pattern = r"move (\d+) from (\d) to (\d)"

file = open('day5/input.txt')
contents = file.read().split('\n\n')

def parse_current_state(input: str):
    stacks = []
    for i in range(9):
        stacks.append([])

    lines = input.split('\n')[:-1]
    for line in lines:
        crates = re.match(state_pattern, line).groups()
        
        for i in range(9):
            if crates[i] != ' ':
                stacks[i].insert(0, crates[i])
    
    return stacks
    
def parse_instructions(input: str):
    lines = contents[1].splitlines()
    
    instructions = [re.match(instruction_pattern, l).groups() for l in lines]
    
    return [dict(amount=int(i[0]), source=int(i[1]), destination=int(i[2])) for i in instructions]

def process_instructions(stacks, instructions):
    for instruction in instructions:
        source_stack = stacks[instruction['source'] - 1]
        destination_stack = stacks[instruction['destination'] - 1]
        stack_amount = instruction['amount']
        
        added = source_stack[-stack_amount:]
        destination_stack.extend(added)
        stacks[instruction['source'] - 1] = source_stack[:-stack_amount]
        

stacks = parse_current_state(contents[0])
instructions = parse_instructions(contents[1])

process_instructions(stacks, instructions)

print(''.join([s[-1] for s in stacks]))