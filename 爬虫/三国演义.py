import urllib.request
from bs4 import BeautifulSoup
import time


def handle_request(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    }
    request = urllib.request.Request(url, headers=headers)
    return request


def parse_content(content, fp):
    # 生成soup对象
    soup = BeautifulSoup(content, 'lxml')
    # 查找所有的章节链接和标题内容
    oa_list = soup.select('.book-mulu > ul > li > a')
    # print(len(oa_list))
    # 遍历列表，依次获取每一个链接和内容
    for oa in oa_list:
        # 获取链接
        href = 'http://www.shicimingju.com' + oa['href']
        # 获取标题
        title = oa.string
        print('正在下载--%s--......' % title)
        # 获取章节内容函数
        text = get_text(href)
        # 写入文件
        fp.write(title + text + '\n')
        print('结束下载--%s--' % title)
        # time.sleep(1)


# 提取得到章节内容
def get_text(href):
    # 构建请求对象
    request = handle_request(href)
    content = urllib.request.urlopen(request).read().decode('utf8')
    # 生成soup对象
    soup = BeautifulSoup(content, 'lxml')
    # 查找包含内容的div
    odiv = soup.find('div', class_='chapter_content')
    return odiv.text


def main():
    # 打开文件
    fp = open('三国演义.txt', 'w', encoding='utf8')
    url = 'http://www.shicimingju.com/book/sanguoyanyi.html'
    # 构建请求对象
    request = handle_request(url)
    # 发送请求，得到响应
    content = urllib.request.urlopen(request).read().decode('utf8')
    # 解析内容即可
    parse_content(content, fp)
    fp.close()


if __name__ == '__main__':
    main()
