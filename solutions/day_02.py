from utils.read_input import read_input


def day_two_part_one():
    """Solve Day 2, Part 1 of the challenge."""

    # Read and parse input to list of [a, b] pairs
    inp = read_input("solutions/inputs/day_02.txt")
    inp = str(inp).split(",")
    inp = [list(map(int, pair.split("-"))) for pair in inp]

    total = 0

    for num_range in inp:
        for num in range(num_range[0], num_range[1] + 1):
            if str(num)[0 : len(str(num)) // 2] == str(num)[len(str(num)) // 2 :]:
                total += num

    print("Invalid ID sum:", total)
    return total


if __name__ == "__main__":
    day_two_part_one()
