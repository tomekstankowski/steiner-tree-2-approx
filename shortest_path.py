import sys


class _Node:
    def __init__(self, number):
        self.number = number
        self.distance = sys.maxsize
        self.visited = False


def shortest_paths_lengths(adj_list, src):
    n = len(adj_list)
    nodes = [_Node(i) for i in range(n)]
    unvisited_nodes = nodes.copy()
    nodes[src].distance = 0
    while len(unvisited_nodes) > 0:
        node = min(unvisited_nodes, key=lambda n: n.distance)
        for (number, weight) in adj_list[node.number]:
            adj_node = nodes[number]
            if adj_node.visited == True:
                continue
            alt_distance = node.distance + weight
            if adj_node.distance > alt_distance:
                adj_node.distance = alt_distance
        node.visited = True
        unvisited_nodes.remove(node)
    return list(map(lambda n: n.distance, nodes))
