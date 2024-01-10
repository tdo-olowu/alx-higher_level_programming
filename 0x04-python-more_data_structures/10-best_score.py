#!/usr/bin/python3
def best_score(a_dictionary):
    if (not a_dictionary):
        return None
    a_keys = list(a_dictionary)
    lngth = len(a_keys)
    if (lngth > 0):
        best_key = a_keys[0]
        best_score = a_dictionary[best_key]
        for i in range(1, lngth):
            key = a_keys[i]
            score = a_dictionary[key]
            if (best_score < score):
                best_score = score
                best_key = key
        return best_key
