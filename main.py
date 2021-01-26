from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

my_label = Label(text="I am a label", font=("Ariel", 24, "bold"))
my_label.grid(column=0, row=0)

my_label.config(text="New Text")

def button_clicked():
    change_label = input.get()
    my_label.config(text=change_label)


button = Button(text="Click Me", command=lambda: button_clicked())
button.grid(column=1, row=1)

button2 = Button(text="Button2")
button2.grid(column=2, row=0)

input = Entry(width=10)
input.grid(column=3, row=2)




window.mainloop()