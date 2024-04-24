from tkinter import *
from quiz_brain import *

THEME_COLOR = "#375362"


class QuizGUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, highlightthickness=0,
                           padx=20, pady=20)

        self.canvas = Canvas(self.window, width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125, width=280, text="Question screen", fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        check_img = PhotoImage(file="images/true.png")
        check_x = PhotoImage(file="images/false.png")
        self.check_button = Button(image=check_img, command=self.true_answer)
        self.x_button = Button(image=check_x, command=self.false_answer)
        self.check_button.grid(row=2, column=0)
        self.x_button.grid(row=2, column=1)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.quiz_next_question()
        self.window.mainloop()

    def quiz_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz_brain.still_has_questions():
            q_text = self.quiz_brain.next_question()
            if q_text:
                self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"Final score: {self.quiz_brain.score}")

    def true_answer(self):
        if self.quiz_brain.check_answer("True"):
            self.score_label.config(text=f"Score: {self.quiz_brain.score}")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.quiz_next_question)

    def false_answer(self):
        if self.quiz_brain.check_answer("False"):
            self.score_label.config(text=f"Score: {self.quiz_brain.score}")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.quiz_next_question)
