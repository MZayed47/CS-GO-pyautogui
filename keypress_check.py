# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 17:27:34 2021

@author: HP
"""


from pynput.keyboard import Key, Listener


def show(key):

    pressed_key = str(key).replace("'", "")
    print(" key: ", pressed_key)

    if key == Key.esc:
        # Stop listener
        return False


# Listener
with Listener(on_press=show) as listener:
    listener.join()