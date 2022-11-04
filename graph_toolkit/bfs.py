from collections import deque


def recursive_bfs(adj_list):
    visited = [False] * len(adj_list)
    node_list = []
    queue = deque()

    def _recursive_bfs_worker(node):
        if not visited[node]:
            node_list.append(node)
            visited[node] = True

        for neigh in adj_list[node]:
            if not visited[neigh]:
                queue.appendleft(neigh)

        while queue:
            neigh = queue.pop()
            _recursive_bfs_worker(neigh)

    for node in range(len(adj_list)):
        if not visited[node]:
            _recursive_bfs_worker(node)

    return node_list


def non_recursive_bfs(adj_list):
    visited = [False] * len(adj_list)
    node_list = []
    queue = deque()

    def _non_recursive_bfs_worker(start_node):
        queue.append(start_node)
        while queue:
            node = queue.pop()
            if not visited[node]:
                node_list.append(node)
                visited[node] = True
        for neigh in adj_list[node]:
            if not visited[neigh]:
                queue.appendleft(neigh)

    for node in range(len(adj_list)):
        if not visited[node]:
            _non_recursive_bfs_worker(node)

    return node_list


if __name__ == "__main__":
    adj_list_tree = [[1, 5], [2], [3], [4], [], [6], [7], [8], []]
    assert recursive_bfs(adj_list_tree) == non_recursive_bfs(adj_list_tree)
    print(recursive_bfs(adj_list_tree))

    adj_list_cycle = [[1], [2], [3], [4], [5], [0]]
    assert recursive_bfs(adj_list_cycle) == non_recursive_bfs(adj_list_cycle)
    print(recursive_bfs(adj_list_cycle))

    adj_list_line = [[1], [2], [3], [4], [5], [6], [7], [8], []]
    assert recursive_bfs(adj_list_line) == non_recursive_bfs(adj_list_line)
    print(recursive_bfs(adj_list_line))

    adj_list_rhombus = [[1], [2, 3], [], [0, 2]]
    assert recursive_bfs(adj_list_rhombus) == non_recursive_bfs(adj_list_rhombus)
    print(recursive_bfs(adj_list_rhombus))
