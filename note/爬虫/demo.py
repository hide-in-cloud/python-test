import requests


def download_img(url):
    # 从url中获取文件名
    filename = url[url.rfind('/') + 1:]

    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 "
            "Safari/537.36 SE 2.X MetaSr 1.0 "
    }
    res = requests.get(url, headers)  # 生成请求对象
    with open(filename, 'wb') as file:
        file.write(res.content)  # 获取的是二进制


url = 'https://icon.qiantucdn.com/static/images/public/greenlogo.png'
download_img(url)
