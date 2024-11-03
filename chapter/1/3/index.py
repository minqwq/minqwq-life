import os
import sys
import tqdm
import pygame
import time

def printa(text):
    for i in text:
        print(i, end="", flush=True)
        time.sleep(0.05)
    print("")

pygame.mixer.init()
se_boom = pygame.mixer.Sound("./se/boom.mp3")
se_beep = pygame.mixer.Sound("./se/beep.mp3")
se_sti1 = pygame.mixer.Sound("./se/shooting1.mp3")
se_sti2 = pygame.mixer.Sound("./se/shooting2.mp3")
se_dialup = pygame.mixer.Sound("./se/dial-modem-sound-effect-042160010_nw_prev_new.mp3")
printa("幻想乡，727号公路旁的枫叶林，min家 | 2017-04-10")
pygame.mixer.music.load("./music/Year-Round_Absorbed_Curiosity_Chiptune_remix_and_no_main_melody__--_minqwq.mp3")
pygame.mixer.music.play()
print("音乐:Year-Round Absorbed Curiosity(Chiptune remix and no main melody) | by minqwq")
printa("<minqwq> (伸腰)")
input()
printa("然后远处传来了爆炸声。")
input()
printa("<minqwq> ?")
input()
printa("我从窗外看去。")
input()
printa("我看到了两个人在用弹幕战斗。")
input()
se_sti1.play()
printa("<???> 啊啊啊啊啊啊！！！！！！")
input()
se_sti2.play()
printa("<???> 哈--------！！！！")
input()
printa("...没动静了？")
input()
printa("好像有一方受伤了...")
input()
printa("<minqwq> 我可能需要打个救护车过来...")
input()
se_beep.play()
printa("(启动电脑...)")
input()
print("* Screen View *")
input()
print("PY OS Improved 2.6.1_pre")
while True:
    pcloginuser = input("Localhost login: ")
    if pcloginuser == "minqwq":
        break
    else:
        print("Unknown user, please retry...(tips:minqwq)")
print("Welcome to PY OS Improved!")
print("tips:type 'mail'")
print("autoexec.py | Line 1 | dialup")
se_dialup.play()
print("Network connecting")
for i in range(16):
    print(".", end = "", flush = True)
    time.sleep(1)
# time.sleep(16)
print("\nWelcome to the Internet!")
print("You dont have any new mail received.")
while True:
    cmd = input("/ # ")
    if cmd == "mail":
        break
    else:
        print("Type 'mail'")
print("emergency@genhospital.moe\nFrom:minqwq\nTitle:这里有一个女孩受伤了\nContent:\n位置:727号公路旁树林\n如需详细位置，请回邮。")
input()
print("* Player View *")
input()
printa("<minqwq> 好，发送")
input()
printa("伴随着一阵刺耳的拨号上网音，邮件成功发出去了。")
input()
printa("另外说一下，因为这是幻想乡，所以因为弹幕受伤的不在少数")
input()
printa("接下来就是等着了。")
input()
