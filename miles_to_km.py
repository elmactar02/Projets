import tkinter


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=400,height=200)
window.config(padx=80,pady=40)
def on_clicked():
    nombre = float(entree.get()) * 1.609
    text4["text"] =  str(nombre)

text1 = tkinter.Label(text="is equal to",font=("Arial",15))
text1.grid(column=0,row=1)

text2 = tkinter.Label(text="Km",font=("Arial",15))
text2.grid(column=2,row=1)


text3 = tkinter.Label(text="Miles",font=("Arial",15))
text3.grid(column=2,row=0)

text4 = tkinter.Label(text="0",font=("Arial",15))
text4.grid(column=1,row=1)

entree = tkinter.Entry(width=10)
entree.grid(column=1,row=0)

buttn = tkinter.Button(text="Calculate",command=on_clicked)
buttn.grid(column=1,row=2)









window.mainloop()