from deck import Deck
from random import shuffle, choice

class Hand:

    def __init__(self):
        self.deck = Deck().build_deck()
        self.single_card = []

    def deal_card(self):
        self.single_card = choice(self.deck)
        return self.single_card
