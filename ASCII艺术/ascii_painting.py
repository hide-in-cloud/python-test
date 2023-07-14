from PIL import Image, ImageFilter, ImageFont
import numpy as np


def mapping_ascii(brightness, symbols):
    if (brightness.max() - brightness.min()) != 0:
        brightness = (brightness - brightness.min()) / (brightness.max() - brightness.min()) * (symbols.size - 1)
    return brightness


def load_image():
    im = Image.open('卡卡西小队.jpg', 'r')
    return im


def get_im_bright(im):
    im = im.convert('L')
    np_im_bright = np.array(im)
    return np_im_bright


def get_symbols():
    ascii_list = list("`^\",:;Il!i~+_-?][}{1)(|/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$")
    symbols = np.array(ascii_list)
    return symbols


def generate_ascii_painting(im):
    np_im_bright = get_im_bright(im)
    symbols = get_symbols()
    np_brightness = mapping_ascii(np_im_bright, symbols)
    np_ascii = symbols[np_brightness.astype(int)]
    lines = "\n".join(("".join(r) for r in np_ascii))
    print(lines)


def main():
    im = load_image()
    generate_ascii_painting(im)


if __name__ == '__main__':
    main()
