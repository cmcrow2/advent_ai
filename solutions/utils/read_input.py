def read_input(file_path):
    """Read the file and remove trailing newline characters"""
    with open(file_path, "r") as file:
        return file.read().splitlines()
