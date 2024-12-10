# Chapter 1-1 by minqwq
import pygame
import os
import sys
import time

def printa(text):
    for i in text:
        print(i, end="", flush=True)
        time.sleep(0.05)
    print("")

pygame.mixer.init()
pygame.mixer.music.load("./music/You,_and_nothing,_but_you_still_happy_--_minqwq.mp3")
pygame.mixer.music.play()
print("幻想乡，某座山上 | 2017-04-08")
input("") # 这个东西表示"按下enter键显示下一句" | minqwq | 2024-09-12
printa("<???> 抱歉----麻烦能打扰一下吗？")
input("")
printa("我听到一个可爱的声音叫住了我。")
input("")
printa("<???> 厕...厕所在哪里？")
input("")
printa("<minqwq> 这条路前面有个分岔路口，你左转应该就能看到了。")
input("")
printa("<???> (快速离开)")
input("")
printa("这座山是我们这为数不多的景点")
input("")
printa("但是风景非常优美")
input("")
printa("常常会吸引许多人来此地旅游")
input("")
printa("<???> 抱歉，我还是没找到，能带我去吗？")
input("")
printa("<minqwq> ...好吧。")
input("")
printa("第一次被一个女生这样跟着，我的心嘭嘭直跳。")
input("")
printa("<minqwq> 好了，就是这里")
input("")
printa("<???> 谢谢~")
input("")
printa("她走进了厕所。")
input("")
printa("回家的路上，我仍然忘不了这如此甜美的声音")
pygame.mixer.music.stop()
os.system("python ./chapter/1/2/index.py")
