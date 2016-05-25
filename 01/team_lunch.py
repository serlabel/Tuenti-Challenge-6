#!/usr/bin/env python3

def tables(diners):
    if diners == 0:
        return 0  # no diner, no table
    elif diners <= 4:
        return 1  # up to four diners in a table
    else:
        return 1 + (diners - 3)//2  # two diners for extra table

if __name__ == "__main__":
    test_cases = int(input())
    for case in range(1, test_cases+1):
        d = int(input())
        print("Case #{}: {}".format(case, tables(d)))
