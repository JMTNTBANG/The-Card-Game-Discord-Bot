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
        def gen_deck():
            deck = []                                                           # Creates Deck List

            for number in range(10):                                            # Loops Through Each Number
                for color in range(5):                                              # Loops Through Each Color
                    if color > 0:                                                       # If Color isn't Wild
                        deck.append(self.Card(color, number))                               # Add Card to Deck
                        print(f"C:{color} N:{number}")
                        if number != 0:                                                     # If Card isn't 0
                            deck.append(self.Card(color, number))                               # Add Another Card
                            print(f"C:{color} N:{number}")

            for card in range(5):                                               # Loops Through Each Card Type
                for color in range(5):                                              # Loops Through Each Color
                    if color == 0 and card == 4:                                        # If Card is Wild Draw
                        for i in range(4):                                                  #
                            deck.append(self.Card(color, 10, card))                         # Adds Card 4 Times
                            print(f"C:{color} T:{card}")
                    elif card == 3:                                                     # Else If Type is Wild
                        for i in range(4):  # Loops 4 Times                                 #
                            deck.append(self.Card(color, 10, card))                         # Adds Card 4 Times
                            print(f"C:{color} T:{card}")
                    elif card != 3:                                                     # Else If Type isn't Wild
                        for i in range(2):  # Loops Twice                                   #
                            deck.append(self.Card(color, 10, card))                         # Adds Card Twice
                            print(f"C:{color} T:{card}")
            return deck

        self.deck = gen_deck()
