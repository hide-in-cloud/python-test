def text_justification(text, pw):
    words = [len(word) for word in text.split()]
    len_words = len(words)
    DP = {}
    DP[0] = 0
    for i in range(1, len_words+1):
        tem_sum = []
        for j, wj in enumerate(words[:i]):
            badness = (pw - sum(words[j:i])) ** 3
            if badness < 0:  # 越界
                badness = float("inf")
            tem_sum.append(DP[j] + badness)
        DP[i] = min(tem_sum)
    return DP


if __name__ == '__main__':
    text = "panda panda panda panda reallong_wordsfor"
    pw = 16
    DP = text_justification(text, pw)
    print(DP)
