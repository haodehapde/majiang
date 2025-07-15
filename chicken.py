
def count_chickens(hand, melds, chicken_tile):
    all_tiles = hand + [t for group in melds for t in group]
    return all_tiles.count(chicken_tile)
