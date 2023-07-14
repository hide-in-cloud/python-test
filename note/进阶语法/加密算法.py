import getpass
import hashlib

# 输入隐藏, 只能在终端运行
# pwd = getpass.getpass()  # 相当于input(), 默认为"password:"
# print(pwd)

# ------------------demo----------------------
msg = "I love you"
md5 = hashlib.md5(msg.encode('utf-8'))
print(md5.hexdigest())  # 16进制数
print(len(md5.hexdigest()))  # 32位

sha1 = hashlib.sha1(msg.encode('utf-8'))
print(sha1.hexdigest())
print(len(sha1.hexdigest()))  # 40位

sha256 = hashlib.sha256(msg.encode('utf-8'))
print(sha256.hexdigest())
print(len(sha256.hexdigest()))  # 64位
# --------------------------------------------


"""密码都是加密后再存入数据库的"""
password = "123456"
list1 = []  # 模拟数据库
sha256 = hashlib.sha256()  # 生成对象
# sha256 = hashlib.sha256("#$*".encode('utf-8'))  # 算法加盐，在密码基础上加上自定义字符
sha256.update(password.encode('utf-8'))  # 加密算法
hash_passwd = sha256.hexdigest()  # 提取加密后的密码
list1.append(hash_passwd)  # 加入到列表

# 登录验证
pwd = input("请输入密码:")
sha256 = hashlib.sha256(pwd.encode('utf-8'))  #
pwd = sha256.hexdigest()
# 用加密后的密码与数据库存放的密码比较
for i in list1:
    if pwd == i:
        print("登录成功")
    else:
        print("密码不正确")
