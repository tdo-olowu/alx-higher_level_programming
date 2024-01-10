#!/usr/bin/python3
def uniq_add(my_list=[]):
    # tis inefficient but it works
    if (my_list is None):
        return None
    seen = []
    total = 0
    for num in my_list:
        if (num not in seen):
            total += num
            seen.append(num)
    return total
