# Card Colors:
# 0: None
# 1: Red
# 2: Yellow
# 3: Blue
# 4: Green

# Card Types:
# 0: Normal
# 1: Reverse
# 2: Draw
# 3: Wild
# 4: Wild Draw


class Game:
    class Card:
        def __init__(self, color: int, number: int, card: int = 0):
            self.color = color
            self.number = number
            self.card = card

    def __init__(self):
