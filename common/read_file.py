
def read_file_into_list(filename):
    lines = []

    file = open(filename, "r")
    for line in file:
        lines.append(int(line))

    return lines
