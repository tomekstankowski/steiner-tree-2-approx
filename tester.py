import sys
from time import time
from steiner_tree import steiner_tree_weight, Edge

def readline_or_error(f):
    line = f.readline()
    if line == '':
        raise IOError('Empty line readed')
    return line

def load_problem(path):
    f = open(path, 'r')
    line = f.readline()
    while not line.lower().startswith('section graph'):
        line = readline_or_error(f)
    while not line.lower().startswith('nodes'):
        line = readline_or_error(f)
    n = int(line.lower().replace('nodes', ''))
    E = []
    while not line.lower().startswith('end'):
        line = readline_or_error(f)
        if line.lower().startswith('e '):
            line_parts = line.split(' ')
            u = int(line_parts[1]) - 1
            v = int(line_parts[2]) - 1
            w = int(line_parts[3])
            edge = Edge(u,v,w)
            E.append(edge)
    while not line.lower().startswith('section terminals'):
        line = readline_or_error(f)
    while not line.lower().startswith('terminals'):
        line = readline_or_error(f)
    T = []
    while not line.lower().startswith('end'):
        line = readline_or_error(f)
        if line.lower().startswith('t'):
            terminal = int(line.split(' ')[1]) - 1
            T.append(terminal)
    return (n, E, T)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('Provide graph file path')
        sys.exit()
    test_file_path = sys.argv[1]
    print('Loading ', test_file_path)
    (n, E, T) = load_problem(test_file_path)
    print('Computing steiner tree weight')
    start = time()
    weight = steiner_tree_weight(n, E, T)
    end = time()
    print('Steiner tree 2-approximated weight is {}, took {}s'.format(weight, end - start))
