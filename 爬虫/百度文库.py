import urllib.request
from bs4 import BeautifulSoup
import time


def handle_request(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
    }
    # 获取请求对象
    request = urllib.request.Request(url, headers=headers)
    # 获取响应
    response = urllib.request.urlopen(request)
    # 根据响应获取内容
    content = response.read().decode('utf-8')
    return content


def parse_content(content, fp):
    # 生成soup对象
    soup = BeautifulSoup(content, "lxml")
    # 根据具体标签获取
    div = soup.find(name="div", attrs={'class': 'ie-fix'})
    p = div.find_all(name='p')
    length = len(p)
    for i in range(length):
        time.sleep(1)
        fp.write(p[i].text)


def main():
    # 打开文件
    fp = open('志愿者论文.txt', 'w+', encoding='utf-8')
    url = 'https://wenku.baidu.com/view/c0db1fccdc3383c4bb4cf7ec4afe04a1b171b04d.html'
    # 构建请求对象
    content = handle_request(url)
    # 解析内容
    parse_content(content, fp)
    fp.close()


if __name__ == '__main__':
    main()
