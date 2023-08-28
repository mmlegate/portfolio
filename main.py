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


def find_set(subsets):
    # v is the set of all combinations of a group of cards
    indices = []
    sets_indices = []
    sets = []
    v = subsets.copy()
    for i in range(len(v)):
        for j in range(4):
            if (v[i][0][j] == v[i][1][j] == v[i][2][j]) or (v[i][0][j] != v[i][1][j] and v[i][0][j] != v[i][2][j]):
                indices = np.append(indices, i)
            else:
                break
        if len(indices) >= 4:
            for i in range(len(indices) - 4):
                if indices[i] == indices[i + 1] == indices[i + 2] == indices[i + 3]:
                    sets_indices = np.append(sets_indices, indices[i])
        sets_indices = np.unique(sets_indices)
        for i in range(len(sets_indices)):
            sets = np.append(sets, v[int(sets_indices[i])])
        sets = np.reshape(sets, (int(len(sets) / 12), 3, 4))
    return sets


def get_spread(deck):
    v = deck[:12]
    deck_new = deck[12:]
    subsets = list(combo(v, 3))
    sets = find_set(subsets)
    if len(sets) == 0:
        v = np.append(v, deck[:3])
        deck_new = deck_new[3:]
        subsets = list(combo(v, 3))
        sets = find_set(subsets)
        if len(sets) == 0:
            v = np.append(v, deck[:3])
            deck_new = deck_new[3:]
            subsets = list(combo(v, 3))
            sets = find_set(subsets)

    key = sets[0]
    indices = []
    for i in range(3):
        for j in range(len(v)):
            for k in range(4):
                if key[i][k] == v[j][k]:
                    indices = np.append(indices, j)
    for k in range(len(indices)):
        v[int(indices[k])] = deck_new[k]
    new_deck = np.append(v, deck_new[len(indices):])

    if len(deck_new[len(indices):]) <= 18 and len(sets) == 0:
        return "Yay!"
    get_spread(new_deck)
get_spread(get_deck())
