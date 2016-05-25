#!/usr/bin/env python3

def almost_combo(moves):
    combos = 0
    for i in range(len(moves)-2):
        # D-RD-R-(P)
        # This case is also True for L-LD-D-RD-R-(P)
        # but I should count only one (not two)
        if (moves[i] == 'D' and moves[i+1] == 'RD' and
            moves[i+2] == 'R' and (i+3 == len(moves) or moves[i+3] != 'P')):
            combos += 1
        # R-D-RD-(P)
        if (moves[i] == 'R' and moves[i+1] == 'D' and
            moves[i+2] == 'RD' and (i+3 == len(moves) or moves[i+3] != 'P')):
            combos += 1
        # D-LD-L-(K)
        # This case is also True for R-RD-D-LD-L-(K)
        if (moves[i] == 'D' and moves[i+1] == 'LD' and
            moves[i+2] == 'L' and (i+3 == len(moves) or moves[i+3] != 'K')):
            combos += 1
    return combos

if __name__ == "__main__":
    test_cases = int(input())
    for case in range(1, test_cases+1):
        moves = input().split('-')
        print("Case #{}: {}".format(case, almost_combo(moves)))
