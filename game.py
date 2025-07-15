from deck import Deck
from player import Player
from rule_checker import is_hu
from chicken import count_chickens

class Game:
    def __init__(self):
        self.deck = Deck()
        self.players = [Player(f"玩家{i+1}") for i in range(4)]
        hands = self.deck.deal()
        for i in range(4):
            self.players[i].hand = hands[i]
            self.players[i].sort_hand()  # 初始手牌排序
        self.chicken_tile = None  # 初始鸡牌设为 None

    def update_chicken_tile(self):
        # 更新鸡牌
        self.chicken_tile = self.deck.flip_chicken()
        print(f"新的鸡牌: {self.chicken_tile}")

    def play(self):
        turn = 0
        while self.deck.tiles:
            current_player = self.players[turn % 4]
            tile = self.deck.draw()
            if tile:
                current_player.draw_tile(tile)
                print(f"\n=== 第 {turn+1} 轮 - {current_player.name} ===")
                print(f"{current_player.name} 摸牌：{tile}")
                # 胡牌判断
                if is_hu(current_player.hand):
                    if self.chicken_tile is None:
                        self.update_chicken_tile()  # 首次胡牌时更新鸡牌
                    chickens = count_chickens(current_player.hand, current_player.melds, self.chicken_tile)
                    print(f"🎉 {current_player.name} 七对胡牌！🐔数：{chickens}")
                    break
                # 根据玩家选择出牌
                if current_player.name == "玩家1":
                    out_tile = current_player.choose_discard()
                else:
                    out_tile = current_player.auto_discard()
                print(f"{current_player.name} 出牌：{out_tile}")
            turn += 1