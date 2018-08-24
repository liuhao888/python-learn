import threading
import pyautogui
num = 10
def time_handler():
    global num
    num = num * -1
    pyautogui.moveRel(num,0,duration=0.25)
    global timer
    timer = threading.Timer(30,time_handler)
    timer.start()

# while input('输入你好') != '你好':
#     print()

time_handler()