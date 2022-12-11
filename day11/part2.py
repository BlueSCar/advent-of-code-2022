import numpy as np
import re
from math import prod
from typing import List

items_pattern = r"Starting items: (.+)"
operation_pattern = r"Operation: new = (.+)"
divisor_pattern = r"Test: divisible by (\d+)"
throw_pattern = r"throw to monkey (\d+)"

class Monkey:
    def __init__(self, items, evaluator, divisor, test_pass_monkey, test_fail_monkey):
        self.inspections = 0
        self.items = items
        self.evaluator = compile(evaluator, '<string>', 'eval')
        self.divisor = divisor
        self.test_pass_monkey = test_pass_monkey
        self.test_fail_monkey = test_fail_monkey
        
    def inspect(self, lcm):
        self.inspections += 1
        item = self.items.pop()
        
        worry_level = eval(self.evaluator, {'old': item}) % lcm
        if worry_level % self.divisor == 0:
            to_monkey = self.test_pass_monkey
        else:
            to_monkey = self.test_fail_monkey
            
        return dict(to_monkey=to_monkey, worry_level=worry_level)
    
def read_input(filename):    
    file = open(filename)
    raw_monkeys = file.read().split('\n\n')
    monkeys = []

    for monk in raw_monkeys:
        lines = monk.split('\n')
        items = [int(i.strip()) for i in re.findall(items_pattern, lines[1])[0].split(', ')]
        evaluator = re.findall(operation_pattern, lines[2])[0]
        divisor = re.findall(divisor_pattern, lines[3])[0]
        success_throw = re.findall(throw_pattern, lines[4])[0]
        fail_throw = re.findall(throw_pattern, lines[5])[0]
        
        monkeys.append(Monkey(items, evaluator, int(divisor), int(success_throw), int(fail_throw)))
        
    return monkeys

def simulate_round(monkeys : List[Monkey], lcm: int):
    for monkey in monkeys:
        while monkey.items:
            result = monkey.inspect(lcm)
            monkeys[result['to_monkey']].items.append(result['worry_level'])
            
def get_monkey_business(monkeys: List[Monkey], rounds):
    lcm = np.lcm.reduce([m.divisor for m in monkeys])
    
    for _ in range(rounds):
        simulate_round(monkeys, lcm)
        
    inspections = sorted([m.inspections for m in monkeys], reverse=True)
    return prod(inspections[:2])
            
monkeys = read_input('day11/input.txt')
monkey_business = get_monkey_business(monkeys, 10000)
    
print(monkey_business)
