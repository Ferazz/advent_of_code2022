from typing import List

def part1():
    message_stream = open("day6/input.txt")
    
    #LENGTH = 4 # Part 1
    LENGTH = 14 # Part 2
    marker = [0 for x in range(LENGTH)]
    for line in message_stream:
        for i, char in enumerate(line):
            marker[i % LENGTH] = char
            if found_marker(marker):
                print(f"Found marker at i: {i+1}")
                break
def found_marker(marker: List[str]):
    found = []
    for char in marker:
        if char in found:
            return False
        found.append(char)
    return True

if __name__ == "__main__":
    part1()