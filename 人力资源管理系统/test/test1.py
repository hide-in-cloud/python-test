from tkinter import *
from tkinter import ttk
from 人力资源管理系统.数据库.mysql import Database
from 人力资源管理系统.utils.utils import str_plus_one


class Application(Frame):
    def __init__(self, master=None, parent=None, user=None):
        super().__init__(master=master)
        self.master = master
        self.parent = parent
        self.user = user
        self.db = Database(database='human_resources')
        self.createWidget()

    def createWidget(self):
        # frame1 = Frame(self)
        # frame1.pack()
        # Label(frame1).pack()
        # Button(frame1, text='btn').pack()
        # ttk.Label(frame1).pack()
        # ttk.Button(frame1, text='qwer').pack()

        tree_frame = Frame(self)
        tree_frame.pack(pady=50)
        yscroll = Scrollbar(tree_frame, orient=VERTICAL)
        columns = ['名称']
        self.tree = ttk.Treeview(tree_frame, columns=columns, height=15, yscrollcommand=yscroll.set)
        for column in columns:
            self.tree.heading(column=column, text=column, anchor=CENTER)
            self.tree.column(column=column, width=100, minwidth=100, anchor=CENTER)
        yscroll.config(command=self.tree.yview)
        yscroll.pack(side=RIGHT, fill=Y)
        self.tree.pack(fill=BOTH)
        self.show_tree()

        button_frame = Frame(self)
        button_frame.pack()
        Button(button_frame, text='添加一级机构', command=self.add_primaryOrganization).grid(row=0, column=0, padx=50)
        Button(button_frame, text='添加二级机构', command=self.add_secondaryOrganization).grid(row=0, column=1, padx=50)
        Button(button_frame, text='添加三级机构').grid(row=0, column=2, padx=50)
        Button(button_frame, text='返回').grid(row=0, column=3, padx=50)

    def show_tree(self):
        # 一级机构
        primes = self.db.select_primaryOrganization_all()
        for prime in primes:
            code = prime[0]
            name = prime[1]
            text = '一级机构' + code
            self.tree.insert('', END, iid=text, text=text, values=name)

        # 二级机构
        seconds = self.db.select_secondaryOrganization_all()
        for second in seconds:
            code = second[0]
            parent_code = second[1]
            parent = '一级机构' + parent_code
            name = second[2]
            text = '二级机构' + code
            self.tree.insert(parent, END, iid=text, text=text, values=name)

        # 三级机构
        thirds = self.db.select_tertiaryOrganization_all()
        for third in thirds:
            code = third[0]
            parent_code = third[1]
            parent = '二级机构' + parent_code
            name = third[2]
            text = '三级机构' + code
            self.tree.insert(parent, END, iid=text, text=text, values=name)

        # prim = self.tree.insert('', 0, iid='一级机构1', text='一级机构1', values='1')
        # second_a = self.tree.insert(prim, 0, iid='二级机构1', text='二级机构1', values=('2-1'))
        # second_b = self.tree.insert(prim, 1, iid='二级机构2', text='二级机构2', values=('2-2'))
        # second_c = self.tree.insert(prim, 2, iid='二级机构3', text='二级机构3', values=('2-3'))
        # third_a = self.tree.insert(second_a, 0, iid='三级机构1', text='三级机构1', values=('3-a-1'))
        # third_b = self.tree.insert(second_a, 1, iid='三级机构2', text='三级机构2', values=('3-a-2'))
        # third_c = self.tree.insert(second_a, 2, iid='三级机构3', text='三级机构3', values=('3-a-3'))
        # third_d = self.tree.insert(second_b, 0, iid='三级机构4', text='三级机构4', values=('3-b-4'))
        # third_e = self.tree.insert(second_b, 1, iid='三级机构5', text='三级机构5', values=('3-b-5'))
        # third_f = self.tree.insert(second_b, 2, iid='三级机构6', text='三级机构6', values=('3-b-6'))
        # third_g = self.tree.insert(second_c, 0, iid='三级机构7', text='三级机构7', values=('3-c-7'))
        # third_h = self.tree.insert(second_c, 1, iid='三级机构8', text='三级机构8', values=('3-c-8'))

    def add_primaryOrganization(self):
        top = Toplevel()
        screenwidth = top.winfo_screenwidth()
        screenheight = top.winfo_screenheight()
        width = 350
        height = 250
        x = (screenwidth - width) // 2
        y = (screenheight - height) // 2
        top.title("添加一级机构")
        top.geometry("{}x{}+{}+{}".format(width, height, x, y))

        frame1 = Frame(top)
        frame1.pack(pady=30)
        Label(frame1, text='一级机构名称：').grid(row=0, column=0)
        self.primeName = StringVar()
        self.entry_prime = Entry(frame1, textvariable=self.primeName)
        self.entry_prime.grid(row=0, column=1)

        frame2 = Frame(top)
        frame2.pack()
        Button(frame2, text='添加', command=self.add_prime_active).grid()

    def add_secondaryOrganization(self):
        top = Toplevel()
        screenwidth = top.winfo_screenwidth()
        screenheight = top.winfo_screenheight()
        width = 350
        height = 250
        x = (screenwidth - width) // 2
        y = (screenheight - height) // 2
        top.title("添加二级机构")
        top.geometry("{}x{}+{}+{}".format(width, height, x, y))

        frame1 = Frame(top)
        frame1.pack(pady=30)
        Label(frame1, text='一级机构名称：').grid(row=0, column=0)
        prime = StringVar()
        cbb_prime = ttk.Combobox(frame1, width=17, state='readonly', textvariable=prime)
        cbb_prime['values'] = self.db.select_primaryOrganization()
        cbb_prime.grid(row=0, column=1, pady=15)
        Label(frame1, text='二级机构名称：').grid(row=1, column=0)
        self.secondName = StringVar()
        entry_second = Entry(frame1, textvariable=self.secondName)
        entry_second.grid(row=1, column=1)

        frame2 = Frame(top)
        frame2.pack()
        Button(frame2, text='添加', command=self.add_second_active).grid()

    def add_prime_active(self):
        name = self.primeName.get()
        if name == "":
            print('名称不能为空!')
            return
        for organization in self.db.select_primaryOrganization():
            if name == organization[0]:
                print('该名称已存在!')
                return
        codes = self.db.select_PrimaryOrganization_allCode()
        max_code = max(codes)[0]
        code = str_plus_one(max_code, 2)

        text = '一级机构' + code
        self.tree.insert('', END, iid=text, text=text, values=name)

    def add_second_active(self):
        name = self.secondName.get()
        if name == "":
            print('名称不能为空!')
            return
        for organization in self.db.select_secondaryOrganization():
            if name == organization[0]:
                print('该名称已存在!')
                return
        codes = self.db.select_PrimaryOrganization_allCode()
        max_code = max(codes)[0]
        code = str_plus_one(max_code, 2)

        text = '一级机构' + code
        self.tree.insert('', END, iid=text, text=text, values=name)


if __name__ == '__main__':
    root = Tk()
    root.title("人力资源管理系统")  # 设置窗口标题
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    width = 1002
    height = 560
    x = (screenwidth - width) // 2
    y = (screenheight - height) // 2
    root.geometry("{}x{}+{}+{}".format(width, height, x, y))  # 设置窗口大小
    app = Application(master=root)
    app.pack()

    root.mainloop()
