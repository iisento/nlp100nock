def count_lines(path):
    count = 0
    with open(path) as f:
        line = f.readline()
        while line:
            count += 1
            line = f.readline()
    return count
