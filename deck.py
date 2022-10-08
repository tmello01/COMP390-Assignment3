from suit import Suit
from value import Value
from card import Card

from random import sample

class Deck:
    def __init__(self):
        self.Cards = []

    def create_cards(self):
        for suits in Suit:
            for values in Value:
                self.Cards.append(Card(suits, values))

    def shuffle_deck(self):
        shuffled_cards = []

        for index in sample(range(0, 52), 52):
            shuffled_cards.append(self.Cards[index])
        self.Cards = shuffled_cards
