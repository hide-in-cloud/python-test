import time
from tkinter import *
from tkinter import ttk, messagebox
from 人力资源管理系统.数据库.mysql import Database


class PayrollReview(Frame):
    def __init__(self, master=None, parent=None, user=None):
        super().__init__(master=master)
        self.master = master
        self.parent = parent
        self.user = user
        self.db = Database(database='human_resources')
        self.createWidget()

    def createWidget(self):
        frame1 = Frame(self)
        frame1.pack()

        Label(frame1, text='您正在做的业务是：人力资源--薪酬发放管理--薪酬发放复核').pack()

        # 待复核的薪酬发放单
        length = 0
        items = self.db.search_reviewing_PayrollRegister()
        if items is not None:
            length = len(items)
        # 建立列表
        table_frame = Frame(self)
        table_frame.pack(pady=30)
        Label(table_frame, text='当前等待复核的薪酬发放单总数: %d 例' % length).pack()
        xscroll = Scrollbar(table_frame, orient=HORIZONTAL)  # 水平滚动条
        yscroll = Scrollbar(table_frame, orient=VERTICAL)  # 垂直滚动条
        columns = ['薪酬发放单编号', 'I级机构', 'II级机构', 'III级机构', '人数', '基本薪酬总额']
        self.table = ttk.Treeview(table_frame, columns=columns, height=15, show='headings',
                                  xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
        for column in columns:
            self.table.heading(column=column, text=column, anchor=CENTER)  # 定义表头
            self.table.column(column=column, width=100, minwidth=100, anchor=CENTER)  # 定义列
        xscroll.config(command=self.table.xview)
        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.config(command=self.table.yview)  # 垂直滚动条绑定table的y轴事件
        yscroll.pack(side=RIGHT, fill=Y)
        self.table.pack(fill=BOTH, expand=True)  # 放置table，必须写在放置水平和垂直滚动条之后

        btn_frame = Frame(self)
        btn_frame.pack()
        Button(btn_frame, text='复核', command=self.review).grid(row=0, column=0, padx=50)
        Button(btn_frame, text='返回', command=self.back).grid(row=0, column=1, padx=50)

        self.show_table(items)

    def show_table(self, items):
        """查看state为'待复核'的薪酬单"""
        # 清空历史记录
        children = self.table.get_children()
        for child in children:
            self.table.delete(child)
        # 插入搜索结果
        if items is not None:
            for item in items:
                self.table.insert('', END, values=item)

    def review(self):
        # 获取选中行信息
        item = self.table.item(self.table.focus())['values']
        if item is not None:
            """薪酬单明细"""
            self.top = Toplevel()
            self.top.title("人力资源管理系统")  # 设置窗口标题
            self.top.geometry("1000x560+160+160")  # 设置窗口大小

            frame1 = Frame(self.top)
            frame1.pack()

            Label(frame1, text='您正在做的业务是：人力资源--薪酬发放管理--薪酬发放单复核').pack(side=LEFT)

            frame2 = Frame(self.top)
            frame2.pack(pady=20)

            Label(frame2, text='薪酬发放单编号:').grid(row=0, column=0)
            self.payrollCode = StringVar()
            self.label_payrollCode = Label(frame2, textvariable=self.payrollCode)
            self.label_payrollCode.grid(row=0, column=1)

            Label(frame2, text='机构:').grid(row=0, column=2)
            self.organization = StringVar()
            self.label_organization = Label(frame2, textvariable=self.organization)
            self.label_organization.grid(row=0, column=3)

            Label(frame2, text='总人数:').grid(row=1, column=0)
            self.totalNumber = StringVar()
            self.label_totalNumber = Label(frame2, textvariable=self.totalNumber)
            self.label_totalNumber.grid(row=1, column=1)

            Label(frame2, text='基本薪酬总额:').grid(row=1, column=2)
            self.payroll = StringVar()
            self.label_payroll = Label(frame2, textvariable=self.payroll)
            self.label_payroll.grid(row=1, column=3)

            Label(frame2, text='实发总额:').grid(row=1, column=4)
            self.actualPayroll = StringVar()
            self.label_actualPayroll = Label(frame2, textvariable=self.actualPayroll)
            self.label_actualPayroll.grid(row=1, column=5)

            Label(frame2, text='复核人:').grid(row=2, column=0)
            self.reviewer = StringVar()
            self.entry_reviewer = Entry(frame2, textvariable=self.reviewer)
            self.reviewer.set(self.user)
            self.entry_reviewer.grid(row=2, column=1)

            Label(frame2, text='复核时间: ').grid(row=2, column=2)
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self.reviewTime = StringVar(value=current_time)
            self.label_reviewTime = Label(frame2, textvariable=self.reviewTime)
            self.label_reviewTime.grid(row=2, column=3)

            # 待复核的薪酬单
            table_frame = Frame(self.top)
            table_frame.pack()
            xscroll = Scrollbar(table_frame, orient=HORIZONTAL)  # 水平滚动条
            yscroll = Scrollbar(table_frame, orient=VERTICAL)  # 垂直滚动条
            columns = ['档案编号', '姓名', '基本工资', '交通补助', '午餐补助', '通信补助', '养老保险', '失业保险',
                       '医疗保险', '住房公积金', '奖励奖金', '应扣奖金']
            self.table_payroll = ttk.Treeview(table_frame, columns=columns, height=15, show='headings',
                                              xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
            for column in columns:
                self.table_payroll.heading(column=column, text=column, anchor=CENTER)  # 定义表头
                self.table_payroll.column(column=column, width=100, minwidth=80, anchor=CENTER)  # 定义列
            xscroll.config(command=self.table_payroll.xview)
            xscroll.pack(side=BOTTOM, fill=X)
            yscroll.config(command=self.table_payroll.yview)  # 垂直滚动条绑定table的y轴事件
            yscroll.pack(side=RIGHT, fill=Y)
            self.table_payroll.pack(fill=BOTH, expand=True)  # 放置table，必须写在放置水平和垂直滚动条之后
            btn_frame = Frame(self.top)
            btn_frame.pack()
            Button(btn_frame, text='修改奖金', command=self.modify_bonus).grid(row=0, column=0, padx=50, pady=20)
            Button(btn_frame, text='复核通过', command=self.reviewPass).grid(row=0, column=1, padx=50, pady=20)

            self.set_data(item[0])
            self.show_payrollDetail(item[0], item[3])

    def set_data(self, payrollCode):
        # 搜索薪酬发放登记表信息
        data = self.db.select_PayrollRegister(payrollCode)
        payrollCode = data[0]
        primaryOrganization = data[1]
        secondaryOrganization = data[2]
        tertiaryOrganization = data[3]
        totalNumber = data[4]
        payroll = data[5]
        actualPayroll = data[6]

        # 搜索薪酬发放单对应员工信息
        # data = self.db.select_SalaryRegister(salaryStandardCode)
        self.payrollCode.set(payrollCode)
        self.organization.set(primaryOrganization + '/' + secondaryOrganization + '/' + tertiaryOrganization)
        self.totalNumber.set(totalNumber)
        self.payroll.set(payroll)
        self.actualPayroll.set(actualPayroll)

    def show_payrollDetail(self, payrollCode, tertiaryOrganization):
        # 清空历史记录
        items = self.table_payroll.get_children()
        for item in items:
            self.table_payroll.delete(item)
        # 搜索薪酬发放单对应员工信息
        items = self.db.search_terOrg_salaryDetail(tertiaryOrganization)
        if items is not None:
            for item in items:
                bonus = self.db.search_bonus_deductedBonus(payrollCode, item[0])
                item = item + bonus
                self.table_payroll.insert('', END, values=item)

    def modify_bonus(self):
        self.top2 = Toplevel()
        self.top2.title("人力资源管理系统")  # 设置窗口标题
        self.top2.geometry("300x200+400+300")  # 设置窗口大小

        frame1 = Frame(self.top2)
        frame1.pack(pady=30)

        Label(frame1, text='奖励奖金:').grid(row=0, column=0)
        self.bonus = StringVar()
        self.entry_bonus = Entry(frame1, textvariable=self.bonus)
        self.entry_bonus.grid(row=0, column=1)
        Label(frame1, text='应扣奖金:').grid(row=1, column=0)
        self.deductedBonus = StringVar()
        self.entry_deductedBonus = Entry(frame1, textvariable=self.deductedBonus)
        self.entry_deductedBonus.grid(row=1, column=1)

        frame2 = Frame(self.top2)
        frame2.pack()
        Button(frame2, text='修改', command=self.modify_commit).grid()

    def modify_commit(self):
        self.table_payroll.set(item=self.table_payroll.focus(), column='奖励奖金', value=self.bonus.get())
        self.table_payroll.set(item=self.table_payroll.focus(), column='应扣奖金', value=self.deductedBonus.get())
        # 修改实发薪酬
        bonus = 0
        deductedBonus = 0
        for item in self.table_payroll.get_children():
            bonus = bonus + float(self.table_payroll.item(item, option='values')[-2])
            deductedBonus = deductedBonus + float(self.table_payroll.item(item, option='values')[-1])
        self.actualPayroll.set(float(self.payroll.get()) + bonus - deductedBonus)

        self.top2.destroy()

    def reviewPass(self):
        payrollCode = self.payrollCode.get()
        actualPayroll = float(self.actualPayroll.get())
        reviewer = self.reviewer.get()
        reviewTime = self.reviewTime.get()

        if (self.db.insert_PayrollReview(payrollCode, actualPayroll, reviewer, reviewTime)
                and self.db.update_actualSalary(payrollCode, actualPayroll)):
            if self.db.update_state('payrollRegister', 'payrollCode', payrollCode, '执行'):
                for item in self.table_payroll.get_children():
                    employeeID = self.table_payroll.item(item, option='values')[0]
                    bonus = float(self.table_payroll.item(item, option='values')[-2])
                    deductedBonus = float(self.table_payroll.item(item, option='values')[-1])
                    totalSalary = float(self.db.search_totalSalary(employeeID))
                    actualSalary = totalSalary + bonus - deductedBonus
                    if not self.db.update_bonus_deductedBonus(payrollCode, employeeID, bonus, deductedBonus,
                                                              actualSalary):
                        messagebox.showinfo('提示', '提交失败')
                messagebox.showinfo('提示', '提交成功')
                self.top.destroy()
                self.show_table(items=self.db.search_reviewing_PayrollRegister())
        else:
            messagebox.showinfo('提示', '提交失败')

    def back(self):
        self.db.close()
        self.destroy()
        self.parent.pack()


if __name__ == '__main__':
    root = Tk()
    root.title("人力资源管理系统")  # 设置窗口标题
    root.geometry("1002x560")  # 设置窗口大小
    app = PayrollReview(master=root, user='admin')
    app.pack()

    root.mainloop()
