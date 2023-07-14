import time
from tkinter import *
from tkinter import ttk, messagebox
from 人力资源管理系统.数据库.mysql import Database


class ArchiveRegister(Frame):
    """档案登记"""

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
        """创建组件"""

        # 窗口1
        frame1 = Frame(self)
        frame1.pack(fill=X)

        # 当前业务提示
        label_register = Label(frame1, text='您正在做的业务是：人力资源--人力资源档案管理--人力资源档案登记')
        label_register.pack(side=LEFT)

        # 窗口2
        frame2 = Frame(self)
        frame2.pack(fill=X, pady=10)

        # I级机构
        Label(frame2, text="I级机构", bg="light green", relief=GROOVE, width=14).grid(row=0, column=0)
        primaryOrganizations = self.db.select_primaryOrganization()  # 获取一级机构
        self.cbb_primaryOrganization = ttk.Combobox(frame2, state='readonly', textvariable=self.primaryOrganization,
                                                    values=primaryOrganizations, width=16)
        self.cbb_primaryOrganization.grid(row=0, column=1, padx=1)
        self.cbb_primaryOrganization.current(0)
        self.cbb_primaryOrganization.bind('<<ComboboxSelected>>', self.primOrgListener)

        # II级机构
        Label(frame2, text="II级机构", bg="light green", relief=GROOVE, width=14).grid(row=0, column=2)
        secondaryOrganizations = self.db.select_secondaryOrganization(self.primaryOrganization.get())  # 获取二级机构
        self.cbb_secondaryOrganization = ttk.Combobox(frame2, state='readonly', textvariable=self.secondaryOrganization,
                                                      values=secondaryOrganizations, width=16)
        self.cbb_secondaryOrganization.grid(row=0, column=3, padx=1)
        self.cbb_secondaryOrganization.current(0)
        self.cbb_secondaryOrganization.bind('<<ComboboxSelected>>', self.secOrgListener)

        # III级机构
        Label(frame2, text="III级机构", bg="light green", relief=GROOVE, width=14).grid(row=0, column=4)
        tertiaryOrganizations = self.db.select_tertiaryOrganization(self.secondaryOrganization.get())  # 获取三级机构
        self.cbb_tertiaryOrganization = ttk.Combobox(frame2, state='readonly', textvariable=self.tertiaryOrganization,
                                                     values=tertiaryOrganizations, width=16)
        self.cbb_tertiaryOrganization.current(0)
        self.cbb_tertiaryOrganization.grid(row=0, column=5, padx=2)

        # 职位类别
        Label(frame2, text="职位类别", bg="light green", relief=GROOVE, width=14).grid(row=1, column=0)
        self.cbb_positionCategory = ttk.Combobox(frame2, state='readonly', textvariable=self.positionCategory, width=16)
        self.cbb_positionCategory['values'] = self.db.select_positionCategory()
        # self.cbb_positionCategory.current(0)
        self.cbb_positionCategory.bind('<<ComboboxSelected>>', self.posCategoryListener)
        self.cbb_positionCategory.grid(row=1, column=1, padx=1)

        # 职位名称
        Label(frame2, text="职位名称", bg="light green", relief=GROOVE, width=14).grid(row=1, column=2)
        self.cbb_positionName = ttk.Combobox(frame2, state='readonly', textvariable=self.positionName, width=16)
        self.cbb_positionName['values'] = self.db.select_positionName(self.positionCategory.get())
        # self.cbb_positionName.current(0)
        self.cbb_positionName.bind('<<ComboboxSelected>>', self.posNameListener)
        self.cbb_positionName.grid(row=1, column=3, padx=1)

        # 职称
        label_title = Label(frame2, text="职称", bg="light green", relief=GROOVE, width=14)
        label_title.grid(row=1, column=4)
        self.cbb_title = ttk.Combobox(frame2, state='readonly', textvariable=self.title, width=16)
        self.cbb_title['values'] = self.db.select_title(self.positionName.get())
        # self.cbb_title.current(0)
        self.cbb_title.grid(row=1, column=5, padx=2)

        # 姓名
        Label(frame2, text='姓名', bg="light green", relief=GROOVE, width=14).grid(row=2, column=0)
        self.name = StringVar()
        self.entry_name = Entry(frame2, width=19, textvariable=self.name)
        self.entry_name.grid(row=2, column=1, padx=1)

        # 性别
        Label(frame2, text="性别", bg="light green", relief=GROOVE, width=14).grid(row=2, column=2)
        self.cbb_gender = ttk.Combobox(frame2, state='readonly', textvariable=self.gender, width=16)
        self.cbb_gender['values'] = ['男', '女']
        self.cbb_gender.current(0)
        self.cbb_gender.grid(row=2, column=3, padx=1)

        # EMAIL
        Label(frame2, text='EMAIL', bg="light green", relief=GROOVE, width=14).grid(row=2, column=4)
        self.email = StringVar()
        self.entry_email = Entry(frame2, width=19, textvariable=self.email)
        self.entry_email.grid(row=2, column=5, padx=2)

        # 电话
        Label(frame2, text='电话', bg="light green", relief=GROOVE, width=14).grid(row=3, column=0)
        self.phone = StringVar()
        self.entry_phone = Entry(frame2, width=19, textvariable=self.phone)
        self.entry_phone.grid(row=3, column=1, padx=1)

        # QQ
        Label(frame2, text='QQ', bg="light green", relief=GROOVE, width=14).grid(row=3, column=2)
        self.qq = StringVar()
        self.entry_qq = Entry(frame2, width=19, textvariable=self.qq)
        self.entry_qq.grid(row=3, column=3, padx=1)

        # 手机号码
        Label(frame2, text='手机号码', bg="light green", relief=GROOVE, width=14).grid(row=3, column=4)
        self.mobilePhone = StringVar()
        self.entry_mobilePhone = Entry(frame2, width=19, textvariable=self.mobilePhone)
        self.entry_mobilePhone.grid(row=3, column=5, padx=1)

        # 住址
        Label(frame2, text='住址', bg="light green", relief=GROOVE, width=14).grid(row=4, column=0)
        self.address = StringVar()
        self.entry_address = Entry(frame2, width=54, textvariable=self.address)
        self.entry_address.grid(row=4, column=1, columnspan=3, padx=2)

        # 邮编
        Label(frame2, text='邮编', bg="light green", relief=GROOVE, width=14).grid(row=4, column=4)
        self.postcode = StringVar()
        self.entry_postcode = Entry(frame2, width=19, textvariable=self.postcode)
        self.entry_postcode.grid(row=4, column=5, padx=1)

        # 国籍
        Label(frame2, text='国籍', bg="light green", relief=GROOVE, width=14).grid(row=5, column=0)
        countries = ['中国', '印度','美国','加拿大','日本','英国']
        self.cbb_country = ttk.Combobox(frame2, state='readonly', textvariable=self.country, values=countries, width=16)
        self.cbb_country.grid(row=5, column=1, padx=1)
        self.cbb_country.current(0)

        # 出生地
        Label(frame2, text='出生地', bg="light green", relief=GROOVE, width=14).grid(row=5, column=2)
        self.birthplace = StringVar()
        self.entry_birthplace = Entry(frame2, width=19, textvariable=self.birthplace)
        self.entry_birthplace.grid(row=5, column=3, padx=1)

        # 生日
        Label(frame2, text='生日', bg="light green", relief=GROOVE, width=14).grid(row=5, column=4)
        self.birthdate = StringVar()
        self.entry_birthdate = Entry(frame2, width=19, textvariable=self.birthdate)
        self.entry_birthdate.grid(row=5, column=5, padx=1)

        # 民族
        Label(frame2, text='民族', bg="light green", relief=GROOVE, width=14).grid(row=5, column=6)
        nations = ['汉', '藏', '蒙古', '回', '维吾尔', '苗', '壮', '朝鲜', '满', '白', '其他']
        self.cbb_nation = ttk.Combobox(frame2, state='readonly', textvariable=self.nation, values=nations, width=16)
        self.cbb_nation.grid(row=5, column=7)
        self.cbb_nation.current(0)

        # 宗教信仰
        Label(frame2, text='宗教信仰', bg="light green", relief=GROOVE, width=14).grid(row=6, column=0)
        self.cbb_religion = ttk.Combobox(frame2, state='readonly', textvariable=self.religion, width=16)
        self.cbb_religion['values'] = ['无', '佛教', '基督教', '伊斯兰教', '其他']
        self.cbb_religion.grid(row=6, column=1)
        self.cbb_religion.current(0)

        # 政治面貌
        Label(frame2, text='政治面貌', bg="light green", relief=GROOVE, width=14).grid(row=6, column=2)
        politicalAffiliations = ['无', '群众', '共青团员', '共产党员', '中共预备党员', '民革党员', '民盟盟员', '其他']
        self.cbb_politicalAffiliation = ttk.Combobox(frame2, state='readonly', textvariable=self.politicalAffilication,
                                                     values=politicalAffiliations, width=16)
        self.cbb_politicalAffiliation.grid(row=6, column=3)
        self.cbb_politicalAffiliation.current(0)

        # 身份证号码
        Label(frame2, text='身份证号码', bg="light green", relief=GROOVE, width=14).grid(row=6, column=4)
        self.identityID = StringVar()
        self.entry_identityID = Entry(frame2, width=19, textvariable=self.identityID)
        self.entry_identityID.grid(row=6, column=5, padx=1)

        # 社会保障号码
        Label(frame2, text='社会保障号码', bg="light green", relief=GROOVE, width=14).grid(row=6, column=6)
        self.SSN = StringVar()
        self.entry_SSN = Entry(frame2, width=19, textvariable=self.SSN)
        self.entry_SSN.grid(row=6, column=7, padx=1)

        # 年龄
        label_age = Label(frame2, text='年龄', bg="light green", relief=GROOVE, width=14)
        label_age.grid(row=7, column=0)
        self.age = StringVar()
        self.entry_age = Entry(frame2, width=19, textvariable=self.age)
        self.entry_age.grid(row=7, column=1, padx=1)

        # 学历
        label_education = Label(frame2, text='学历', bg="light green", relief=GROOVE, width=14)
        label_education.grid(row=7, column=2)
        educations = ['无', '小学','初中','高中','本科','研究生','博士']
        self.cbb_education = ttk.Combobox(frame2, state='readonly', textvariable=self.education, values=educations,
                                          width=16)
        self.cbb_education.grid(row=7, column=3)
        self.cbb_education.current(0)

        # 教育年限
        label_educationYear = Label(frame2, text='教育年限', bg="light green", relief=GROOVE, width=14)
        label_educationYear.grid(row=7, column=4)
        educationYears = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        self.cbb_educationYear = ttk.Combobox(frame2, state='readonly', textvariable=self.educationYear,
                                              values=educationYears, width=16)
        self.cbb_educationYear.grid(row=7, column=5)
        self.cbb_educationYear.current(0)

        # 学历专业
        label_major = Label(frame2, text='学历专业', bg="light green", relief=GROOVE, width=14)
        label_major.grid(row=7, column=6)
        majors = ['无', '计科','软工','信管','机制','文学','法学']
        self.cbb_major = ttk.Combobox(frame2, state='readonly', textvariable=self.major, values=majors, width=16)
        self.cbb_major.grid(row=7, column=7)
        self.cbb_major.current(0)

        # 薪酬标准
        label_salaryStandard = Label(frame2, text='薪酬标准', bg="light green", relief=GROOVE, width=14)
        label_salaryStandard.grid(row=8, column=0)
        salaryStandards = [0,3000,4000,5000,6000,7000,8000,9000,10000]
        self.cbb_salaryStandard = ttk.Combobox(frame2, state='readonly', textvariable=self.salaryStandard,
                                               values=salaryStandards, width=16)
        self.cbb_salaryStandard.grid(row=8, column=1)
        self.cbb_salaryStandard.current(0)

        # 开户行
        label_accountBank = Label(frame2, text='开户行', bg="light green", relief=GROOVE, width=14)
        label_accountBank.grid(row=8, column=2)
        self.accountBank = StringVar()
        self.entry_accountBank = Entry(frame2, width=19, textvariable=self.accountBank)
        self.entry_accountBank.grid(row=8, column=3, padx=1)

        # 账号
        label_account = Label(frame2, text='账号', bg='light green', relief=GROOVE, width=14)
        label_account.grid(row=8, column=4)
        self.account = StringVar()
        self.entry_account = Entry(frame2, width=19, textvariable=self.account)
        self.entry_account.grid(row=8, column=5, padx=1)

        # 登记人
        label_registrant = Label(frame2, text='登记人', bg='light green', relief=GROOVE, width=14)
        label_registrant.grid(row=8, column=6)
        self.registrant = StringVar()
        self.entry_registrant = Entry(frame2, state='readonly', width=19, textvariable=self.registrant)
        self.registrant.set(self.user)
        self.entry_registrant.grid(row=8, column=7, padx=1)

        # 登记时间
        label_registrationTime = Label(frame2, text='登记时间', bg='light green', relief=GROOVE, width=14)
        label_registrationTime.grid(row=9, column=0)
        self.registrationTime = StringVar()
        self.entry_registrationTime = Entry(frame2, state='readonly', width=19, textvariable=self.registrationTime)
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.registrationTime.set(current_time)
        self.entry_registrationTime.grid(row=9, column=1, padx=1)

        # 特长
        label_specialty = Label(frame2, text='特长', bg="light green", relief=GROOVE, width=14)
        label_specialty.grid(row=9, column=2)
        specialties = ['无','数据库','python','java','C++','C']
        self.cbb_specialty = ttk.Combobox(frame2, state='readonly', textvariable=self.specialty,
                                          values=specialties, width=16)
        self.cbb_specialty.grid(row=9, column=3)
        self.cbb_specialty.current(0)

        # 爱好
        label_hobby = Label(frame2, text='爱好', bg="light green", relief=GROOVE, width=14)
        label_hobby.grid(row=9, column=4)
        hobbies = ['无', '篮球','足球','音乐','看书','学习','看电影']
        self.cbb_hobby = ttk.Combobox(frame2, state='readonly', textvariable=self.hobby,
                                      values=hobbies, width=16)
        self.cbb_hobby.grid(row=9, column=5)
        self.cbb_hobby.current(0)

        # 空白
        Label(frame2, text='', bg="light green", relief=GROOVE, width=14).grid(row=9, column=6)
        Label(frame2, text='', relief=GROOVE, width=19).grid(row=9, column=7)

        # 个人履历
        label_resume = Label(frame2, text='个人履历', bg="light green", relief=GROOVE, width=14, height=4)
        label_resume.grid(row=10, column=0)
        self.text_resume = Text(frame2, width=125, height=5)
        self.text_resume.grid(row=10, column=1, columnspan=7)

        # 家庭关系信息
        label_familyRelationship = Label(frame2, text='家庭关系信息', bg="light green", relief=GROOVE, width=14, height=4)
        label_familyRelationship.grid(row=11, column=0)
        self.text_familyRelationship = Text(frame2, width=125, height=5)
        self.text_familyRelationship.grid(row=11, column=1, columnspan=7)

        # 备注
        label_remarks = Label(frame2, text='备注', bg="light green", relief=GROOVE, width=14, height=4)
        label_remarks.grid(row=12, column=0)
        self.text_remarks = Text(frame2, width=125, height=5)
        self.text_remarks.grid(row=12, column=1, columnspan=7)

        # 窗口3
        frame3 = Frame(self)
        frame3.pack(pady=10)

        # 按钮
        Button(frame3, text="提交", command=self.submit).grid(row=0, column=0, padx=50)
        Button(frame3, text="返回", command=self.back).grid(row=0, column=2, padx=50)

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
        """监听职称类别,获取下层属性(职位名称(职称))"""
        self.cbb_positionName['values'] = self.db.select_positionName(self.positionCategory.get())
        self.cbb_positionName.current(0)
        self.cbb_title['values'] = self.db.select_title(self.positionName.get())
        self.cbb_title.current(0)

    def posNameListener(self, *args):
        """监听职位名称,获取下层属性(职称)"""
        self.cbb_title['values'] = self.db.select_title(self.positionName.get())
        self.cbb_title.current(0)

    def submit(self):
        """提交并显示提示框"""
        primaryOrganizationCode = self.db.select_primaryOrganizationCode(self.primaryOrganization.get())
        secondaryOrganizationCode = self.db.select_secondaryOrganizationCode(self.secondaryOrganization.get())
        tertiaryOrganizationCode = self.db.select_tertiaryOrganizationCode(self.tertiaryOrganization.get())
        positionCategoryCode = self.db.select_positionCategoryCode(self.positionCategory.get())
        positionNameCode = self.db.select_positionNameCode(self.positionName.get())
        ID = self.db.select_ID(primaryOrganizationCode, secondaryOrganizationCode, tertiaryOrganizationCode)
        title = self.title.get()
        employeeName = self.entry_name.get()
        gender = self.gender.get()
        email = self.entry_email.get()
        phone = self.phone.get()
        qqNumber = self.entry_qq.get()
        mobilePhone = self.entry_mobilePhone.get()
        address = self.entry_address.get()
        postcode = self.entry_postcode.get()
        country = self.country.get()
        birthplace = self.entry_birthplace.get()
        birthdate = self.entry_birthdate.get()
        nation = self.nation.get()
        religion = self.religion.get()
        politicalAffilication = self.politicalAffilication.get()
        identityID = self.identityID.get()
        SSN = self.SSN.get()
        age = int(self.age.get())
        education = self.education.get()
        educationYear = int(self.educationYear.get())
        major = self.major.get()
        salaryStandard = float(self.salaryStandard.get())
        accountBank = self.accountBank.get()
        accountNumber = self.account.get()
        specialty = self.specialty.get()
        hobby = self.hobby.get()
        personalResume = self.text_resume.get(1.0, END)
        familyRelationship = self.text_familyRelationship.get(1.0, END)
        remarks = self.text_remarks.get(1.0, END)
        registrant = self.registrant.get()
        registrationTime = self.registrationTime.get()

        if ID is None:
            ID = '01'
        else:
            if max(ID)[0] is not '01':  # 字符串ID + 1
                max_id = int(max(ID)[0])
                ID = str(max_id + 1)
                if max_id < 10:
                    ID = '0' + ID
                    print(ID)


        if self.db.insert_ArchiveDetail(ID, primaryOrganizationCode, secondaryOrganizationCode, tertiaryOrganizationCode,
                                     positionCategoryCode, positionNameCode, title, employeeName, gender, email, phone,
                                     qqNumber, mobilePhone, address, postcode, country, birthplace, birthdate, nation,
                                     religion, politicalAffilication, identityID, SSN, age, education, educationYear,
                                     major, salaryStandard, accountBank, accountNumber, specialty, hobby,
                                     personalResume, familyRelationship, remarks, registrant, registrationTime):
            employeeID = registrationTime[0:4]+primaryOrganizationCode+secondaryOrganizationCode+tertiaryOrganizationCode+ID
            if self.db.insert_ArchiveBrief(employeeID, self.primaryOrganization.get(), self.secondaryOrganization.get(),
                                        self.tertiaryOrganization.get(), self.positionCategory.get(), self.positionName.get()):
                messagebox.showinfo('提示','登记成功')
                self.destroy()
                self.parent.pack()
        else:
            messagebox.showinfo('提示','登记失败')

    def back(self):
        self.destroy()
        self.parent.pack()


if __name__ == '__main__':
    root = Tk()
    root.title("人力资源管理系统")  # 设置窗口标题
    root.geometry("1002x580")  # 设置窗口大小
    root.tk.eval('package require Tix')  # 引入升级包，这样才能使用升级的组合控件
    app = ArchiveRegister(master=root, user='admin')
    app.pack()
    root.mainloop()
