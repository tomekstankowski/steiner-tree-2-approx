class _Subset:
    def __init__(self, v):
        self.parent = v
        self.rank = 0


def _unite(subsets, a, b):
    if subsets[a].rank > subsets[b].rank:
        subsets[b].parent = a
    elif subsets[b].rank > subsets[a].rank:
        subsets[a].parent = b
    else:
        subsets[a].parent = b
        subsets[b].rank += 1


def _find_root_subset(subsets, v):
    if subsets[v].parent == v:
        return v
    return _find_root_subset(subsets, subsets[v].parent)


def min_spanning_tree_weight(n, E):
    tree_weigth = 0
    tree_edge_count = 0
    edges = E.copy()
    edges.sort(key=lambda e: e.w)
    subsets = [_Subset(i) for i in range(n)]

    while len(edges) > 0:
        e = edges.pop(0)
        u_subset = _find_root_subset(subsets, e.u)
        v_subset = _find_root_subset(subsets, e.v)
        if u_subset != v_subset:
            _unite(subsets, u_subset, v_subset)
            tree_weigth += e.w
            tree_edge_count += 1
            if tree_edge_count == n - 1:
                return tree_weigth
    return None
