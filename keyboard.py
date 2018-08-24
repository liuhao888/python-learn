import threading
import pyautogui

def time_handler():
    pyautogui.keyDown('ctrlleft')
    pyautogui.press('shiftleft')
    pyautogui.keyUp('ctrlleft')
    global timer
    timer = threading.Timer(3,time_handler)
    timer.start()

time_handler()