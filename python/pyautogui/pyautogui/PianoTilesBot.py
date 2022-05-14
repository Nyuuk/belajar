# PIANO TILES BOT PYTHON SCRIPT.
# AKSHITH KANDIVANAM.

# importing the required modules.
import pyautogui
import time
import keyboard

'''
This project aimed to automate the Piano Tiles game using the PyAutoGUI module's functions.

The main idea is to simply recognize if any of the 4 pixels we took match the RGB colour code of the tile that must be clicked.
If any of the pixels match the desired tile's colour , we perform the click operation. To stop the clicking process, a while loop is set in place and will be terminated upon pressing 'q'.

Step 1. I used the IDLE IDE for Python to scope out the X & Y coordinates for 4 pixels in each of the 4 columns. I also scoped out the RGB value of the tile that is expected to be clicked.
Step 2. I wrote this Python script and worked with the PyAutoGUI's 'click()' and 'pixelMatchesColor()' functions.

WHEN I SCOPED OUT THE COORDINATES THEY CAME OUT AS:

LEFTMOST COLUMN: X-761, Y-707.
LEFT COLUMN: X-887, Y-707.
RIGHT COLUMN: X-1007, Y-707.
RIGHTMOST COLUMN: X-1136, Y-707.

THE RGB CODE OF THE TILE TO CLICK WAS (17, 17, 17)

**Note: This program works with the Piano Tiles game from the website: http://tanksw.com/piano-tiles/. To play it on another website, adjust the coordinates and find the appropriate RGB value for the tile to click. 
'''

# creating the main function for the click of the mouse.
# function takes in the parameters of a pixel's X & Y coordinates in each of the 4 columns.
def click_event(x, y):

    # using the module's 'click' function to click on the pixel.
    pyautogui.click(x, y)
    time.sleep(0)

# creating a function to perform the clicking event on the leftmost column.
def leftmost_column():

    # creating an if-statement to check if the pixel (761, 707) in the leftmost column matches the RGB code of the desired tile.
    if pyautogui.pixelMatchesColor(761, 707, (17, 17, 17)):

        # if the pixel does match the RGB code, we call the 'click_event' function and pass the appropriate coordinates of the pixel.
        click_event(761, 707)

# creating a function to perform the clicking event on the left column.
def left_column():

    # creating an if-statement to check if the pixel (887, 707) in the left column matches the RGB code of the desired tile.
    if pyautogui.pixelMatchesColor(887, 707, (17, 17, 17)):

        # if the pixel does match the RGB code, we call the 'click_event' function and pass the appropriate coordinates of the pixel.
        click_event(887, 707)

# creating a function to perform the clicking event on the right column.
def right_column():

    # creating an if-statement to check if the pixel (1007, 707) in the right column matches the RGB code of the desired tile.
    if pyautogui.pixelMatchesColor(1007, 707, (17, 17, 17)):

        # if the pixel does match the RGB code, we call the 'click_event' function and pass the appropriate coordinates of the pixel.
        click_event(1007, 707)

# creating a function to perform the clicking event on the rightmost column.
def rightmost_column():

    # creating an if-statement to check if the pixel (1136, 707) in the rightmost column matches the RGB code of the desired tile.
    if pyautogui.pixelMatchesColor(1136, 707, (17, 17, 17)):

        # if the pixel does match the RGB code, we call the 'click_event' function and pass the appropriate coordinates of the pixel.
        click_event(1136, 707)

# creating a while-loop to iterate until the key 'q' is pressed to quit the program.
while keyboard.is_pressed('q') == False:

    # calling all the functions to find if the pixels in their respective columns represent the RGB code for the tile to click.
    leftmost_column()
    left_column()
    right_column()
    rightmost_column()
