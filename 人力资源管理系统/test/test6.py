from tkinter import Tk, Frame, Label, Entry, StringVar

class Fruitlist:
    def entryupdate(self, sv, i):
        print(sv, i, self.fruit[i], sv.get())

    def __init__(self, root):
        cf = Frame(root)
        cf.pack()
        self.string_vars = []
        self.fruit = ("Apple", "Banana", "Cherry", "Date")
        for f in self.fruit:
            i = len(self.string_vars)
            self.string_vars.append(StringVar())
            self.string_vars[i].trace("w", lambda name, index, mode, var=self.string_vars[i], i=i:
                              self.entryupdate(var, i))
            Label(cf, text=f).grid(column=2, row=i)
            Entry(cf, width=6, textvariable=self.string_vars[i]).grid(column=4, row=i)

root = Tk()
root.title("EntryUpdate")
root.geometry("300x200")
app = Fruitlist(root)
root.mainloop()