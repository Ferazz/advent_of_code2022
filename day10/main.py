def part1():
    input_instructions = open("day10/input.txt")
    cycles = 0
    X = 1
    sig_tot = 0
    cycles_to_check = [20, 60, 100, 140, 180, 220]
    cycle_index = 0
    instructions = get_instructions(input_instructions)
    instr_index = 0
    wait_time = 1
    to_be_added = 0
    while instr_index < len(instructions):
        wait_time -= 1
        
        ## Multiply
        if cycle_index != len(cycles_to_check) and cycles_to_check[cycle_index] == cycles:
            sig_tot += cycles * X
            cycle_index += 1
        
        if wait_time == 0:
            X += to_be_added
            instr_pair = instructions[instr_index]
            first = instr_pair[0]
            to_be_added = 0
            if first == "noop":
                wait_time = 1
            elif first == "addx":
                to_be_added = int(instr_pair[1])
                wait_time = 2
            instr_index += 1

        cycles += 1
    print(f"Total signal strength is: {sig_tot}")


def part2():
    input_instructions = open("day10/input.txt")
    cycles = 0
    X = 1
    
    CRT = [['.' for x in range(40)] for y in range(6)]
    crt_index = 0


    instructions = get_instructions(input_instructions)
    instr_index = 0
    wait_time = 0
    to_be_added = 0
    while instr_index < len(instructions):
        if wait_time == 0:
            X += to_be_added
            instr_pair = instructions[instr_index]
            first = instr_pair[0]
            to_be_added = 0
            if first == "noop":
                wait_time = 1
            elif first == "addx":
                to_be_added = int(instr_pair[1])
                wait_time = 2
            instr_index += 1

        write_pixel(CRT, crt_index % (6*40), X)

        crt_index += 1
        cycles += 1
        wait_time -= 1
    for line in CRT:
        print(''.join(line))


def get_instructions(input_instructions):
    res = []
    for line in input_instructions:
        splits = line.strip().split(" ")
        res.append(tuple(splits))
    return res

def write_pixel(mat, pos, X):
    x = pos % len(mat[0])
    y = pos // len(mat[0])
    if y == 6:
        return


    if abs(X - x) <= 1:
        mat[y][x] = '#'

if __name__ == "__main__":
    part2()