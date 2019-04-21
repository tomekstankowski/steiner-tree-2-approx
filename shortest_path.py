import sys


class _Node:
    def __init__(self, number):
        self.number = number
        self.distance = sys.maxsize
        self.visited = False


def shortest_path_length(adj_list, src, dest):
    n = len(adj_list)
    nodes = [_Node(i) for i in range(n)]
    unvisited_nodes = nodes.copy()
    nodes[src].distance = 0
    while not nodes[dest].visited:
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
    return nodes[dest].distance
