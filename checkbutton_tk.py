from tkinter import *


window = Tk()
lbl = Label(window, text='Choose what you want to do:')
frame = Frame(window)
movies = Checkbutton(frame, text='Movies')
books = Checkbutton(frame, text='Books')
music = Checkbutton(frame, text='Music')

lbl.pack()
frame.pack()
movies.pack()
books.pack()
music.pack()

window.mainloop()
