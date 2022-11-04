from collections import deque


def recursive_topological_sort(adj_list):
    visited = [False] * len(adj_list)
    sorted_nodes = []
    stack = deque()
    
    def _recursive_topological_sort_worker(node):
        for neigh in adj_list[node]:
            if not visited[neigh]:
                stack.append(neigh)

        while stack:
            neigh = stack.pop()
            _recursive_topological_sort_worker(neigh)

        if not visited[node]:
            sorted_nodes.append(node)
            visited[node] = True
    
    for node in range(len(adj_list)):
        if not visited[node]:
            _recursive_topological_sort_worker(node)

    sorted_nodes.reverse()
    return sorted_nodes


def non_recursive_topological_sort(adj_list):
    visited = [False] * len(adj_list)
    sorted_nodes = []
    stack = deque()

    def _non_recursive_topological_sort_worker(start_node):
        stack.append(start_node)
        while stack:
            node = stack.pop()
            visited[node] = True
            has_unvisited = False
            for neigh in adj_list[node]:
                if not visited[neigh]:
                    stack.append(node)
                    stack.append(neigh)
                    has_unvisited = True
                    break

            if not has_unvisited:
                sorted_nodes.append(node)

    for node in range(len(adj_list)):
        if not visited[node]:
            _non_recursive_topological_sort_worker(node)

    sorted_nodes.reverse()
    return sorted_nodes


if __name__ == "__main__":
    adj_list_tree = [[1, 5], [2], [3], [4], [], [6], [7], [8], []]
    assert recursive_topological_sort(adj_list_tree) == non_recursive_topological_sort(adj_list_tree)
    print(recursive_topological_sort(adj_list_tree))

    adj_list_acyclic_cycle = [[1, 5], [2], [3], [4], [5], []]
    assert recursive_topological_sort(adj_list_acyclic_cycle) == non_recursive_topological_sort(adj_list_acyclic_cycle)
    print(non_recursive_topological_sort(adj_list_acyclic_cycle))

    adj_list_line = [[1], [2], [3], [4], [5], [6], [7], [8], []]
    assert recursive_topological_sort(adj_list_line) == non_recursive_topological_sort(adj_list_line)
    print(recursive_topological_sort(adj_list_line))

    adj_list_acyclic_rhombus = [[1, 3], [2, 3], [], [2]]
    assert recursive_topological_sort(adj_list_acyclic_rhombus) == non_recursive_topological_sort(adj_list_acyclic_rhombus)
    print(recursive_topological_sort(adj_list_acyclic_rhombus))

    adj_list_acyclic_rhombus2 = [[1], [2], [], [0, 1, 2]]
    assert recursive_topological_sort(adj_list_acyclic_rhombus2) == non_recursive_topological_sort(adj_list_acyclic_rhombus2)
    print(recursive_topological_sort(adj_list_acyclic_rhombus2))
