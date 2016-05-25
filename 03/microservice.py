#!/usr/bin/env python3

import sys
import yaml as pyml

# Use pyyaml to load input
def load_input():
    with sys.stdin as input:
        data = pyml.load(input)
    return data['code'], data['tapes']
    
if __name__ == "__main__":
    # Get machine code and tapes
    code, tapes = load_input()
    for tape in tapes:
        finalt = list(tapes[tape])
        state = 'start'
        position = 0
        # While the state is not final
        while state != 'end':
            # If the position is greater than
            # the tape length append a space
            if position >= len(finalt):
                finalt.append(' ')
            action = code[state][finalt[position]]
            if 'write' in action:
                finalt[position] = action['write']
            if 'move' in action:
                if action['move'] == 'left':
                    position -= 1
                elif action['move'] == 'right':
                    position += 1
            if 'state' in action:
                state = action['state']
        print("Tape #{}: {}".format(tape, "".join(finalt).strip()))
