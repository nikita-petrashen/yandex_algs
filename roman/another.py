from collections import Counter

MAPPING = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90,
           "CD": 400, "CM": 900}

THREE_CONS_RESTR = {"I", "X", "C", "M"}
SINGLE_RESTR = {"V", "L", "D"}


def check_single_excs(number):
    count = Counter(number)
    for c in SINGLE_RESTR:
        if count[c] > 1:
            return False

    return True


def is_descending(number):
    chunks = split_number(number)
    cur_max_val = 1000
    for chunk in chunks:
        val = MAPPING[chunk]
        if val > cur_max_val:
            return False
        else:
            if val == 9 or val == 4:
                cur_max_val = 0
            elif val == 90 or val == 40:
                cur_max_val = 9
            elif val == 900 or val == 400:
                cur_max_val = 90
            else:
                cur_max_val = val

    return True


def check_excs_restr(number):
    chunks = split_number(number)
    for chunk in chunks:
        if chunk not in MAPPING:
            return False

    return True


def check_three_cons_restr(number):
    cons_count = 0
    cons_char = None
    for c in number:
        if c in THREE_CONS_RESTR:
            if c == cons_char:
                cons_count += 1
                if cons_count > 3:
                    return False
            else:
                cons_count = 1
                cons_char = c

    return True


def check_restrs(number):
    return check_excs_restr(number) and check_single_excs(number) and check_three_cons_restr(number) and is_descending(number)


def split_number(number):
    i = 0
    chunks = []
    while i < len(number):
        if i == len(number)-1:
            chunks.append(number[i])
            break
        cur, nxt = number[i], number[i+1]
        cur_val, nxt_val = MAPPING[cur], MAPPING[nxt]
        if cur_val < nxt_val:
            chunks.append(cur+nxt)
            i += 2
        else:
            chunks.append(cur)
            i += 1

    return chunks


def convert_to_arabic(number: str) -> int:
    if not check_restrs(number):
        return -1
    chunks = split_number(number)
    result = 0
    for chunk in chunks:
        result += MAPPING[chunk]

    return result


# 2
roman_number = "II"
print(f"{roman_number}:", convert_to_arabic(roman_number))

# 1961
roman_number = "MCMLXI"
print(f"{roman_number}:", convert_to_arabic(roman_number))
# 94
roman_number = "XCIV"
print(f"{roman_number}:", convert_to_arabic(roman_number))
# 1
roman_number = "I"
print(f"{roman_number}:", convert_to_arabic(roman_number))
# 350
roman_number = "CCCL"
print(f"{roman_number}:", convert_to_arabic(roman_number))
# 1666
roman_number = "MDCLXVI"
print(f"{roman_number}:", convert_to_arabic(roman_number))
# 7
roman_number = "VII"
print(f"{roman_number}:", convert_to_arabic(roman_number))
# 1109
roman_number = "MCIX"
print(f"{roman_number}:", convert_to_arabic(roman_number))
# -1
roman_number = "VIV"
print(f"{roman_number}:", convert_to_arabic(roman_number))
# -1
roman_number = "IXI"
print(f"{roman_number}:", convert_to_arabic(roman_number))
# -1
roman_number = "IXX"
print(f"{roman_number}:", convert_to_arabic(roman_number))
# -1
roman_number = "LXIVI"
print(f"{roman_number}:", convert_to_arabic(roman_number))

# -1
roman_number = ""
print(f"{roman_number}:", convert_to_arabic(roman_number))

# -1
roman_number = "IM"
print(f"{roman_number}:", convert_to_arabic(roman_number))

# -1
roman_number = "IIIX"
print(f"{roman_number}:", convert_to_arabic(roman_number))

# 39
roman_number = "XXXIX"
print(f"{roman_number}:", convert_to_arabic(roman_number))

# 294
roman_number = "CCXCIV"
print(f"{roman_number}:", convert_to_arabic(roman_number))

# 999
roman_number = "CMXCIX"
print(f"{roman_number}:", convert_to_arabic(roman_number))



