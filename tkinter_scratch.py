from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


def gui():
    window = Tk()
    name = Label(window, text='Movie App', bg='grey', fg='Orange', font=('Sans', 38))
    img = Image.open("coder's_heaven.png")
    logo = ImageTk.PhotoImage(img)
    image = Label(window, image=logo)

    frame = Frame(window)
    username = Label(frame, text='Username', font=('Sans', 12))
    inputBox = Entry(frame)
    button = Button(window, text="Let's Go Ahead", command=showMessage)

    name.pack()
    image.pack()
    frame.pack()
    username.pack(side=LEFT)
    inputBox.pack(side=RIGHT)
    button.pack(side=BOTTOM)

    window.mainloop()


def showMessage():
    messagebox.showinfo('Movie App - All in one Place', 'Welcome')


if __name__ == "__main__":
    gui()
