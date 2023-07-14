import pymysql
import logging


class Database:
    def __init__(self, database=None):
        self.host = "localhost"
        self.port = 3306
        self.user = "root"
        self.passwd = "wdc123826715"
        self.database = database
        self.charset = "utf8"
        self.connect_database()

    def connect_database(self):
        # 2.连接MySQL服务
        self.db = pymysql.Connect(
            user=self.user,
            password=self.passwd,
            host=self.host,
            database=self.database,
            port=self.port,
            charset=self.charset
        )
        # 3.创建游标
        self.cursor = self.db.cursor()

    def insert_User(self, name, password):
        """插入用户名、密码到数据库"""
        # 查找name是否已存在
        sql = "select * from User where userName='%s'" % name
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        if result:  # name已存在
            return False

        # 插入到数据库中
        sql = "insert into User(userName, password) values(%s, %s)"
        try:
            self.cursor.execute(sql, [name, password])
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            return False

    def login(self, name, password):
        sql = "select * from user where userName='%s' and password='%s'" % (name, password)
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            if result:
                return True
            else:
                return False
        except Exception as e:
            logging.exception(e)

    # def search_secondaryOrganization_parent(self, primaryOrganizationCode):
    #     """查询父节点名称"""
    #     sql = """
    #         select primaryOrganization
    #         from PrimaryOrganization
    #         where primaryOrganizationCode='%s'
    #         """ % primaryOrganizationCode
    #     try:
    #         self.cursor.execute(sql)
    #         data = self.cursor.fetchone()
    #         if data:
    #             return data[0]
    #     except Exception as e:
    #         print(repr(e))

    def select_primaryOrganization(self):
        """查询一级机构名称"""
        sql = "select primaryOrganization from PrimaryOrganization"
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            if data:
                return data
        except Exception as e:
            print(repr(e))

    def select_secondaryOrganization(self, primaryOrganization):
        """查询一级机构包含的二级机构名称"""
        sql = """
            select primaryOrganizationCode
            from PrimaryOrganization
            where primaryOrganization='%s'
            """ % primaryOrganization
        self.cursor.execute(sql)
        primaryCode = self.cursor.fetchone()
        sql = "select secondaryOrganization from SecondaryOrganization where primaryOrganizationCode='%s'" % primaryCode
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            if data:
                return data
        except Exception as e:
            print(repr(e))

    def select_tertiaryOrganization(self, secondaryOrganization):
        """查询一级机构包含的三级机构名称"""
        sql = "select secondaryOrganizationCode from SecondaryOrganization where secondaryOrganization='%s'" % secondaryOrganization
        self.cursor.execute(sql)
        secondaryCode = self.cursor.fetchone()
        sql = "select tertiaryOrganization from TertiaryOrganization where secondaryOrganizationCode='%s'" % secondaryCode
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    def select_positionCategory(self):
        """查询职称类别名称"""
        sql = """
            select positionCategory
            from PositionCategory
        """
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            if data:
                return data
        except Exception as e:
            print(repr(e))

    def select_positionName(self, positionCategory):
        """查询职称类别包含的职位名称"""
        sql = """
            select positionName
            from PositionName A, PositionCategory B
            where positionCategory='%s' and
            A.positionCategoryCode=B.positionCategoryCode
        """ % positionCategory
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            if data:
                return data
        except Exception as e:
            print(repr(e))

    def select_title(self, positionName):
        """查询职位名称包含的'职称'名称"""
        sql = """
            select title
            from Title, PositionName
            where positionName='%s' and
            Title.positionNameCode=PositionName.positionNameCode
        """ % positionName
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            if data:
                return data
        except Exception as e:
            print(repr(e))

    def select_primaryOrganization_all(self):
        """查询一级机构所有"""
        sql = """
            select *
            from PrimaryOrganization
        """
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            if data:
                return data
        except Exception as e:
            print(repr(e))

    def select_PrimaryOrganization_allCode(self):
        """查询一级机构所有编号"""
        sql = """
            select primaryOrganizationCode
            from PrimaryOrganization
        """
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            if data:
                return data
        except Exception as e:
            print(repr(e))

    def select_secondaryOrganization_all(self):
        """查询二级机构所有"""
        sql = """
            select *
            from SecondaryOrganization
        """
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            if data:
                return data
        except Exception as e:
            print(repr(e))

    def select_tertiaryOrganization_all(self):
        """查询二级机构所有"""
        sql = """
            select *
            from tertiaryOrganization
        """
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            if data:
                return data
        except Exception as e:
            print(repr(e))

    def insert_ArchiveDetail(self, ID, primaryOrganizationCode, secondaryOrganizationCode, tertiaryOrganizationCode,
                             positionCategoryCode, positionNameCode, title, employeeName, gender, email, phone,
                             qqNumber, mobilePhone, address, postcode, country, birthplace, birthdate, nation, religion,
                             politicalAffilication, identityID, SSN, age, education, educationYear, major,
                             salaryStandard, accountBank, accountNumber, specialty, hobby, personalResume,
                             familyRelationship, remarks, registrant, registrationTime):
        """插入员工详细档案"""

        sql = """
            insert into
            ArchiveDetail(
            ID, primaryOrganizationCode, secondaryOrganizationCode, tertiaryOrganizationCode, positionCategoryCode,positionNameCode,
            title, employeeName, gender, email, phone, qqNumber, mobilePhone, address, postcode, country, birthplace,
            birthdate, nation, religion, politicalAffilication, identityID, SSN, age, education, educationYear, major,
            salaryStandard, accountBank, accountNumber, specialty,hobby, personalResume, familyRelationship, remarks,
            registrant, registrationTime)
            values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',
            '%s','%s',%d,'%s',%d,'%s',%f,'%s','%s','%s','%s','%s','%s','%s','%s','%s')
        """ % (ID, primaryOrganizationCode, secondaryOrganizationCode, tertiaryOrganizationCode, positionCategoryCode,
               positionNameCode,
               title, employeeName, gender, email, phone, qqNumber, mobilePhone, address, postcode, country, birthplace,
               birthdate, nation, religion, politicalAffilication, identityID, SSN, age, education, educationYear,
               major, salaryStandard, accountBank, accountNumber, specialty, hobby, personalResume, familyRelationship,
               remarks, registrant, registrationTime)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            return True
        except Exception as e:
            print(repr(e))
            self.db.rollback()
            return False

    def insert_ArchiveBrief(self, employeeID, primaryOrganization, secondaryOrganization, tertiaryOrganization,
                            positionCategory, positionName):
        """插入员工简述档案"""

        sql = """
            insert into ArchiveBrief
            values('%s','%s','%s','%s','%s','%s')
        """ % (employeeID, primaryOrganization, secondaryOrganization, tertiaryOrganization, positionCategory,
               positionName)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            return True
        except Exception as e:
            print(repr(e))
            self.db.rollback()
            return False

    def select_primaryOrganizationCode(self, primaryOrganization):
        """查询一级机构名称对应的编号"""
        sql = """
            select primaryOrganizationCode
            from PrimaryOrganization
            where primaryOrganization='%s'
        """ % primaryOrganization
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchone()
            if data:
                return data[0]
        except Exception as e:
            logging.exception(e)

    def select_secondaryOrganizationCode(self, secondaryOrganization):
        """查询二级机构名称对应的编号"""
        sql = """
            select secondaryOrganizationCode
            from SecondaryOrganization
            where secondaryOrganization='%s'
        """ % secondaryOrganization
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchone()
            if data:
                return data[0]
        except Exception as e:
            logging.exception(e)

    def select_tertiaryOrganizationCode(self, tertiaryOrganization):
        """查询三级机构名称对应的编号"""
        sql = """
            select tertiaryOrganizationCode
            from TertiaryOrganization
            where tertiaryOrganization='%s'
        """ % tertiaryOrganization
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchone()
            if data:
                return data[0]
        except Exception as e:
            logging.exception(e)

    def select_positionCategoryCode(self, positionCategory):
        sql = """
            select positionCategoryCode
            from PositionCategory
            where positionCategory='%s'
        """ % positionCategory
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchone()
            if data:
                return data[0]
        except Exception as e:
            logging.exception(e)

    def select_positionNameCode(self, positionName):
        sql = """
            select positionNameCode
            from PositionName
            where positionName='%s'
        """ % positionName
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchone()
            if data:
                return data[0]
        except Exception as e:
            logging.exception(e)

    def select_ID(self, primaryOrganizationCode, secondaryOrganizationCode, tertiaryOrganizationCode):
        sql = """
            select ID
            from ArchiveDetail
            where primaryOrganizationCode='%s' and
            secondaryOrganizationCode='%s' and
            tertiaryOrganizationCode='%s'
        """ % (primaryOrganizationCode, secondaryOrganizationCode, tertiaryOrganizationCode)
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            if data:
                return data
            else:
                return None
        except Exception as e:
            logging.exception(e)

    def select_ArchiveDetail(self, employeeID):
        """查询档案详情"""
        sql = """
            select *
            from ArchiveDetail
            where employeeID='%s'
        """ % employeeID
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchone()
            if data:
                return data
        except Exception as e:
            print(repr(e))

    def search_ArchiveReview(self):
        """查询待复核的档案"""
        sql = """
            select A.employeeID, B.employeeName, B.gender, A.primaryOrganization, secondaryOrganization,
                    tertiaryOrganization, positionCategory, positionName, B.state
            from ArchiveBrief A, ArchiveDetail B
            where A.employeeID = B.employeeID and
            B.state='待复核'
        """
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            if data:
                return data
        except Exception as e:
            print(repr(e))

    def update_ArchiveDetail(self, data):
        """更新人资档案明细表"""
        sql = """
            update ArchiveDetail
            set title=%(title)s,
                employeeName=%(employeeName)s, 
                gender=%(gender)s, 
                email=%(email)s, 
                phone=%(phone)s,
                qqNumber=%(qqNumber)s, 
                mobilePhone=%(mobilePhone)s, 
                address=%(address)s, 
                postcode=%(postcode)s, 
                country=%(country)s, 
                birthplace=%(birthplace)s, 
                birthdate=%(birthdate)s, 
                nation=%(nation)s,
                religion=%(religion)s, 
                politicalAffilication=%(politicalAffilication)s, 
                identityID=%(identityID)s, 
                SSN=%(SSN)s, 
                age=%(age)s, 
                education=%(education)s, 
                educationYear=%(educationYear)s,
                major=%(major)s, 
                salaryStandard=%(salaryStandard)s, 
                accountBank=%(accountBank)s, 
                accountNumber=%(accountNumber)s, 
                specialty=%(specialty)s, 
                hobby=%(hobby)s,
                personalResume=%(personalResume)s, 
                familyRelationship=%(familyRelationship)s, 
                remarks=%(remarks)s, 
                registrant=%(registrant)s, 
                registrationTime=%(registrationTime)s
            where employeeID=%(employeeID)s
        """
        try:
            self.cursor.execute(sql, data)
            self.db.commit()
            return True
        except Exception as e:
            logging.exception(e)
            self.db.rollback()
            return False

    def insert_ArchiveReview(self, employeeID, reviewer, reviewTime):
        """数据插入到档案复核表"""

        sql = """
            insert into ArchiveReview
            values('%s','%s','%s')
        """ % (employeeID, reviewer, reviewTime)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            return True
        except Exception as e:
            print(repr(e))
            self.db.rollback()
            return False

    def select_ArchiveSearch(self, primaryOrganization, secondaryOrganization, tertiaryOrganization, positionCategory,
                             positionName, former_time, latter_time):
        sql = """
            select A.employeeID, B.employeeName, B.gender, A.primaryOrganization, secondaryOrganization,
                    tertiaryOrganization, positionCategory, positionName, B.state
            from ArchiveBrief A, ArchiveDetail B
            where A.employeeID = B.employeeID and
            A.primaryOrganization=%s and
            A.secondaryOrganization=%s and
            A.tertiaryOrganization=%s and
            A.positionCategory=%s and
            A.positionName=%s
        """
        params = ()
        if former_time == "" and latter_time == "":
            params = (primaryOrganization, secondaryOrganization, tertiaryOrganization, positionCategory,
                      positionName)
        elif former_time == "" and latter_time != "":
            sql = sql + "and B.registrationTime <= %s"
            params = (primaryOrganization, secondaryOrganization, tertiaryOrganization, positionCategory,
                      positionName, latter_time)
        elif former_time != "" and latter_time == "":
            sql = sql + "and B.registrationTime >= %s"
            params = (primaryOrganization, secondaryOrganization, tertiaryOrganization, positionCategory,
                      positionName, former_time)
        elif former_time != "" and latter_time != "":
            sql = sql + "and B.registrationTime >= %s and B.registrationTime <= %s"
            params = (primaryOrganization, secondaryOrganization, tertiaryOrganization, positionCategory,
                      positionName, former_time, latter_time)
        try:
            self.cursor.execute(sql, params)
            data = self.cursor.fetchall()
            if data:
                return data
        except Exception as e:
            print(repr(e))

    def update_state(self, table_name, primary_key_name, primary_key_value, state):
        sql = """
            update %s
            set state='%s'
            where %s='%s'
        """ % (table_name, state, primary_key_name, primary_key_value)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            return True
        except Exception as e:
            print(repr(e))
            self.db.rollback()
            return False

    def select_salaryStandardCode(self):
        sql = """
            select right(salaryStandardCode, 4)
            from SalaryRegister
            where left(salaryStandardCode,6)=date_format(now(), '%Y%m')
        """
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            if data:
                return data
        except Exception as e:
            print(repr(e))

    def select_employeeName(self):
        """查询状态为'正常'，且尚未登记薪酬登记表的档案 """

        sql = """
            select employeeName
            from ArchiveDetail
            where state='正常' and
            employeeID not in (
                select employeeID
                from SalaryRegister
                );
        """
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            if data:
                return data
        except Exception as e:
            logging.exception(e)

    def search_positionName(self, employeeID):
        """查询员工的职位名称"""
        sql = """
            select positionName
            from ArchiveBrief
            where employeeID='%s'
        """ % employeeID
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchone()
            if data:
                return data[0]
        except Exception as e:
            print(repr(e))

    def search_employeeID(self, employeeName):
        """查找员工档案编号"""
        sql = """
            select employeeID
            from ArchiveDetail
            where employeeName='%s'
        """ % employeeName
        try:
            self.cursor.execute(sql)
            employeeID = self.cursor.fetchone()
            if employeeID:
                return employeeID[0]
        except Exception as e:
            print(repr(e))

    def insert_SalaryRegister(self, salaryStandardCode, salaryStandardName, employeeName, registrant, basicSalary,
                              transportationSalary, lunchAllowance, communicationSubsidy):
        """插入薪酬登记表"""

        employeeID = self.search_employeeID(employeeName)

        # 插入
        sql = """
            insert into
            SalaryRegister(salaryStandardCode,salaryStandardName,employeeID,employeeName,registrant,
            basicSalary,transportationSalary,lunchAllowance,communicationSubsidy)
            values('%s','%s','%s','%s','%s','%f','%f','%f','%f')
        """ % (
            salaryStandardCode, salaryStandardName, employeeID, employeeName, registrant, basicSalary,
            transportationSalary,
            lunchAllowance, communicationSubsidy)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            return True
        except Exception as e:
            print(repr(e))
            self.db.rollback()
            return False

    def update_salaryStandard(self, employeeName, totalSalary):
        """更新员工薪酬标准"""
        sql = """
            update archivedetail
            set salaryStandard='%f'
            where employeeName='%s'
        """ % (totalSalary, employeeName)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            return True
        except Exception as e:
            print(repr(e))
            self.db.rollback()
            return False

    def search_reviewing_SalaryRegister(self):
        """查询待复核的薪酬标准"""
        sql = """
            select salaryStandardCode, salaryStandardName, totalSalary, employeeName, registrant, state
            from SalaryRegister
            where state='待复核'
        """
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            if data:
                return data
        except Exception as e:
            print(repr(e))

    def select_SalaryRegister(self, salaryStandardCode):
        """查询薪酬登记表全部信息"""
        sql = """
            select *
            from SalaryRegister
            where salaryStandardCode='%s'
        """ % salaryStandardCode
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchone()
            if data:
                return data
        except Exception as e:
            print(repr(e))

    def insert_SalaryReview(self, SalaryStandardCode, employeeName, reviewer, reviewTime, reviewComments):
        """插入数据到薪酬复核表"""
        sql = """
            insert into SalaryReview
            values('%s','%s','%s','%s','%s')
        """ % (SalaryStandardCode, employeeName, reviewer, reviewTime, reviewComments)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            return True
        except Exception as e:
            print(repr(e))
            self.db.rollback()
            return False

    def search_salary_keyword(self, SalaryStandardCode, keyword, former_time, latter_time):
        """薪酬登记表关键字查询"""
        SalaryStandardCode = '%' + SalaryStandardCode + '%'
        keyword = '%' + keyword + '%'
        sql = """
            select salaryStandardCode, salaryStandardName, employeeName, registrant,registrationTime, basicSalary,
                    transportationSalary,lunchAllowance, communicationSubsidy,endowmentInsurance,unemploymentInsurance,
                    medicalInsurance,housingProvidentFund,totalSalary,state
            from SalaryRegister
            where SalaryStandardCode like %s and
            (salaryStandardName like %s or
            employeeName like %s or
            registrant like %s or
            SalaryStandardCode in (
                select SalaryStandardCode
                from SalaryReview
                where reviewer like %s
                )
            )
        """
        params = ()
        if former_time == "" and latter_time == "":
            params = (SalaryStandardCode, keyword, keyword, keyword, keyword)
        elif former_time == "" and latter_time != "":
            sql = sql + "and registrationTime <= %s"
            params = (SalaryStandardCode, keyword, keyword, keyword, keyword, latter_time)
        elif former_time != "" and latter_time == "":
            sql = sql + "and registrationTime >= %s"
            params = (SalaryStandardCode, keyword, keyword, keyword, keyword, former_time)
        elif former_time != "" and latter_time != "":
            sql = sql + "and registrationTime >= %s and registrationTime <= %s"
            params = (SalaryStandardCode, keyword, keyword, keyword, keyword, former_time, latter_time)
        try:
            self.cursor.execute(sql, params)
            data = self.cursor.fetchall()
            if data:
                return data
        except Exception as e:
            print(repr(e))

    def search_payrollCode(self):
        """查询薪酬发放单号"""
        sql = """
            select right(payrollCode, 10)
            from payrollRegister
        """
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            if data:
                return data
        except Exception as e:
            print(repr(e))

    def search_payroll(self):
        """档案表按三级机构分组,且薪酬登记表的状态为'正常'，且尚未登记的，最后统计人数和薪酬总额"""
        sql = """
            select primaryOrganization, secondaryOrganization, tertiaryOrganization, count(*), sum(totalSalary)
            from ArchiveBrief A, SalaryRegister S
            where A.employeeID = S.employeeID and S.state='正常'
            group by tertiaryOrganization
            having tertiaryOrganization not in(
                select tertiaryOrganization
                from payrollRegister
            );
        """
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            if data:
                return data
        except Exception as e:
            print(repr(e))

    def search_terOrg_salaryDetail(self, tertiaryOrganization):
        """查询第三级机构的薪酬标准详情"""
        sql = """
            select A.employeeID,employeeName,basicSalary,transportationSalary,lunchAllowance, communicationSubsidy,
                    endowmentInsurance,unemploymentInsurance,medicalInsurance,housingProvidentFund
            from SalaryRegister S, ArchiveBrief A
            where A.employeeID = S.employeeID and
            A.tertiaryOrganization='%s' and
            S.state='正常';
        """ % tertiaryOrganization
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            if data:
                return data
        except Exception as e:
            print(repr(e))

    def insert_payrollRegister(self, payrollCode, primaryOrganization, secondaryOrganization, tertiaryOrganization,
                               totalNumber, payroll, actualPayroll, registrant, registrationTime):
        """插入数据"""
        sql = """
            insert into
            PayrollRegister(payrollCode, primaryOrganization, secondaryOrganization, tertiaryOrganization,
                totalNumber, payroll, actualPayroll, registrant, registrationTime)
            values('%s','%s','%s','%s',%d,%f,%f,'%s','%s')
        """ % (payrollCode, primaryOrganization, secondaryOrganization, tertiaryOrganization,
               totalNumber, payroll, actualPayroll, registrant, registrationTime)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            return True
        except Exception as e:
            print(repr(e))
            self.db.rollback()
            return False

    def insert_payrollDetail(self, payrollCode, employeeID, employeeName, bonus, deductedBonus, actualSalary):
        """插入到薪酬发放单详情表中"""
        sql = """
            insert into
            payrollDetail
            values('%s','%s','%s',%f,%f,%f)
        """ % (payrollCode, employeeID, employeeName, bonus, deductedBonus, actualSalary)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            return True
        except Exception as e:
            print(repr(e))
            self.db.rollback()
            return False

    def search_totalSalary(self, employeeID):
        """查询员工薪酬标准总额"""
        sql = """
            select totalSalary
            from SalaryRegister
            where employeeID = '%s'
        """ % employeeID
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchone()
            if data:
                return data[0]
        except Exception as e:
            print(repr(e))

    def search_reviewing_PayrollRegister(self):
        """查询state为'待复核'的"""
        sql = """
            select payrollCode,primaryOrganization,secondaryOrganization,tertiaryOrganization,totalNumber,payroll
            from PayrollRegister
            where state='待复核'
        """
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            if data:
                return data
        except Exception as e:
            print(repr(e))

    def select_PayrollRegister(self, payrollCode):
        """查询薪酬登记表全部信息"""
        sql = """
            select *
            from PayrollRegister
            where payrollCode='%s'
        """ % payrollCode
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchone()
            if data:
                return data
        except Exception as e:
            print(repr(e))

    def search_bonus_deductedBonus(self, payrollCode, employeeID):
        """查询员工的奖励金额和应扣金额"""
        sql = """
            select bonus,deductedBonus
            from PayrollDetail
            where payrollCode='%s' and
            employeeID='%s'
        """ % (payrollCode, employeeID)
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchone()
            if data:
                return data
        except Exception as e:
            print(repr(e))

    def update_bonus_deductedBonus(self, payrollCode, employeeID, bonus, deductedBonus, actualSalary):
        """更新员工的奖励金额和应扣金额"""
        sql = """
            update PayrollDetail
            set bonus = %f, deductedBonus = %f, actualSalary=%f
            where payrollCode='%s' and
            employeeID='%s'
        """ % (bonus, deductedBonus, actualSalary, payrollCode, employeeID)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            return True
        except Exception as e:
            print(repr(e))
            self.db.rollback()
            return False

    def insert_PayrollReview(self, payrollCode, actualPayroll, reviewer, reviewTime):
        """数据插入到薪酬发放单复核表中"""
        sql = """
            insert into
            PayrollReview
            values('%s',%f,'%s','%s')
        """ % (payrollCode, actualPayroll, reviewer, reviewTime)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            return True
        except Exception as e:
            print(repr(e))
            self.db.rollback()
            return False

    def update_actualSalary(self, payrollCode, actualPayroll):
        """更新薪酬发放单的实发金额"""
        sql = """
            update payrollRegister
            set actualPayroll=%f
            where payrollCode='%s'
        """ % (actualPayroll, payrollCode)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            return True
        except Exception as e:
            print(repr(e))
            self.db.rollback()
            return False

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.db:
            self.db.close()
