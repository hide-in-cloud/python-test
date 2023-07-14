import csv
import requests
import bs4


def open_url(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"}
    res = requests.get(url, headers=headers)
    return res


def find_movies(res):
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    # 电影名
    movies = []
    targets = soup.find_all("div", class_="hd")
    for each in targets:
        movies.append(each.a.span.text)

    # 评分
    ranks = []
    targets = soup.find_all("span", class_="rating_num")
    for each in targets:
        ranks.append(" 评分:%s " % each.text)

    # 资料
    messages = []
    targets = soup.find_all("div", class_="bd")
    for each in targets:
        try:
            messages.append(each.p.text.split('\n')[1].strip() +
                            each.p.text.split('\n')[2].strip())
        except:
            continue

    result = []
    length = len(movies)
    for i in range(length):
        result.append(movies[i] + ranks[i] + messages[i] + '\n')

    return result


# 找出一共多少个页面
def find_depth(res):
    suop = bs4.BeautifulSoup(res.text, "html.parser")
    depth = suop.find("span", class_="next").previous_sibling.previous_sibling.text
    return int(depth)


def main():
    host = "http://movie.douban.com/top250"
    res = open_url(host)
    depth = find_depth(res)

    result = []
    for i in range(depth):
        url = host + "?start={}&filter=".format(i * 25)
        res = open_url(url)
        result.append(find_movies(res))

    with open('豆瓣TOP250电影.csv', 'w', encoding='utf-8', newline='') as f:
        f_csv = csv.writer(f)
        for each in result:
            f_csv.writerow(each)
    print("over!")


if __name__ == '__main__':
    main()
