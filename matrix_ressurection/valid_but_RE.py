from typing import List


def get_flattened_idx(i, j, n, m):
    return i*m + j


def get_neighbors(i, j, matrix):
    n, m = len(matrix), len(matrix[0])
    neighbors = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
    adj_neighbors = []
    rev_adj_neighbors = []
    for k, l in neighbors:
        flattened_idx = get_flattened_idx(k, l, n, m)
        if (0 <= k < n) and (0 <= l < m):
            if matrix[k][l] > matrix[i][j]:
                adj_neighbors.append(flattened_idx)
            elif matrix[k][l] < matrix[i][j]:
                rev_adj_neighbors.append(flattened_idx)

    return adj_neighbors, rev_adj_neighbors


def build_graph(matrix):
    n, m = len(matrix), len(matrix[0])
    adj_list = []
    start_nodes = []
    for i in range(n):
        for j in range(m):
            adj_neighbors, rev_adj_neighbors = get_neighbors(i, j, matrix)
            adj_list.append(adj_neighbors)
            if len(rev_adj_neighbors) == 0:
                flattened_idx = get_flattened_idx(i, j, n, m)
                start_nodes.append(flattened_idx)

    return adj_list, start_nodes


def get_longest_increasing_path(matrix: List[List[int]]) -> int:
    n, m = len(matrix), len(matrix[0])
    adj_list, start_nodes = build_graph(matrix)
    path_lens = [1]*m*n

    def dfs(node):
        if len(adj_list[node]) == 0:
            path_lens[node] = 1
            return 1
        else:
            child_dists = []
            for child in adj_list[node]:
                child_dists.append(dfs(child))

            path_lens[node] = max(child_dists) + 1

            return path_lens[node]

    candidate_lens = []
    for start_node in start_nodes:
        candidate_lens.append(dfs(start_node))

    return max(candidate_lens)


def read_matrix() -> List[List[int]]:
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    return matrix


# matrix = [[10, 8, 5],
#           [10, 5, 4]]
# print(get_longest_increasing_path(matrix))
#
# matrix = [[1, 1],
#           [1, 1]]
# print(get_longest_increasing_path(matrix))
#
# matrix = [[10, 9],
#           [9, 11]]
# print(get_longest_increasing_path(matrix))
#
#
# matrix = [[1]]
# print(get_longest_increasing_path(matrix))
#
# matrix = [[5, 4, 3, 2, 1]]
# print(get_longest_increasing_path(matrix))
#
# matrix = [[5], [4], [3], [2], [1]]
# print(get_longest_increasing_path(matrix))



matrix = []
n = 10
for i in range(n):
    matrix.append([])
    if i % 2 == 0:
        for j in range(n):
            matrix[-1].append(n*i + j)
    else:
        for j in range(n-1, -1, -1):
            matrix[-1].append(n*i + j)

adj_list, start_nodes = build_graph(matrix)
print(start_nodes)
print(adj_list)
# print(get_longest_increasing_path(matrix))
