import pyautogui
import keyboard
from time import sleep

sleep(3)
print("sleep ssudah")
def click(x,y):
    pyautogui.click(x,y)
    pyautogui.click(x,y)
    print("Click %s %s" %(x,y))
    sleep(0)

while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(201,412)[0] == 0:
        click(201,412)
    if pyautogui.pixel(292,412)[0] == 0:
        click(292,412)
    if pyautogui.pixel(367,412)[0] == 0:
        click(367,412)
    if pyautogui.pixel(462,412)[0] == 0:
        click(462,412)
