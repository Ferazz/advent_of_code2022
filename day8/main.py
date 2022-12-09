from dataclasses import dataclass

@dataclass
class Direction:
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

def get_directions():
    return [Direction.UP, Direction.RIGHT, Direction.DOWN, Direction.LEFT]

def part1():
    trees_input = open("day8/input.txt")
    tree_mat = get_tree_matrix(trees_input)
    
    init_l_o_s = [-1 for x in range(len(tree_mat))]
    # Holds tallest height of tree in direction
    tree_line_of_sight_mat_dict = {
        0: init_l_o_s.copy(), # UP
        1: init_l_o_s.copy(), # RIGHT
        2: init_l_o_s.copy(), # DOWN
        3: init_l_o_s.copy()  # LEFT
    }
    sum_visible_trees = 0
    for y in range(len(tree_mat)):
        for x in range(len(tree_mat[0])):
            tree_visible = search_directions(tree_mat, tree_line_of_sight_mat_dict, x, y)
            if tree_visible:
                sum_visible_trees += 1
                if x == 0 or y == 0 or x == len(tree_mat)-1 or y == len(tree_mat)-1:
                    continue
                print(f"Found visible X: {x}, Y: {y} with value: {tree_mat[y][x]}")
    print(f"In total {sum_visible_trees} trees are visible")


def part2():
    trees_input = open("day8/input.txt")
    tree_mat = get_tree_matrix(trees_input)

    highest_scenic_score = 0
    pos = []
    for y in range(len(tree_mat)):
        for x in range(len(tree_mat[0])):
            tree_score = search_scores(tree_mat, x, y)
            if tree_score > highest_scenic_score:
                highest_scenic_score = tree_score
                pos = [x, y]

    print(f"The highest scenic score is: {highest_scenic_score} with position: {pos}")

def search_direction(tree_mat, tree_los_mat_dict, DIR, x, y):
    current_tree = tree_mat[y][x]

    if DIR == Direction.UP:
        for yi in range(0, y):
            other_tree = tree_mat[yi][x]
            if current_tree <= other_tree:
                tree_los_mat_dict[DIR][x] = other_tree
                return False

    elif DIR == Direction.RIGHT:
        for xi in range(len(tree_mat[0])-1, x, -1):
            other_tree = tree_mat[y][xi]
            if current_tree <= other_tree:
                tree_los_mat_dict[DIR][y] = other_tree
                return False
    
    elif DIR == Direction.DOWN:
        for yi in range(len(tree_mat)-1, y, -1):
            other_tree = tree_mat[yi][x]
            if current_tree <= other_tree:
                tree_los_mat_dict[DIR][x] = other_tree
                return False
    
    elif DIR == Direction.LEFT:
        for xi in range(0, x):
            other_tree = tree_mat[y][xi]
            if current_tree <= other_tree:
                tree_los_mat_dict[DIR][y] = other_tree
                return False

    #tree_los_mat_dict[DIR][index] = current_tree
    return True


def get_score(tree_mat, DIR, x, y):
    current_tree = tree_mat[y][x]

    sum_score = 0
    if DIR == Direction.UP:
        for yi in range(y-1,-1, -1):
            other_tree = tree_mat[yi][x]
            sum_score += 1
            if current_tree <= other_tree:
                break

    elif DIR == Direction.RIGHT:
        for xi in range(x+1, len(tree_mat[0])):
            other_tree = tree_mat[y][xi]
            sum_score += 1
            if current_tree <= other_tree:
                break
    
    elif DIR == Direction.DOWN:
        for yi in range(y+1, len(tree_mat)):
            other_tree = tree_mat[yi][x]
            sum_score += 1
            if current_tree <= other_tree:
                break
    
    elif DIR == Direction.LEFT:
        for xi in range(x-1, -1, -1):
            other_tree = tree_mat[y][xi]
            sum_score += 1
            if current_tree <= other_tree:
                break
    return sum_score

def get_tree_matrix(trees):
    res = []
    for line in trees:
        res.append(list(map(int, line.strip())))
    return res

def search_directions(tree_mat, tree_los_mat_dict, x, y) -> bool:
    is_visible_mat = [True for x in range(4)]
    
    for direction in get_directions():
        is_visible_mat[direction] = search_direction(tree_mat, tree_los_mat_dict, direction, x, y)

    return True in is_visible_mat

def search_scores(tree_mat, x, y):
    sum_scenic_score = 1
    
    for direction in get_directions():
        sum_scenic_score *= get_score(tree_mat, direction, x, y)

    return sum_scenic_score
if __name__ == "__main__":
    part1()
    part2()