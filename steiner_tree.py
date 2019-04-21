from min_spanning_tree import min_spanning_tree_weight
from shortest_path import shortest_path_length

class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w


def steiner_tree_weight(n, E, T):
    t = len(T)
    adj_list = [[] for i in range(n)]
    for edge in E:
        adj_list[edge.u].append((edge.v, edge.w))
        adj_list[edge.v].append((edge.u, edge.w))
    Ec = []
    for i in range(t):
        for j in range(i + 1, t):
            weight = shortest_path_length(adj_list, T[i], T[j])
            edge = Edge(i, j, weight)
            Ec.append(edge)
    return min_spanning_tree_weight(t, Ec)
