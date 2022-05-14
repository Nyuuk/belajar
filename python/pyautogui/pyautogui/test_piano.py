import keyboard, pyautogui
#from pynput.mouse import Controller,Button,Listener
#from mss import mss

#mouse = Controller()
#def click(x,y):
#    mouse.position = (x,y)
#    mouse.click(Button.left, 1)
#    print("Click %s %s" %(x,y))

def upper():
    y_cor = 182
    if pyautogui.pixel(227,y_cor)[0] == 17:
        pyautogui.press('a')
        #click(227,y_cor)
    if pyautogui.pixel(327,y_cor)[0] == 17:
        pyautogui.press('s')
        #click(327,y_cor)
    if pyautogui.pixel(427,y_cor)[0] == 17:
        pyautogui.press('d')
        #click(427,y_cor)
    if pyautogui.pixel(527,y_cor)[0] == 17:
        pyautogui.press('f')
        #click(527,y_cor)
def midle():
    y_cor = 333
    if pyautogui.pixel(227,y_cor)[0] == 17:
        pyautogui.press('a')
        #click(227,y_cor)
    if pyautogui.pixel(327,y_cor)[0] == 17:
        pyautogui.press('s')
        #click(327,y_cor)
    if pyautogui.pixel(427,y_cor)[0] == 17:
        pyautogui.press('d')
        #click(427,y_cor)
    if pyautogui.pixel(527,y_cor)[0] == 17:
        pyautogui.press('f')
        #click(527,y_cor)
def down():
    y_cor = 494
    if pyautogui.pixel(227,y_cor)[0] == 17:
        pyautogui.press('a')
        #click(227,y_cor)
    if pyautogui.pixel(327,y_cor)[0] == 17:
        pyautogui.press('s')
        #click(327,y_cor)
    if pyautogui.pixel(427,y_cor)[0] == 17:
        pyautogui.press('d')
        #click(427,y_cor)
    if pyautogui.pixel(527,y_cor)[0] == 17:
        pyautogui.press('f')
        #click(527,y_cor)

total = 1
while keyboard.is_pressed('q') == False:
    if 10 >= total:
        down()
    elif 20 >= total:
        midle()
    else:
        upper()
    print(f'total: {total}')

