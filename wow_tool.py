import pyautogui
from AppKit import NSWorkspace
from Cocoa import NSRunningApplication, NSApplicationActivateIgnoringOtherApps

#wow正在前台
def isWowForeground():
    return NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName'] == "Wow"
    #return True

def recordMousePositionAndColor():
    mousePosition = pyautogui.position()
    pixel = pyautogui.pixel(mousePosition.x, mousePosition.y)
    print("XY:{} RGB:{}",mousePosition, pixel)

def recordTargetRed():
    pixel = pyautogui.pixel(461, 981)
    print("RGB:{}", pixel)

#游戏循环
while True:
    if isWowForeground():
        recordTargetRed()
    else:
        print("游戏未开始")
    pyautogui.sleep(3)