import numpy as np


def generate_cards(n):
    import random
    import itertools
    SUITS = 'cdhs'  # 四种花色
    RANKS = '23456789TJQKA'  # 十三种面值
    DECK = tuple(''.join(card) for card in itertools.product(RANKS, SUITS))
    hand = random.sample(DECK, n)
    return hand


def crazy_eight(cards):
    trick = {}
    parent = {}
    trick[0] = 1
    parent[0] = None

    for i, ci in enumerate(cards):
        tem_trick = []
        if i > 0:
            for j, cj in enumerate(cards[:i]):
                if is_trick(ci, cj):
                    tem_trick.append(trick[j])
                else:
                    tem_trick.append(0)
            max_trick = max(tem_trick)
            trick[i] = 1 + max_trick
            ind_max = np.argmax(tem_trick)
            if is_trick(ci, cards[ind_max]):
                parent[i] = ind_max
            else:
                parent[i] = None
    return trick, parent


def is_trick(c1, c2):
    if c1[0] == c2[0]:
        return True
    elif c1[1] == c2[1]:
        return True
    elif c1[0] == '8' or c2[0] == '8':
        return True
    else:
        return False


def get_longest_subsequence(cards, trick, parent):
    ind_max = max(trick.keys(), key=(lambda key: trick[key]))
    subsequence = []
    while ind_max is not None:
        subsequence.append(cards[ind_max])
        ind_max = parent[ind_max]
    subsequence.reverse()
    return subsequence


if __name__ == '__main__':
    cards = generate_cards(10)
    trick, parent = crazy_eight(cards)
    subsequence = get_longest_subsequence(cards, trick, parent)
    print('cards=', cards)
    print('trick=', trick)
    print('subsequence=', subsequence)
