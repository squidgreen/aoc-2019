
def read_file_into_list(filename):
    lines = []

    file = open(filename, "r")
    for line in file:
        lines.append(int(line))

    return lines

def read_intcode(filename):
    with open(filename, "r") as f:
        line = f.read()
        line = line.split(',')
        ints = [int(x) for x in line]
        return ints
