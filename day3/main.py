from typing import List

def part1():
    # Part 1
    item_data = open("day3/input.txt")
    sum_priority = 0
    for backpack in item_data:
        common_item = get_common_item(backpack.strip())
        sum += get_priority(common_item)
    print(f"Total sum is: {sum}")

def part2():
    # Part 2
    item_data = list(open("day3/input.txt"))
    sum_priority = 0
    
    elf_n = 1
    current_group: List[str] = []
    for i in range(len(item_data)):
        current_group.append(item_data[i].strip())
        if elf_n == 3:

            badge = get_badge(current_group)
            sum_priority += get_priority(badge)
            current_group.clear()
            elf_n = 0
        elf_n += 1

    print(f"Total sum is: {sum_priority}")

def get_common_item(backpack_items):
    # Part 1
    comp_a = backpack_items[:len(backpack_items)//2]
    comp_b = backpack_items[len(backpack_items)//2:]

    for item in comp_a:
        if item in comp_b:
            return item

def get_badge(elves_backpacks: List[List[str]]):
    # Part 2
    for item in elves_backpacks[0]:
        if item in elves_backpacks[1] and item in elves_backpacks[2]:
            return item
    


def get_priority(item:str):
    if item.islower():
        return ord(item) - 96 # Start priority 1
    else:
        return ord(item) - 38 # Start priority 27
if __name__ == "__main__":
    part2()