import time
import tkinter
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class UserInterface:
    def __init__(self,quiz:QuizBrain):       
        self.ecran = tkinter.Tk()
        self.ecran.config(bg=THEME_COLOR,padx=10,pady=10)
        self.ecran.title("Question App")
        self.quiz = quiz
        self.score_text = tkinter.Label(text=f"Score: {self.quiz.score}/{self.quiz.question_list.__len__()}",bg=THEME_COLOR)
        self.score_text.grid(column=1,row=0)

        self.canvas = tkinter.Canvas(bg="white",width=400,height=400)
        self.question = self.canvas.create_text(200,200,text="",font=("Arial",15,"normal"),fill=THEME_COLOR,width=350,justify="center")
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)

        phto_true = tkinter.PhotoImage(file="images/true.png",width=100,height=97)
        self.button_true = tkinter.Button(image=phto_true,highlightthickness=0,pady=100,command= self.answer_true)
        self.button_true.grid(column=0,row=3)

        phto_false = tkinter.PhotoImage(file="images/false.png",width=100,height=97)
        self.button_false = tkinter.Button(image=phto_false,highlightthickness=0,pady=100,command= self.answer_false)
        self.button_false.grid(column=1,row=3)

        self.change()
        self.ecran.mainloop()

    def change_score(self):
        self.score_text["text"] = f"Score: {self.quiz.score}/{self.quiz.question_list.__len__()}"
    def change_texte(self,text2):
        self.canvas.itemconfig(self.question,text = text2)

    def answer_true(self):
        res = self.quiz.check_answer("true")
        if res == True:
            self.canvas.config(bg="green")
            self.change_score()
        else:
            self.canvas.config(bg="red")
        self.ecran.after(2000, self.change)
    
    def answer_false(self):
        res = self.quiz.check_answer("false")
        if res == True:
            self.canvas.config(bg="green")
            self.change_score()
        else:
            self.canvas.config(bg="red")
        self.ecran.after(2000, self.change)
    
    def change(self):
        self.canvas.config(bg="white")
        try:
            str = self.quiz.next_question()
        except:
            self.ecran.destroy()
        else:
            self.canvas.itemconfig(self.question,text=str)
