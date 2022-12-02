from typing import List

def main_part1():
    # Part 1
    elf_data = open("day2/input.txt")
    score = 0
    for line in elf_data:
        # Remove EOL and split for data
        moves = line.strip().split(" ")
        print(moves)
        opp_move = moves[0]
        my_move = moves[1]

        if my_move == "X":
            score += 1
        elif my_move == "Y":
            score += 2
        elif my_move == "Z":
            score += 3
        score += calculate_round_part1(opp_move, my_move)
    print(f"My total score would be: {score} pts")

def main_part2():
    # Part 2
    elf_data = open("day2/input.txt")
    score = 0
    for line in elf_data:
        # Remove EOL and split for data
        moves = line.strip().split(" ")
        opp_move = moves[0]
        game_decision = moves[1]
        my_move = calculate_round_part2(opp_move, game_decision)
        score += calculate_move_pts_part2(my_move)
        score += calculate_round_part1(opp_move, my_move)
        
    print(f"My total score would be: {score} pts")


def calculate_round_part1(opp_move, my_move):
    if opp_move == "A":
        if my_move == "X":
            return 3
        elif my_move == "Y":
            return 6
        else:
            return 0
    elif opp_move == "B":
        if my_move == "X":
            return 0
        elif my_move == "Y":
            return 3
        elif my_move == "Z":
            return 6
    elif opp_move == "C":
        if my_move == "X":
            return 6
        elif my_move == "Y":
            return 0
        elif my_move == "Z":
            return 3
    else:
        print("Faulty data")


def calculate_move_pts_part2(move):
    if move == "X":
        return 1
    elif move == "Y":
        return 2
    elif move == "Z":
        return 3

def calculate_round_part2(opp_move, my_move):
    if my_move == "X": # Lose
        if opp_move == "A":
            return "Z"
        elif opp_move == "B":
            return "X"
        elif opp_move == "C":
            return "Y"
    elif my_move == "Y": # Draw
        if opp_move == "A":
            return "X"
        elif opp_move == "B":
            return "Y"
        elif opp_move == "C":
            return "Z"
    elif my_move == "Z": # Win
        if opp_move == "A":
            return "Y"
        elif opp_move == "B":
            return "Z"
        elif opp_move == "C":
            return "X"
if __name__ == "__main__":
    main_part2()