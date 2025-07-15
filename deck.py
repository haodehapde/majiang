import random

SUITS = ['万', '条', '筒']
ALL_TILES = [f"{n}{suit}" for suit in SUITS for n in range(1, 10)]
TILE_SET = ALL_TILES * 4  # 108张

# 牌堆与抽牌逻辑
class Deck:
    def __init__(self):
        self.tiles = TILE_SET.copy()
        random.shuffle(self.tiles)

    # 从牌堆顶部抽一张牌
    def draw(self):
        if self.tiles:
            return self.tiles.pop()
        return None

    # 从牌堆底部抽一张牌
    def draw_from_bottom(self):
        if self.tiles:
            return self.tiles.pop(0)
        return None

    # 默认 4 名玩家，每人 13 张初始手牌
    def deal(self, num_players=4, tiles_per_player=13):
        return [[self.draw() for _ in range(tiles_per_player)] for _ in range(num_players)]

    def flip_chicken(self):
        # 翻出下一张牌作为鸡牌
        return self.tiles[-1] if self.tiles else None
