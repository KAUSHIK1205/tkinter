from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("first tkinter screen")
lbl=Label(text="hey there!",fg="black",bg="WHITE",height=2,width=400)
n_lbl=Label(text="full name",bg="cyan")
window.geometry("500x600")
def key(event):
    print("you pressed the key")
    print(event.char)
    
window.bind("<Key>",key)
def btnclick(event):
    print("you clicked the button")

button=Button(text="click me")
button.pack()
button. bind("<Button-1>",btnclick)
lbl.pack()
n_lbl.pack()

def msg():
    messagebox.showwarning("alert","stop virus found")

bt2=Button(text="scan for virus",command=msg)
bt2.pack()



window.mainloop()