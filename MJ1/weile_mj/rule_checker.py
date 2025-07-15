import copy
from collections import Counter

# 普通七对：7个对子
def is_seven_pairs(hand):
    return len(hand) == 14 and all(v == 2 for v in Counter(hand).values())

# 龙七对：1个四张 + 其他6个对子
def is_long_qidui(hand):
    count = Counter(hand)
    quads = sum(1 for v in count.values() if v == 4)
    pairs = sum(1 for v in count.values() if v == 2)
    return quads == 1 and pairs == 6

# 豪华七对：至少2个四张 + 剩下的是对子（总共7对）
def is_luxury_qidui(hand):
    count = Counter(hand)
    quads = sum(1 for v in count.values() if v >= 4)
    pairs = sum(1 for v in count.values() if v % 2 == 0 and v < 4)
    total_pairs = quads * 2 + pairs
    return total_pairs == 7 and quads >= 2

# 双豪华七对：至少3个四张 + 剩下的是对子（总共7对）
def is_super_luxury_qidui(hand):
    count = Counter(hand)
    quads = sum(1 for v in count.values() if v >= 4)
    pairs = sum(1 for v in count.values() if v % 2 == 0 and v < 4)
    total_pairs = quads * 2 + pairs
    return total_pairs == 7 and quads >= 3

def is_pong_pong_hu(hand):
    count = Counter(hand)
    triples = sum(v // 3 for v in count.values())
    pairs = sum(1 for v in count.values() if v == 2)
    return triples >= 4 and pairs == 1

def is_pure_suit(hand):
    suits = set(tile[-1] for tile in hand)
    return len(suits) == 1

# 检查是否有顺子
def has_sequence(hand):
    suits = ['万', '条', '筒']
    for suit in suits:
        suit_tiles = [int(tile[:-1]) for tile in hand if tile.endswith(suit)]
        suit_tiles.sort()
        for i in range(len(suit_tiles) - 2):
            if suit_tiles[i + 1] == suit_tiles[i] + 1 and suit_tiles[i + 2] == suit_tiles[i] + 2:
                return True
    return False

# 移除一张牌的辅助函数
def remove_tile(tiles, tile):
    if tile in tiles:
        tiles.remove(tile)
        return True
    return False

# 判断一组牌是否能组成若干顺子或刻子（递归实现）
def can_form_melds(tiles):
    if not tiles:
        return True

    tiles = sorted(tiles)
    first = tiles[0]

    # 尝试作为刻子（三张相同牌）
    count = tiles.count(first)
    if count >= 3:
        new_tiles = copy.copy(tiles)
        new_tiles.remove(first)
        new_tiles.remove(first)
        new_tiles.remove(first)
        if can_form_melds(new_tiles):
            return True

    # 尝试作为顺子（连续三张）
    suit = first[-1]
    num = int(first[:-1])
    next1 = str(num + 1) + suit
    next2 = str(num + 2) + suit
    if next1 in tiles and next2 in tiles:
        new_tiles = copy.copy(tiles)
        new_tiles.remove(first)
        new_tiles.remove(next1)
        new_tiles.remove(next2)
        if can_form_melds(new_tiles):
            return True

    return False

# 主函数：判断是否可以胡牌
def is_valid_mahjong_hand(hand):
    if len(hand) != 14:
        return False  # 麻将胡牌必须是14张牌

    count = Counter(hand)

    # 枚举所有可能的对子（将牌）
    for tile in count:
        if count[tile] >= 2:
            # 模拟移除一对将牌
            new_hand = hand[:]
            new_hand.remove(tile)
            new_hand.remove(tile)

            # 检查剩下的牌是否可以组成4组面子
            if can_form_melds(sorted(new_hand)):
                return True

    return False

# 综合胡牌判断
def is_hu(hand):
    # 特殊七对类型优先判断
    if is_super_luxury_qidui(hand):
        print("胡牌类型：双豪华七对")
        return True
    if is_luxury_qidui(hand):
        print("胡牌类型：豪华七对")
        return True
    if is_long_qidui(hand):
        print("胡牌类型：龙七对")
        return True
    if is_seven_pairs(hand):
        print("胡牌类型：七对")
        return True

    # 碰碰胡
    if is_pong_pong_hu(hand):
        print("胡牌类型：碰碰胡")
        return True

    # 清一色 + 标准胡牌
    if is_pure_suit(hand) and is_valid_mahjong_hand(hand):
        print("胡牌类型：清一色顺子胡")
        return True

    # 标准胡牌
    if is_valid_mahjong_hand(hand):
        print("胡牌类型：顺子胡")
        return True

    return False

# 判断是否听牌
def is_listening(hand):
    SUITS = ['万', '条', '筒']
    ALL_TILES = [f"{n}{suit}" for suit in SUITS for n in range(1, 10)]

    # 遍历所有可能的牌，检查摸入该牌后是否能胡牌
    for tile in ALL_TILES:
        new_hand = hand + [tile]
        if is_hu(new_hand):
            return True
    return False
