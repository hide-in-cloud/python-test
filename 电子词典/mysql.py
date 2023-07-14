import pymysql
import hashlib

SALT = "#$*"  # 盐

def encryption(name, passwd):
    """
        对密码进行加密
    :param name: 用户名
    :param passwd: 用户输入的密码
    :return: 加密后的密码
    """
    hash = hashlib.sha1((name + SALT).encode())  # 加密的算法
    hash.update(passwd.encode())  # 对密码进行算法加密
    passwd = hash.hexdigest()
    return passwd

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
            user=self.user,  # The first four arguments is based on DB-API 2.0 recommendation.
            password=self.passwd,
            host=self.host,
            database=self.database,
            port=self.port,
            charset=self.charset
        )

    def create_cursor(self):
        self.cursor = self.db.cursor()

    def insert_data(self, name, passwd):
        """插入用户名、密码到数据库"""
        # 查找name是否已存在
        sql = "select * from user where name='%s'" % name
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        if result:  # name已存在
            return False
        # 否则将密码加密
        passwd = encryption(name, passwd)
        # 插入到数据库中
        sql = "insert into user (name, passwd) values (%s, %s)"
        try:
            self.cursor.execute(sql, [name, passwd])
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            return False

    def login(self, name, passwd):
        passwd = encryption(name, passwd)
        sql = "select * from user where name='%s' and passwd='%s'" % (name, passwd)
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        if result:
            return True
        else:
            return False

    def query(self, word):
        sql = "select mean from words where word='%s'" % word
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        if result:
            return result[0]

    def insert_into_history(self, name, word):
        """插入到历史记录"""
        sql = "insert into history (name, word) values(%s, %s)"
        try:
            self.cursor.execute(sql, [name, word])
            self.db.commit()
        except Exception:
            self.db.rollback()

    def display_history(self, name):
        """显示历史记录"""
        sql = "select name,word,time from history where name='%s' order by time desc limit 10" % name
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    def close(self):
        self.db.close()
