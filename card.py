from dataclasses import dataclass

SUITS = ["♣", "♦", "♥", "♠"]
RANKS = [
    "2", "3", "4", "5", "6", "7", "8",
    "9", "10", "J", "Q", "K", "A"
]

# we'll map ranks to numeric values for comparison
RANK_VALUES = {rank: i for i, rank in enumerate(RANKS, start=2)}

@dataclass(frozen=True)
class Card:
    rank: str | None
    suit: str | None
    is_joker: bool = False

    def value(self) -> int:
        """
        Returns a numeric value for comparison.
        Jokers are treated as highest possible value.
        """
        if self.is_joker:
            return 100  # bigger than any normal card
        return RANK_VALUES[self.rank]

    def __str__(self) -> str:
        if self.is_joker:
            return "🃏 Joker"
        return f"{self.rank}{self.suit}"