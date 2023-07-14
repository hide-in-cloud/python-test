from tkinter import *
from 人力资源管理系统.人资档案管理.archive_register import ArchiveRegister


class MyMenu:
    def __init__(self, master=None, parent=None):
        self.master = master
        self.parent = parent
        self.createWidget()

    def createWidget(self):
        self.menubar = Menu(self.master)

        self.systemMenu = Menu(self.menubar, tearoff=False)
        self.systemMenu.add_command(label='档案设置', command=self.add_setting)
        self.systemMenu.add_command(label='薪酬设置', command=self.add_setting)
        self.menubar.add_cascade(label='系统设置', menu=self.systemMenu)

        self.archiveMenu = Menu(self.menubar, tearoff=False)
        self.archiveMenu.add_command(label='档案登记', command=self.archive_register)
        self.archiveMenu.add_command(label='档案变更', command=self.add_setting)
        self.archiveMenu.add_command(label='档案查询', command=self.add_setting)
        self.archiveMenu.add_command(label='档案复核', command=self.add_setting)
        self.menubar.add_cascade(label='档案管理', menu=self.archiveMenu)

        self.salaryMenu = Menu(self.menubar, tearoff=False)
        self.salaryMenu.add_command(label='薪酬登记', command=self.add_setting)
        self.salaryMenu.add_command(label='薪酬查询', command=self.add_setting)
        self.salaryMenu.add_command(label='薪酬复核', command=self.add_setting)
        self.menubar.add_cascade(label='薪酬标准管理', menu=self.salaryMenu)

        self.payrollMenu = Menu(self.menubar, tearoff=False)
        self.payrollMenu.add_command(label='发放登记', command=self.add_setting)
        self.payrollMenu.add_command(label='发放复核', command=self.add_setting)
        self.menubar.add_cascade(label='薪酬发放管理', menu=self.payrollMenu)

        self.master.config(menu=self.menubar)

    def add_setting(self):
        pass

    def archive_register(self):
        app = ArchiveRegister(master=self.master)
        app.pack()


if __name__ == '__main__':
    root = Tk()
    root.title("人力资源管理系统")  # 设置窗口标题
    root.geometry("1002x560")  # 设置窗口大小
    app = MyMenu(master=root)

    root.mainloop()
