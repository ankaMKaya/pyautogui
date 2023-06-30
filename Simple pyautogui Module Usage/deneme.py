import pyautogui
import time

while True:
    pyautogui.press('volumedown')
    time.sleep(1)
    pyautogui.press('volumeup')
    time.sleep(300)
