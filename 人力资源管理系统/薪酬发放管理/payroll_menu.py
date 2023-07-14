from tkinter import *
from 人力资源管理系统.薪酬发放管理.payroll_register import PayrollRegister
from 人力资源管理系统.薪酬发放管理.payroll_review import PayrollReview


class PayrollMenu(Frame):
    def __init__(self, master=None, parent=None, user=None):
        super().__init__(master=master)
        self.master = master
        self.parent = parent
        self.user = user
        # self.pack()
        self.createWidget()

    def createWidget(self):
        frame1 = Frame(self)
        frame1.grid()

        Label(frame1, text='您正在做的业务是：人力资源--薪酬发放管理').grid()

        frame2 = Frame(self)
        frame2.grid(pady=25)

        # 档案登记
        self.btn_register = Button(frame2, text='发放登记', command=self.registerActive, bg='light green',
                                   width=20, height=2)
        self.btn_register.grid(pady=15)

        # 档案复核
        self.btn_review = Button(frame2, text='发放复核', command=self.reviewActive, bg='light green',
                                 width=20, height=2)
        self.btn_review.grid(pady=15)

        # 返回上一级
        self.btn_back = Button(frame2, text='返回', command=self.backActive, bg='light green',
                               width=20, height=2)
        self.btn_back.grid(pady=15)

    def registerActive(self):
        self.pack_forget()
        register = PayrollRegister(master=self.master, parent=self, user=self.user)
        register.pack()

    def reviewActive(self):
        self.pack_forget()
        review = PayrollReview(master=self.master, parent=self, user=self.user)
        review.pack()

    def backActive(self):
        self.destroy()
        self.parent.pack()


if __name__ == '__main__':
    root = Tk()
    root.title("人力资源管理系统")  # 设置窗口标题
    root.geometry("1002x560")  # 设置窗口大小
    app = PayrollMenu(master=root, user='admin')
    app.pack()

    root.mainloop()
