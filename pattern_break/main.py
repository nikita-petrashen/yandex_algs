def collapse_stars(template):
    collapsed_template = ""
    i = 0
    while i < len(template):
        collapsed_template += template[i]
        if template[i] == "*":
            while i+1 < len(template) and template[i+1] == "*":
                i += 1
        i += 1

    return collapsed_template


def string_matches_template(s: str, template: str) -> bool:
    template = collapse_stars(template)
    if template[0] == "*":
        first = True
        rest = True
    elif template[0] == "?":
        first = True
        rest = False
    else:
        if template[0] == s[0]:
            first = True
            rest = False
        else:
            return False

    dp = [[first]]
    for _ in range(len(s)-1):
        dp.append([rest])

    if len(template) > 1:
        if template[1] == "*":
            second = True
        elif template[0] == "*":
            if template[1] == "?":
                second = True
            else:
                second = template[1] == s[0]
        else:
            second = False
        dp[0].extend([second]+[False]*(len(template)-2))

    for i in range(1, len(s)):
        for j in range(1, len(template)):
            prev_match = dp[i-1][j] or dp[i][j-1]
            if template[j] in ["*", "?"]:
                cur_match = True
            else:
                cur_match = s[i] == template[j]

            dp[i].append(prev_match and cur_match)

    return dp[-1][-1]




template = "*a*"
string_to_check = "bbbabbb"
print(template)
print(string_to_check)
print(string_matches_template(string_to_check, template))
print("")

template = "*"
string_to_check = "adce"
print(template)
print(string_to_check)
print(string_matches_template(string_to_check, template))
print("")

template = "?"
string_to_check = "a"
print(template)
print(string_to_check)
print(string_matches_template(string_to_check, template))
print("")

template = "??"
string_to_check = "a"
print(template)
print(string_to_check)
print(string_matches_template(string_to_check, template))
print("")

template = "?"
string_to_check = "aa"
print(template)
print(string_to_check)
print(string_matches_template(string_to_check, template))
print("")

template = "*?"
string_to_check = "a"
print(template)
print(string_to_check)
print(string_matches_template(string_to_check, template))
print("")


template = "?*"
string_to_check = "a"
print(template)
print(string_to_check)
print(string_matches_template(string_to_check, template))
print("")

template = "*a?"
string_to_check = "aa"
print(template)
print(string_to_check)
print(string_matches_template(string_to_check, template))
print("")

template = "algorithms"
string_to_check = "algorithmus"
print(template)
print(string_to_check)
print(string_matches_template(string_to_check, template))
print("")

