from typing import List
from collections import deque


def get_flattened_idx(i, j, n, m):
    return i*m + j


def get_neighbors(i, j, matrix):
    n, m = len(matrix), len(matrix[0])
    neighbors = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
    adj_neighbors = set()
    rev_adj_neighbors = set()
    for k, l in neighbors:
        flattened_idx = get_flattened_idx(k, l, n, m)
        if (0 <= k < n) and (0 <= l < m):
            if matrix[k][l] > matrix[i][j]:
                adj_neighbors.add(flattened_idx)
            elif matrix[k][l] < matrix[i][j]:
                rev_adj_neighbors.add(flattened_idx)

    return adj_neighbors, rev_adj_neighbors


def build_graph(matrix):
    n, m = len(matrix), len(matrix[0])
    adj_list = []
    rev_adj_list = []
    start_nodes = []
    for i in range(n):
        for j in range(m):
            adj_neighbors, rev_adj_neighbors = get_neighbors(i, j, matrix)
            adj_list.append(adj_neighbors)
            rev_adj_list.append(rev_adj_neighbors)
            if len(rev_adj_neighbors) == 0:
                flattened_idx = get_flattened_idx(i, j, n, m)
                start_nodes.append(flattened_idx)

    return adj_list, rev_adj_list, start_nodes


def topological_sort(adj_list):
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


def get_longest_increasing_path(matrix: List[List[int]]) -> int:
    n, m = len(matrix), len(matrix[0])
    adj_list, rev_adj_list, start_nodes = build_graph(matrix)
    sorted_nodes = topological_sort(adj_list)
    path_lens = [1]*m*n
    max_path_len = 1
    for node in sorted_nodes:
        for neigh in adj_list[node]:
            path_lens[neigh] = max(path_lens[node]+1, path_lens[neigh])
            max_path_len = max(max_path_len, path_lens[neigh])

    return max_path_len


def read_matrix() -> List[List[int]]:
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    return matrix


matrix = [[10, 8, 5],
          [10, 5, 4]]

print(get_longest_increasing_path(matrix))

matrix = [[1, 1],
          [1, 1]]
print(get_longest_increasing_path(matrix))

matrix = [[10, 9],
          [9, 11]]
print(get_longest_increasing_path(matrix))


matrix = [[1]]
print(get_longest_increasing_path(matrix))

matrix = [[5, 4, 3, 2, 1]]
print(get_longest_increasing_path(matrix))

matrix = []
n = 1000
for i in range(n):
    matrix.append([])
    if i % 2 == 0:
        for j in range(n):
            matrix[-1].append(n*i + j)
    else:
        for j in range(n-1, -1, -1):
            matrix[-1].append(n*i + j)
print(get_longest_increasing_path(matrix))
