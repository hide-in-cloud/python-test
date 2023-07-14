import time
from tkinter import *
from tkinter import ttk, messagebox
from 人力资源管理系统.数据库.mysql import Database


def str_plus_one(str_number, length):
    """字符串数字 + 1"""
    number = int(str_number)
    str_number = str(number + 1)
    while len(str_number) < length:
        str_number = '0' + str_number
    return str_number


class SalaryRegister(Frame):
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

        Label(frame1, text='您正在做的业务是：人力资源--薪酬标准管理--薪酬标准登记').pack()

        frame2 = Frame(self)
        frame2.pack(pady=50)

        # 薪酬标准编号
        Label(frame2, text='薪酬标准编号', bg="light green", relief=GROOVE, width=14).grid(row=0, column=0)
        self.salary_id = StringVar()
        self.entry_salary_id = Entry(frame2, state='readonly', width=19, textvariable=self.salary_id)
        # 设置编号
        codes = self.db.select_salaryStandardCode()
        if codes is None:
            code = '0001'
        else:
            code = str_plus_one(max(codes)[0], 4)
        self.salary_id.set(time.strftime("%Y%m", time.localtime()) + code)
        self.entry_salary_id.grid(row=0, column=1, padx=1)

        # 薪酬标准名称
        Label(frame2, text='薪酬标准名称', bg="light green", relief=GROOVE, width=14).grid(row=0, column=2)
        self.salaryName = StringVar()
        self.entry_salaryName = Entry(frame2, state='readonly', width=19, textvariable=self.salaryName)
        self.entry_salaryName.grid(row=0, column=3, padx=1)

        # 薪酬总额
        Label(frame2, text='薪酬总额', bg="light green", relief=GROOVE, width=14).grid(row=0, column=4)
        self.total_salary = StringVar()
        self.entry_total_salary = Entry(frame2, state='readonly', width=19, textvariable=self.total_salary)
        self.entry_total_salary.grid(row=0, column=5, padx=1)

        # 制定人
        Label(frame2, text='制定人', bg="light green", relief=GROOVE, width=14).grid(row=1, column=0)
        self.employeeName = StringVar()
        self.cbb_employeeName = ttk.Combobox(frame2, state='readonly', width=16, textvariable=self.employeeName)
        self.cbb_employeeName['values'] = self.db.select_employeeName()
        self.cbb_employeeName.bind('<<ComboboxSelected>>', self.employeeNameListener)
        self.cbb_employeeName.grid(row=1, column=1, padx=1)

        # 登记人
        Label(frame2, text='登记人', bg="light green", relief=GROOVE, width=14).grid(row=1, column=2)
        self.registrant = StringVar()
        self.entry_registrant = Entry(frame2, width=19, textvariable=self.registrant)
        self.registrant.set(self.user)
        self.entry_registrant.grid(row=1, column=3, padx=1)

        # 登记时间
        Label(frame2, text='登记时间', bg="light green", relief=GROOVE, width=14).grid(row=1, column=4)
        self.registration_time = StringVar()
        self.entry_registration_time = Entry(frame2, state='readonly', width=19, textvariable=self.registration_time)
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.registration_time.set(current_time)
        self.entry_registration_time.grid(row=1, column=5, padx=1)

        # 薪酬项目列表
        frame3 = Frame(self)
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

        btn_frame = Frame(self)
        btn_frame.pack(pady=30)
        Button(btn_frame, text='提交', command=self.register).grid(row=0, column=0, padx=50)
        Button(btn_frame, text='返回', command=self.back).grid(row=0, column=1, padx=50)

    def employeeNameListener(self, *args):
        """监听员工姓名"""
        self.salaryName.set(self.db.search_positionName(self.db.search_employeeID(self.employeeName.get())))

    def enterActive(self, *args):
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

    def register(self):
        """登记信息"""
        salaryName = self.salaryName.get()
        employeeName = self.employeeName.get()
        registrant = self.registrant.get()
        if salaryName == '' or employeeName == '' or registrant == '':
            messagebox.showinfo('提示', '请完善信息')
        else:
            if self.db.insert_SalaryRegister(self.salary_id.get(), salaryName, employeeName, registrant,
                                             float(self.basicSalary.get()), float(self.transportationSalary.get()),
                                             float(self.lunchAllowance.get()), float(self.communicationSubsidy.get())):
                messagebox.showinfo('提示', '登记成功')
                self.destroy()
                self.parent.pack()
            else:
                messagebox.showinfo('提示', '登记失败,可能已登记过')

    def back(self):
        self.destroy()
        self.parent.pack()


if __name__ == '__main__':
    root = Tk()
    root.title("人力资源管理系统")  # 设置窗口标题
    root.geometry("1002x560")  # 设置窗口大小
    app = SalaryRegister(master=root, user='admin')
    app.pack()

    root.mainloop()
