import shelve


def create_file():
    shelfFile = shelve.open('mydata')
    cats = ['Zophie', 'Pooka', 'Simon']
    shelfFile['cats'] = cats
    shelfFile.close()


def read_file():
    shelfFile = shelve.open('mydata')
    # print(shelfFile['cats'])
    print(list(shelfFile.values()))
    shelfFile.close()


if __name__ == '__main__':
    read_file()
