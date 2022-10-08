from suit import Suit
from value import Value
from card import Card
class Deck:
    def __init__(self):
        self.Cards = []

    def create_cards(self):
        for suits in Suit:
            for values in Value:
                self.Cards.append(Card(suits, values))

    