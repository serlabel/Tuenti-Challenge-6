#!/usr/bin/env python3

def immiscible(x):
    # Remove 2-and-5-factors
    zeros = 0
    while x%10 == 0:
        zeros += 1
        x //= 10
    if x%2 == 0:
        while x%2 == 0:
            zeros += 1
            x //= 2
    elif x%5 == 0:
        while x%5 == 0:
            zeros += 1
            x //= 5
    # immiscible(x) = immiscible(x') * 10**zeros
    # inmiscible(x') is an all-ones number
    ones = 1
    n = 1%x
    while n != 0:
        n = ((10*n)%x + 1)%x
        ones += 1
    return ones, zeros

if __name__ == "__main__":
    test_cases = int(input())
    for case in range(1, test_cases+1):
        n = int(input())
        ones, zeros = immiscible(n)
        print("Case #{}: {} {}".format(case, ones, zeros))
