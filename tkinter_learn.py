import tkinter

page = tkinter.Tk()
page.title("Titre")
page.minsize(width=500,height=300)

def on_clicked():
    text_input = zone_txt.get()
    label["text"] = text_input

label = tkinter.Label(text="Label",font=("Arial",24))
label.grid(column=0,row=0)

zone_txt = tkinter.Entry(highlightcolor="black")
zone_txt.grid(column=3,row=2)



button = tkinter.Button(text="Confirm",command= on_clicked)
button.grid(column=1,row=1)

button = tkinter.Button(text="New_button",command= on_clicked)
button.grid(column=2,row=0)




page.mainloop()