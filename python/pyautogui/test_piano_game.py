import pyautogui
import keyboard
from time import sleep

sleep(3)
print("sleep ssudah")
def click(x,y):
    pyautogui.click(x,y)
    print("Click %s %s" %(x,y))
    sleep(0)

while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(397,468)[0] == 0:
        click(397,468)
    if pyautogui.pixel(492,468)[0] == 0:
        click(492,468)
    if pyautogui.pixel(573,468)[0] == 0:
        click(573,468)
    if pyautogui.pixel(659,468)[0] == 0:
        click(659,468)
