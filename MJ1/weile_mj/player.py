from collections import Counter

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.discards = []
        self.melds = []  # 碰、杠牌区

    def draw_tile(self, tile):
        self.hand.append(tile)

    def discard_tile(self, tile):
        if tile in self.hand:
            self.hand.remove(tile)
            self.discards.append(tile)
            return tile
        return None

    def auto_discard(self):
        # 暂时随机丢一张
        tile = self.hand[0]
        self.hand.remove(tile)
        self.discards.append(tile)
        return tile

    def try_pong(self, tile):
        if self.hand.count(tile) >= 2:
            self.hand.remove(tile)
            self.hand.remove(tile)
            self.melds.append([tile] * 3)
            return True
        return False

    def try_gang(self, tile):
        if self.hand.count(tile) == 3:
            self.hand = [t for t in self.hand if t != tile]
            self.melds.append([tile] * 4)
            return True
        return False
