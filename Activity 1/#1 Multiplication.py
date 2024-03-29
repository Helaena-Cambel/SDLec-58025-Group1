import tkinter as tk
from tkinter import messagebox
import random

class MultiplicationGame:
    def __init__(self):
        self.points = 0
        self.window = tk.Tk()
        self.window.title("Multiplication Game")
        width = self.window.winfo_screenwidth()
        height = self.window.winfo_screenheight()
        w = (width - 400) // 2
        h = (height - 350) // 2
        self.window.geometry(f"{400}x{350}+{w}+{h}")
        self.window.configure(bg="#29C5F6")
        self.create_widgets()
        self.ask_question()

    def create_widgets(self):
        self.question_label = tk.Label(
            self.window, text="", font=("Comic Sans MS", 16), bg="#1260CC", fg="#9FDFE0"
        )
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(
            self.window, font=("Comic Sans MS", 14), justify="center", width=5
        )
        self.answer_entry.pack(pady=20)

        self.submit_button = tk.Button(
            self.window,
            text="Submit",
            command=self.check_answer,
            font=("Comic Sans MS", 14),
            bg="#00008B",
            fg="#FFFFFF",
        )
        self.submit_button.pack()

        self.score_label = tk.Label(
            self.window, text="Score: 0", font=("Comic Sans MS", 14), bg="#55AAFF", fg="#23297A"
        )
        self.score_label.pack(pady=20)

        self.exit_button = tk.Button(
            self.window,
            text="Quit",
            command=self.window.destroy,
            font=("Comic Sans MS", 14),
            bg="#00008B",
            fg="#FFFFFF",
        )
        self.exit_button.pack(pady=10)

    def ask_question(self):
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        self.correct_answer = num1 * num2
        self.question_label.config(text=f"How much is {num1} times {num2}?")
        self.answer_entry.delete(0, tk.END)

    def check_answer(self):
        user_answer = self.answer_entry.get()
        try:
            user_answer = int(user_answer)
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number.")
            return

        if user_answer == self.correct_answer:
            messagebox.showinfo("Correct", "You are correct!")
            self.points += 5
            self.ask_question()
        else:
            messagebox.showwarning("Incorrect", "Incorrect. Please try again.")
            self.points = max(0, self.points - 5)

        self.score_label.config(text=f"Score: {self.points}")

        if self.points > 0:
            self.answer_entry.delete(0, tk.END)
        else:
            messagebox.showinfo("Game Over", "Game over. You have no more points to be deducted.")
            self.window.destroy()

if __name__ == "__main__":
    game = MultiplicationGame()
    game.window.mainloop()
