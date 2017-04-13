__author__ = 'Jialijun'

import win32api
import win32con
import time
from ctypes import *

def mouse_click(x=None,y=None):
    if not x is None and not y is None:
        mouse_move(x,y)
        time.sleep(0.05)
        for i in range(500):
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
            time.sleep(0.1)

def mouse_move(x,y):
    windll.user32.SetCursorPos(x, y)

if __name__ == "__main__":
    mouse_click(673,521)