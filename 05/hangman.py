#!/usr/bin/env python3

import telnetlib

def load_words():
    """ Loads the dictionary """
    with open("words.txt") as f:
        words = f.read().split()
    return words

def get_words(guess, dictionary, used):
    # If I didn't use any letter yet
    # Return words with equal length
    if len(used) == 0:
        return [word for word in dictionary if len(word) == len(guess)]
    # If I used some letters
    else:
        w = []
        for word in dictionary:
            valid = True
            for i in range(len(guess)): 
                if guess[i] == '_' and word[i] in used:
                    valid = False
                elif guess[i] != '_' and guess[i] != word[i]:
                    valid = False
            if valid:
                w.append(word)
        return w
        

def most_freq_letters(words):
    # Gets a frequency dict
    freqs = {}
    for word in words:
        for letter in set(word):
            if letter not in freqs:
                freqs[letter] = 1
            else:
                freqs[letter] += 1
    # Returns a sorted list of letters by (decreasing) frequency
    l = [(freqs[key], key) for key in freqs]
    l.sort(reverse=True)
    return [it[1] for it in l]
    

if __name__ == "__main__":
    tn = telnetlib.Telnet("52.49.91.111", 9988)

    end = False
    while not end:
        print(tn.read_until(b"Press enter to continue...").decode('ascii'))
        input()
        tn.write(b"\n")
        
        print(tn.read_until(b"|\n\n").decode('ascii'))
        guess_word = tn.read_until(b"\n").decode('ascii')
        print(guess_word)
        guess_word = "".join(guess_word.split())
        
        possible_words = load_words()
        used_letters = []
        while '_' in guess_word:
            print(tn.read_until(b">").decode('ascii'))
            possible_words = get_words(guess_word,
                                       possible_words,
                                       used_letters)
            letters = most_freq_letters(possible_words)
            for letter in letters:
                if letter not in used_letters:
                    used_letters.append(letter)
                    tn.write(letter.encode('ascii')+b"\n")
                    break

            aux = tn.read_until(b"\n").decode('ascii')
            print(aux)
            if("Level " in aux):  # Yes!
                break
            if("Congratulations" in aux):  # Hooray!
                end = True
                break
            aux = tn.read_until(b"|\n\n").decode('ascii')
            print(aux)
            if("GAME OVER" in aux):  # D'oh!
                end = True
                break

            guess_word = tn.read_until(b"\n").decode('ascii')
            print(guess_word)
            guess_word = "".join(guess_word.split())

        print(tn.read_until(b"Get ready for next level!").decode('ascii'))

    tn.read_all()

