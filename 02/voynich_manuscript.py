#!/usr/bin/env python3

def load_corpus():
    words = []
    with open("corpus.txt") as corpus:
        words = corpus.read().split()
    return words

if __name__ == "__main__":
    words = load_corpus()
    test_cases = int(input())
    for case in range(1, test_cases+1):
        start, end = map(int, input().split())
        # Create a frequency dictionary
        frequencies = {}
        for i in range(start-1, end):
            if words[i] not in frequencies:
                frequencies[words[i]] = 1
            else:
                frequencies[words[i]] += 1
        # Get a list of tuples (frequency, word)
        f = [(frequencies[word], word) for word in frequencies]
        # Sort the previous list in decremental order
        f.sort(reverse=True)
        # Get the three most frequent words
        print("Case #{}: {} {},{} {},{} {}".format(case,
                                                   f[0][1], f[0][0],
                                                   f[1][1], f[1][0],
                                                   f[2][1], f[2][0]))
