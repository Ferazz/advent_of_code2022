def main():
    droplet_input = open("day18/input.txt")
    blocks = get_blocks(droplet_input)
    total_sides = len(blocks) * 6
    print(f"Starting sides: {total_sides}")
    for i in range(len(blocks)):
        for y in range(len(blocks)):
            if i == y:
                continue
            x_dist = abs(blocks[i][0] - blocks[y][0])
            y_dist = abs(blocks[i][1] - blocks[y][1])
            z_dist = abs(blocks[i][2] - blocks[y][2])
            if x_dist + y_dist + z_dist == 1:
                print(f"Removing sides for: {blocks[i]} and {blocks[y]}")
                total_sides -= 1
    print(f"Total sides: {total_sides}")



def get_blocks(droplet_input):
    blocks = []

    for line in droplet_input:
        blocks.append(list(map(int, line.strip().split(","))))
    return blocks

if __name__ == "__main__":
    main()