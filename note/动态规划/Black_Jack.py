import numpy as np

def get_player_cards(cards, i, p):
    player_cards = []
    player_cards.append(cards[i])
    player_cards.append(cards[i + 2])
    for k in range(0, p):
        player_cards.append(cards[i + 4 + k])
    return player_cards


def get_dealer_cards(cards, i, p, d):
    dealer_cards = []
    dealer_cards.append(cards[i + 1])
    dealer_cards.append(cards[i + 3])
    for k in range(0, d):
        dealer_cards.append(cards[i + 4 + p + k])
    return dealer_cards


def black_jack_iterative(cards):
    global n
    n = len(cards)
    bj_table = {}
    bj_table[n] = 0
    parent = {}
    parent[0] = None
    for i in range(n - 1, -1, -1):  # 自底向上
        bj_table[i], parent[i] = black_jack(i, bj_table)
    return bj_table, parent


def black_jack(i, bj_table):
    if n-i < 4:
        return 0
    options = []
    for p in range(0, n-i-3):
        player_cards = get_player_cards(cards, i, p)
        player = sum(player_cards)
        if player > 21:
            options.append(-1+bj_table[i+4+p])
            break
        # 庄家
        dealer = 0
        max_d = 0
        for d in range(0, n-i-p-3):
            dealer_cards = get_dealer_cards(cards, i, p, d)
            dealer = sum(dealer_cards)
            if dealer >= 17:
                max_d = d
                break
        if dealer > 21:
            dealer = 0
        options.append(cmp(player, dealer) + bj_table[i+4+p+max_d])
    ind_max = np.argmax(options)
    return max(options), ind_max


def cmp(a, b):
    return (a > b) - (a < b)


def generate_cards(num):
    import random
    cards = [random.randint(1, 11) for i in range(num)]
    random.shuffle(cards)
    return cards


def get_sequence(bj_table):
    sequence = []
    index = bj_table[0]
    while index is not None:
        sequence.append(index)
        index = parent[index]
    return sequence


if __name__ == '__main__':
    cards = generate_cards(108)
    print('cards=', cards)
    bj_table, parent = black_jack_iterative(cards)
    print('bj_table=', bj_table)
