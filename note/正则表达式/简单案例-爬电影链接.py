import re
import urllib.request


def get_movie_links():
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 "
            "Safari/537.36 SE 2.X MetaSr 1.0 "
    }
    file_list_url = "https://www.dytt8.net/html/gndy/dyzz/list_23_1.html"
    response_list = urllib.request.urlopen(file_list_url, headers)
    # 获取到二进制的页面信息
    response_list_data = response_list.read()
    # 解码
    response_list_text = response_list_data.decode("GBK")
    # print(response_list_text)
    url_list = re.findall(r'<a href=\"(.*)\" class=\"ulink\">(.*)</a>', response_list_text)
    print(url_list)
    for content_url, film_name in url_list:
        response = urllib.request.urlopen(content_url, headers)
        response_data = response.read()
        response_text = response_data.decode("GBK")
        result = re.search(r'')


def main():
    get_movie_links()


if __name__ == '__main__':
    main()
