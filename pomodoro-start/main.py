import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timerr = None
mark = ""
import tkinter, threading

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global timerr
    canvas.after_cancel(timerr)
    canvas.itemconfig(timer_text,text="00:00")
    timer_titre.config(text="Timer")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_start():
    global reps,n1 
    reps += 1
    work_time = WORK_MIN*60
    break_time = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if (reps % 2) != 0 and reps < 9 :
        count_down(work_time)
        timer_titre.config(text="Timer",fg=GREEN)
    elif (reps % 2) == 0 and reps < 8:
        count_down(break_time)
        timer_titre.config(text="Break",fg=RED)
    elif reps == 8:
        count_down(long_break)
        timer_titre.config(text="Long Break",fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global mark
    minutes = math.floor(count/60)
    if minutes / 10 < 1:
        minutes = f"0{minutes}"
    secondes = count % 60
    
    if secondes == 0 :
        secondes = "00"
    elif secondes / 10 < 1:
        secondes = f"0{secondes}"
    
    time = f"{minutes}:{secondes}"
    canvas.itemconfig(timer_text, text= time)
    if count > 0:
        global timerr
        mark = ""
        timerr = ecran.after(1000,count_down,count-1)
        check_mark.config(text= mark)
    else:
        timer_start()
        if reps % 2 == 0 :
            mark = "✅"
            check_mark.config(text= mark)

# ---------------------------- UI SETUP ------------------------------- #

ecran = tkinter.Tk()
ecran.title("Pomodoro app")
ecran.config(padx=100,pady=50,bg=YELLOW)


canvas = tkinter.Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
img = tkinter.PhotoImage(file="tomato.png")

canvas.create_image(100,112,image=img)
timer_text = canvas.create_text(103,140,text="00:00",fill="white",font=(FONT_NAME,30,"bold"))
canvas.grid(column=1,row=1)

timer_titre = tkinter.Label(text="Timer",fg=GREEN,font=(FONT_NAME,25,"bold"),bg=YELLOW)
timer_titre.grid(column=1,row=0)

start_bttn = tkinter.Button(text="Start",fg="black",font=(FONT_NAME,12,"normal"),bg=YELLOW,command=timer_start)
start_bttn.grid(column=0,row=2)

resset_bttn = tkinter.Button(text="Reset",fg="black",font=(FONT_NAME,12,"normal"),bg=YELLOW,command=reset)
resset_bttn.grid(column=2,row=2)

check_mark = tkinter.Label(text=mark,fg=GREEN,bg=YELLOW)
check_mark.grid(column=1,row=3)

ecran.mainloop() 