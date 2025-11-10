import tkinter as tk
from tkinter import ttk, messagebox
from game import HigherLowerGame, SameSuitGame, PrecisionGame
from card import RANKS


class CardGameApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Card Games")
        self.geometry("460x400")
        self.resizable(False, False)

        # current settings
        self.current_game = None
        self.current_mode = tk.StringVar(value="higher-lower")
        self.joker_count = tk.IntVar(value=0)

        # global stats
        self.stats = {
            "games_played": 0,
            "best_score": 0,
            "total_score": 0,
            "last_game_rounds": [],
        }

        self.config_frame = None
        self.play_frame = None

        self.show_config_screen()

    # ---------------- CONFIG SCREEN ----------------
    def show_config_screen(self):
        if self.play_frame:
            self.play_frame.destroy()

        self.config_frame = tk.Frame(self, padx=20, pady=20)
        self.config_frame.pack(fill="both", expand=True)

        title = tk.Label(self.config_frame, text="Choose your game", font=("Helvetica", 18, "bold"))
        title.pack(pady=(0, 15))

        # game selection
        tk.Label(self.config_frame, text="Game mode:", font=("Helvetica", 12)).pack(anchor="w")
        ttk.Combobox(
            self.config_frame,
            textvariable=self.current_mode,
            values=["higher-lower", "same-suit", "precision"],
            state="readonly"
        ).pack(fill="x", pady=(0, 10))

        # jokers selection
        tk.Label(self.config_frame, text="Number of jokers:", font=("Helvetica", 12)).pack(anchor="w", pady=(10, 0))
        tk.Spinbox(
            self.config_frame,
            from_=0,
            to=2,
            textvariable=self.joker_count,
            width=5
        ).pack(anchor="w", pady=(0, 15))

        # start button
        tk.Button(self.config_frame, text="Start game", command=self.start_game, width=15).pack(pady=5)

        # NEW: rules button
        tk.Button(self.config_frame, text="Game rules", command=self.show_rules).pack(pady=5)

    # ---------------- PLAY SCREEN ----------------
    def start_game(self):
        mode = self.current_mode.get()
        jokers = self.joker_count.get()

        # streaks always on
        if mode == "higher-lower":
            self.current_game = HigherLowerGame(add_jokers=jokers, use_streaks=True)
        elif mode == "same-suit":
            self.current_game = SameSuitGame(add_jokers=jokers, use_streaks=True)
        else:
            self.current_game = PrecisionGame(add_jokers=jokers, use_streaks=True)

        if self.config_frame:
            self.config_frame.destroy()
            self.config_frame = None

        self.show_play_screen(mode)

    def show_play_screen(self, mode: str):
        if self.play_frame:
            self.play_frame.destroy()

        self.play_frame = tk.Frame(self, padx=20, pady=20)
        self.play_frame.pack(fill="both", expand=True)

        header = tk.Label(
            self.play_frame,
            text=f"Playing: {mode.replace('-', ' ').title()} (Jokers: {self.joker_count.get()})",
            font=("Helvetica", 14, "bold")
        )
        header.pack(pady=(0, 15))

        self.card_label = tk.Label(self.play_frame, text=str(self.current_game.current_card), font=("Helvetica", 30))
        self.card_label.pack(pady=10)

        self.score_label = tk.Label(self.play_frame, text=f"Score: {self.current_game.score}", font=("Helvetica", 12))
        self.score_label.pack(pady=(0, 4))

        # streak label
        self.streak_label = tk.Label(self.play_frame, text=f"Streak: {self.current_game.streak}", font=("Helvetica", 11))
        self.streak_label.pack(pady=(0, 2))

        # multiplier label
        current_multiplier = 1 + (self.current_game.streak // 3)
        self.mult_label = tk.Label(self.play_frame, text=f"Multiplier: x{current_multiplier}", font=("Helvetica", 11))
        self.mult_label.pack(pady=(0, 10))

        self.message_label = tk.Label(self.play_frame, text="", font=("Helvetica", 11))
        self.message_label.pack(pady=(0, 10))

        self.buttons_frame = tk.Frame(self.play_frame)
        self.buttons_frame.pack(pady=5)

        if mode == "higher-lower":
            self.make_higher_lower_buttons()
        elif mode == "same-suit":
            self.make_same_suit_buttons()
        else:
            self.make_precision_widgets()

        self.bottom_frame = tk.Frame(self.play_frame)
        self.bottom_frame.pack(pady=10, fill="x")

        self.play_again_btn = tk.Button(self.bottom_frame, text="Play again", command=self.play_again, state="disabled")
        self.play_again_btn.pack(side="left", padx=(0, 8))

        self.stats_btn = tk.Button(self.bottom_frame, text="View stats", command=self.show_stats, state="disabled")
        self.stats_btn.pack(side="left", padx=(0, 8))

        self.back_btn = tk.Button(self.bottom_frame, text="Back to menu", command=self.back_to_menu)
        self.back_btn.pack(side="left")

    # -------- BUTTON SETS --------
    def make_higher_lower_buttons(self):
        tk.Button(self.buttons_frame, text="Higher", width=10,
                  command=lambda: self.handle_guess("h")).grid(row=0, column=0, padx=5)
        tk.Button(self.buttons_frame, text="Lower", width=10,
                  command=lambda: self.handle_guess("l")).grid(row=0, column=1, padx=5)

    def make_same_suit_buttons(self):
        tk.Button(self.buttons_frame, text="Same suit (Yes)", width=15,
                  command=lambda: self.handle_guess("y")).grid(row=0, column=0, padx=5)
        tk.Button(self.buttons_frame, text="Different (No)", width=15,
                  command=lambda: self.handle_guess("n")).grid(row=0, column=1, padx=5)

    def make_precision_widgets(self):
        tk.Label(self.buttons_frame, text="Guess next rank:").grid(row=0, column=0, padx=5)
        self.rank_var = tk.StringVar(value=RANKS[0])
        ttk.Combobox(self.buttons_frame, textvariable=self.rank_var, values=RANKS, state="readonly", width=5)\
            .grid(row=0, column=1, padx=5)
        tk.Button(self.buttons_frame, text="Guess", command=self.handle_precision_guess).grid(row=0, column=2, padx=5)

    # -------- HANDLERS --------
    def _update_top_labels(self):
        self.score_label.config(text=f"Score: {self.current_game.score}")
        self.streak_label.config(text=f"Streak: {self.current_game.streak}")
        mult = 1 + (self.current_game.streak // 3)
        self.mult_label.config(text=f"Multiplier: x{mult}")

    def handle_guess(self, guess: str):
        if self.current_game.is_over():
            self.end_game()
            return

        correct, current_card, next_card, score = self.current_game.guess(guess)

        self.card_label.config(text=str(next_card))
        self._update_top_labels()

        if correct:
            self.message_label.config(text="✅ Correct!", fg="green")
            if self.current_game.is_over():
                self.end_game()
        else:
            self.message_label.config(text="❌ Wrong!", fg="red")
            self.end_game()

    def handle_precision_guess(self):
        if self.current_game.is_over():
            self.end_game()
            return

        guessed_rank = self.rank_var.get()
        correct, current_card, next_card, score = self.current_game.guess(guessed_rank)

        self.card_label.config(text=str(next_card))
        self._update_top_labels()

        if correct:
            self.message_label.config(text="🎯 Exact!", fg="green")
            if self.current_game.is_over():
                self.end_game()
        else:
            self.message_label.config(text="Not quite...", fg="red")
            if self.current_game.is_over():
                self.end_game()

    def end_game(self):
        for child in self.buttons_frame.winfo_children():
            child.config(state="disabled")

        # update global stats
        self.stats["games_played"] += 1
        self.stats["total_score"] += self.current_game.score
        self.stats["best_score"] = max(self.stats["best_score"], self.current_game.score)
        self.stats["last_game_rounds"] = getattr(self.current_game, "rounds", [])

        self.play_again_btn.config(state="normal")
        self.stats_btn.config(state="normal")

        messagebox.showinfo("Game over", f"Final score: {self.current_game.score}")

    def play_again(self):
        mode = self.current_mode.get()
        jokers = self.joker_count.get()

        if mode == "higher-lower":
            self.current_game = HigherLowerGame(add_jokers=jokers, use_streaks=True)
        elif mode == "same-suit":
            self.current_game = SameSuitGame(add_jokers=jokers, use_streaks=True)
        else:
            self.current_game = PrecisionGame(add_jokers=jokers, use_streaks=True)

        self.show_play_screen(mode)

    def back_to_menu(self):
        if self.play_frame:
            self.play_frame.destroy()
            self.play_frame = None
        self.show_config_screen()

    def show_stats(self):
        stats_win = tk.Toplevel(self)
        stats_win.title("Stats summary")
        stats_win.geometry("360x360")

        games = self.stats["games_played"]
        best = self.stats["best_score"]
        total = self.stats["total_score"]
        avg = total / games if games else 0

        tk.Label(stats_win, text="Session Stats", font=("Helvetica", 14, "bold")).pack(pady=10)
        tk.Label(stats_win, text=f"Games played: {games}").pack(anchor="w", padx=10)
        tk.Label(stats_win, text=f"Best score: {best}").pack(anchor="w", padx=10)
        tk.Label(stats_win, text=f"Average score: {avg:.2f}").pack(anchor="w", padx=10)

        tk.Label(stats_win, text="Last game rounds:", font=("Helvetica", 12, "bold")).pack(pady=(10, 0), anchor="w", padx=10)

        frame = tk.Frame(stats_win)
        frame.pack(fill="both", expand=True, padx=10, pady=5)

        rounds_box = tk.Text(frame, height=10, width=40)
        rounds_box.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(frame, command=rounds_box.yview)
        scrollbar.pack(side="right", fill="y")
        rounds_box.configure(yscrollcommand=scrollbar.set)

        for i, r in enumerate(self.stats["last_game_rounds"], start=1):
            rounds_box.insert("end", f"{i}. {r}\n")

        rounds_box.config(state="disabled")

    # ---------- NEW: RULES POPUP ----------
    def show_rules(self):
        win = tk.Toplevel(self)
        win.title("Game rules")
        win.geometry("420x380")

        text = tk.Text(win, wrap="word")
        text.pack(fill="both", expand=True, padx=10, pady=10)

        rules_text = """
GAME RULES

1) Higher / Lower
- You see the current card.
- You guess if the NEXT card will be higher or lower in value.
- Aces are high.
- Jokers (if present) are treated as highest.
- Correct guesses increase your streak.
- Every 3 streak increases your multiplier.

2) Same Suit
- You see the current card.
- You guess if the NEXT card will be the SAME suit.
- Jokers never match suits.
- Correct guesses increase your streak and score.

3) Precision
- You guess the EXACT RANK of the next card (e.g. '5', 'Q', 'A').
- Exact match: high points.
- Close (±1 rank): small points.
- Jokers can’t be predicted.

Scoring & Multiplier
- Base score goes up on correct answers.
- Streak: number of consecutive correct answers.
- Multiplier = 1 + (streak // 3)
  e.g. streak 0–2 → x1, streak 3–5 → x2, streak 6–8 → x3
"""
        text.insert("1.0", rules_text)
        text.config(state="disabled")

        tk.Button(win, text="Close", command=win.destroy).pack(pady=5)


if __name__ == "__main__":
    print("Launching GUI...")
    app = CardGameApp()
    app.mainloop()
