#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#servo motion file
import set_joint_trajectory
#record
import pyaudio
import wave
#docomo api 
import requests
#codama wakeup word detect
import RPi.GPIO as GPIO
#openJtalk
import jtalk
import time
#import record2text.py file 音声認識用
from record2text import record2text
#to get angle of audio direction by codama 
import subprocess
from subprocess import PIPE
#sound library for ラジオ体操or流したい曲
import pygame
#文字列から数字だけ取り出す用
import re

#joint trajectory instance
codama = set_joint_trajectory.robot_pose([0,0,0])

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN)
while True:
    if GPIO.input(27) == GPIO.HIGH:
        print("detected")
        
        #Getting direction of audio angle 
        proc = subprocess.run(["./codama_i2c DOAANGLEKWD"],cwd = "/home/pi/codama/codama-doc-r0/utils",stdout=PIPE, shell=True)
        angle=proc.stdout.decode("utf8")
        print(angle)
        angle = int(re.sub(r'\D','',angle)) #remove letters except number then change to int type 

        codama.joint_trajectory([0,0,angle],30)

        #最近話しかけていないver
        jtalk.jtalk("おかえり。でも最近話しかけてくれないね、寂しいな。もう知らない。", sp=0.5)
        time.sleep(6)
        
        ####運動不足ver########
        
        #jtalk.jtalk("お帰り。実はわたしはあなたの健康状態とリンクしているの。肩もこってるし腰が痛くてもう動けない。最近、運動不足でしょ。これを踊って運動不足解消してね。")
        #time.sleep(13)
        #pygame.mixer.init()
        #pygame.mixer.music.load("yourmusic.mp3")
        #pygame.mixer.music.play(-1)
        #time.sleep(20)
        #pygame.mixer.music.stop()
        
        #####################

        record_text = record2text()
        if "ごめん" in record_text:
            codama.joint_trajectory([180,180,180],60)
            jtalk.jtalk("こんにちは、ごめんねは誰でも言えるよ、もう一度出直してこい")
        elif "すき" in record_text or "好き" in record_text:
            codama.joint_trajectory([180,180,180],30)
            jtalk.jtalk("こういうときだけ、言うんだ。いつもは言わないのにね。")
        else:
            jtalk.jtalk("ふーん、特別に許してあげる")
            codama.joint_trajectory([90,90,90],30)

            codama.joint_trajectory([110,110,110],30)
            codama.joint_trajectory([70,70,70],30)
            codama.joint_trajectory([110,110,110],30)
        break
    #print("not detected")




