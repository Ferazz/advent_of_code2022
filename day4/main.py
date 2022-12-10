from typing import List

def part1():
    item_data = open("day4/input.txt")
    sum_contained_sections = 0
    for line in item_data:
        given_sections: List[str] = line.strip().split(',')
        elf1_numbers: List[int] = get_numbers(given_sections[0])
        elf2_numbers: List[int] = get_numbers(given_sections[1])
        
        if is_contained(elf1_numbers, elf2_numbers):
            sum_contained_sections += 1
        elif is_contained(elf2_numbers, elf1_numbers):
            sum_contained_sections += 1
    print(f"Total duplicated sections: {sum_contained_sections}")

def part2():
    item_data = open("day4/input.txt")
    sum_overlapping_sections = 0
    for line in item_data:
        given_sections: List[str] = line.strip().split(',')
        elf1_numbers: List[int] = get_numbers(given_sections[0])
        elf2_numbers: List[int] = get_numbers(given_sections[1])
        
        if is_overlapping(elf1_numbers, elf2_numbers):
            sum_overlapping_sections += 1
        elif is_overlapping(elf2_numbers, elf1_numbers):
            sum_overlapping_sections += 1
    print(f"Total duplicated sections: {sum_overlapping_sections}")


def get_numbers(sections):
    nums = sections.split('-')
    return list(map(int, nums))

def is_contained(base, check):
    return check[0] >= base[0] and check[1] <= base[1]

def is_overlapping(base, check):
    return (check[0] >= base[0] and check[0] <= base[1]) or (check[1] >= base[0] and check[1] <= base[1])

if __name__ == "__main__":
    part2()