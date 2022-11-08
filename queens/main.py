from typing import List
from collections import defaultdict


def get_occupied_diags(positions):
    h_diags = defaultdict(int)
    v_diags = defaultdict(int)
    for i, j in enumerate(positions):
        h_diags[i+j] += 1
        v_diags[i-j] += 1

    return h_diags, v_diags


def get_new_positions(positions, new_i, new_j):
    new_positions = positions.copy()
    for i in range(len(new_positions)):
        if new_positions[i] >= new_j:
            new_positions[i] += 1

    new_positions.insert(new_i, new_j)
    return new_positions


def test_positions(positions):
    h_diags, v_diags = get_occupied_diags(positions)
    for i, j in enumerate(positions):
        h_diag = i + j
        v_diag = i - j
        if h_diags[h_diag] > 1 or v_diags[v_diag] > 1:
            return False

    return True


def get_next_positions(positions):
    next_positions = []
    for i in range(len(positions) + 1):
        for j in range(len(positions) + 1):
            new_positions = get_new_positions(positions, i, j)
            if test_positions(new_positions):
                next_positions.append(new_positions)

    return next_positions


# the solution works for n up to 7 while not passing even the 5th the test somehow
#TODO: make it work for n >= 8
def get_all_peaceful_combinations(n) -> List[List[int]]:
    if n == 1:
        return [[1]]
    elif n == 2:
        return []
    elif n == 3:
        return []
    combinations = [[1, 3, 0, 2], [2, 0, 3, 1]]
    cur_n = 4
    while cur_n < n:
        new_combinations = []
        for i, positions in enumerate(combinations):
            combs = get_next_positions(positions)
            new_combinations.extend(combs)
        cur_n += 1
        combinations = new_combinations

    for num_comb in range(len(combinations)):
        for i in range(n):
            combinations[num_comb][i] += 1

    return combinations

n = int(input())
combinations = get_all_peaceful_combinations(n)

print(len(combinations))
for combination in combinations:
    print(*combination)
