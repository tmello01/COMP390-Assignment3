# Tyler Mello
# COMP390 - Assignment 3
# 10/17/2022
from deck import Deck

def main():
    new_deck = Deck()
    new_deck.create_cards()
    print_deck(new_deck)  # prints in-order deck, since it's brand new

    new_deck.shuffle_deck()

    print_deck(new_deck)  # prints randomly shuffled deck


def print_deck(deck):
    counter = 1
    for card in deck.cards:
        print(f'card {counter}: {card.Value.name} of {card.Suit.name}')
        counter += 1
    print()


if __name__ == '__main__':
    main()

