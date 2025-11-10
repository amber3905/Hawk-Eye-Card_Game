import random
from card import Card, SUITS, RANKS

class Deck:
    def __init__(self, add_jokers: int = 0, rng: random.Random | None = None):
        self._rng = rng or random.Random()
        self.cards = self._build_deck(add_jokers)
        self.shuffle()

    def _build_deck(self, add_jokers: int):
        cards = [Card(rank=r, suit=s) for s in SUITS for r in RANKS]
        for _ in range(add_jokers):
            cards.append(Card(rank=None, suit=None, is_joker=True))
        return cards

    def shuffle(self):
        self._rng.shuffle(self.cards)

    def draw(self):
        if not self.cards:
            return None
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)