from typing import List
import queue

def part1():
    item_data = open("day5/input.txt")
    crates, commands = get_crate_data(item_data)
    stacks = setup_crates(crates)
    for command_line in commands:
        command = get_move_command(command_line)
        for i in range(command[0]):
            if stacks[command[1]-1].empty():
                continue
            stacks[command[2]-1].put(stacks[command[1]-1].get())
    
    print_top_crates(stacks)

def part2():
    item_data = open("day5/input.txt")
    crates, commands = get_crate_data(item_data)
    stacks = setup_crates(crates)
    for command_line in commands:
        command = get_move_command(command_line)
        crates_to_move = []
        for i in range(command[0]):
            if stacks[command[1]-1].empty():
                continue
            crates_to_move.append(stacks[command[1]-1].get())
        
        for crate_to_move in reversed(crates_to_move):
            stacks[command[2]-1].put(crate_to_move)
        
    print_top_crates(stacks)


def get_crate_data(item_data):
    crates = []
    commands = []
    split = False
    for line in item_data:
        if split:
            commands.append(line.strip())
            continue
        if line.strip() == "":
            split = True
        crates.append(line.strip())
    return crates, commands

def setup_crates(crates):
    rev_crates = reversed(crates)
    stacks = [queue.LifoQueue() for x in range(9)]

    index = 0
    for line in rev_crates:
        for i in range(len(line)):
            if (i - 1) % 4 == 0:
                if line[i] != " ":
                    stacks[index].put(line[i])
                index += 1
        index = 0
    return stacks

def get_move_command(command_line):
    res = []
    splice = command_line.split(" ")
    res.append(int(splice[1]))
    res.append(int(splice[3]))
    res.append(int(splice[5]))
    return res

def get_top(stacks: List[queue.LifoQueue]):
    res = []
    for stack in stacks:
        if stack.empty():
            res.append(" ")
        else:
            res.append(stack.get())
    return res

def print_top_crates(stacks):
    for crate in get_top(stacks):
        print(crate,end="")
if __name__ == "__main__":
    part2()