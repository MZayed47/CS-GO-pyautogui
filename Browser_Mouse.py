# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 13:43:29 2021

@author: HP
"""

import os
import pyautogui
import mouse
import keyboard
import time

os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
time.sleep(5)

print(pyautogui.position())

pyautogui.moveTo(503, 402, duration = 1)
pyautogui.click(503, 402)
time.sleep(5)


pyautogui.moveTo(903, 202, duration = 1)
keyboard.press_and_release('shift+f5')