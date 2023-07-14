from tkinter import *
from 人力资源管理系统.登录模块.login_interface import Login


if __name__ == '__main__':
    root = Tk()
    root.title("人力资源管理系统")  # 设置窗口标题
    root.geometry("1002x580")  # 设置窗口大小
    login = Login(master=root)
    login.pack()

    root.mainloop()
