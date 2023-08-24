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
    return deck[:12], deck


def find_set(v):
    set = []
    for i in range(len(v)):
        for j in range(3):
            if v[i][0][j] == v[i][1][j] and v[i][0][j] != v[i][2][j]:
                break
            elif v[i][0][j] == v[i][2][j] and v[i][0][j] != v[i][1][j]:
                break
            elif v[i][2][j] == v[i][1][j] and not v[i][2][j] != v[i][0][j]:
                break
            else:
                set = np.append(set, v[i])
    return set


def get_spread(v, deck):
    subsets = list(combo(v, 3))
    sets = find_set(subsets)
    if len(sets) == 0:
        v = np.append(v, deck[:3])
        deck = deck[3:]
        subsets = list(combo(v, 3))
        sets = find_set(subsets)
        if len(sets) == 0:
            v = np.append(v, deck[:3])
            deck = deck[3:]
            subsets = list(combo(v, 3))
            sets = find_set(subsets)
    index = []
    for i in range(len(v)):
        if v[i] == sets[0][0] or v[i] == sets[0][1] or v[i] == sets[0][2]:
            index = np.append(index, i)
        elif len(index) >= 3:
            break
    for i in range(len(index)):
        v[index[i]] = deck[i]
    deck = deck[3:]
    if len(deck) <= 18 and len(sets) == 0:
        return "done"
    get_spread(v, deck)


get_spread(get_deck()[0], get_deck()[1])
