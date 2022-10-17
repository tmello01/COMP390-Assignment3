from suit import Suit
from value import Value
from card import Card
from random import sample
from exceptions import EmptyDeckException


class Deck:
    def __init__(self):
        self.cards = []
        self.deck_position = 0

    def create_cards(self):
        self.cards = []
        for suits in Suit:
            for values in Value:
                self.cards.append(Card(suits, values))

    def shuffle_deck(self):
        self.deck_position = 0
        shuffled_cards = []
        for index in sample(range(0, 52), 52):
            shuffled_cards.append(self.cards[index])
        self.cards = shuffled_cards

    def get_card(self):
        if self.deck_position == 52:
            raise EmptyDeckException("unable to get next card, empty deck found.")
        card = self.cards[self.deck_position]
        self.deck_position += 1
        return card
