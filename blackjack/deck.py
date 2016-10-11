
class Deck:

    def __init__(self):
        self.suits = ["♠", "♥", "♦", "♣"]
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.deck = []

    def build_deck(self):
        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append(rank + suit)
        return self.deck
