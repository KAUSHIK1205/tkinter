from tkinter import *
window=Tk()
window.title("first tkinter screen")
window.geometry("500x600")
lbl=Label(text="hey there!",fg="black",bg="WHITE",height=2,width=400)
n_lbl=Label(text="full name",bg="cyan")
n_entry=Entry()
def show():
    n=n_entry.get()
    global msg
    msg="hello"+ n +"welcome to my new app"
    text_box.insert(END,msg)
text_box=Text(height=5)
bt=Button(text="click me",command=show)
lbl.pack()
n_lbl.pack()
n_entry.pack()
bt.pack()
text_box.pack()

window.mainloop()