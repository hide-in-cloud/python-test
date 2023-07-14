from PIL import Image, ImageDraw

im = Image.new('RGBA', (200,200), 'white')  # 加载图像对象
draw = ImageDraw.Draw(im)
draw.line([(0,0), (199,0),(199,199), (0,199),(0,0)], fill='black')
draw.rectangle((20,30,60,50), fill='blue')
im.save('drawing.png')
