import pyautogui
from pynput.keyboard import Key, Controller
import keyboard
import time

k = Controller()

running = False
KEY = "e"
DELAY = 0.2

def onkeypress(event):
    global running
    if event.name == 'q':
        if running == True:
            print("Stopping...")
            running = False
        else:
            print("Starting...")
            running = True

def press(key):
    k.press(key)
    k.release(key)

keyboard.on_press(onkeypress)
while True:
    if running == True:
        if pyautogui.locateOnScreen('images/image.png', confidence=0.5) != None:
            print("NAMERIH")
            press(KEY)
            time.sleep(7)
            print("Cast again")
            press(KEY)
        time.sleep(DELAY)
