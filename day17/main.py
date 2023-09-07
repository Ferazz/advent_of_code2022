from dataclasses import dataclass
from typing import List

@dataclass
class Point():
    x: int = -1
    y: int = -1

def part1():
    
    gas_blow = open("day17/input.txt").readline().strip()
    gas_index = 0

    WIDTH = 7

    height_map = [0 for x in range(WIDTH)]
    block_creator = BlockCreator()

    num_blocks_dropped = 0
    curr_block = None
    while num_blocks_dropped != 2022:
        print(get_height(height_map))
        if curr_block is None:
            curr_block = block_creator.get_next_block(get_height(height_map))
            print("new block!")
            num_blocks_dropped += 1
        else:
            push_right = None

            if get_next_push(gas_blow, gas_index) == '>':
                push_right = True
            else:
                push_right = False
            gas_index += 1
            if gas_index == len(gas_blow):
                gas_index = 0
            move_block_sideways(curr_block, height_map, push_right)

            if not move_block_down(curr_block, height_map):
                # Current block should stop
                stop_block(curr_block, height_map)
                curr_block = None
    

    print(f"Maximum height achieved: {max(height_map)}")
    

def get_height(height_map):
    return max(height_map)

def get_next_push(gas_blow, index):
    return gas_blow[index]
    

def move_block_down(block: List[Point], height_map) -> bool:
    """ Return True if block could be moved down """
    # Check for collision
    for point in block:
        if height_map[point.x]+1 == point.y:
            return False
        elif point.y == 0:
            print("????")
        else:
            print("ÄÄÄÄ")
    
    # Move block
    for point in block:
        point.y -= 1
    return True


def move_block_sideways(block: List[Point], height_map, move_right: bool) -> bool:
    """ Returns True if block could be moved sideways """
    WIDTH = 7
    if move_right:

        right_most_points = []
        last_y = -1
        largest_x = 0
        for point in block:
            if point.y != last_y:
                ...

        max_point_x = max(block, key=lambda point : point.x)
        if max_point_x.x+1 == WIDTH:
            # Collision
            return False
        else:
            for point in block:
                point.x += 1
    else:
        min_point_x = min(block, key=lambda point : point.x)
        if min_point_x.x == 0:
            # Collision
            return False
        else:
            for point in block:
                point.x -= 1
    return True
    
def stop_block(block, height_map):
    """ Change height map in place with new block"""
    for point in block:
        if height_map[point.x] < point.y:
            height_map[point.x] = point.y
        

class BlockCreator():
    
    i = 0
    NUM_BLOCKS = 5
    DIST = 3
    def get_next_block(self, highest_block) -> List[Point]:
        bottom_block_height = highest_block + self.DIST
        res = []
        match self.i: 
            case 0: # ---- block
                res = [Point(2, bottom_block_height), Point(3, bottom_block_height), Point(4, bottom_block_height), Point(5, bottom_block_height)]
            case 1: # + block
                res = [Point(3, bottom_block_height + 2), Point(2, bottom_block_height + 1), Point(3, bottom_block_height + 1), Point(4, bottom_block_height + 1), Point(3, bottom_block_height)]
            case 2: # rev-L block
                res = [Point(4, bottom_block_height+2), Point(4, bottom_block_height+1), Point(2, bottom_block_height), Point(3, bottom_block_height), Point(4, bottom_block_height)]
            case 3: # I block 
                res = [Point(2, bottom_block_height+3), Point(2, bottom_block_height+2), Point(2, bottom_block_height+1), Point(2, bottom_block_height)]
            case 4: # :: block
                res = [Point(2, bottom_block_height+1), Point(3, bottom_block_height+1), Point(2, bottom_block_height), Point(3, bottom_block_height)]
        self.i += 1
        if self.i == 5:
            self.i = 0
        return res
if __name__ == "__main__":
    part1()