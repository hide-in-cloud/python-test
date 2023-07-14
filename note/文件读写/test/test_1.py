import os
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable()
logging.debug('Start of program')

# print(os.getcwd())  # 当前工作目录
# print(os.path.abspath('.'))  # 绝对路径
# print(os.path.relpath('E:\\123456789'))  # 相对路径
# path = os.getcwd()
# print(os.path.dirname(path))  # 返回最后一个斜杠之前的内容
# print(os.path.basename(path))  # 返回最后一个斜杠之后的内容
# print(path.split(os.path.sep))
# print(os.listdir('E:\\pythonHello'))
# print(os.path.getsize(os.path.join(path, '读写文件.py')))

# print(os.listdir("C:\\Program Files\\Adobe"))

# os.walk()返回值：
# 1.当前文件夹名称的字符串。
# 2．当前文件夹中子文件夹的字符串的列表。
# 3．当前文件夹中文件的字符串的列表。
for folderName, subfolders, fileNames in os.walk('C:\\Program Files\\Adobe'):
    if os.path.getsize(folderName) > 10000:
        print('The current folder is ' + folderName)
        logging.debug('size: ' + str(os.path.getsize(folderName)))
        for subfolder in subfolders:
            if os.path.getsize(os.path.join(folderName, subfolder)) > 1000000:
                print('SUBFOLDER of ' + folderName + ': ' + subfolder)
                logging.debug('size: ' + str(os.path.getsize(os.path.join(folderName, subfolder))))
        for filename in fileNames:
            if os.path.getsize(os.path.join(folderName, filename)) > 1000000:
                print('FILE INSIDE ' + folderName + ': ' + filename)
                logging.debug('size: ' + str(os.path.getsize(os.path.join(folderName, filename))))
        print('')

logging.debug('End of program')
