#! python3
import pyautogui
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

width, height = pyautogui.size()

pyautogui.scroll(100)
# pyautogui.moveTo(200,200,duration=0.25)  # 屏幕位置(x,y)  duration:持续时间
# pyautogui.moveTo(400,200,duration=0.25)
# pyautogui.moveTo(400,400,duration=0.25)
# pyautogui.moveRel(100,0,duration=0.25)  # 当前鼠标位置(水平移动,垂直移动)  向右100个像素, 向下0个像素
# pyautogui.moveRel(0,100,duration=0.25)
# pyautogui.moveRel(-100,0,duration=0.25)
# pyautogui.moveRel(0,-100,duration=0.25)
