url = 'https://icon.qiantucdn.com/static/images/public/greenlogo.png'
# 从url中获取文件名
filename = url[url.rfind('/')+1:]  # 从右往左找第一个'/'
print(filename)

print(url.split('/'))  # 以'/'作为分割符

print(url.split('/')[2].strip())

str = "123abc213"
print(str.strip('123'))  # 用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列

