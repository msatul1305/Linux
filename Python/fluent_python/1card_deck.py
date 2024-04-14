import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])
print(Card)


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    print(ranks)
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
print(Card('Q', 'hearts') in deck)
print(Card('A', 'hearts') in deck)
print(Card('2', 'hearts') in deck)

# sort cards by power -> A>K>Q>J>10..., Spades>Hearts>Diamond>Clubs

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
print(suit_values)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    print(card, card.rank, rank_value, card.suit)
    print(rank_value * len(suit_values) + suit_values[card.suit])
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):
    print(card)
