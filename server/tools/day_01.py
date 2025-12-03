import time

from utils.read_input import read_input


def day_one_part_one():
    """Solve Day 1, Part 1 of the challenge."""

    start_time = time.perf_counter()

    # Get input and initialize variables
    inp = read_input("solutions/inputs/day_01.txt")
    inp = [int(line.replace("L", "-").replace("R", "")) for line in inp]
    dial_point = 50
    total_zeros = 0

    # Process each instruction
    for change in inp:
        dial_point = (dial_point + change) % 100
        if dial_point == 0:
            total_zeros += 1

    end_time = time.perf_counter()

    print(f"\tTotal times dial hit 0 (p1): {total_zeros}")
    print(f"\tExecution time: {end_time - start_time:.6f} seconds\n")
    return total_zeros


def day_one_part_two():
    """Solve Day 1, Part 2 of the challenge."""

    start_time = time.perf_counter()

    # Get input and initialize variables
    inp = read_input("solutions/inputs/day_01.txt")
    inp = [int(line.replace("L", "-").replace("R", "")) for line in inp]
    dial_point = 50
    total_zeros = 0

    # Process each instruction
    for change in inp:
        raw_end = dial_point + change

        # Calculate how many times we passed zero, including wrap to zero
        if change > 0:
            zeros_passed = raw_end // 100 - dial_point // 100
        else:
            zeros_passed = (dial_point - 1) // 100 - (raw_end - 1) // 100

        # Wrap the dial into 0-99
        dial_point = raw_end % 100

        # Add to total
        total_zeros += zeros_passed

    end_time = time.perf_counter()

    print(f"\tTotal times dial passed and hit 0 (p2): {total_zeros}")
    print(f"\tExecution time: {end_time - start_time:.6f} seconds\n")
    return total_zeros


if __name__ == "__main__":
    print("\n\t───── Day 1 Solutions ─────\n")
    day_one_part_one()
    day_one_part_two()
