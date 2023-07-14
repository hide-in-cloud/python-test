from tkinter import *

root = Tk()
root.geometry("300x200")
sv1 = StringVar()
sv2 = StringVar()


def callback_1():
    print(sv1.get())
    return True


def callback_2():
    print(sv2.get())
    return True


Label(root, text='label1').grid(column=0, row=0)
e = Entry(root, textvariable=sv1, validate="focusout", validatecommand=callback_1)
e.grid(column=1, row=0)
Label(root, text='label2').grid(column=0, row=1)
e = Entry(root, textvariable=sv2, validate="focusout", validatecommand=callback_2)
e.grid(column=1, row=1)
root.mainloop()
