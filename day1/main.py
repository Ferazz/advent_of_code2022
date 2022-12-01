from typing import List

def main():
    # Part 1
    elf_data = open("day1/input.txt")

    elf = 0
    calorie_l = [0]
    for line in elf_data:
        if line == '\n':
            elf += 1
            calorie_l.append(0)
            continue

        calorie_l[elf] += int(line)
    
    max_calorie = max(calorie_l)
    print(f"Elf with max calories has: {max_calorie} calories")


    # Part 2
    print(f"Top 3 elves has in total: {part2(calorie_l)} calories")
def part2(calorie_list: List[int]):
    sum_top_3 = 0
    for i in range(3):
        curr_max_cal = max(calorie_list)
        sum_top_3 += curr_max_cal
        calorie_list.remove(curr_max_cal)
    return sum_top_3
if __name__ == "__main__":
    main()