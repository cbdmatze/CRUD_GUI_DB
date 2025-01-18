from tkinter import *


window = Tk()
lbl = Label(window, text='Gender:')
var = StringVar()
male = Radiobutton(window, text='Male', variable=var, value='M')
female = Radiobutton(window, text='Female', variable=var, value='F')
lbl.pack()
male.pack()
female.pack()

window.mainloop()
