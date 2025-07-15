from collections import Counter

def is_seven_pairs(hand):
    return len(hand) == 14 and all(v == 2 for v in Counter(hand).values())

def is_pong_pong_hu(hand):
    count = Counter(hand)
    triples = sum(v // 3 for v in count.values())
    pairs = sum(1 for v in count.values() if v == 2)
    return triples >= 4 and pairs == 1

def is_pure_suit(hand):
    suits = set(tile[-1] for tile in hand)
    return len(suits) == 1
