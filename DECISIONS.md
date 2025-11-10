# 🧠 Design Decisions & Future Improvements

This document explains the reasoning behind the structure, key technical choices, and creative extensions implemented for the **Hawk-Eye Card Game** project.

---

## 🏗️ Architectural Decisions

### 1️⃣ Object-Oriented Design
**Why:**  
Each card game needed its own rules, yet shared deck and card behaviour.  
Using classes (`Card`, `Deck`, `HigherLowerGame`, etc.) allowed isolated logic while reusing shared methods.

**Benefits:**  
- Clean separation of concerns  
- Easier debugging and unit testing  
- Simplified expansion for new game types  

---

### 2️⃣ Tkinter GUI
**Why:**  
Tkinter is built into the official Python distribution and doesn’t require external dependencies, making it simple and portable.

**Benefits:**  
- Cross-platform  
- Lightweight  
- Easily styled with frames and widgets  

**Alternatives considered:**  
- `PyQt5`: more advanced visuals but heavier setup  
- `pygame`: better for animation but overkill for card logic  

---

### 3️⃣ Streak Combo System
**Why:**  
Adds a skill-based scoring layer that rewards accuracy and consistency — thematically matching Hawk-Eye’s focus on *precision and tracking*.  

**Implementation:**  
`multiplier = 1 + (streak // 3)`  
Every 3 correct answers increases the multiplier (x2, x3, etc.), visibly shown in the GUI.

**Result:**  
- Engages players with a “combo” feeling  
- Encourages cautious risk-taking  
- Demonstrates thoughtful algorithmic design  

---

### 4️⃣ GUI-Driven Flow
**Why:**  
User experience and accessibility are important in real products.  
Instead of restarting the CLI each time, players can:
- Change game mode and deck settings  
- Replay instantly  
- View stats  
- Read rules inside the app  

This event-driven model also shows understanding of state management.

---

### 5️⃣ Stats & Replay System
**Why:**  
A data summary connects gameplay with analytics — again echoing Hawk-Eye’s brand of *insight through data*.

**Details:**  
- Tracks total games, best score, average score, and full round log  
- Presented in a scrollable popup window  
- Future-ready for saving to a JSON or database file  

---

### 6️⃣ Game Rules Popup
**Why:**  
Documentation shouldn’t live only in code comments.  
The in-app “Game Rules” popup offers built-in help and improves discoverability for new users.

---

## 🚀 Future Improvements

These ideas extend the project while demonstrating creative and technical growth:

| Idea | Description | Impact |
|------|--------------|--------|
| 🌐 **Online / Local Leaderboard** | Save high scores and compare globally or locally | Demonstrates persistence and simple networking |
| 🎴 **Card Graphics & Animations** | Replace text with visual cards and flip effects | UI polish and user engagement |
| 🧮 **AI Hint System** | Suggest probabilities (e.g., 60% higher) | Combines logic with data analysis |
| ⏱️ **Timed Mode / Speed Run** | 60-second countdown for quick games | Adds excitement and challenge |
| 💾 **Persistent Stats** | Save and reload stats across sessions | File handling, serialization, data integrity |
| 🌙 **Dark/Light Theme Toggle** | User-selectable themes | Demonstrates GUI customization |
| 👥 **Multiplayer / Pass-and-Play** | Alternate turns and shared deck | Adds complexity and social fun |
| 🧑‍💻 **Testing Framework** | Unit tests for deck, card values, and rules | Ensures reliability and clean CI integration |

---

## 🧩 Why These Choices Fit Hawk-Eye

- **Precision & Data:** Scoring and analytics mirror Hawk-Eye’s real-world systems.  
- **Innovation:** The combo system and multiple game modes show creativity.  
- **Software Craftsmanship:** Clear modular code, GUI, and documentation show engineering discipline.

---

## 🏁 Summary

This project balances creativity, simplicity, and structure:
- Robust **game logic** foundation  
- Interactive **Tkinter GUI**  
- Measurable **stats and analytics**  
- Polished **user experience**

Together, these demonstrate practical engineering skill and thoughtful design — the core values Hawk-Eye looks for.
