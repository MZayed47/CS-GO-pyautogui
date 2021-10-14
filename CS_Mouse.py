# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 11:39:51 2021

@author: HP
"""

import os
import pyautogui
import mouse
import keyboard
import time


os.startfile("steam://rungameid/730")
time.sleep(40)


# Screen size and Current Position of the cursor
print(pyautogui.size())
print(pyautogui.position())


# How many demo files I want to record
x = 4
n = 10

for x in range(x+1):
    # console demoui
    time.sleep(3)
    pyautogui.moveTo(750, 565, duration = 1)
    pyautogui.click(750, 565)
    
    keyboard.press_and_release('o')
    time.sleep(1)
    pyautogui.typewrite("demoui")
    
    
    # submit
    pyautogui.moveTo(1285, 565, duration = 1)
    pyautogui.click(1285, 565)
    
    
    # Load
    pyautogui.moveTo(35, 505, duration = 1)
    pyautogui.click(35, 505)
    
    
    # Click on top folder
    pyautogui.moveTo(625, 280, duration = 1)
    pyautogui.click(625, 280)
    
    
    # Move down
    for i in range(n+1):
        keyboard.press_and_release('down')
    n += 1
    
    
    # Open demo
    pyautogui.moveTo(930, 520, duration = 1)
    pyautogui.click(930, 520)
    
    
    
    # Pause First
    time.sleep(60)
    pyautogui.moveTo(95, 420, duration = 1)
    pyautogui.click(95, 420)
    
    
    # Resume
    time.sleep(1)
    pyautogui.moveTo(95, 420, duration = 1)
    pyautogui.click(95, 420)
    
    
    # Cross the loader
    time.sleep(1)
    pyautogui.moveTo(335, 400, duration = 1)
    pyautogui.click(335, 400)
    
    
    # Start Recording
    time.sleep(1)
    pyautogui.hotkey("win", "alt", "r")
    
    
    # End Recording
    time.sleep(4500)
    pyautogui.hotkey("win", "alt", "r")



##############################################################################
##############################################################################
'''
# Cross the dem selector
pyautogui.moveTo(965, 205, duration = 1)
pyautogui.click(965, 205)


# Cross the loader
pyautogui.moveTo(335, 400, duration = 1)
pyautogui.click(335, 400)


# Cross the console
pyautogui.moveTo(1323, 39, duration = 1)
pyautogui.click(1323, 39)


# console demoui
pyautogui.moveTo(750, 565, duration = 1)
pyautogui.click(750, 565)

keyboard.press_and_release('o')
time.sleep(1)
pyautogui.typewrite("demoui")


# submit
pyautogui.moveTo(1285, 565, duration = 1)
pyautogui.click(1285, 565)


# Load
pyautogui.moveTo(35, 505, duration = 1)
pyautogui.click(35, 505)


# Click on top folder
pyautogui.moveTo(625, 280, duration = 1)
pyautogui.click(625, 280)


# Move down
for i in range(n+1):
    keyboard.press_and_release('down')
n += 1
'''
##############################################################################
##############################################################################






