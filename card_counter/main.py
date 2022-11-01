def cumsum(arr):
    cumsum = 0
    cumsum_arr = [0]
    for elem in arr:
        cumsum += elem
        cumsum_arr.append(cumsum)

    return cumsum_arr


def get_card_count(n, k, cards) -> int:
    if k >= len(cards):
        return sum(cards)

    cumsum_left = cumsum(cards[:k])
    cumsum_right = cumsum(cards[:-k-1:-1])
    max_score = 0
    for i in range(k+1):
        cur_score = cumsum_left[i] + cumsum_right[k-i]
        max_score = max(max_score, cur_score)

    return max_score

n = 7
k = 3
cards = [5, 8, 2, 1, 3, 4, 11]

print(get_card_count(n, k, cards))

n = 5
k = 5
cards = [1, 2, 3, 4, 5]

print(get_card_count(n, k, cards))

n = 7
k = 4
cards = [1, 1, 9, 2, 2, 2, 6]
print(get_card_count(n, k, cards))
