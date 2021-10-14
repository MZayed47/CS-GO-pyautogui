# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 15:03:00 2021

@author: HP
"""

import os
import pyautogui
import mouse
import keyboard
import time


os.startfile("C:\Program Files (x86)\Steam\steam.exe")
time.sleep(5)


print(pyautogui.position())

pyautogui.moveTo(530, 417, duration = 1)
pyautogui.click(530, 417)
time.sleep(50)

print(pyautogui.position())

pyautogui.moveTo(930, 417, duration = 1)
pyautogui.click(930, 417)
keyboard.press_and_release('`')