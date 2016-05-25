#!/usr/bin/env python3

from fractions import Fraction

import numpy as np
    
def seat_change(probabilities, src_chair, n_changes):
    # Detect connected nodes (chairs) to src chair
    chairs = probabilities.shape[0]
    visited = [False] * chairs
    connected = [False] * chairs
    connected[src_chair] = True
    completed = False
    while not completed:
        completed = True
        for i in range(chairs):
            if connected[i] and not visited[i]:
                for j in range(chairs):
                    if probabilities[i,j].numerator != 0:
                        connected[j] = True
                        completed = False
                visited[i] = True
    nodes = [i for i in range(len(connected)) if connected[i]]
    probs = probabilities[nodes, :][:, nodes]
    # Get the probabilities matrix (probs**n_changes)
    m = np.linalg.matrix_power(probs, n_changes)
    # Get the greatest probability
    best_chair = m.shape[0]-1
    for i in range(m.shape[0]-1, -1, -1):
        if m[nodes.index(src_chair), best_chair] < m[nodes.index(src_chair), i]:
            best_chair = i
    num = m[nodes.index(src_chair), best_chair].numerator%10
    den = m[nodes.index(src_chair), best_chair].denominator%10
    return nodes[best_chair], num, den
    
if __name__ == "__main__":
    chairs = int(input())
    n_probs = int(input())
    probs = np.empty((chairs, chairs), dtype=Fraction)
    probs.fill(Fraction())
    for prob in range(n_probs):
        src, dst, pr = input().split()
        probs[int(src), int(dst)] = Fraction(int(pr.split('/')[0]), 100)
    n_questions = int(input())
    for q in range(1, n_questions+1):
        chair, changes = map(int, input().split())
        c, num, den = seat_change(probs, chair, changes)
        print("Case #{}: Chair: {} Last digits: {}/{}".format(q, c, num, den))
