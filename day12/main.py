import queue
import copy

from typing import List

def part1():
    height_map_input = open("day12/input.txt")
    height_map = []
    for line in height_map_input:
        height_map.append(list(map(lambda x : ord(x) - ord('a'), line.strip())))
    start = None
    end = None
    for y in range(len(height_map)):
        for x in range(len(height_map[0])):
            if height_map[y][x] == ord('S') - ord('a'): # ord('S')
                start = (x, y)
                height_map[y][x] = ord('a') - ord('a')
            elif height_map[y][x] == ord('E') - ord('a'): # ord('E')
                end = (x, y)
                height_map[y][x] = ord('z') - ord('a')
    
    ans = find_path(start, end, height_map)
    print(f"Steps taken: {len(ans)-2}")


def part2():
    height_map_input = open("day12/input.txt")
    height_map = []
    for line in height_map_input:
        height_map.append(list(map(lambda x : ord(x) - ord('a'), line.strip())))
    starts = []
    end = None
    for y in range(len(height_map)):
        for x in range(len(height_map[0])):
            if height_map[y][x] == ord('S') - ord('a'): # ord('S')
                starts.append((x, y))
                height_map[y][x] = 0
            elif height_map[y][x] == ord('E') - ord('a'): # ord('E')
                end = (x, y)
                height_map[y][x] = ord('z') - ord('a')
            elif height_map[y][x] == 0: # a
                starts.append((x, y))

    min_length = 1000000
    while starts:
        print(f"Starts left: {len(starts)}")
        start = starts[0]
        path = find_path(start, end, height_map)
        length = len(path)
        if length == 0:
            starts.remove(start)
            continue
        
        diff = 0
        for pos in path:
            diff += 1
            if height_map[pos[1]][pos[0]] == 0: # a, remove this from starts and reduce length
                if pos not in starts:
                    break

                length -= diff
                diff = 0
                print(f"Removing: {pos}")
                try:
                    starts.remove(pos)
                except:
                    print("Already removed")
                    pass
        print(f"Length: {length}")
        if length < min_length:
            min_length = length
    
    print(f"Minimum steps taken: {min_length}")



def find_path(start, end, height_map):
    q = queue.Queue()
    # [[PATH]]
    q.put([start])
    visited = [start]
    ans = None
    while True:
        if q.qsize() == 0:
            return []
        curr_path: List[tuple] = q.get()
        curr_pos = curr_path[-1]
        x, y = curr_pos
        current_height = height_map[y][x]

        if curr_pos == end:
            # Finished
            curr_path.append(curr_pos)
            ans = curr_path
            print("FINITO")
            break

        neighbours = get_neighbour_positions(x, y, height_map)
        for neighbour_pos in neighbours:
            #print(f"Neighbour: {neighbour_pos} with height: {height_map[neighbour_pos[1]][neighbour_pos[0]]}")
            # Ignore already visited positions
            if neighbour_pos in visited:
                continue

            neighbour_height = height_map[neighbour_pos[1]][neighbour_pos[0]]
            if current_height >= neighbour_height or current_height == neighbour_height - 1:
                cpy_path = copy.deepcopy(curr_path)
                cpy_path.append(neighbour_pos)
                visited.append(neighbour_pos)
                q.put(cpy_path)
    return ans


def get_neighbour_positions(x, y, height_map) -> List[tuple]:
    res = []

    
    # Make a 'plus' of positions
    for yi in range(y-1, y+2):
        if yi == y or yi < 0:
            continue
        try:
            _ = height_map[yi][x]
            res.append((x, yi))
        except:
            continue
    for xi in range(x-1, x+2):
        if xi == x or xi < 0:
            continue
        try:
            _ = height_map[y][xi]
            res.append((xi, y))
        except:
            continue

    return res

if __name__ == "__main__":
    #print(ord('a'))
    part2()