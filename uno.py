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
# 3: Skip
# 4: Wild
# 5: Wild Draw

# Number 10 Represents an Action Card


class Game:
    class Card:
        def __init__(self, color: int, number: int, card: int = 0):
            self.color = color
            self.number = number
            self.card = card

    def __init__(self):
        def gen_deck():
            deck = []
            for number in range(11):
                for color in range(5):
                    for kind in range(6):
                        if number < 10 and kind == 0:
                            if color > 0:
                                deck.append(self.Card(color, number))
                                if number > 0:
                                    deck.append(self.Card(color, number))
                        elif number == 10:
                            if 0 < kind < 4 and color > 0:
                                for i in range(2):
                                    deck.append(self.Card(color, number, kind))
                            elif kind > 3 and color == 0:
                                for i in range(4):
                                    deck.append(self.Card(color, number, kind))

            return deck
        self.deck = gen_deck()
