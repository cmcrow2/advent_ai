import time

from utils.read_input import read_input


def day_two_part_one():
    """Solve Day 2, Part 1 of the challenge."""

    start_time = time.perf_counter()

    # Read and parse input to list of [a, b] pairs
    inp = read_input("tools/inputs/day_02.txt")
    inp = str(inp).split(",")
    inp = [list(map(int, pair.split("-"))) for pair in inp]

    total = 0

    for num_range in inp:
        for num in range(num_range[0], num_range[1] + 1):
            # Check if the number is a repeated pattern by comparing halves
            if str(num)[0 : len(str(num)) // 2] == str(num)[len(str(num)) // 2 :]:
                total += num

    end_time = time.perf_counter()

    print(f"\tInvalid ID sum (p1): {total}")
    print(f"\tExecution time: {end_time - start_time:.6f} seconds\n")
    return total


def day_two_part_two():
    """Solve Day 2, Part 2 of the challenge."""

    start_time = time.perf_counter()

    # Read and parse input to list of [start, end] pairs
    inp = read_input("tools/inputs/day_02.txt")
    inp = str(inp).split(",")
    ranges = [list(map(int, pair.split("-"))) for pair in inp]

    total = 0

    for start, end in ranges:
        for num in range(start, end + 1):
            string_num = str(num)
            string_num_len = len(string_num)
            # Only need to check pattern lengths up to half the number
            for pattern_len in range(1, string_num_len // 2 + 1):
                # Pattern must divide evenly into the number length
                if string_num_len % pattern_len != 0:
                    continue
                pattern = string_num[:pattern_len]
                # Check if repeating the pattern forms the original number
                if pattern * (string_num_len // pattern_len) == string_num:
                    total += num
                    break

    end_time = time.perf_counter()

    print(f"\tInvalid ID sum (p2): {total}")
    print(f"\tExecution time: {end_time - start_time:.6f} seconds\n")
    return total


if __name__ == "__main__":
    print("\n\t───── Day 2 Solutions ─────\n")
    day_two_part_one()
    day_two_part_two()
