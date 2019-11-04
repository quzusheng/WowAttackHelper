import pyautogui
from AppKit import NSWorkspace
from Cocoa import NSRunningApplication, NSApplicationActivateIgnoringOtherApps

def isWowForeground():
    return NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName'] == "Wow"
    #return True

def recordMousePositionAndColor():
    mousePosition = pyautogui.position()
    pixel = pyautogui.pixel(mousePosition.x, mousePosition.y)
    print("XY:{} RGB:{}",mousePosition, pixel)

def recordTargetRed():
    pixel = pyautogui.pixel(180, 65)
    print("RGB:{}", pixel)


while True:
    if isWowForeground():
        recordTargetRed()
    else:
        print("游戏未开始")
    pyautogui.sleep(3)