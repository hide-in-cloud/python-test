import json

import requests


def get_comments(url):
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 "
            "Safari/537.36 SE 2.X MetaSr 1.0 ",
        "referer": "https://music.163.com/"
    }
    params = "0iKdqYfnanI9sZ1FrRi5FY4NYIt38vRXY + mb + gY77B0W + nOkWxS / oZKD1iTYloJsrm6vtzYLJURlTud4vqwuIBxI4ZIQmo0EZjWQEyYNMpoD5CbXhBjZALBWWhm / cHbO + 99AjSyp7UyEeQE7n9dBy9asUg5hDDjpjVwEhLdlZzQWEqWWnnw2UqlSkk1NaYv69YuHwElx2nOtr3lP4dUBVICefqG3wK + qfeZKV4BhtfdiUXWBGKGG0FfjYFwRfzvnBz7m2i8PYgQ2CELDqZplNRGn57Ka9N3tFnwIbFn5wWI="
    encseckey = "8dd6a8484ed462f08627c838e9f770cc9fd44d451af41e24c190ce0abf6d79cb8f7abee76f9959b2158a920274164e0a9f7aad55ca9eefa707a0fd1c8e61c9e1aa2a83ca6caf4917011b49b01067975189a4ad679b75da8a9cf59c3ba9d695f437924649e5e49913c64b3b4e3f5a19c35f3fb9102d45bd32108c4e8139e8ad98"
    data = {
        "params": params,
        "encseckey": encseckey
    }
    # name_id = url.split('=')[1]
    target_url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="
    res = requests.get(target_url, headers=headers, data=data)
    return res


def get_hot_comments(res):
    comments_josn = json.loads(res.text)
    hot_comments = comments_josn['hotComments']
    with open('comments.txt', 'w', encoding='utf-8') as file:
        for each in hot_comments:
            file.write(each['user']['nickname'] + ':\n')
            file.write(each['content'] + '\n')
            file.write("---------------------------------------------\n")


def main():
    url = "https://music.163.com/#/song?id=28754106"
    res = get_comments(url)
    with open('comments.txt', 'w', encoding='utf-8') as file:
        file.write(res.text)


if __name__ == '__main__':
    main()
