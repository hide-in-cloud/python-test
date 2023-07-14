import time
from tkinter import *
from tkinter import ttk, messagebox
from 人力资源管理系统.数据库.mysql import Database


class SalaryReview(Frame):
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

        Label(frame1, text='您正在做的业务是：人力资源--薪酬标准管理--薪酬标准登记复核').pack()

        # 待复核的档案
        table_frame = Frame(self)
        table_frame.pack(pady=50)
        Label(table_frame, text='当前等待复核的薪酬标准总数:n例').pack()
        xscroll = Scrollbar(table_frame, orient=HORIZONTAL)  # 水平滚动条
        yscroll = Scrollbar(table_frame, orient=VERTICAL)  # 垂直滚动条
        columns = ['薪酬标准编号', '薪酬标准名称', '薪酬总额', '制定人', '登记人', '状态']
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
        Button(btn_frame, text='复核', command=self.reviewDetail).grid(row=0, column=0, padx=50)
        Button(btn_frame, text='返回', command=self.back).grid(row=0, column=1, padx=50)

        self.show_table()

    def show_table(self):
        # 清空历史记录
        items = self.table.get_children()
        # print(items)
        for item in items:
            self.table.delete(item)
        # 插入搜索结果
        items = self.db.search_reviewing_SalaryRegister()
        if items is not None:
            for item in items:
                self.table.insert('', END, values=item)

    def reviewDetail(self):
        # 获取选中行信息
        item = self.table.item(self.table.selection())['values']
        if item is not None:
            salaryStandardCode = item[0]

            self.top = Toplevel()
            self.top.title("人力资源管理系统")  # 设置窗口标题
            self.top.geometry("900x500")  # 设置窗口大小

            frame1 = Frame(self.top)
            frame1.pack()

            Label(frame1, text='您正在做的业务是：人力资源--薪酬标准管理--薪酬标准登记复核').pack()

            frame2 = Frame(self.top)
            frame2.pack(pady=40)

            # 薪酬标准编号
            Label(frame2, text='薪酬标准编号', bg="light green", relief=GROOVE, width=14).grid(row=0, column=0)
            self.salary_id = StringVar()
            self.entry_salary_id = Entry(frame2, state='readonly', width=19, textvariable=self.salary_id)
            self.salary_id.set(salaryStandardCode)
            self.entry_salary_id.grid(row=0, column=1, padx=1)

            # 薪酬标准名称
            Label(frame2, text='薪酬标准名称', bg="light green", relief=GROOVE, width=14).grid(row=0, column=2)
            self.salary_name = StringVar()
            self.entry_salary_name = Entry(frame2, width=19, textvariable=self.salary_name)
            self.entry_salary_name.grid(row=0, column=3, padx=1)

            # 薪酬总额
            Label(frame2, text='薪酬总额', bg="light green", relief=GROOVE, width=14).grid(row=0, column=4)
            self.total_salary = StringVar()
            self.entry_total_salary = Entry(frame2, state='readonly', width=19, textvariable=self.total_salary)
            self.entry_total_salary.grid(row=0, column=5, padx=1)

            # 制定人
            Label(frame2, text='制定人', bg="light green", relief=GROOVE, width=14).grid(row=1, column=0)
            self.employee_name = StringVar()
            self.entry_employee_name = Entry(frame2, width=19, textvariable=self.employee_name)
            self.entry_employee_name.grid(row=1, column=1, padx=1)

            # 复核人
            Label(frame2, text='复核人', bg="light green", relief=GROOVE, width=14).grid(row=1, column=2)
            self.reviewer = StringVar()
            self.entry_reviewer = Entry(frame2, width=19, textvariable=self.reviewer)
            self.reviewer.set(self.user)
            self.entry_reviewer.grid(row=1, column=3, padx=1)

            # 复核时间
            Label(frame2, text='复核时间', bg="light green", relief=GROOVE, width=14).grid(row=1, column=4)
            self.time = StringVar()
            self.entry_time = Entry(frame2, state='readonly', width=19, textvariable=self.time)
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self.time.set(current_time)
            self.entry_time.grid(row=1, column=5, padx=1)

            # 复核意见
            Label(frame2, text='复核意见', bg="light green", relief=GROOVE, width=14, height=3).grid(row=2, column=0)
            self.text_comments = Text(frame2, width=90, height=4)
            self.text_comments.grid(row=2, column=1, columnspan=5, padx=1)

            # 薪酬项目列表
            frame3 = Frame(self.top)
            frame3.pack()

            Label(frame3, text='序号', bg="light green", relief=GROOVE, width=30).grid(row=0, column=0)
            Label(frame3, text='1', bg="light green", relief=GROOVE, width=30).grid(row=1, column=0)
            Label(frame3, text='2', bg="light green", relief=GROOVE, width=30).grid(row=2, column=0)
            Label(frame3, text='3', bg="light green", relief=GROOVE, width=30).grid(row=3, column=0)
            Label(frame3, text='4', bg="light green", relief=GROOVE, width=30).grid(row=4, column=0)
            Label(frame3, text='5', bg="light green", relief=GROOVE, width=30).grid(row=5, column=0)
            Label(frame3, text='6', bg="light green", relief=GROOVE, width=30).grid(row=6, column=0)
            Label(frame3, text='7', bg="light green", relief=GROOVE, width=30).grid(row=7, column=0)
            Label(frame3, text='8', bg="light green", relief=GROOVE, width=30).grid(row=8, column=0)

            Label(frame3, text='薪酬项目名称', bg="light green", relief=GROOVE, width=30).grid(row=0, column=2)
            Label(frame3, text='基本工资', bg="light green", relief=GROOVE, width=30).grid(row=1, column=2)
            Label(frame3, text='交通补助', bg="light green", relief=GROOVE, width=30).grid(row=2, column=2)
            Label(frame3, text='午餐补助', bg="light green", relief=GROOVE, width=30).grid(row=3, column=2)
            Label(frame3, text='通信补助', bg="light green", relief=GROOVE, width=30).grid(row=4, column=2)
            Label(frame3, text='养老保险', bg="light green", relief=GROOVE, width=30).grid(row=5, column=2)
            Label(frame3, text='失业保险', bg="light green", relief=GROOVE, width=30).grid(row=6, column=2)
            Label(frame3, text='医疗保险', bg="light green", relief=GROOVE, width=30).grid(row=7, column=2)
            Label(frame3, text='住房公积金', bg="light green", relief=GROOVE, width=30).grid(row=8, column=2)

            Label(frame3, text='余额', bg="light green", relief=GROOVE, width=30).grid(row=0, column=3)
            # 基本工资
            self.basicSalary = StringVar(value=0)
            self.entry_basicSalary = Entry(frame3, width=30, textvariable=self.basicSalary)
            self.entry_basicSalary.bind("<Return>", self.enterActive)
            self.entry_basicSalary.grid(row=1, column=3)
            # 交通工资
            self.transportationSalary = StringVar(value=0)
            self.entry_transportationSalary = Entry(frame3, width=30, textvariable=self.transportationSalary)
            self.entry_transportationSalary.bind("<Return>", self.enterActive)
            self.entry_transportationSalary.grid(row=2, column=3)
            # 午餐补助
            self.lunchAllowance = StringVar(value=0)
            self.entry_lunchAllowance = Entry(frame3, width=30, textvariable=self.lunchAllowance)
            self.entry_lunchAllowance.bind("<Return>", self.enterActive)
            self.entry_lunchAllowance.grid(row=3, column=3)
            # 通信补助
            self.communicationSubsidy = StringVar(value=0)
            self.entry_communicationSubsidy = Entry(frame3, width=30, textvariable=self.communicationSubsidy)
            self.entry_communicationSubsidy.bind("<Return>", self.enterActive)
            self.entry_communicationSubsidy.grid(row=4, column=3)
            # 养老保险
            self.endowmentInsurance = StringVar()
            self.entry_endowmentInsurance = Entry(frame3, state='readonly', width=30, textvariable=self.endowmentInsurance)
            self.entry_endowmentInsurance.grid(row=5, column=3)
            # 失业保险
            self.unemploymentInsurance = StringVar()
            self.entry_unemploymentInsurance = Entry(frame3, state='readonly', width=30,
                                                     textvariable=self.unemploymentInsurance)
            self.entry_unemploymentInsurance.grid(row=6, column=3)
            # 医疗保险
            self.medicalInsurance = StringVar()
            self.entry_medicalInsurance = Entry(frame3, state='readonly', width=30, textvariable=self.medicalInsurance)
            self.entry_medicalInsurance.grid(row=7, column=3)
            # 住房公积金
            self.housingProvidentFund = StringVar()
            self.entry_housingProvidentFund = Entry(frame3, state='readonly', width=30,
                                                    textvariable=self.housingProvidentFund)
            self.entry_housingProvidentFund.grid(row=8, column=3)

            btn_frame = Frame(self.top)
            btn_frame.pack(pady=20)
            Button(btn_frame, text='复核通过', command=self.reviewPass).grid(row=0, column=0, padx=50)
            Button(btn_frame, text='不通过', command=self.reviewFail).grid(row=0, column=1, padx=50)

            self.set_data(salaryStandardCode)

    def set_data(self, salaryStandardCode):
        # 搜索详细信息
        data = self.db.select_SalaryRegister(salaryStandardCode)
        salaryStandardName = data[1]
        # employeeID = data[2]
        employeeName = data[3]
        # reviewer = data[4]
        # time = data[5]
        basicSalary = data[6]
        transportationSalary = data[7]
        lunchAllowance = data[8]
        communicationSubsidy = data[9]
        endowmentInsurance = data[10]
        unemploymentInsurance = data[11]
        medicalInsurance = data[12]
        housingProvidentFund = data[13]
        totalSalary = data[14]

        # 把数据输入到界面中
        self.salary_id.set(salaryStandardCode)
        self.salary_name.set(salaryStandardName)
        self.employee_name.set(employeeName)
        self.basicSalary.set(basicSalary)
        self.transportationSalary.set(transportationSalary)
        self.lunchAllowance.set(lunchAllowance)
        self.communicationSubsidy.set(communicationSubsidy)
        self.endowmentInsurance.set(endowmentInsurance)
        self.unemploymentInsurance.set(unemploymentInsurance)
        self.medicalInsurance.set(medicalInsurance)
        self.housingProvidentFund.set(housingProvidentFund)
        self.total_salary.set(totalSalary)

    def enterActive(self, *args):
        """回车事件"""
        if self.basicSalary.get() == '':
            self.basicSalary.set(0)
        self.endowmentInsurance.set(float(self.basicSalary.get()) * 0.08)
        self.unemploymentInsurance.set(float(self.basicSalary.get()) * 0.005)
        self.medicalInsurance.set(float(self.basicSalary.get()) * 0.02 + 3)
        self.housingProvidentFund.set(float(self.basicSalary.get()) * 0.08)
        if self.transportationSalary.get() == '':
            self.transportationSalary.set(0)
        if self.lunchAllowance.get() == '':
            self.lunchAllowance.set(0)
        if self.communicationSubsidy.get() == '':
            self.communicationSubsidy.set(0)
        self.total_salary.set(str(float(self.basicSalary.get()) + float(self.transportationSalary.get()) +
                                  float(self.lunchAllowance.get()) + float(self.communicationSubsidy.get()) +
                                  float(self.endowmentInsurance.get()) + float(self.unemploymentInsurance.get()) +
                                  float(self.medicalInsurance.get()) + float(self.housingProvidentFund.get()))
                              )

    def reviewPass(self):
        """复核后的薪酬单状态为'正常', 修改薪酬标准对应数据，在人力资源档案管理修改员工薪酬标准"""
        salaryStandardCode = self.salary_id.get()
        employeeName = self.employee_name.get()
        if (self.db.insert_SalaryReview(salaryStandardCode, employeeName, self.reviewer.get(),
                                        self.time.get(), self.text_comments.get(1.0, END))
                and self.db.update_state(table_name='SalaryRegister', primary_key_name='salaryStandardCode',
                                         primary_key_value=salaryStandardCode, state='正常')
                and self.db.update_salaryStandard(employeeName, float(self.total_salary.get()))):

            messagebox.showinfo('提示', "复核通过")
        else:
            messagebox.showinfo('提示', "复核失败")
        self.show_table()
        self.top.destroy()

    def reviewFail(self):
        """未通过的保持原样不变"""
        messagebox.showinfo('提示', "复核不通过")
        self.top.destroy()

    def back(self):
        self.destroy()
        self.parent.pack()


if __name__ == '__main__':
    root = Tk()
    root.title("人力资源管理系统")  # 设置窗口标题
    root.geometry("1002x560")  # 设置窗口大小
    app = SalaryReview(master=root, user='admin')
    app.pack()

    root.mainloop()
