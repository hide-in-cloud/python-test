from multiprocessing import Queue
from multiprocessing import Process
from time import sleep


def download(queue):
    images = ['girl.jpg', 'boy.jpg', 'man.jpg']
    for image in images:
        print("正在下载:", image)
        sleep(0.5)
        queue.put(image)


def getfile(queue):
    while True:
        try:
            file = queue.get(timeout=3)
            print("{}保存成功!".format(file))
        except:
            print("为空")
            break


if __name__ == '__main__':
    q = Queue(5)
    p1 = Process(target=download, args=(q,))
    p2 = Process(target=getfile, args=(q,))

    p1.start()
    p2.start()
    p2.join()

    print("over")
