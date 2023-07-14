import time
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from 人力资源管理系统.数据库.mysql import Database


class ArchiveSearch(Frame):
    def __init__(self, master=None, parent=None, user=None):
        super().__init__(master=master)
        self.master = master
        self.parent = parent
        self.user = user
        self.db = Database(database='human_resources')
        self.gender = StringVar()
        self.hobby = StringVar()
        self.major = StringVar()
        self.education = StringVar()
        self.country = StringVar()
        self.nation = StringVar()
        self.specialty = StringVar()
        self.salaryStandard = StringVar()
        self.educationYear = StringVar()
        self.politicalAffilication = StringVar()
        self.positionName = StringVar()
        self.positionCategory = StringVar()
        self.tertiaryOrganization = StringVar()
        self.secondaryOrganization = StringVar()
        self.primaryOrganization = StringVar()
        self.title = StringVar()
        self.religion = StringVar()
        self.createWidget()

    def createWidget(self):
        frame1 = Frame(self)
        frame1.grid(row=0)

        Label(frame1, text='您正在做的业务是：人力资源--人力资源档案管理--人力资源档案查询').grid()

        frame2 = Frame(self)
        frame2.grid(row=1)

        # I级机构
        Label(frame2, text="I级机构", bg="light green", relief=GROOVE, width=14).grid(row=0, column=0)
        primaryOrganizations = self.db.select_primaryOrganization()  # 获取一级机构
        self.cbb_primaryOrganization = ttk.Combobox(frame2, state='readonly', textvariable=self.primaryOrganization,
                                                    values=primaryOrganizations, width=16)
        self.cbb_primaryOrganization.grid(row=0, column=1, padx=1)
        self.cbb_primaryOrganization.current(0)
        self.cbb_primaryOrganization.bind('<<ComboboxSelected>>', self.primOrgListener)

        # II级机构
        Label(frame2, text="II级机构", bg="light green", relief=GROOVE, width=14).grid(row=1, column=0)
        secondaryOrganizations = self.db.select_secondaryOrganization(self.primaryOrganization.get())  # 获取二级机构
        self.cbb_secondaryOrganization = ttk.Combobox(frame2, state='readonly', textvariable=self.secondaryOrganization,
                                                      values=secondaryOrganizations, width=16)
        self.cbb_secondaryOrganization.grid(row=1, column=1, padx=1)
        self.cbb_secondaryOrganization.current(0)
        self.cbb_secondaryOrganization.bind('<<ComboboxSelected>>', self.secOrgListener)

        # III级机构
        Label(frame2, text="III级机构", bg="light green", relief=GROOVE, width=14).grid(row=2, column=0)
        tertiaryOrganizations = self.db.select_tertiaryOrganization(self.secondaryOrganization.get())  # 获取三级机构
        self.cbb_tertiaryOrganization = ttk.Combobox(frame2, state='readonly', textvariable=self.tertiaryOrganization,
                                                     values=tertiaryOrganizations, width=16)
        self.cbb_tertiaryOrganization.current(0)
        self.cbb_tertiaryOrganization.grid(row=2, column=1, padx=2)

        # 职位类别
        Label(frame2, text="职位类别", bg="light green", relief=GROOVE, width=14).grid(row=3, column=0)
        self.cbb_positionCategory = ttk.Combobox(frame2, state='readonly', textvariable=self.positionCategory, width=16)
        self.cbb_positionCategory['values'] = self.db.select_positionCategory()
        # self.cbb_positionCategory.current(0)
        self.cbb_positionCategory.bind('<<ComboboxSelected>>', self.posCategoryListener)
        self.cbb_positionCategory.grid(row=3, column=1, padx=1)

        # 职位名称
        Label(frame2, text="职位名称", bg="light green", relief=GROOVE, width=14).grid(row=4, column=0)
        self.cbb_positionName = ttk.Combobox(frame2, state='readonly', textvariable=self.positionName, width=16)
        self.cbb_positionName['values'] = self.db.select_positionName(self.positionCategory.get())
        # self.cbb_positionName.current(0)
        # self.cbb_positionName.bind('<<ComboboxSelected>>', self.posNameListener)
        self.cbb_positionName.grid(row=4, column=1, padx=1)

        # 建档时间
        Label(frame2, text="建档时间", bg="light green", relief=GROOVE, width=14).grid(row=5, column=0)
        self.former_time = Entry(frame2, width=19)
        self.former_time.grid(row=5, column=1, padx=1)
        Label(frame2, text='至').grid(row=5, column=2)
        self.latter_time = Entry(frame2, width=19)
        self.latter_time.grid(row=5, column=3, padx=1)
        Label(frame2, text='(YYYY.MM.DD)').grid(row=5, column=4)

        # 查询
        btn_quit = Button(frame2, text="查询", command=self.searchActive, activeforeground="white", bg='light green',
                          activebackground="red")
        btn_quit.grid(row=6, column=1, padx=30, pady=15)

        # 返回上一级
        Button(frame2, text='返回', command=self.backActive).grid(row=6, column=3, pady=15)

        # 查询结果表
        table_frame = Frame(self)
        table_frame.grid()
        xscroll = Scrollbar(table_frame, orient=HORIZONTAL)  # 水平滚动条
        yscroll = Scrollbar(table_frame, orient=VERTICAL)  # 垂直滚动条
        columns = ['档案编号', '姓名', '性别', '一级机构', '二级机构', '三级机构', '职位分类', '职位名称', '状态']
        self.table = ttk.Treeview(table_frame, columns=columns, height=12, show='headings',
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
        btn_frame.grid()
        Button(btn_frame, text='查看明细(修改)', command=self.modify).grid(row=0, column=0, padx=50)
        Button(btn_frame, text='删除', command=self.delete).grid(row=0, column=1, padx=50)
        Button(btn_frame, text='恢复', command=self.reinstate).grid(row=0, column=2, padx=50)

    def primOrgListener(self, *args):
        """监听一级机构"""
        # 获取二级机构
        self.cbb_secondaryOrganization['values'] = self.db.select_secondaryOrganization(self.primaryOrganization.get())
        self.cbb_secondaryOrganization.current(0)
        # 获取三级机构
        self.cbb_tertiaryOrganization['values'] = self.db.select_tertiaryOrganization(self.secondaryOrganization.get())
        self.cbb_tertiaryOrganization.current(0)

    def secOrgListener(self, *args):
        """监听二级机构"""
        # 获取三级机构
        self.cbb_tertiaryOrganization['values'] = self.db.select_tertiaryOrganization(self.secondaryOrganization.get())
        self.cbb_tertiaryOrganization.current(0)

    def posCategoryListener(self, *args):
        """监听职称类别,获取下层属性(职位名称)"""
        self.cbb_positionName['values'] = self.db.select_positionName(self.positionCategory.get())
        self.cbb_positionName.current(0)

    def searchActive(self):
        # 清空历史记录
        items = self.table.get_children()
        for item in items:
            self.table.delete(item)

        # 获取关键信息
        primaryOrganization = self.primaryOrganization.get()
        secondaryOrganization = self.secondaryOrganization.get()
        tertiaryOrganization = self.tertiaryOrganization.get()
        positionCategory = self.positionCategory.get()
        positionName = self.positionName.get()
        former_time = self.former_time.get()
        latter_time = self.latter_time.get()
        # 查询
        info = self.db.select_ArchiveSearch(primaryOrganization, secondaryOrganization, tertiaryOrganization,
                                            positionCategory, positionName, former_time, latter_time)
        if info is not None:
            for index, data in enumerate(info):
                self.table.insert('', END, values=data)
        else:
            messagebox.showinfo('提示', '查无信息')

    def backActive(self):
        self.destroy()
        self.parent.pack()

    def modify(self):
        # 获取选中行信息
        item = self.table.item(self.table.focus())['values']
        employeeID = item[0]
        primaryOrganization = item[3]
        secondaryOrganization = item[4]
        tertiaryOrganization = item[5]
        positionCategory = item[6]
        positionName = item[7]
        state = item[8]

        if state == '正常' or state == '待复核':
            # 搜索详细信息
            data = self.db.select_ArchiveDetail(employeeID)
            ID = data[1]
            title = data[7]
            employeeName = data[8]
            gender = data[9]
            email = data[10]
            phone = data[11]
            qqNumber = data[12]
            mobilePhone = data[13]
            address = data[14]
            postcode = data[15]
            country = data[16]
            birthplace = data[17]
            birthdate = data[18]
            nation = data[19]
            religion = data[20]
            politicalAffilication = data[21]
            identityID = data[22]
            SSN = data[23]
            age = data[24]
            education = data[25]
            educationYear = data[26]
            major = data[27]
            salaryStandard = data[28]
            accountBank = data[29]
            accountNumber = data[30]
            specialty = data[31]
            hobby = data[32]
            personalResume = data[33]
            familyRelationship = data[34]
            remarks = data[35]

            self.top = Toplevel()
            self.top.title("人力资源管理系统")  # 设置窗口标题
            self.top.geometry("1000x580+160+160")  # 设置窗口大小

            # 窗口1
            frame1 = Frame(self.top)
            frame1.pack(fill=X)

            # 当前业务提示
            label_register = Label(frame1, text='您正在做的业务是：人力资源--人力资源档案管理--人力资源档案更改')
            label_register.pack(side=LEFT)

            # 窗口2
            frame2 = Frame(self.top)
            frame2.pack(fill=X)
            Label(frame2, text="档案编号", bg="light green", relief=GROOVE, width=14).grid(row=0, column=0)
            self.employeeID = StringVar(value=employeeID)
            Label(frame2, textvariable=self.employeeID, bg="light green", relief=GROOVE, width=89).grid(row=0, column=1,
                                                                                                        columnspan=5,
                                                                                                        padx=1)

            # 窗口3
            frame3 = Frame(self.top)
            frame3.pack(fill=X)

            # I级机构
            Label(frame3, text="I级机构", bg="light green", relief=GROOVE, width=14).grid(row=0, column=0)
            self.cbb_primaryOrganization = ttk.Combobox(frame3, state='disable', textvariable=self.primaryOrganization,
                                                        width=16)
            self.cbb_primaryOrganization.grid(row=0, column=1, padx=1)

            # II级机构
            Label(frame3, text="II级机构", bg="light green", relief=GROOVE, width=14).grid(row=0, column=2)
            self.cbb_secondaryOrganization = ttk.Combobox(frame3, state='disable',
                                                          textvariable=self.secondaryOrganization,
                                                          width=16)
            self.cbb_secondaryOrganization.grid(row=0, column=3, padx=1)

            # III级机构
            Label(frame3, text="III级机构", bg="light green", relief=GROOVE, width=14).grid(row=0, column=4)
            self.cbb_tertiaryOrganization = ttk.Combobox(frame3, state='disable',
                                                         textvariable=self.tertiaryOrganization,
                                                         width=16)
            self.cbb_tertiaryOrganization.grid(row=0, column=5, padx=2)

            # 职位类别
            Label(frame3, text="职位类别", bg="light green", relief=GROOVE, width=14).grid(row=1, column=0)
            self.cbb_positionCategory = ttk.Combobox(frame3, state='disable', textvariable=self.positionCategory,
                                                     width=16)
            self.cbb_positionCategory.grid(row=1, column=1, padx=1)

            # 职位名称
            Label(frame3, text="职位名称", bg="light green", relief=GROOVE, width=14).grid(row=1, column=2)
            self.cbb_positionName = ttk.Combobox(frame3, state='disable', textvariable=self.positionName, width=16)
            self.cbb_positionName.grid(row=1, column=3, padx=1)

            # 职称
            label_title = Label(frame3, text="职称", bg="light green", relief=GROOVE, width=14)
            label_title.grid(row=1, column=4)
            self.cbb_title = ttk.Combobox(frame3, state='readonly', textvariable=self.title, width=16)
            self.cbb_title.grid(row=1, column=5, padx=2)

            # 姓名
            Label(frame3, text='姓名', bg="light green", relief=GROOVE, width=14).grid(row=2, column=0)
            self.name = StringVar()
            self.entry_name = Entry(frame3, width=19, textvariable=self.name)
            self.entry_name.grid(row=2, column=1, padx=1)

            # 性别
            Label(frame3, text="性别", bg="light green", relief=GROOVE, width=14).grid(row=2, column=2)
            self.cbb_gender = ttk.Combobox(frame3, state='readonly', textvariable=self.gender, width=16)
            self.cbb_gender['values'] = ['男', '女']
            self.cbb_gender.current(0)
            self.cbb_gender.grid(row=2, column=3, padx=1)

            # EMAIL
            Label(frame3, text='EMAIL', bg="light green", relief=GROOVE, width=14).grid(row=2, column=4)
            self.email = StringVar()
            self.entry_email = Entry(frame3, width=19, textvariable=self.email)
            self.entry_email.grid(row=2, column=5, padx=2)

            # 电话
            Label(frame3, text='电话', bg="light green", relief=GROOVE, width=14).grid(row=3, column=0)
            self.phone = StringVar()
            self.entry_phone = Entry(frame3, width=19, textvariable=self.phone)
            self.entry_phone.grid(row=3, column=1, padx=1)

            # QQ
            Label(frame3, text='QQ', bg="light green", relief=GROOVE, width=14).grid(row=3, column=2)
            self.qq = StringVar()
            self.entry_qq = Entry(frame3, width=19, textvariable=self.qq)
            self.entry_qq.grid(row=3, column=3, padx=1)

            # 手机号码
            Label(frame3, text='手机号码', bg="light green", relief=GROOVE, width=14).grid(row=3, column=4)
            self.mobilePhone = StringVar()
            self.entry_mobilePhone = Entry(frame3, width=19, textvariable=self.mobilePhone)
            self.entry_mobilePhone.grid(row=3, column=5, padx=1)

            # 住址
            Label(frame3, text='住址', bg="light green", relief=GROOVE, width=14).grid(row=4, column=0)
            self.address = StringVar()
            self.entry_address = Entry(frame3, width=54, textvariable=self.address)
            self.entry_address.grid(row=4, column=1, columnspan=3, padx=2)

            # 邮编
            Label(frame3, text='邮编', bg="light green", relief=GROOVE, width=14).grid(row=4, column=4)
            self.postcode = StringVar()
            self.entry_postcode = Entry(frame3, width=19, textvariable=self.postcode)
            self.entry_postcode.grid(row=4, column=5, padx=1)

            # 国籍
            Label(frame3, text='国籍', bg="light green", relief=GROOVE, width=14).grid(row=5, column=0)
            countries = ['中国', '印度']
            self.cbb_country = ttk.Combobox(frame3, state='readonly', textvariable=self.country, values=countries,
                                            width=16)
            self.cbb_country.grid(row=5, column=1, padx=1)
            self.cbb_country.current(0)

            # 出生地
            Label(frame3, text='出生地', bg="light green", relief=GROOVE, width=14).grid(row=5, column=2)
            self.birthplace = StringVar()
            self.entry_birthplace = Entry(frame3, width=19, textvariable=self.birthplace)
            self.entry_birthplace.grid(row=5, column=3, padx=1)

            # 生日
            Label(frame3, text='生日', bg="light green", relief=GROOVE, width=14).grid(row=5, column=4)
            self.birthdate = StringVar()
            self.entry_birthdate = Entry(frame3, width=19, textvariable=self.birthdate)
            self.entry_birthdate.grid(row=5, column=5, padx=1)

            # 民族
            Label(frame3, text='民族', bg="light green", relief=GROOVE, width=14).grid(row=5, column=6)
            nations = ['汉', '藏', '蒙古', '回', '维吾尔', '苗', '壮', '朝鲜', '满', '白', '其他']
            self.cbb_nation = ttk.Combobox(frame3, state='readonly', textvariable=self.nation, values=nations, width=16)
            self.cbb_nation.grid(row=5, column=7)
            self.cbb_nation.current(0)

            # 宗教信仰
            Label(frame3, text='宗教信仰', bg="light green", relief=GROOVE, width=14).grid(row=6, column=0)
            self.cbb_religion = ttk.Combobox(frame3, state='readonly', textvariable=self.religion, width=16)
            self.cbb_religion['values'] = ['无', '佛教', '基督教', '伊斯兰教', '其他']
            self.cbb_religion.grid(row=6, column=1)
            self.cbb_religion.current(0)

            # 政治面貌
            Label(frame3, text='政治面貌', bg="light green", relief=GROOVE, width=14).grid(row=6, column=2)
            politicalAffiliations = ['无', '群众', '共青团员', '共产党员', '中共预备党员', '民革党员', '民盟盟员', '其他']
            self.cbb_politicalAffiliation = ttk.Combobox(frame3, state='readonly',
                                                         textvariable=self.politicalAffilication,
                                                         values=politicalAffiliations, width=16)
            self.cbb_politicalAffiliation.grid(row=6, column=3)
            self.cbb_politicalAffiliation.current(0)

            # 身份证号码
            Label(frame3, text='身份证号码', bg="light green", relief=GROOVE, width=14).grid(row=6, column=4)
            self.identityID = StringVar()
            self.entry_identityID = Entry(frame3, width=19, textvariable=self.identityID)
            self.entry_identityID.grid(row=6, column=5, padx=1)

            # 社会保障号码
            Label(frame3, text='社会保障号码', bg="light green", relief=GROOVE, width=14).grid(row=6, column=6)
            self.SSN = StringVar()
            self.entry_SSN = Entry(frame3, width=19, textvariable=self.SSN)
            self.entry_SSN.grid(row=6, column=7, padx=1)

            # 年龄
            label_age = Label(frame3, text='年龄', bg="light green", relief=GROOVE, width=14)
            label_age.grid(row=7, column=0)
            self.age = StringVar()
            self.entry_age = Entry(frame3, width=19, textvariable=self.age)
            self.entry_age.grid(row=7, column=1, padx=1)

            # 学历
            label_education = Label(frame3, text='学历', bg="light green", relief=GROOVE, width=14)
            label_education.grid(row=7, column=2)
            educations = ['无', '本科']
            self.cbb_education = ttk.Combobox(frame3, state='readonly', textvariable=self.education, values=educations,
                                              width=16)
            self.cbb_education.grid(row=7, column=3)
            self.cbb_education.current(0)

            # 教育年限
            label_educationYear = Label(frame3, text='教育年限', bg="light green", relief=GROOVE, width=14)
            label_educationYear.grid(row=7, column=4)
            educationYears = [0]
            self.cbb_educationYear = ttk.Combobox(frame3, state='readonly', textvariable=self.educationYear,
                                                  values=educationYears, width=16)
            self.cbb_educationYear.grid(row=7, column=5)
            self.cbb_educationYear.current(0)

            # 学历专业
            label_major = Label(frame3, text='学历专业', bg="light green", relief=GROOVE, width=14)
            label_major.grid(row=7, column=6)
            majors = ['无', '计算机']
            self.cbb_major = ttk.Combobox(frame3, state='readonly', textvariable=self.major, values=majors, width=16)
            self.cbb_major.grid(row=7, column=7)
            self.cbb_major.current(0)

            # 薪酬标准
            label_salaryStandard = Label(frame3, text='薪酬标准', bg="light green", relief=GROOVE, width=14)
            label_salaryStandard.grid(row=8, column=0)
            salaryStandards = [0, 5000]
            self.cbb_salaryStandard = ttk.Combobox(frame3, state='readonly', textvariable=self.salaryStandard,
                                                   values=salaryStandards, width=16)
            self.cbb_salaryStandard.grid(row=8, column=1)
            self.cbb_salaryStandard.current(0)

            # 开户行
            label_accountBank = Label(frame3, text='开户行', bg="light green", relief=GROOVE, width=14)
            label_accountBank.grid(row=8, column=2)
            self.accountBank = StringVar()
            self.entry_accountBank = Entry(frame3, width=19, textvariable=self.accountBank)
            self.entry_accountBank.grid(row=8, column=3, padx=1)

            # 账号
            label_account = Label(frame3, text='账号', bg='light green', relief=GROOVE, width=14)
            label_account.grid(row=8, column=4)
            self.account = StringVar()
            self.entry_account = Entry(frame3, width=19, textvariable=self.account)
            self.entry_account.grid(row=8, column=5, padx=1)

            # 登记人
            label_registrant = Label(frame3, text='登记人', bg='light green', relief=GROOVE, width=14)
            label_registrant.grid(row=8, column=6)
            self.registrant = StringVar()
            self.entry_registrant = Entry(frame3, state='readonly', width=19, textvariable=self.registrant)
            self.registrant.set(self.user)
            self.entry_registrant.grid(row=8, column=7, padx=1)

            # 登记时间
            label_registrationTime = Label(frame3, text='登记时间', bg='light green', relief=GROOVE, width=14)
            label_registrationTime.grid(row=9, column=0)
            self.registrationTime = StringVar()
            self.entry_registrationTime = Entry(frame3, state='readonly', width=19, textvariable=self.registrationTime)
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self.registrationTime.set(current_time)
            self.entry_registrationTime.grid(row=9, column=1, padx=1)

            # 特长
            label_specialty = Label(frame3, text='特长', bg="light green", relief=GROOVE, width=14)
            label_specialty.grid(row=9, column=2)
            specialties = ['无', 'python']
            self.cbb_specialty = ttk.Combobox(frame3, state='readonly', textvariable=self.specialty,
                                              values=specialties, width=16)
            self.cbb_specialty.grid(row=9, column=3)
            self.cbb_specialty.current(0)

            # 爱好
            label_hobby = Label(frame3, text='爱好', bg="light green", relief=GROOVE, width=14)
            label_hobby.grid(row=9, column=4)
            hobbies = ['无', '音乐']
            self.cbb_hobby = ttk.Combobox(frame3, state='readonly', textvariable=self.hobby,
                                          values=hobbies, width=16)
            self.cbb_hobby.grid(row=9, column=5)
            self.cbb_hobby.current(0)

            # 空白
            Label(frame3, text='', bg="light green", relief=GROOVE, width=14).grid(row=9, column=6)
            Label(frame3, text='', relief=GROOVE, width=19).grid(row=9, column=7)

            # 个人履历
            label_resume = Label(frame3, text='个人履历', bg="light green", relief=GROOVE, width=14, height=4)
            label_resume.grid(row=10, column=0)
            self.text_resume = Text(frame3, width=125, height=5)
            self.text_resume.grid(row=10, column=1, columnspan=7)

            # 家庭关系信息
            label_familyRelationship = Label(frame3, text='家庭关系信息', bg="light green", relief=GROOVE, width=14, height=4)
            label_familyRelationship.grid(row=11, column=0)
            self.text_familyRelationship = Text(frame3, width=125, height=5)
            self.text_familyRelationship.grid(row=11, column=1, columnspan=7)

            # 备注
            label_remarks = Label(frame3, text='备注', bg="light green", relief=GROOVE, width=14, height=4)
            label_remarks.grid(row=12, column=0)
            self.text_remarks = Text(frame3, width=125, height=5)
            self.text_remarks.grid(row=12, column=1, columnspan=7)

            # 把数据输入到界面中
            self.primaryOrganization.set(primaryOrganization)
            self.secondaryOrganization.set(secondaryOrganization)
            self.tertiaryOrganization.set(tertiaryOrganization)
            self.positionCategory.set(positionCategory)
            self.positionName.set(positionName)
            self.title.set(title)
            self.name.set(employeeName)
            self.gender.set(gender)
            self.email.set(email)
            self.phone.set(phone)
            self.qq.set(qqNumber)
            self.mobilePhone.set(mobilePhone)
            self.address.set(address)
            self.postcode.set(postcode)
            self.country.set(country)
            self.birthplace.set(birthplace)
            self.birthdate.set(birthdate)
            self.nation.set(nation)
            self.religion.set(religion)
            self.politicalAffilication.set(politicalAffilication)
            self.identityID.set(identityID)
            self.SSN.set(SSN)
            self.age.set(age)
            self.education.set(education)
            self.educationYear.set(educationYear)
            self.major.set(major)
            self.salaryStandard.set(salaryStandard)
            self.accountBank.set(accountBank)
            self.account.set(accountNumber)
            self.specialty.set(specialty)
            self.hobby.set(hobby)
            self.text_resume.insert(1.0, personalResume)
            self.text_familyRelationship.insert(1.0, familyRelationship)
            self.text_remarks.insert(1.0, remarks)
            # registrant = self.registrant.get()
            # registrationTime = self.registrationTime

            # 窗口4
            frame4 = Frame(self.top)
            frame4.pack(pady=10)

            # 按钮
            Button(frame4, text="更改", command=self.submit).grid(row=0, column=0, padx=50)
        else:
            messagebox.showinfo('提示', "只有状态为'正常'和'待复核'的员工才能更改")

    def submit(self):
        """更新档案信息"""
        data = {}
        data['employeeID'] = self.employeeID.get()
        data['title'] = self.title.get()
        data['employeeName'] = self.entry_name.get()
        data['gender'] = self.gender.get()
        data['email'] = self.entry_email.get()
        data['phone'] = self.phone.get()
        data['qqNumber'] = self.entry_qq.get()
        data['mobilePhone'] = self.entry_mobilePhone.get()
        data['address'] = self.entry_address.get()
        data['postcode'] = self.entry_postcode.get()
        data['country'] = self.country.get()
        data['birthplace'] = self.entry_birthplace.get()
        data['birthdate'] = self.entry_birthdate.get()
        data['nation'] = self.nation.get()
        data['religion'] = self.religion.get()
        data['politicalAffilication'] = self.politicalAffilication.get()
        data['identityID'] = self.identityID.get()
        data['SSN'] = self.SSN.get()
        data['age'] = int(self.age.get())
        data['education'] = self.education.get()
        data['educationYear'] = int(self.educationYear.get())
        data['major'] = self.major.get()
        data['salaryStandard'] = float(self.salaryStandard.get())
        data['accountBank'] = self.accountBank.get()
        data['accountNumber'] = self.account.get()
        data['specialty'] = self.specialty.get()
        data['hobby'] = self.hobby.get()
        data['personalResume'] = self.text_resume.get(1.0, END)
        data['familyRelationship'] = self.text_familyRelationship.get(1.0, END)
        data['remarks'] = self.text_remarks.get(1.0, END)
        data['registrant'] = self.registrant.get()
        data['registrationTime'] = self.registrationTime.get()

        if self.db.update_ArchiveDetail(data):
            messagebox.showinfo('提示', '修改成功')
            self.top.destroy()
        else:
            messagebox.showinfo('提示', '修改失败')

    def delete(self):
        """ '正常'状态改为'已删除' """
        data = self.table.item(self.table.selection())['values']
        employeeID = data[0]
        state = data[8]
        if state == '正常':
            option = messagebox.askokcancel('提示', '确认删除该员工档案吗?')
            if option is True:
                if self.db.update_state(table_name='ArchiveDetail', primary_key_name='employeeID',
                                        primary_key_value=employeeID, state='已删除'):
                    self.searchActive()
                    messagebox.showinfo('提示', "删除成功")
                else:
                    messagebox.showinfo('提示', "删除失败")
        else:
            messagebox.showinfo('提示', "只有状态为'正常'的员工才能删除")

    def reinstate(self):
        """ '已删除'状态改为'正常' """
        data = self.table.item(self.table.selection())['values']
        employeeID = data[0]
        state = data[8]
        if state == '已删除':
            option = messagebox.askokcancel('提示', '确认恢复该员工档案吗?')
            if option is True:
                if self.db.update_state(table_name='ArchiveDetail', primary_key_name='employeeID',
                                        primary_key_value=employeeID, state='正常'):
                    self.searchActive()
                    messagebox.showinfo('提示', "恢复成功")
                else:
                    messagebox.showinfo('提示', "恢复失败")
        else:
            messagebox.showinfo('提示', "只有状态为'已删除'的员工才能恢复")


if __name__ == '__main__':
    root = Tk()
    root.title("人力资源管理系统")  # 设置窗口标题
    root.geometry("1002x580")  # 设置窗口大小
    app = ArchiveSearch(master=root)
    app.pack()

    root.mainloop()
