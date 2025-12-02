from utils.read_input import read_input


def day_one_part_one():
    """Solve Day 1, Part 1 of the challenge."""

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

    print(f"Total times dial hit 0 (p1): {total_zeros}")
    return total_zeros


def day_one_part_two():
    """Solve Day 1, Part 2 of the challenge."""

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

    print(f"Total times dial hit 0 (p2): {total_zeros}")
    return total_zeros


if __name__ == "__main__":
    day_one_part_one()
    day_one_part_two()
