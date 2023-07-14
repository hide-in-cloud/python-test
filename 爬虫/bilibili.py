import bs4
import requests


def find_info(url):
    res = requests.get(url)
    suop = bs4.BeautifulSoup(res.text, "html.parser")

    # 视频的标题和网址
    videos = []
    targets = suop.find_all('li', class_='video-item matrix')
    for each in targets:
        videos.append(each.a['title'] + '  ' + each.a['href'])

    # 标签
    tags = []
    targets = suop.find_all('div', class_='info')
    for each in targets:
        tags.append(' 播放量:%s ' % each.find('span', title='观看').text.strip() +
                    ' 弹幕:%s ' % each.find('span', title='弹幕').text.strip() +
                    ' 上传时间:%s ' % each.find('span', title='上传时间').text.strip() +
                    ' up主:%s ' % each.find('span', title='up主').text.strip())

    result = []
    length = len(videos)
    for i in range(length):
        result.append('%d、' % (i+1) + videos[i] + tags[i] + '\n')

    return result


def main():
    keyword = input('请输入搜索关键字：')
    url = "https://search.bilibili.com/all?keyword=" + keyword
    result = []
    result.extend(find_info(url))
    with open("bilibili.txt", 'w', encoding='utf-8') as file:
        for each in result:
            file.write(each)


if __name__ == '__main__':
    main()