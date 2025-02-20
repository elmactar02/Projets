BACKGROUND_COLOR = "#B1DDC6"
import random
import tkinter, sys, pandas
sys.path.append('./images')

ecran = tkinter.Tk()
ecran.title("Flash Card French-English")
#ecran.minsize(width=600,height=600)
ecran.config(padx=40,pady=40,bg=BACKGROUND_COLOR)
donnee_linguistiques = pandas.read_csv("D:/flutter/100DAYS/flash-card-project-start/data/french_words.csv")
list_data = [row for (index,row) in donnee_linguistiques.iterrows()]
try:
    mots_appris = open("learnt_word.csv","r")
except: 
    mots_appris = open("learnt_word.csv","w")
    mots_appris.write(f"English,French\n")
finally:
    mots_appris.close()
list_correct = [ ]
word_line = random.choice(list_data)

def change():
    canvas.itemconfig(bckground,image = image_dessus)
    canvas.itemconfig(verb,text=word_line.French,fill="black")
    canvas.itemconfig(langue,text="French",fill="black")

def change_back():
    canvas.itemconfig(bckground,image = image_dessous)
    canvas.itemconfig(verb,text=word_line.English,fill="black")
    canvas.itemconfig(langue,text="English",fill="black")

def generate_word_and_supp():
    global word_line, list_data
    list_correct.append(word_line)
    with open("learnt_word.csv","a") as file:
        file.write(f"{word_line.English},{word_line.French}\n")
    word_line = random.choice(list_data)
    change_back()
    for it in list_correct:
        if it.English == word_line.English:
            word_line = random.choice(list_data)
    ecran.after(5000,change)

def keep_and_generate_new():
    global word_line,list_data
    word_line = random.choice(list_data)
    change_back()
    ecran.after(5000,change)

canvas = tkinter.Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
image_dessus = tkinter.PhotoImage(file="D:/flutter/100DAYS/flash-card-project-start/images/card_front.png")
image_dessous = tkinter.PhotoImage(file="D:/flutter/100DAYS/flash-card-project-start/images/card_back.png")
bckground = canvas.create_image(400,263,image=image_dessous)
verb = canvas.create_text(400,263,text= word_line.English,font=("Arial",35,"bold"),fill="white")
langue = canvas.create_text(400,170,text= "English",font=("Arial",20,"italic"),fill="white")
canvas.grid(column=0,row=0,columnspan=2)

image_false = tkinter.PhotoImage(file="D:/flutter/100DAYS/flash-card-project-start/images/wrong.png")
button_false = tkinter.Button(width=100,height=99,image= image_false,highlightthickness=0,bd=0,command=keep_and_generate_new)
button_false.grid(column=0,row=1)

image_true = tkinter.PhotoImage(file="D:/flutter/100DAYS/flash-card-project-start/images/right.png")
button_true = tkinter.Button(width=100,height=100,image= image_true,highlightthickness=0,bd=0,command=generate_word_and_supp)
button_true.grid(column=1,row=1)
ecran.after(5000,change)



ecran.mainloop()

