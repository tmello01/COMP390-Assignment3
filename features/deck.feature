Feature: testing deck shuffling
  Scenario: New deck
    Given the deck is brand new
      When the top card is pulled
      Then the card is an ace of spades

  Scenario: Shuffled deck
    Given the deck has been shuffled
      When the top card is pulled
      Then the card is not an ace of spades