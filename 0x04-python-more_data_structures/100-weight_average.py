#!/usr/bin/python3
def weight_average(my_list=[]):
    # handle errors - None, etc.
    weighted_sum = 0
    total_weights = 0
    lngth = len(my_list)
    for i in range(lngth):
        pair = my_list[i]
        val = pair[0]
        weight = pair[1]
        weighted_sum += val * weight
        total_weights += weight
    return (weighted_sum / total_weights)
