import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WHITE_COLOR = "#ffffff"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizz")
        self.window.configure(background=THEME_COLOR, pady=20, padx=20)

        self.score_label = tk.Label(text="Score: 0", bg=THEME_COLOR, fg=WHITE_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = tk.Canvas(width=300, height=250, bg=WHITE_COLOR, highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=260,
            text="Question Text Shall Go There!",
            fill=THEME_COLOR,
            font=("Arial", 18),
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        true_image = tk.PhotoImage(file="images/true.png")
        self.true_button = tk.Button(image=true_image, highlightthickness=0, command=self.btn_true_pressed)
        self.true_button.grid(row=2, column=0)

        false_image = tk.PhotoImage(file="images/false.png")
        self.false_button = tk.Button(image=false_image, highlightthickness=0, command=self.btn_false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg=WHITE_COLOR)
        if self.quiz.still_has_questions():
            self.score_label.configure(text=f"Score: {self.quiz.score}")
            q_next = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_next)
        else:
            self.canvas.itemconfig(
                self.question_text,
                text=f"You've completed the quiz!\n{self.quiz.score}/{self.quiz.question_number}",
                justify="center")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def btn_true_pressed(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def btn_false_pressed(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.get_next_question)

