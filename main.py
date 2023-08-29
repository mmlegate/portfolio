import random
import math
import numpy as np
from itertools import combinations as combo

# initializing attributes
color = [0, 1, 2]
text = [0, 1, 2]
shape = [0, 1, 2]
mult = [0, 1, 2]
attr = [color, text, shape, mult]


# get rand deck
def get_deck():
    deck = np.zeros((81, 4))
    for i in range(81):
        # Multiplicity
        deck[i][0] = i % 3
        # Texture
        if (int(i / 3)) % 3 == 0:
            pass
        elif (int(i / 3)) % 3 == 1:
            deck[i][1] = 1
        else:
            deck[i][1] = 2
        # Color
        if (int(i / 9)) % 3 == 0:
            pass
        elif (int(i / 9)) % 3 == 1:
            deck[i][2] = 1
        else:
            deck[i][2] = 2
        # Shape
        if (int(i / 27)) % 3 == 0:
            pass
        elif (int(i / 27)) % 3 == 1:
            deck[i][3] = 1
        else:
            deck[i][3] = 2
        # Shuffling
    np.random.shuffle(deck)
    return deck


def find_set(spread):
    subsets = list(combo(spread,3))
    if len(subsets) == 0:
        return "End of Deck."
    else:
        n = len(subsets)
        indices = np.zeros(n)
        for i in range(n):
            for j in range(4):
                if (subsets[i][0][j] == subsets[i][1][j] == subsets[i][2][j]) or (subsets[i][0][j] != subsets[i][1][j] != subsets[i][2][j] != subsets[i][0][j]):
                    indices[i] += 1
                else:
                    break
        for i in range(n):
            if indices[i] >= 4:
                set_index = i
                break
    if set_index == 0:
        sets = []
    else:
        sets = subsets[set_index]
    return sets


def get_spread(deck):
    if len(deck) <= 12:
        spread = deck.copy()
        sets = find_set(spread)
        if len(sets) == 0:
            return "Yippee"
        key = sets[0]
        counts = np.zeros(len(spread))
        for i in range(len(spread)):
            for j in range(3):
                for k in range(4):
                    if key[j][k] == spread[i][k]:
                        counts[i] += 1
        for i in range(len(spread)):
            if counts[i] >= 4:
                spread_new = np.remove(spread, i)
        get_spread(spread_new)
    else:
        spread = deck[:12]
        deck_new = deck[12:]
        sets = find_set(spread)
        if len(sets) == 0 and len(deck_new) >= 3:
            spread = np.append(spread, deck[:3])
            deck_new = deck_new[3:]
            sets = find_set(spread)
            if len(sets) == 0 and len(deck_new >= 3):
                spread = np.append(spread, deck[:3])
                deck_new = deck_new[3:]
                sets = find_set(spread)
            elif len(sets) == 0 and len(deck_new) < 3:
                return "Yurpee"
        elif len(sets) == 0 and len(deck_new) < 3:
            return "Yorpee"
        key = sets[0]
        indices = np.zeros(len(spread))
        for i in range(3):
            for j in range(len(spread)):
                for k in range(4):
                    if key[i][k] == spread[j][k]:
                        indices[j] += 1
        for k in range(len(indices)):
            if indices[k] >= 4:
                spread[k] = deck_new[k]
        new_deck = np.append(spread, deck_new[len(indices):])
        new_deck = np.reshape(new_deck, (int(len(new_deck)/4), 4))
        return get_spread(get_deck())


get_spread(get_deck())
