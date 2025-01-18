from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


def greetUser(event):
    username = inputBox.get()
    greet['text'] = 'Welcome' + username

    window = Tk()
    name = Label(window, text="Movie App", bg="grey", fg="Orange", font=("Sans", 38))
    img = Image.open("Coder's_heaven.png")
    logo = ImageTk.PhotoImage(img)
    image = Label(window, image=logo)

    frame = Frame(window)
    username = Label(frame, text="Username", font=("Sans", 12))
    inputBox = Entry(frame)
    button = Button(window, text="Go Ahead")
    button.bind("<Button-1>", greetUser)
    greet = Label(window)

    name.pack()
    image.pack()
    frame.pack()
    username.pack(side=LEFT)
    inputBox.pack(side=RIGHT)
    button.pack()
    greet.pack()

    window.mainloop()
