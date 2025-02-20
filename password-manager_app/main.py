import json
import tkinter,sys
from tkinter import messagebox
sys.path.append('../')
from mdp_generator import mdp_genr

############################# Search a password ##########################
def search_pwd():
    website_provider = wb_entry.get().capitalize()
    try :
        with open("data.json","r")  as file:
               data = json.load(file)
        result = data[website_provider]
        email = result["email"]
        pwd = result["password"]
    except:
        messagebox.showerror(website_provider,"No existing password for this website")
    else:
        messagebox.showinfo(website_provider,f" Informations \n Email: {email} \n Password: {pwd} ")
              

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_the_pwd():
    pwd_entry.delete(0,len(pwd_entry.get()))
    mdp_gen = mdp_genr()
    mdp_gen.generate()
    pwd_entry.insert(0,mdp_gen.mdp)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_to_file():
    website = wb_entry.get().capitalize()
    email = email_entry.get().lower()
    pwd = pwd_entry.get()

    new_entry = {
         website: {
              "email": email,
              "password": pwd
         }
    }
    if website == "" or pwd == "" :
        messagebox.showerror(title="Error",message="One of the field isn't filled correctly")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"Here are the informations \n\n Email: {email} \n Mot de passe: {pwd} \n\n Do you want to save ? ")

        if is_ok:
                wb_entry.delete(0,len(wb_entry.get()))
                pwd_entry.delete(0,len(pwd_entry.get()))
                try:
                    file = open("data.json","r")
                except FileNotFoundError:
                    file= open("data.json","w")
                    json.dump(new_entry,file,indent=4)
                else:
                    data = json.load(file)
                    data.update(new_entry)
                    file2 = open("data.json","w")
                    json.dump(data,file2,indent=4)
                    file2.close()
                finally:
                     file.close()

# ---------------------------- UI SETUP ------------------------------- #
ecran = tkinter.Tk()
ecran.config(padx=20,pady=20)
ecran.title("Password Manager")
canvas = tkinter.Canvas(width=200,height=200)
canvas.grid(column=1,row=0) 
img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100,100,image = img)

webs_txt = tkinter.Label(text="Website: ")
webs_txt.grid(column=0,row=1)

mail_txt = tkinter.Label(text="Email/Username: ")
mail_txt.grid(column=0,row=2)

pwd_txt = tkinter.Label(text="Password: ")
pwd_txt.grid(column=0,row=3)

wb_entry = tkinter.Entry(width=35)
wb_entry.grid(column=1,row=1,columnspan=2,sticky="w")

email_entry = tkinter.Entry(width=35)
email_entry.insert(0,"mactargueye2003@gmail.com")
email_entry.grid(column=1,row=2,columnspan=2,sticky="w")

pwd_entry = tkinter.Entry(width=21)
pwd_entry.grid(column=1,row=3,sticky="w")

add_btn = tkinter.Button(text="Add",bd=1,command=add_to_file)
add_btn.grid(column=1,row=4)

gen_btn = tkinter.Button(text="Generate Password",bd=1,command=generate_the_pwd)
gen_btn.grid(column=2,row=3,)

srch_btn = tkinter.Button(text="Search",bd=1,command=search_pwd)
srch_btn.grid(column=2,row=1,)





ecran.mainloop()