from tkinter import *
window=Tk()
window.title("first tkinter screen")
window.geometry("500x600")
lbl=Label(text="hey there!, wanna multiply",fg="black",bg="WHITE",height=2,width=400)
n_lbl=Label(text="ENTER NUMBER 1",bg="teal")
n_entry=Entry()

n_lbl2=Label(text="ENTER NUMBER 2",bg="teal")
n_entry2=Entry()
def show():
    n=int(n_entry.get())
    n2=int(n_entry.get())
    global msg
    msg=n*n2
    text_box.insert(END,msg)

text_box=Text(height=5)
bt=Button(text="product",command=show)
lbl.pack()
n_lbl.pack()
n_entry.pack()
n_lbl2.pack()
n_entry2.pack()
bt.pack()
text_box.pack()

window.mainloop()