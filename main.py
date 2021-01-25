from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

my_label = Label(text="I am a label", font=("Ariel", 24, "bold"))
my_label.pack()

my_label.config(text="New Text")

def button_clicked():
    print("hello")
    # my_label.config(text="I got clicked")


button = Button(text="Click Me", command=lambda: button_clicked())
button.pack()


window.mainloop()