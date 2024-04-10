import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])
print(Card)


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        print(self._cards)

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck()
print(deck.__len__())
print(len(deck))
print(deck.__getitem__(51))
print(deck[0])
from random import choice
print(choice(deck))
print(deck[:3])  # top 3 cards
print(deck[12::13])  # print aces starting at index 12 and skipping 13 cards at a time
print(deck[::13])  # print all 2
for card in deck:
    print(card)
for card in reversed(deck):
    print(card)
