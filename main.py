# Tyler Mello
# COMP390 - Assignment 3
# 10/17/2022
from deck import Deck
from exceptions import EmptyDeckException


def main():
    new_deck = Deck()
    new_deck.create_cards()
    print("NEW DECK:")
    print_deck(new_deck)  # prints in-order deck, since it's brand new

    new_deck.shuffle_deck()

    print("SHUFFLED DECK:")
    print_deck(new_deck)  # prints randomly shuffled deck


def print_deck(deck):
    counter = 1
    while True:
        try:
            card = deck.get_card()
        except EmptyDeckException:  # if an empty deck exception occurs, just break
            break
        print(f'card {counter}: {card.Value.name} of {card.Suit.name}')
        counter += 1
    print()


if __name__ == '__main__':
    main()

