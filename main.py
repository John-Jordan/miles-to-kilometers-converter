from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=260, height=100)

label1 = Label(text="Miles")
label1.grid(column=2, row=0)

label2 = Label(text="is equal to: ")
label2.grid(column=0, row=1)

label3 = Label(text="Km")
label3.grid(column=2, row=1)

label4 = Label(text="0")
label4.grid(column=1, row=1)



def button_clicked():
    change_label = int(input.get())*2.2
    label4.config(text=change_label)


button = Button(text="Calculate", command=lambda: button_clicked())
button.grid(column=1, row=2)

input = Entry(width=10)
input.grid(column=1, row=0)




window.mainloop()