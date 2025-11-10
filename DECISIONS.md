# Design Decisions

1. **Language**: Chose Python because it allows quick iteration and produces a readable CLI in a few files.
2. **Separation of concerns**: Split the code into `card`, `deck`, and `game` modules so that adding new game modes does not require rewriting the deck.
3. **Card modelling**: Used ranks and suits as strings and a `value()` helper for comparison. This makes it easy to display friendly symbols (♣, ♦, ♥, ♠).
4. **Jokers**: Treated jokers as always-highest to avoid edge-case comparisons.
5. **CLI**: Kept interaction text-based to satisfy the requirement and to make automated testing easier.
6. **Extensibility**: Showed a second game (`SameSuitGame`) to demonstrate that the deck abstraction works for other rules.
7. **Shuffling**: Relied on Python’s built-in `random.shuffle`, which is adequate for this use case.
