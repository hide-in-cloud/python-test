from tkinter import *
from 人力资源管理系统.系统设置管理.setting_menu import Setting
from 人力资源管理系统.人资档案管理.archive_menu import ArchiveMenu
from 人力资源管理系统.薪酬标准管理.salary_menu import SalaryMenu
from 人力资源管理系统.薪酬发放管理.payroll_menu import PayrollMenu
# from 人力资源管理系统.login_interface import Login
# from 人力资源管理系统.test3 import MyMenu


class House(Frame):
    def __init__(self, master=None, parent=None, user=None):
        super().__init__(master=master)
        self.master = master
        self.parent = parent
        self.user = user
        # MyMenu(master=self.master)
        self.createWidget()

    def createWidget(self):
        frame1 = Frame(self)
        frame1.grid()

        Label(frame1, text='您正在做的业务是：人力资源').grid()

        frame2 = Frame(self)
        frame2.grid(pady=50)

        # 系统设置
        self.btn_setting = Button(frame2, text='系统设置', command=self.settingActive, bg='light green',
                                  width=20, height=2)
        self.btn_setting.grid(pady=20)

        # 档案管理
        self.btn_archives = Button(frame2, text='人力资源档案管理', command=self.archivesActive, bg='light green',
                                   width=20, height=2)
        self.btn_archives.grid(pady=20)

        # 薪酬标准
        self.btn_salaryStandard = Button(frame2, text='薪酬标准管理', command=self.salaryActive, bg='light green',
                                         width=20, height=2)
        self.btn_salaryStandard.grid(pady=20)

        # 薪酬发放
        self.btn_payroll = Button(frame2, text='薪酬发放管理', command=self.payrollActive, bg='light green',
                                  width=20, height=2)
        self.btn_payroll.grid(pady=20)

        # 注销
        self.btn_logout = Button(frame2, text='注销', command=self.logoutActive, bg='light green',
                                 width=20, height=2)
        self.btn_logout.grid(pady=15)

    def settingActive(self):
        self.pack_forget()
        app = Setting(master=self.master, parent=self, user=self.user)
        app.pack()

    def archivesActive(self):
        self.pack_forget()
        app = ArchiveMenu(master=self.master, parent=self, user=self.user)
        app.pack()

    def salaryActive(self):
        self.pack_forget()
        app = SalaryMenu(master=self.master, parent=self, user=self.user)
        app.pack()

    def payrollActive(self):
        self.pack_forget()
        app = PayrollMenu(master=self.master, parent=self, user=self.user)
        app.pack()

    def logoutActive(self):
        """注销"""
        self.destroy()
        # self.login = Login(master=self.master)
        # self.login.pack()
        self.parent.pack()


if __name__ == '__main__':
    root = Tk()
    root.title("人力资源管理系统")  # 设置窗口标题
    root.geometry("1002x580")  # 设置窗口大小
    house = House(master=root)
    house.pack()

    root.mainloop()
