# 🃏 Hawk-Eye Card Game

A Python-based card game collection built for the **Hawk-Eye Innovations Software Engineering Placement**.  
This project demonstrates clean object-oriented design, GUI development using Tkinter, and creative gameplay mechanics.

---

## 🎮 Overview

This app implements several mini card games using a standard 52-card deck (optionally with Jokers).  
You can play directly in a **graphical interface (GUI)** or extend the logic for CLI or further games.

---

## 🧩 Features

| Category | Feature | Description |
|-----------|----------|-------------|
| 🎯 **Core Gameplay** | Higher/Lower, Same Suit, Precision | Three playable games with unique rules. |
| 🃏 **Deck Model** | Standard 52-card deck + optional Jokers | Fully shuffled deck logic. |
| 🔄 **Streak Combo System** | Dynamic scoring multiplier | Every 3 correct answers increases score multiplier (x2, x3, etc.). |
| 📈 **Stats Summary** | Session stats + last-game replay | Tracks total games, best score, average score, and detailed round log. |
| 🪄 **GUI Interface** | Tkinter front-end | Choose mode, jokers, and view scores interactively. |
| 📖 **Rules Popup** | In-app help menu | View all game rules directly from the main menu. |
| 🔁 **Replay Button** | Restart same mode instantly | Skip back to menu only when you want to. |

---

## 🕹️ Game Modes

### 1️⃣ Higher / Lower
Guess whether the next card will be higher or lower in rank than the current one.  
- Aces are high.  
- Jokers (if included) are treated as the highest cards.  
- Streaks and multipliers increase with consecutive correct guesses.  

### 2️⃣ Same Suit
Guess if the next card will share the same suit as the current one.  
- Jokers never count as the same suit.  

### 3️⃣ Precision
Predict the **exact rank** (e.g., “5”, “K”, “A”) of the next card.  
- Exact match = high score.  
- Off by one = partial credit.  

---

## 💯 Scoring System

| Condition | Points | Notes |
|------------|---------|-------|
| Correct guess | +1 × multiplier | Base for Higher/Lower & Same Suit |
| Exact rank (Precision) | +3 × multiplier | Big reward |
| Close (±1 rank, Precision) | +1 | No multiplier |
| Wrong guess | 0 | Streak resets |

**Multiplier formula:**

multiplier = 1 + (streak // 3)

e.g.  
Streak 0–2 → x1  
Streak 3–5 → x2  
Streak 6–8 → x3  

---

## 🧠 Stats & Replay

After each game, you can:
- View your **final score**  
- Access a **stats window** summarizing:  
  - Games played this session  
  - Best score  
  - Average score  
  - Full list of recent rounds  
- Replay instantly or return to the menu.

---

## 🖥️ How to Run

Make sure you’re using the official **Python 3.12+ installer** (not Homebrew) so Tkinter works correctly.

Command Line Game:

```bash
python cli.py
```

Graphical User Interface Game:
```bash
python gui.py
```

---

## 🧱 Project Structure

```bash
Hawk-Eye-Card_Game/
├── card.py          # Card and rank definitions
├── deck.py          # Deck model with shuffle/draw
├── game.py          # Game logic for all modes
├── gui.py           # Tkinter-based user interface
├── DECISIONS.md     # Design decisions and future ideas
└── README.md        # (this file)
```

---

## 💡 Design Decisions

* Object-Oriented Structure: Each game type encapsulated in its own class with shared interfaces.
* Extendable Framework: New game types can be added easily without rewriting GUI logic.
* Stateful GUI: Maintains deck, score, streak, and stats within the app lifecycle.
* On-Brand Inspiration: Precision and analytics mechanics echo Hawk-Eye’s emphasis on accuracy and data.

---

## 🚀 Future Improvements

These ideas are documented in DECISIONS.md for future development:
* 🌐 Online or local leaderboard
* 🎴 Card images and flip animations
* 🧮 AI / hint system for probability predictions
* ⏱️ Timed “speed run” mode
* 💾 Persistent stats (save to JSON)
* 🌙 Dark/light theme toggle
* 👥 Pass-and-play multiplayer
