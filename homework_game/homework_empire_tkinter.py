import tkinter as tk
from tkinter import messagebox
import random

class HomeworkGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Homework Game")
        self.root.geometry("850x600")

        self.funds = 0.0
        self.reputation = 0
        self.answer_value = 5

        self.generate_question()
        self.build_ui()
        self.update_game()

    def build_ui(self):
        tk.Label(self.root, text="Homework Game", font=("Arial", 24, "bold")).pack(pady=10)

        stats = tk.Frame(self.root)
        stats.pack(pady=5)

        self.funds_label = tk.Label(stats, text="", font=("Arial", 14))
        self.funds_label.grid(row=0, column=0, padx=15)

        self.income_label = tk.Label(stats, text="", font=("Arial", 14))
        self.income_label.grid(row=0, column=1, padx=15)

        self.rep_label = tk.Label(stats, text="", font=("Arial", 14))
        self.rep_label.grid(row=0, column=2, padx=15)

        #
        manual = tk.LabelFrame(self.root, text="Manual Homework", padx=15, pady=10)
        manual.pack(fill="x", padx=20, pady=10)

        self.question_label = tk.Label(manual, text="", font=("Arial", 18))
        self.question_label.pack()

        answer_row = tk.Frame(manual)
        answer_row.pack(pady=8)

        self.answer_entry = tk.Entry(answer_row, font=("Arial", 16), width=10)
        self.answer_entry.pack(side="left", padx=5)

        tk.Button(answer_row, text="Submit Answer", command=self.submit_answer, font=("Arial", 12)).pack(side="left")

        self.message_label = tk.Label(manual, text="", font=("Arial", 11))
        self.message_label.pack()

    def generate_question(self):
        self.a = random.randint(1, 10)
        self.b = random.randint(1, 10)
        self.correct_answer = self.a + self.b

    def submit_answer(self):
        try:
            answer = int(self.answer_entry.get())
        except ValueError:
            self.message_label.config(text="Enter a number.")
            return

        if answer == self.correct_answer:
            self.funds += self.answer_value
            self.reputation += 1
            self.message_label.config(text=f"Correct! +${self.answer_value} and +1 reputation.")
        else:
            self.reputation = max(0, self.reputation - 1)
            self.message_label.config(text="Incorrect. -1 reputation.")

        self.answer_entry.delete(0, tk.END)
        self.generate_question()

    def update_game(self):
        self.funds_label.config(text=f"Funds: ${self.funds:,.0f}")
        self.rep_label.config(text=f"Reputation: {self.reputation}")

        self.question_label.config(
            text=f"What is {self.a} + {self.b}?"
        )
        self.root.after(1000, self.update_game)

    def close_game(self):
        self.root.destroy()

root = tk.Tk()
game = HomeworkGame(root)
root.mainloop()
