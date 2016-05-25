#!/usr/bin/env python3

def toast(n, m, k):
    # If k is multiple of m there is, at least,
    #    one solution: k/m piles of m slices
    if k%m != 0 or n*m > k:
        return "IMPOSSIBLE"
    else:
        pows = [m]
        secs = 0
        maxpow = m
        while (n-1)*m + maxpow*2 <= k:
            maxpow *= 2
            pows.append(maxpow)
            secs += 1
        dif = k - ((n-1)*m + maxpow)
        while dif > 0:
            for p in pows[::-1]:
                if p <= dif:
                    dif -= p
                    secs += 1
                    break
        return secs

if __name__ == "__main__":
    test_cases = int(input())
    for case in range(1, test_cases+1):
        n, m, k = map(int, input().split())
        print("Case #{}: {}".format(case, toast(n, m, k)))
