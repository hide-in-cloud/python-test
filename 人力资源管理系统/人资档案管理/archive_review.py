import time
from tkinter import *
from tkinter import ttk
from 人力资源管理系统.数据库.mysql import Database


class ArchiveReview(Frame):
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
        frame1.pack()

        Label(frame1, text='您正在做的业务是：人力资源--人力资源档案管理--人力资源档案复核').pack()

        # 待复核的档案
        table_frame = Frame(self)
        table_frame.pack(pady=40)
        Label(table_frame, text='当前等待复核的人力资源档案总数:n例').pack()
        xscroll = Scrollbar(table_frame, orient=HORIZONTAL)  # 水平滚动条
        yscroll = Scrollbar(table_frame, orient=VERTICAL)  # 垂直滚动条
        columns = ['档案编号', '姓名', '性别', '一级机构', '二级机构', '三级机构', '职位分类', '职位名称', '状态']
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

        info = self.db.search_ArchiveReview()
        if info is not None:
            for index, data in enumerate(info):
                self.table.insert('', END, values=data)

    def review(self):
        # 获取选中行信息
        item = self.table.item(self.table.focus())['values']
        employeeID = item[0]
        primaryOrganization = item[3]
        secondaryOrganization = item[4]
        tertiaryOrganization = item[5]
        positionCategory = item[6]
        positionName = item[7]

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
        label_register = Label(frame1, text='您正在做的业务是：人力资源--人力资源档案管理--人力资源档案复核')
        label_register.pack(side=LEFT)

        # 窗口2
        frame2 = Frame(self.top)
        frame2.pack(fill=X)
        Label(frame2, text="档案编号", bg="light green", relief=GROOVE, width=14).grid(row=0, column=0)
        self.employeeID = StringVar(value=employeeID)
        Label(frame2, textvariable=self.employeeID, bg="light green", relief=GROOVE, width=89).grid(row=0, column=1, columnspan=5, padx=1)

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
        self.cbb_secondaryOrganization = ttk.Combobox(frame3, state='disable', textvariable=self.secondaryOrganization,
                                                      width=16)
        self.cbb_secondaryOrganization.grid(row=0, column=3, padx=1)

        # III级机构
        Label(frame3, text="III级机构", bg="light green", relief=GROOVE, width=14).grid(row=0, column=4)
        self.cbb_tertiaryOrganization = ttk.Combobox(frame3, state='disable', textvariable=self.tertiaryOrganization,
                                                     width=16)
        self.cbb_tertiaryOrganization.grid(row=0, column=5, padx=2)

        # 职位类别
        Label(frame3, text="职位类别", bg="light green", relief=GROOVE, width=14).grid(row=1, column=0)
        self.cbb_positionCategory = ttk.Combobox(frame3, state='disable', textvariable=self.positionCategory, width=16)
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
        self.cbb_country = ttk.Combobox(frame3, state='readonly', textvariable=self.country, values=countries, width=16)
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
        politicalAffilications = ['无', '群众', '共青团员', '共产党员', '中共预备党员', '民革党员', '民盟盟员', '其他']
        self.cbb_politicalAffilication = ttk.Combobox(frame3, state='readonly', textvariable=self.politicalAffilication,
                                                      values=politicalAffilications, width=16)
        self.cbb_politicalAffilication.grid(row=6, column=3)
        self.cbb_politicalAffilication.current(0)

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

        # 复核人
        label_reviewer = Label(frame3, text='复核人', bg='light green', relief=GROOVE, width=14)
        label_reviewer.grid(row=8, column=6)
        self.reviewer = StringVar()
        self.entry_reviewer = Entry(frame3, state='readonly', width=19, textvariable=self.reviewer)
        self.reviewer.set(self.user)
        self.entry_reviewer.grid(row=8, column=7, padx=1)

        # 复核时间
        label_reviewTime = Label(frame3, text='复核时间', bg='light green', relief=GROOVE, width=14)
        label_reviewTime.grid(row=9, column=0)
        self.reviewTime = StringVar()
        self.entry_reviewTime = Entry(frame3, state='readonly', width=19, textvariable=self.reviewTime)
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.reviewTime.set(current_time)
        self.entry_reviewTime.grid(row=9, column=1, padx=1)

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
        Button(frame4, text="复核通过", command=self.submit).grid(row=0, column=0, padx=50)

    def submit(self):
        """状态改为'正常' """
        employeeID = self.employeeID.get()
        if (self.db.update_state('ArchiveDetail', 'employeeID', employeeID, state='正常') and
                self.db.insert_ArchiveReview(employeeID, self.reviewer.get(), self.reviewTime.get())):
            self.table.delete(self.table.selection())
            self.top.destroy()

    def back(self):
        self.destroy()
        self.parent.pack()


if __name__ == '__main__':
    root = Tk()
    root.title("人力资源管理系统")  # 设置窗口标题
    root.geometry("1002x560")  # 设置窗口大小
    app = ArchiveReview(master=root, user='admin')
    app.pack()

    root.mainloop()
