#!/usr/bin/python3
combinations = [
        "{}{}".format(i, j)
        for i in range(10)
        for j in range(i + 1, 10)
    ]
print(", ".join(combinations))
