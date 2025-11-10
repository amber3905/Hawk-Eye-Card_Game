import argparse
from game import HigherLowerGame, SameSuitGame

def run_higher_lower(jokers: int):
    game = HigherLowerGame(add_jokers=jokers)
    print("Welcome to Higher / Lower!")
    print(f"Jokers in deck: {jokers}")
    print(f"Starting card: {game.current_card}")

    while True:
        if game.is_over():
            print("No more cards. Final score:", game.score)
            break

        guess = input("Will the next card be (h)igher or (l)ower? ").strip()
        if guess.lower() not in ("h", "higher", "l", "lower"):
            print("Please enter 'h' or 'l'.")
            continue

        correct, current_card, next_card, score = game.guess(guess)
        # current_card and next_card are actually the same here
        print(f"Next card was: {next_card}")
        if correct:
            print("✅ Correct!")
            print("Score:", score)
        else:
            print("❌ Wrong!")
            print("Final score:", score)
            break


def run_same_suit(jokers: int):
    game = SameSuitGame(add_jokers=jokers)
    print("Welcome to Same Suit?")
    print(f"Jokers in deck: {jokers}")
    print(f"Starting card: {game.current_card}")

    while True:
        if game.is_over():
            print("No more cards. Final score:", game.score)
            break

        guess = input("Will the next card be the SAME suit? (y/n) ").strip()
        if guess.lower() not in ("y", "yes", "n", "no"):
            print("Please enter 'y' or 'n'.")
            continue

        correct, current_card, next_card, score = game.guess(guess)
        print(f"Next card was: {next_card}")
        if correct:
            print("✅ Correct!")
            print("Score:", score)
        else:
            print("❌ Wrong!")
            print("Final score:", score)
            break


def main():
    parser = argparse.ArgumentParser(description="CLI Card Games")
    parser.add_argument("--mode", choices=["higher-lower", "same-suit"], default="higher-lower")
    parser.add_argument("--jokers", type=int, default=0, help="Number of jokers to add (0, 1, 2)")
    args = parser.parse_args()

    if args.mode == "higher-lower":
        run_higher_lower(args.jokers)
    else:
        run_same_suit(args.jokers)


if __name__ == "__main__":
    main()