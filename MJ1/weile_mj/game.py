from deck import Deck
from player import Player
from rule_checker import is_seven_pairs, is_pong_pong_hu, is_pure_suit
from chicken import count_chickens

class Game:
    def __init__(self):
        self.deck = Deck()
        self.players = [Player(f"玩家{i+1}") for i in range(4)]
        hands = self.deck.deal()
        for i in range(4):
            self.players[i].hand = hands[i]

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
                if is_seven_pairs(current_player.hand):
                    chickens = count_chickens(current_player.hand, current_player.melds, self.chicken_tile)
                    print(f"🎉 {current_player.name} 七对胡牌！🐔数：{chickens}")
                    break
                # 暂时自动出第一张
                out_tile = current_player.auto_discard()
                print(f"{current_player.name} 出牌：{out_tile}")
            turn += 1
