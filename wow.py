import pyautogui
from AppKit import NSWorkspace
from Cocoa import NSRunningApplication, NSApplicationActivateIgnoringOtherApps

#战斗记录
Fighting = False

#攻击记录 f6普通攻击 f7终结技能

#移动记录（j）
MoveRecord = 0
MoveMaxTry = 50

#连续杀怪数量
KillMonster = 0


#是否有目标
def hasTargetEnemy():
    print("检查是否有敌人")
    return pyautogui.pixelMatchesColor(328, 44, (203, 18, 13))

#是否刚刚战斗结束
def isFightOver():
    print("是否结束战斗")
    return Fighting

#检查攻击距离
def checkAttackDistance():
    print("检查攻击距离")
    return pyautogui.pixelMatchesColor(461, 981, (207, 196, 156))

#开始攻击
def attack():
    print("攻击目标")
    pyautogui.press('j')
    if pyautogui.pixelMatchesColor(561, 47, (88, 17, 20)) :
        pyautogui.press('f6')
    else:
        pyautogui.press('f7')

#走向目标
def moveToTarget():
    global MoveRecord
    global MoveMaxTry
    if MoveRecord < MoveMaxTry:
        MoveRecord = MoveRecord + 1
        print("走向目标")
        pyautogui.press('j')
    else:
        moveFaild()

#移动失败
def moveFaild():
    print("走不到目标")
    print('\7')

#拾取宝物
def pickupTreasure():
    print("拾取宝物")
    pyautogui.rightClick(959,525)
    pyautogui.press('f9')

#搜索敌人
def searchTarget():
    global Fighting
    print("搜索敌人")
    pyautogui.press('f5')
    if hasTargetEnemy():
        Fighting = True

#休息恢复
def rest():
    global KillMonster
    if KillMonster > 2:
        KillMonster = 0
        pyautogui.press('f8')
        pyautogui.sleep(20)

#wow正在前台
def isWowForeground():
    return NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName'] == "Wow"

#机器人AI（每次只执行一个动作）
def aiMind():
    global Fighting
    global MoveRecord
    global KillMonster
    if hasTargetEnemy():
        if checkAttackDistance():
            attack()
        else:
            moveToTarget()
    else:
        if isFightOver() :
            KillMonster = KillMonster + 1
            Fighting = False
            MoveRecord = 0
            pickupTreasure()
            rest()
        else:
            searchTarget()

#机器人大脑
while True:
    if isWowForeground():
        aiMind()
    else:
        print("游戏未开始")
    
    #每次执行动作完都停顿一下
    pyautogui.sleep(0.3)