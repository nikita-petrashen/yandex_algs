from collections import deque, defaultdict

class Node:
    def __init__(self, weight, parent, idx) -> None:
        self.weight = weight
        self.parent = parent
        self.idx = idx
        self.children = []


def gather_subpaths(path, x):
    cumsums = defaultdict(list)
    cumsums[0] = [-1]
    cur_sum = 0
    valid_paths = set()
    for idx, w in path:
        cur_sum += w
        for start_idx in cumsums[cur_sum-x]:
            valid_paths.add((idx, start_idx))
        cumsums[cur_sum].append(idx)

    return valid_paths


# this gets TL at test 32, maybe needs smarter gather_subpaths
def get_number_of_upgoing_paths(root: Node, x: int) -> int:
    all_paths = set()
    stack = deque()
    stack.append(root)
    cur_path = deque()
    visited = set()

    while stack:
        node = stack.pop()
        idx = node.idx

        if idx not in visited:
            cur_path.append((idx, node.weight))

        if node.children:
            child = node.children.pop()
            stack.append(node)
            stack.append(child)
        else:
            if idx not in visited:
                all_paths = all_paths.union(gather_subpaths(cur_path, x))

            cur_path.pop()

        visited.add(idx)

    return len(all_paths)


def read_tree(tree_size: int) -> Node:
    nodes = []
    root = None
    for i in range(tree_size):
        p, w = map(int, input().split())
        nodes.append(Node(w, p, i))
        if p == -1:
            root = nodes[i]
    for i in range(tree_size):
        if nodes[i].parent != -1:
            nodes[nodes[i].parent].children.append(nodes[i])
    return root


n, x = map(int, input().split())
tree = read_tree(n)
print(get_number_of_upgoing_paths(tree, x))
