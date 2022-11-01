from collections import defaultdict

def get_number_of_good_pairs(numbers) -> int:
    if len(numbers) < 2:
        return 0
    else:
        numbers = [num % 200 for num in numbers]
        good_pairs_num = 0
        remainders_counts = defaultdict(int)
        for num in numbers:
            good_pairs_num += remainders_counts.get(num, 0)
            remainders_counts[num] += 1

    return good_pairs_num


n = 5
numbers = [203, 404, 204, 200, 403]

print(get_number_of_good_pairs(numbers))