
from deck import Deck
from card import RANKS


class HigherLowerGame:
    def __init__(self, add_jokers: int = 0, use_streaks: bool = True):
        self.deck = Deck(add_jokers=add_jokers)
        self.score = 0
        self.streak = 0
        self.use_streaks = use_streaks
        self.rounds: list[dict] = []
        self.current_card = self.deck.draw()

    def is_over(self) -> bool:
        return self.current_card is None or len(self.deck) == 0

    def _streak_multiplier(self) -> int:
        if not self.use_streaks:
            return 1
        return 1 + (self.streak // 3)

    def guess(self, guess_str: str):
        if len(self.deck) == 0:
            return False, self.current_card, None, self.score

        next_card = self.deck.draw()
        assert next_card is not None

        g = guess_str.lower()
        is_higher_guess = g in ("h", "higher", "hi")

        current_val = self.current_card.value()
        next_val = next_card.value()

        if next_val == current_val:
            correct = False
        elif is_higher_guess and next_val > current_val:
            correct = True
        elif not is_higher_guess and next_val < current_val:
            correct = True
        else:
            correct = False

        if correct:
            self.streak += 1
            self.score += 1 * self._streak_multiplier()
        else:
            self.streak = 0

        self.rounds.append({
            "mode": "higher-lower",
            "guess": "higher" if is_higher_guess else "lower",
            "from": str(self.current_card),
            "to": str(next_card),
            "correct": correct,
            "score_after": self.score,
            "streak_after": self.streak,
        })

        self.current_card = next_card
        return correct, self.current_card, next_card, self.score


class SameSuitGame:
    def __init__(self, add_jokers: int = 0, use_streaks: bool = True):
        self.deck = Deck(add_jokers=add_jokers)
        self.score = 0
        self.streak = 0
        self.use_streaks = use_streaks
        self.rounds: list[dict] = []
        self.current_card = self.deck.draw()

    def is_over(self) -> bool:
        return self.current_card is None or len(self.deck) == 0

    def _streak_multiplier(self) -> int:
        if not self.use_streaks:
            return 1
        return 1 + (self.streak // 3)

    def guess(self, guess_str: str):
        if len(self.deck) == 0:
            return False, self.current_card, None, self.score

        next_card = self.deck.draw()
        assert next_card is not None

        wants_same = guess_str.lower() in ("y", "yes")
        same_suit = (
            not self.current_card.is_joker
            and not next_card.is_joker
            and self.current_card.suit == next_card.suit
        )

        correct = (wants_same and same_suit) or (not wants_same and not same_suit)

        if correct:
            self.streak += 1
            self.score += 1 * self._streak_multiplier()
        else:
            self.streak = 0

        self.rounds.append({
            "mode": "same-suit",
            "guess": "same" if wants_same else "different",
            "from": str(self.current_card),
            "to": str(next_card),
            "correct": correct,
            "score_after": self.score,
            "streak_after": self.streak,
        })

        self.current_card = next_card
        return correct, self.current_card, next_card, self.score


class PrecisionGame:
    def __init__(self, add_jokers: int = 0, use_streaks: bool = True):
        self.deck = Deck(add_jokers=add_jokers)
        self.score = 0
        self.streak = 0
        self.use_streaks = use_streaks
        self.rounds: list[dict] = []
        self.current_card = self.deck.draw()

    def is_over(self) -> bool:
        return len(self.deck) == 0

    def guess(self, guessed_rank: str):
        if len(self.deck) == 0:
            return False, self.current_card, None, self.score

        next_card = self.deck.draw()
        assert next_card is not None

        if next_card.is_joker:
            correct = False
            points = 0
            self.streak = 0
            actual_rank = None
        else:
            guessed_rank = guessed_rank.upper()
            actual_rank = next_card.rank

            if guessed_rank == actual_rank:
                correct = True
                self.streak += 1
                base_points = 3
                streak_bonus = (self.streak // 3) if self.use_streaks else 0
                points = base_points + streak_bonus
            else:
                # off-by-one gets 1 point, no streak
                try:
                    g_idx = RANKS.index(guessed_rank)
                    a_idx = RANKS.index(actual_rank)
                    if abs(g_idx - a_idx) == 1:
                        correct = False
                        points = 1
                        self.streak = 0
                    else:
                        correct = False
                        points = 0
                        self.streak = 0
                except ValueError:
                    correct = False
                    points = 0
                    self.streak = 0

        self.score += points

        self.rounds.append({
            "mode": "precision",
            "guess": guessed_rank,
            "to": str(next_card),
            "correct": correct,
            "points": points,
            "score_after": self.score,
            "streak_after": self.streak,
        })

        self.current_card = next_card
        return correct, self.current_card, next_card, self.score
