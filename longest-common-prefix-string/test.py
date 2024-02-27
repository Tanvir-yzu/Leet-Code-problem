from icecream import ic


def longest_common_prefix(strs):
    if not strs:
        return ""
    min_len = min(len(s) for s in strs)

    low, high = 0, min_len

    while low < high:
        mid = (low + high + 1) // 2
        if is_common_prefix(strs, mid):
            low = mid
        else:
            high = mid - 1

    return strs[0][:low]


def is_common_prefix(strs, length):
    prefix = strs[0][:length]
    return all(string.startswith(prefix) for string in strs)


strs1 = ["flower", "flow", "floight"]
ic(longest_common_prefix(strs1))
strs2 = ["dog", "racecar", "car"] 
ic(longest_common_prefix(strs2))
