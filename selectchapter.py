import os
import sys
import pygame
pygame.mixer.init()
print("选择章节...")
selectedChapter = input("请按此格式输入章节:大章/小章\n示例:1/2\n> ")
os.system("python ./chapter/" + selectedChapter + "/index.py")

