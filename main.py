from deck import Deck

def main():
    new_deck = Deck()
    new_deck.create_cards()

    print_deck(new_deck)

    new_deck.shuffle_deck()

    print_deck(new_deck)
def print_deck(deck):
    counter = 1
    for card in deck.Cards:
        print(f'card {counter}: {card.Value.name} of {card.Suit.name}')
        counter += 1
    print()


if __name__ == '__main__':
    main()

