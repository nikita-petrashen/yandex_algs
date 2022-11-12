from collections import defaultdict
from bisect import bisect_left


def default_factory():
    return {"eras": [0], "values": [0]}


# this solution does not pass the 11th test
class HistoricalArray:
    def __init__(self, size) -> None:
        self.size = size
        self.values = defaultdict(default_factory)
        self.cur_era = 0

    def set(self, index, value) -> None:
        idx_dict = self.values[index]
        era_idx = bisect_left(idx_dict["eras"], self.cur_era)
        if era_idx < len(idx_dict["eras"]) and idx_dict["eras"][era_idx] == self.cur_era:
            idx_dict["values"][era_idx] = value
        else:
            idx_dict["eras"].insert(era_idx, self.cur_era)
            idx_dict["values"].insert(era_idx, value)

    def get(self, index, era_id) -> int:
        idx_dict = self.values[index]
        era_idx = bisect_left(idx_dict["eras"], era_id)
        if era_idx == len(idx_dict["eras"]) or idx_dict["eras"][era_idx] != era_id:
            value = idx_dict["values"][era_idx-1]
        else:
            value = idx_dict["values"][era_idx]
        return value

    def begin_new_era(self, era_id) -> None:
        self.cur_era = era_id


size = int(input())
q = int(input())
historical_array = HistoricalArray(size)
for i in range(q):
    query = input().split()
    query_type = query[0]
    if query_type == "set":
        historical_array.set(int(query[1]), int(query[2]))
    elif query_type == "begin_new_era":
        historical_array.begin_new_era(int(query[1]))
    else:
        print(historical_array.get(int(query[1]), int(query[2])))
