import heapq


def get_energy_for_union(stones):
    heapq.heapify(stones)
    cur_energy = 0
    while len(stones) > 1:
        stone1, stone2 = heapq.heappop(stones), heapq.heappop(stones)
        cur_energy += stone1 + stone2
        heapq.heappush(stones, stone1+stone2)

    return cur_energy

n = int(input())
stones = list(map(int, input().split()))

print(get_energy_for_union(stones))
