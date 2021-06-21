"""Unit tests for datamodel directory. Uses pytest instead of unittest.
"""
from datamodel import Card, FrenchDeck


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    """Returns a card's ranking by rank (aces high), then suit (spades high).
    """
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


deck = FrenchDeck()


def test_deck_length():
    assert Card('A', 'spades') in deck


def test_iterable_in():
    assert Card('A', 'spades') in deck


def test_sort():
    ranked_cards = [card for card in sorted(deck, key=spades_high)]
    assert ranked_cards[0] == Card(rank='2', suit='clubs')
    assert ranked_cards[-1], Card(rank='A', suit='spades')
