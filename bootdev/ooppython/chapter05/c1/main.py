import random

SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.rank_index = RANKS.index(rank)
        self.suit_index = SUITS.index(suit)

    def __eq__(self, other):
        return (
            self.rank == other.rank
            and self.suit == other.suit
        )

    def __lt__(self, other):
        return (
            self.rank_index < other.rank_index 
            or self.rank_index == other.rank_index 
            and self.suit_index < other.suit_index
        )

    def __gt__(self, other):
        return (
            self.rank_index > other.rank_index 
            or self.rank_index == other.rank_index 
            and self.suit_index > other.suit_index
        )

    # don't touch below this line

    def __str__(self):
        return f"{self.rank} of {self.suit}"
