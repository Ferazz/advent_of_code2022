
def main():
    monkey_input = open("day21/input.txt")
    monkey_calculations = extract_calculations(monkey_input)

    # On left side
    if find_human(monkey_calculations["root"]["monkey1"], monkey_calculations):
        desired_value = recursive_calc(monkey_calculations["root"]["monkey2"], monkey_calculations)
        print(f"Desired: {desired_value}")
        yell_value = recursive_get_value(monkey_calculations["root"]["monkey1"], monkey_calculations, desired_value)
    else:
        desired_value = recursive_calc(monkey_calculations["root"]["monkey1"], monkey_calculations)
        yell_value = recursive_get_value(monkey_calculations["root"]["monkey2"], monkey_calculations, desired_value)
    print(f"Human should yell: {yell_value}")

    #print(f"Root yells: {int(recursive_calc('root', monkey_calculations))}")


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
    return int(current_monkey["value"])

def recursive_get_value(chosen_monkey, monkeys, current_value):
    current_monkey = monkeys[chosen_monkey]
    curr_val = current_value

    if chosen_monkey == "humn":
        return curr_val
    
    # Calculate off-shoots and alter the current value accordingly
    elif find_human(current_monkey["monkey1"], monkeys):
        match(current_monkey["operation"]):
            case "+":
                curr_val -= recursive_calc(current_monkey["monkey2"], monkeys)
                return recursive_get_value(current_monkey["monkey1"], monkeys, curr_val)
            case "-":
                curr_val += recursive_calc(current_monkey["monkey2"], monkeys)
                return recursive_get_value(current_monkey["monkey1"], monkeys, curr_val)
            case "*":
                curr_val /= recursive_calc(current_monkey["monkey2"], monkeys)
                return recursive_get_value(current_monkey["monkey1"], monkeys, curr_val)
            case "/":
                curr_val *= recursive_calc(current_monkey["monkey2"], monkeys)
                return recursive_get_value(current_monkey["monkey1"], monkeys, curr_val)
    else: # Human on right side of operations cause certain issues, see '-' and '/'
        match(current_monkey["operation"]):
            case "+":
                curr_val -= recursive_calc(current_monkey["monkey1"], monkeys)
                return recursive_get_value(current_monkey["monkey2"], monkeys, curr_val)
            case "-":
                curr_val = recursive_calc(current_monkey["monkey1"], monkeys) - curr_val
                return recursive_get_value(current_monkey["monkey2"], monkeys, curr_val)
            case "*":
                curr_val /= recursive_calc(current_monkey["monkey1"], monkeys)
                return recursive_get_value(current_monkey["monkey2"], monkeys, curr_val)
            case "/":
                curr_val = recursive_calc(current_monkey["monkey1"], monkeys) / curr_val
                return recursive_get_value(current_monkey["monkey2"], monkeys, curr_val)


def find_human(monkey, monkeys):
    current_monkey = monkeys[monkey]
    if monkey == "humn":
        return True
    elif current_monkey["value"] is not None:
        return False
    else:
        return find_human(current_monkey["monkey1"], monkeys) or find_human(current_monkey["monkey2"], monkeys)
        

def extract_calculations(monkey_input):
    res = {}

    for line in monkey_input:
        spliced = line.strip().split(": ")
        monkey = spliced[0]
        if monkey == "humn":
            res[monkey] = {}
            continue
        operation_or_num = spliced[1]

        if operation_or_num.isnumeric():
            res[monkey] = {"value" : int(operation_or_num)}
        else:
            recursive_answer = operation_or_num.split(" ")
            monkey1 = recursive_answer[0]
            operation = recursive_answer[1]
            monkey2 = recursive_answer[2]
            res[monkey] = {"monkey1" : monkey1, "monkey2" : monkey2, "operation" : operation, "value" : None, "human" : False}
    return res

if __name__ == "__main__":
    main()