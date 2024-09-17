import random
import colorama as color
import os
import sys
import pygame
randomExitText = ["<Yukari> 再见...希望我们还能再见。", "<Melted> 再见", "<minqwq> by", "<白九> 晚安", "<Rick Astley> Say goodbye", "<mcpe> 没事，再见"]
pygame.mixer.init()
pygame.mixer.music.load("./music/Final_Fight_--_minqwq_usedformsl.mp3")
pygame.mixer.music.play()
print("minqwq's life | minqwq 的一生 | (v0.1uncon) by minqwq 和他的几个朋友")
print("[" + color.Fore.LIGHTRED_EX + "!" + color.Fore.LIGHTWHITE_EX + "] 极早期开发阶段，不代表正式后效果。")
print("请选择选项...")
print("\n1:新的一生")
print("2:选择特定章节(不会做保存功能)")
print("3:睡觉(退出)")
space = 0
while True:
    selectButton = input("> ")
    if selectButton == "1":
        pygame.mixer.music.stop()
        os.system("python3 ./chapter/1/1/index.py")
    elif selectButton == "2":
        os.system("python3 selectchapter.py")
        pygame.mixer.music.stop()
    elif selectButton == "3":
        random.shuffle(randomExitText)
        randomExitTextPrinted = randomExitText[0]
        print(randomExitTextPrinted)
        break
        sys.exit()
