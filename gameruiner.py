import pyautogui as pt
import time

# time to switch tabs GO GO GO
time.sleep(5)

# console location = Point(x=1535, y=86)
# place where typing is for console = Point(x=1485, y=496)
# Game.RuinTheFun(1); is the commnand

def ruinthegame():
    pt.hotkey("ctrl", "shift", "c") # open inspect element
    time.sleep(0.3) # python is slow i use sleep
    pt.moveTo(1535, 86)
    time.sleep(0.3)
    pt.click(1535, 86) # clicks on console
    time.sleep(0.3)
    pt.moveTo(1485, 496)
    time.sleep(0.3)
    pt.click(1485, 496) # clicks on typing area
    time.sleep(0.3)
    pt.typewrite("Game.RuinTheFun(1);") # ruin the game command
    time.sleep(0.3)
    pt.hotkey("enter") # congrats, you ruined the game

ruinthegame() # runs the shit
