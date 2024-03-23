#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_score = max(a_dictionary.values())
    best_score = [key for key, value in a_dictionary.item()if value == max_score][0]
    return best_score
