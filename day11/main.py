from typing import List, Tuple

class Monkey():
    items: List[int] = None
    operation = None
    test_div = None
    next_monkeys = None
    inspections = 0
    def __init__(self, starting_items, operation, test_div, next_monkeys) -> None:
        self.items = starting_items
        self.operation = operation
        self.test_div = test_div
        self.next_monkeys = next_monkeys
    
    def calculate_worry_level(self):
        if self.items:
            return self.items[0]


def part1():
    inp = open("day11/input.txt")
    monkeys = get_monkeys()
    for round in range(20):
        for monkey in monkeys:
            for item in monkey.items:
                new_worry = int(monkey.operation(item) % monkey.test_div)#// 3)
                #print(new_worry)
                if new_worry == 0: # % monkey.test_div == 0 :
                    monkeys[monkey.next_monkeys[0]].items.append(new_worry)
                else:
                    monkeys[monkey.next_monkeys[1]].items.append(new_worry)
                monkey.inspections += 1
            monkey.items.clear() # All items thrown
        
    for i, monkey in enumerate(monkeys):
        print(f"Monkey {i}: {monkey.inspections}")
    
    
    print(f"Total: {get_max_monkey_business(monkeys)}")

def part2():
    inp = open("day11/input.txt")
    monkeys = get_monkeys()
    for round in range(10000):
        for monkey in monkeys:
            for item in monkey.items:
                new_worry = monkey.operation(item) % monkey.test_div

                if new_worry == 0:
                    monkeys[monkey.next_monkeys[0]].items.append(new_worry)
                else:
                    monkeys[monkey.next_monkeys[1]].items.append(new_worry)
                monkey.inspections += 1
            monkey.items.clear() # All items thrown
        print(round)
    for i, monkey in enumerate(monkeys):
        print(f"Monkey {i}: {monkey.inspections}")
    
    print(f"Total: {get_max_monkey_business(monkeys)}")
    
    

def get_max_monkey_business(monkeys):
    inspects = [monkey.inspections for monkey in monkeys]
    max1 = max(inspects)
    inspects.remove(max1)
    max2 = max(inspects)
    return max1 * max2


def get_monkeys():#(input_txt):
    """res = []
    starting_items = []
    operation = None
    test = None
    for line in input_txt:
        if "Monkey" in line:
            res.append(Monkey(starting_items, operation, test))
        elif "Starting" in line:
            starting_items = map(int, line.strip().split(":")[1])
        elif "Operation" in line:
            operation = line.strip().split(":")[1]"""
    monkey0 = Monkey([84, 72, 58, 51], lambda x : x * 3, 13, (1, 7))
    monkey1 = Monkey([88, 58, 58], lambda x : x + 8, 2, (7, 5))
    monkey2 = Monkey([93, 82, 71, 77, 83, 53, 71, 89], lambda x : x * x, 7, (3, 4))
    monkey3 = Monkey([81, 68, 65, 81, 73, 77, 96], lambda x : x + 2, 17, (4, 6))
    monkey4 = Monkey([75, 80, 50, 73, 88], lambda x : x + 3, 5, (6, 0))
    monkey5 = Monkey([59, 72, 99, 87, 91, 81], lambda x : x * 17, 11, (2, 3))
    monkey6 = Monkey([86, 69], lambda x : x + 6, 3, (1, 0))
    monkey7 = Monkey([91], lambda x : x + 1, 19, (2, 5))
    return [monkey0, monkey1, monkey2, monkey3, monkey4, monkey5, monkey6, monkey7]

if __name__ == "__main__":
    part1()