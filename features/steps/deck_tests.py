from behave import *
from deck import Deck
from suit import Suit
from value import Value


@given("the deck is brand new")
def step_impl(context):
    deck = Deck()
    deck.create_cards()
    context.deck = deck
    assert deck.cards is not None


@when("the top card is pulled")
def step_impl(context):
    context.top_card = context.deck.get_card()


@then("the card is an ace of spades")
def step_impl(context):
    card = context.top_card
    assert card is not None
    assert card.Suit is Suit.SPADES
    assert card.Value is Value.ACE


@given("the deck has been shuffled")
def step_impl(context):
    deck = Deck()
    deck.create_cards()
    deck.shuffle_deck()
    context.deck = deck
    assert deck.cards is not None


@then("the card is not an ace of spades")
def step_impl(context):
    card = context.deck.get_card()
    suit_and_value = f'{card.Value.name} of {card.Suit.name}'
    assert suit_and_value != "Ace of Spades"


