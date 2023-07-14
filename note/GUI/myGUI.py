from tkinter import *
from tkinter import ttk

root = Tk()  # 初始化Tk()

root.title("人力资源管理系统")  # 设置窗口标题
root.geometry("1000x600")  # 设置窗口大小(注：是x)
root.resizable(width=True, height=True)  # 设置窗口的长宽是否可以变化
root.tk.eval('package require Tix')  # 引入升级包，这样才能使用升级的组合控件

frame2 = Frame(root)
frame2.grid(row=0)

label_register = Label(frame2, text='您正在做的业务是：人力资源--人力资源档案管理--人力资源档案登记')
label_register.grid(row=1)

frame3 = Frame(root)
frame3.grid(row=2)

btn_quit = Button(frame3, text="退出", command=root.quit, activeforeground="white", activebackground="red")
btn_quit.grid(row=2, column=2)
btn_reset = Button(frame3, text="清除", activeforeground="white", activebackground="red")
btn_reset.grid(row=2, padx=5)

frame1 = Frame(root)
frame1.grid(row=3)  # 铺满X轴

label1 = Label(frame1, text='姓名', bg="light green", relief=GROOVE, width=14)
label1.grid(row=0, column=0)
Entry1 = Entry(frame1)
Entry1.grid(row=0, column=1, padx=1)

label_gender = Label(frame1, text="性别", bg="light green", relief=GROOVE, width=12)
label_gender.grid(row=0, column=2)
value = StringVar()
genders = [0,1,2,3]
cbb_gender = ttk.Combobox(frame1, state='readonly', textvariable=value, values=genders, width=18)
cbb_gender.grid(row=0, column=3, padx=1)

label3 = Label(frame1, text='EMAIL', bg="light green", relief=GROOVE, width=14)
label3.grid(row=0, column=4)
Entry3 = Entry(frame1)
Entry3.grid(row=0, column=5, padx=1)

label2 = Label(frame1, text='您的性别:')
label2.grid(row=1, column=0)
sex = StringVar()
sex_male = Radiobutton(frame1, text='男', fg='blue', variable=sex, value='男')
sex_male.grid(row=1, column=1)
sex_female = Radiobutton(frame1, text='女', fg='red', variable=sex, value='女')
sex_female.grid(row=1, column=2)


def check():
    print(Entry1.get())
    print(type(value.get()))


Button(frame1, text='查看', command=check).grid(row=2, column=0)

root.mainloop()
