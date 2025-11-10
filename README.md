# Hawk-Eye Innovations Coding Task 🎯

A CLI-based **Higher or Lower** card game written in Python.

## Features
- 52-card standard deck
- Shuffle using Python’s random
- “Higher or Lower” gameplay
- Optional Jokers (`--jokers 2`)
- Extra mini-game “Same Suit?”
- Modular design (card/deck/game separation)

## Future Improvements

- **Online leaderboard**: Push scores to a small REST endpoint to compare results across users.
- **Richer animations**: Replace text-based cards with images and add simple flip/deal animations in Tkinter.
- **AI / hints**: Provide probability-based hints (e.g. “likely higher” if remaining deck is skewed).
- **Multiplayer (pass-and-play)**: Alternate turns between players using the same deck and show per-player scores.
- **Timed sprint mode**: 60-second mode where the user must answer as many as possible; useful for showcasing event-loop skills.
- **Persistence**: Store stats in a local JSON file so that session stats survive app restarts.
- **Theming**: Add dark/light theme toggle to show UI customization.

## Run the game
```bash
python cli.py
