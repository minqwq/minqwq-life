import os
import sys
import pygame
os.system("clear")
os.system("cls")
print("选择章节...")
selectedChapter = input("请输入章节号\n> ")
os.system("python ./chapter/c" + selectedChapter + ".py")

