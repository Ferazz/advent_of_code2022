import math

def part1():
    move_input = open("day9/input.txt")
    walked_positions = [(0,0)]
    H_pos = [0,0]
    T_pos = [0,0]

    for line in move_input:
        direction, amount = split_line(line)
        for i in range(amount):
            move(H_pos, direction)

            if get_should_move(H_pos, T_pos):
                move_T(T_pos, H_pos)
                if tuple(T_pos) not in walked_positions:
                    walked_positions.append(tuple(T_pos))
    print(f"Tail walked over a total of {len(walked_positions)} positions")


def part2():
    move_input = open("day9/input.txt")
    walked_positions = [(0,0)]
    knots = [[0,0] for x in range(10)]


    for line in move_input:
        direction, amount = split_line(line)
        for i in range(amount):
            head = knots[0]
            move(head, direction)
            for knot_i in range(1, len(knots)):
                H_pos = knots[knot_i-1]
                T_pos = knots[knot_i]
                if get_should_move(T_pos, H_pos):
                    move_T(T_pos, H_pos)
            
            last = knots[-1]
            if tuple(last) not in walked_positions:
                walked_positions.append(tuple(last))
    print(f"Tail walked over a total of {len(walked_positions)} positions")

def split_line(line):
    l = line.split(" ")
    return l[0], int(l[1])

def move(object, direction):
    if direction == "U":
        object[1] += 1
    elif direction == "R":
        object[0] += 1
    elif direction == "D":
        object[1] -= 1
    elif direction == "L":
        object[0] -= 1

def move_T(T_pos, H_pos):
    is_higher_y = T_pos[1] < H_pos[1]
    is_higher_x = T_pos[0] < H_pos[0]
    is_same_row = T_pos[1] == H_pos[1]
    is_same_column = T_pos[0] == H_pos[0]

    if is_higher_y:
        T_pos[1] += 1
    elif is_same_row:
        pass
    else:
        T_pos[1] -= 1

    if is_higher_x:
        T_pos[0] += 1
    elif is_same_column:
        pass
    else:
        T_pos[0] -= 1

def get_should_move(pos1, pos2):
    diff_x = abs(pos1[0] - pos2[0])
    diff_y = abs(pos1[1] - pos2[1])
    return diff_x > 1 or diff_y > 1

if __name__ == "__main__":
    part2()
