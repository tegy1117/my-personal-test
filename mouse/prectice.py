import pyautogui
import time
import sys

def time_out(time_,imgfile,noreasonm = False):
    if int(time_) != 0:
        start = time.time()
    img = None
    while img is None:
        img = pyautogui.locateOnScreen(str(imgfile))
        if int(time_) != 0:
            end = time.time()
            if end - start > int(time_):
                if bool(noreasonm) is True:
                    print('time_out')
                break
    if img is not None:
        pyautogui.click(img)
    return img


# lol = pyautogui.locateOnScreen("lol.png")
# while lol is None:
#     lol = pyautogui.locateOnScreen("lol.png")
#     print("ㄴㄴ")

# print(lol)
# pyautogui.click(lol)

#print(time_out(5,"lol.png",True))

# pyautogui.mouseInfo()

