
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from 人力资源管理系统.数据库.mysql import Database
from 人力资源管理系统.house_interface import House


class Login(Frame):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.master = master
        self.username = StringVar()
        self.password = StringVar()
        self.identity = StringVar()
        self.db = Database(database='human_resources')

        self.createWidget()

    def createWidget(self):
        frame1 = Frame(self)
        frame1.grid(pady=10)

        Label(frame1, text='身份').grid(row=0, column=0)
        identities = ('人事专员')
        self.cbb_identity = ttk.Combobox(frame1, state='readonly', textvariable=self.identity, values=identities, width=18)
        self.cbb_identity.grid(row=0, column=1)
        self.cbb_identity.current(0)
        self.cbb_identity.bind('<<ComboboxSelected>>', self.selectorListener)

        frame2 = Frame(self)
        frame2.grid(pady=10)

        Label(frame2, text='账号').grid(row=0, column=0)
        entry_user = Entry(frame2, textvariable=self.username)
        entry_user.grid(row=0, column=1)

        frame3 = Frame(self)
        frame3.grid(pady=10)

        Label(frame3, text='密码').grid(row=0, column=0)
        entry_pwd = Entry(frame3, show='*', textvariable=self.password)
        entry_pwd.grid(row=0, column=1)

        Button(self, text='登录', command=self.loginActive).grid()

    def loginActive(self):
        user = self.username.get()
        pwd = self.password.get()
        if len(user) == 0 or len(pwd) == 0:
            messagebox.showinfo('提示:', '请输入完整信息!')
            return

        if self.db.login(user, pwd):
            self.pack_forget()
            # self.db.close()
            self.house = House(master=self.master, parent=self, user=user)
            self.house.pack()
        else:
            messagebox.showinfo('提示：', '用户名或密码不正确!')

    def selectorListener(self, *args):
        print(self.identity.get())

        
if __name__ == '__main__':
    root = Tk()
    root.title("人力资源管理系统")  # 设置窗口标题
    root.geometry("1002x580")  # 设置窗口大小
    login = Login(master=root)
    login.pack()

    root.mainloop()
