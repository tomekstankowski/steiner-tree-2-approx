import sys


def load_problem(path):
    f = open(path, 'r')
    line = f.readline()
    while not line.startswith('SECTION Graph'):
        line = f.readline()
    while not line.startswith('Nodes'):
        line = f.readline()
    n = int(line.replace('Nodes', ''))
    matrix = [[-1 for x in range(n)] for y in range(n)]
    for i in range(n):
        matrix[i][i] = 0
    while not line.startswith('END'):
        line = f.readline()
        if line.startswith('E '):
            line_parts = line.split(' ')
            v = int(line_parts[1])
            u = int(line_parts[2])
            weight = int(line_parts[3])
            matrix[u - 1][v - 1] = weight
            matrix[v - 1][u - 1] = weight
    while not line.startswith('SECTION Terminals'):
        line = f.readline()
    while not line.startswith('Terminals'):
        line = f.readline()
    terminals = []
    while not line.startswith('END'):
        line = f.readline()
        if line.startswith('T'):
            t = int(line.split(' ')[1])
            terminals.append(t)
    return (matrix, terminals)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('Provide test file path')
        sys.exit()
    test_file_path = sys.argv[1]
    print('Loading ', test_file_path)
    (graph, terminals) = load_problem(test_file_path)
