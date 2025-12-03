def read_input(file_path):
    """Read the file and remove trailing newline characters"""
    with open(file_path, "r") as file:
        res = file.read()
        if "\n" in res:
            return res.splitlines()
        return res
