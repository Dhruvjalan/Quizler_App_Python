from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.correct = None
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        self.score=0
        self.score_label = Label(text=f"Score: {self.score}")
        self.score_label.grid(row=0,column=1,padx=20,pady=20)

        self.canvas = Canvas(width=300, height=250,bg="White")
        self.canvas_text = self.canvas.create_text(
            150,
            125,
            text="quote",
            width=280,
            font=("Arial", 20,"italic"),
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0,columnspan=2,padx=20,pady=20)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_clicked)
        self.true_button.grid(row=2, column=0,padx=20,pady=20)
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_clicked)
        self.false_button.grid(row=2, column=1,padx=20,pady=20)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.canvas_text, text=q_text)

    def true_clicked(self):

        if self.quiz.check_answer("True"):
            self.score += 1
            self.score_label["text"] = f"Score: {self.score}"
            self.canvas.config(bg="green")
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.get_next_question)

    def false_clicked(self):
        if self.quiz.check_answer("False"):
            self.score+=1
            self.score_label["text"] = f"Score: {self.score}"
            self.canvas.config(bg="green")
            self.window.after(1000, self.get_next_question)

        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.get_next_question)
