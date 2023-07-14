from PIL import Image

dogIm = Image.open('dog.png')  # 加载图像对象
print(dogIm.size)

miniDogIm = dogIm.crop((75,30,210,145))  # 裁剪图像,矩形区域
dogImWidth, dogImHeight = dogIm.size
miniDogImWidth, miniDogImHeight = miniDogIm.size
dogCopyIm = dogIm.copy()  # 复制返回一个新的图像
width, height = dogIm.size
dogCopyIm = dogCopyIm.resize((width+100, height+100))  # 调整图像大小
# 多个狗头平铺
for left in range(0, dogImWidth, miniDogImWidth):
    for top in range(0, dogImHeight, miniDogImHeight):
        dogCopyIm.paste(miniDogIm, (left, top))
dogCopyIm.save('tiled.png')
