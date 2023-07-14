from PIL import Image, ImageFont
import numpy as np


def ascii_art(file):
    im = Image.open(file)

    # 将图片转换成一张灰阶图
    im = im.convert("L")

    # 图片降采样(缩小)
    sample_rate = 0.15

    # 获取图片长宽比
    font = ImageFont.truetype("SourceCodePro-Regular-12.ttf")
    aspect_ratio = font.getsize("x")[0] / font.getsize("x")[1]

    # 计算新图片的size
    new_im_size = np.array(
        [im.size[0] * sample_rate, im.size[1] * sample_rate * aspect_ratio]
    ).astype(int)

    # 重新设置图片的size
    im = im.resize(new_im_size)

    # 转换成图像像素的numpy数组
    im = np.array(im)

    # 定义字符画中用到的所有字符
    symbols = np.array(list(" .^-vM$"))

    # [0, 5)  5->symbols元素的个数
    if (im.max() - im.min()) != 0:
        im = (im - im.min()) / (im.max() - im.min()) * (symbols.size - 1)

    # 生成字符图片
    ascii = symbols[im.astype(int)]
    lines = "\n".join(("".join(r) for r in ascii))
    print(lines)


if __name__ == '__main__':
    ascii_art("pikaqiu.jpg")
