#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import set_joint_trajectory

#record
import pyaudio
import wave

#docomo api 
import requests
#import json

#codama wakeup word detect
import RPi.GPIO as GPIO

#openJtalk
import jtalk
import time

from record2text import record2text

import subprocess
from subprocess import PIPE

#sound library for ラジオ体操
import pygame

import re

#class instance
codama = set_joint_trajectory.robot_pose([0,90,0])
#codama.joint_trajectory([4,4,4],30)
#codama.joint_trajectory([11,11,11],60)
#codama.joint_trajectory([7,7,7],30)
#def trans_angle(ang):
#        return 11-7*ang/180

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN)
while True:
    if GPIO.input(27) == GPIO.HIGH:
        print("detected")
        
        #Getting direction of audio angle 
        proc = subprocess.run(["./codama_i2c DOAANGLEKWD"],cwd = "/home/pi/codama/codama-doc-r0/utils",stdout=PIPE, shell=True)
        angle=proc.stdout.decode("utf8")
        print(angle)
        angle = int(re.sub(r'\D','',angle))
        
        #振り返る 
        codama.joint_trajectory([0,90,angle],5)
        time.sleep(1)

        #codama.joint_trajectory([0,90,angle],30)
        #time.sleep(1)
        codama.joint_trajectory([30,90,angle],10)
        #codama.joint_trajectory([0,0,0],30)
        #codama.joint_trajectory([180,180,180],30)
        #codama.joint_trajectory([0,0,angle],30)
        #codama.joint_trajectory([0,0,angle],30)
        #最近話しかけていないver
        jtalk.jtalk("おかえり。でも最近話しかけてくれないね、寂しいな。")
        time.sleep(4)
        
        ####運動不足ver########
        
        #jtalk.jtalk("お帰り。実はわたしはあなたの健康状態とリンクしているの。肩もこってるし腰が痛くてもう動けない。最近、運動不足でしょ。これを踊って運動不足解消してね。")
        #time.sleep(13)
        #pygame.mixer.init()
        #pygame.mixer.music.load("radio_exercise.mp3")
        #pygame.mixer.music.play(-1)
        #time.sleep(20)
        #pygame.mixer.music.stop()
        
        #####################
        
        while True:
            record_text = record2text()
            
            if "ごめん" in record_text:
                jtalk.jtalk("そうだね、でもごめんねは誰でも言えるよ、もう一度出直してきたら。")
                time.sleep(6)
                codama.joint_trajectory([20,90,0],10)
                time.sleep(1)
            elif "すき" in record_text or "好き" in record_text:
                jtalk.jtalk("こういうときだけ、言うんだ。いつもは言わないのにね。")
                time.sleep(6)
                codama.joint_trajectory([20,90,180],10)
                time.sleep(1)
            elif "お菓子" in record_text or "お貸し" in record_text or "おかし" in record_text:
                jtalk.jtalk("ふーん、特別に許してあげる")
                codama.joint_trajectory([20,90,angle+30],30)
                codama.joint_trajectory([20,90,angle-30],30)
                codama.joint_trajectory([20,90,angle+30],30)
                codama.joint_trajectory([20,90,angle-30],30)
                codama.joint_trajectory([20,90,angle+30],30)
                codama.joint_trajectory([20,90,angle-30],30)
                break
            else:
                jtalk.jtalk("そんなこと今さら言われてもな。まだ許す気にはなれない。")
                time.sleep(5)
                codama.joint_trajectory([20,90,30],1)
                #codama.joint_trajectory([11,11,11],30)
                time.sleep(1)
        break
    #print("not detected")




