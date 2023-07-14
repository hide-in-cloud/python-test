from tkinter import *
from 人力资源管理系统.系统设置管理.setting_archive import SettingArchive
from 人力资源管理系统.系统设置管理.setting_salary import SettingSalary


class Setting(Frame):
    def __init__(self, master=None, parent=None, user=None):
        super().__init__(master=master)
        self.master = master
        self.parent = parent
        self.user = user
        self.createWidget()

    def createWidget(self):
        frame1 = Frame(self)
        frame1.grid()

        Label(frame1, text='您正在做的业务是：人力资源--系统设置').grid()

        frame2 = Frame(self)
        frame2.grid(pady=50)

        # 档案设置
        self.btn_archivesSetting = Button(frame2, text='档案管理设置', command=self.archivesActive, bg='light green',
                                          width=20, height=2)
        self.btn_archivesSetting.grid(pady=20)

        # 薪酬设置
        self.btn_salarySetting = Button(frame2, text='薪酬管理设置', command=self.salaryActive, bg='light green',
                                        width=20, height=2)
        self.btn_salarySetting.grid(pady=20)

        # 返回上一级
        self.btn_back = Button(frame2, text='返回', command=self.backActive, bg='light green',
                               width=20, height=2)
        self.btn_back.grid(pady=15)

    def archivesActive(self):
        self.pack_forget()
        app = SettingArchive(master=self.master, parent=self, user=self.user)
        app.pack()

    def salaryActive(self):
        self.pack_forget()
        app = SettingSalary(master=self.master, parent=self, user=self.user)
        app.pack()

    def backActive(self):
        self.destroy()
        self.parent.pack()


if __name__ == '__main__':
    root = Tk()
    root.title("人力资源管理系统")  # 设置窗口标题
    root.geometry("1002x560")  # 设置窗口大小
    setting = Setting(master=root)
    setting.pack()

    root.mainloop()
