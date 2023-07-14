from tkinter import *
from tkinter import ttk
from 人力资源管理系统.数据库.mysql import Database


class SalarySearch(Frame):
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

        Label(frame1, text='您正在做的业务是：人力资源--薪酬标准管理--薪酬标准查询').grid()

        frame2 = Frame(self)
        frame2.pack()

        # 薪酬标准编号
        Label(frame2, text="请输入薪酬标准编号", bg="light green", relief=GROOVE, width=16).grid(row=0, column=0)
        self.salaryCode = StringVar()
        self.entry_salaryCode = Entry(frame2, width=42, textvariable=self.salaryCode)
        self.entry_salaryCode.grid(row=0, column=1, columnspan=3, padx=1)

        # 关键字(薪酬标准名称、制定人、变更人和复核人字段)
        Label(frame2, text="请输入关键字", bg="light green", relief=GROOVE, width=16).grid(row=1, column=0)
        self.keyword = StringVar()
        self.entry_keyword = Entry(frame2, width=42, textvariable=self.keyword)
        self.entry_keyword.grid(row=1, column=1, columnspan=3, padx=1)

        # 登记时间
        Label(frame2, text="请输入登记时间", bg="light green", relief=GROOVE, width=16).grid(row=2, column=0)
        self.formerTime = StringVar()
        self.entry_formerTime = Entry(frame2, width=19, textvariable=self.formerTime)
        self.entry_formerTime.grid(row=2, column=1, padx=1)
        Label(frame2, text='至').grid(row=2, column=2)
        self.latterTime = StringVar()
        self.entry_latterTime = Entry(frame2, width=19, textvariable=self.latterTime)
        self.entry_latterTime.grid(row=2, column=3, padx=1)
        Label(frame2, text='(YYYY.MM.DD)').grid(row=2, column=4)

        # 查询
        btn_quit = Button(frame2, text="查询", command=self.searchActive, activeforeground="white", bg='light green',
                          activebackground="red")
        btn_quit.grid(row=6, column=1, padx=30, pady=15)

        # 返回上一级
        Button(frame2, text='返回', command=self.backActive).grid(row=6, column=3, pady=15)

        # 查询结果
        table_frame = Frame(self)
        table_frame.pack()
        xscroll = Scrollbar(table_frame, orient=HORIZONTAL)  # 水平滚动条
        yscroll = Scrollbar(table_frame, orient=VERTICAL)  # 垂直滚动条
        columns = ['薪酬标准编号', '薪酬标准名称', '制定人', '登记人', '登记时间','基本工资', '交通补助', '午餐补助',
                   '通信补助', '养老保险', '失业保险', '医疗保险', '住房公积金', '薪酬总额', '状态']
        self.table = ttk.Treeview(table_frame, columns=columns, height=12, show='headings',
                                  xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
        for column in columns:
            self.table.heading(column=column, text=column, anchor=CENTER)  # 定义表头.column:列标识符;text:列名
            self.table.column(column=column, width=100, minwidth=100, anchor=CENTER)  # 定义列.anchor:对齐方式
        xscroll.config(command=self.table.xview)  # 水平滚动条绑定table的x轴事件
        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.config(command=self.table.yview)  # 垂直滚动条绑定table的y轴事件
        yscroll.pack(side=RIGHT, fill=Y)
        self.table.pack(fill=BOTH, expand=True)  # 放置table，必须写在放置水平和垂直滚动条之后

        btn_frame = Frame(self)
        btn_frame.pack()
        Button(btn_frame, text='更改', command=self.modify).grid(row=0, column=0, pady=20)

    def searchActive(self):
        """在数据库中查找对应的数据"""
        # 清空历史记录
        items = self.table.get_children()
        for item in items:
            self.table.delete(item)

        # 模糊查询
        info = self.db.search_salary_keyword(self.salaryCode.get(), self.keyword.get(), self.formerTime.get(),
                                             self.latterTime.get())
        if info is not None:
            for index, data in enumerate(info):
                self.table.insert('', END, values=data)

    def backActive(self):
        self.destroy()
        self.parent.pack()

    def modify(self):
        """同时修改数据库中的信息"""
        pass


if __name__ == '__main__':
    root = Tk()
    root.title("人力资源管理系统")  # 设置窗口标题
    root.geometry("1002x560")  # 设置窗口大小
    app = SalarySearch(master=root)
    app.pack()

    root.mainloop()
