from tkinter import *
window=Tk()
window.title("activity 1")
window.geometry("250x300")
num=([9,8,7],[6,5,4],[3,2,1],['#',0,'*'])
for i in range(4):
    window.columnconfigure(i,weight=1,minsize=75)
    window.rowconfigure(i,weight=1,minsize=50)
for i in range(4):
    for j in range(3):
        frame=Frame(master=window,relief=RAISED,bg='red')
        frame.grid(row=i,column=j,sticky='nsew')
        label=Label(master=frame,text= num [i][j],bg='blue')
        label.pack(expand=True,fill='both',padx=5,pady=5)








window.mainloop()
