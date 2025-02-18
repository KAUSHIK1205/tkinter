from tkinter import *
from datetime import date, datetime

# Create the main window
window = Tk()
window.title("Age Calculator")
window.geometry("800x900")

# Add labels, entry fields, and a button to the window
lbl = Label(window, text="Hey there!", fg="black", bg="white", height=2, width=400)
n_lbl = Label(window, text="Full Name:", bg="cyan")
n_entry = Entry(window)
dob_lbl = Label(window, text="Date of Birth (dd/mm/yyyy):", bg="cyan")
dob_entry = Entry(window)

def calculate_age():
    # Get the full name and date of birth from the entry fields
    full_name = n_entry.get()
    dob_str = dob_entry.get()
    try:
        dob = datetime.strptime(dob_str, "%d/%m/%Y").date()
        today = date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        global msg
        msg = f"Hello {full_name}, you are {age} years old."
    except ValueError:
        msg = "Invalid date format. Please enter date as dd/mm/yyyy."
    text_box.insert(END, msg)

text_box = Text(window, height=5)
bt = Button(window, text="Click Me", command=calculate_age)

# Pack all elements into the window
lbl.pack()
n_lbl.pack()
n_entry.pack()
dob_lbl.pack()
dob_entry.pack()
bt.pack()
text_box.pack()

# Run the application
window.mainloop()
