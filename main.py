import random
import colorama as color
import os
import sys
import pygame
import time
isWindows = "null"
def slowprint(text):
    for j in text:
        print(j, end="", flush=True)
        time.sleep(0.22)
    print()
    print("\r")
winorlin = input("Windows or Linux?\n1:Windows\n2:Linux\n> ")
if winorlin == "1":
    isWindows = True
elif winorlin == "2":
    isWindows = False
def clearScreen():
    if isWindows == True:
        os.system("cls")
    elif isWindows == False:
        os.system("clear")
pygame.mixer.init()
clearScreen()
pygame.mixer.music.load("./se/init.mp3")
pygame.mixer.music.play()
slowprint("Flandre Studio & 0x1c Studio")
clearScreen()
print("Flandre Studio & 0x1c Studio", end="\r")
slowprint(color.Fore.LIGHTRED_EX + "Flandre Studio & 0x1c Studio" + "\033[0m")
time.sleep(2.88)
clearScreen()
randomExitText = ["<Yukari> 再见...希望我们还能再见。", "<Melted> 再见", "<minqwq> by", "<白九> 晚安", "<Rick Astley> Say goodbye", "<mcpe> 没事，再见"]
space = 0
pygame.mixer.music.load("./music/main.mp3")
pygame.mixer.music.play()
while True:
    print("minqwq's life | minqwq 的一生 | (v0.3) by minqwq 和他的几个朋友")
    print("[" + color.Fore.LIGHTRED_EX + "!" + "\033[0m" + "] 早期开发阶段，不代表正式后效果。")
    print("请选择选项...")
    print("\n1:新的一生")
    print("2:选择特定章节(不会做保存功能)")
    print("3:睡觉(退出)")
    selectButton = input("> ")
    if selectButton == "1":
        pygame.mixer.music.stop()
        if isWindows == True:
            os.system("python chapter\\1\\c1s1.py")
        elif isWindows == False:
            os.system("python ./chapter/1/c1s1.py")
    elif selectButton == "2":
        pygame.mixer.music.stop()
        os.system("python selectchapter.py")
    elif selectButton == "3":
        random.shuffle(randomExitText)
        randomExitTextPrinted = randomExitText[0]
        print(randomExitTextPrinted)
        break
        sys.exit()
    else:
        clearScreen()
