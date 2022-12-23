def part1():
    monkey_input = open("day21/input.txt")
    monkey_calculations = extract_calculations(monkey_input)
    print(f"Root yells: {int(recursive_calc('root', monkey_calculations))}")

def recursive_calc(chosen_monkey: str, monkeys):
    # Base case
    current_monkey = monkeys[chosen_monkey]
    if current_monkey["value"] is not None:
        return current_monkey["value"]
    
    match(monkeys[chosen_monkey]["operation"]):
        case "+":
            current_monkey["value"] = recursive_calc(current_monkey["monkey1"], monkeys) + recursive_calc(current_monkey["monkey2"], monkeys)
        case "-":
            current_monkey["value"] = recursive_calc(current_monkey["monkey1"], monkeys) - recursive_calc(current_monkey["monkey2"], monkeys)
        case "*":
            current_monkey["value"] = recursive_calc(current_monkey["monkey1"], monkeys) * recursive_calc(current_monkey["monkey2"], monkeys)
        case "/":
            current_monkey["value"] = recursive_calc(current_monkey["monkey1"], monkeys) / recursive_calc(current_monkey["monkey2"], monkeys)
    return current_monkey["value"]

def extract_calculations(monkey_input):
    res = {}

    for line in monkey_input:
        spliced = line.strip().split(": ")
        monkey = spliced[0]
        operation_or_num = spliced[1]

        if operation_or_num.isnumeric():
            res[monkey] = {"value" : int(operation_or_num)}
        else:
            recursive_answer = operation_or_num.split(" ")
            monkey1 = recursive_answer[0]
            operation = recursive_answer[1]
            monkey2 = recursive_answer[2]
            res[monkey] = {"monkey1" : monkey1, "monkey2" : monkey2, "operation" : operation, "value" : None}
    return res

if __name__ == "__main__":
    part1()