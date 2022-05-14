import keyboard
from pynput.mouse import Controller,Button,Listener
from mss import mss


def click(x,y):
    mouse.position = (x,y)
    mouse.click(Button.left, 1)
    print("Click %s %s" %(x,y))

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(397,468)[0] == 0:
        click(397,468)
    if pyautogui.pixel(492,468)[0] == 0:
        click(492,468)
    if pyautogui.pixel(573,468)[0] == 0:
        click(573,468)
    if pyautogui.pixel(659,468)[0] == 0:
        click(659,468)
