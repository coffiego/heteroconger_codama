#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 15:32:37 2020

@author: shungokoyama
"""

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

from motion_calisthenics import radio_exercise

#class instance
codama = set_joint_trajectory.robot_pose([0,90,0])#5,4,6
#codama.joint_trajectory([4,4,4],30)
#codama.joint_trajectory([11,11,11],60)
#codama.joint_trajectory([7,7,7],30)

#def trans_angle(ang):
#    return 11-7*ang/180


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
        
        #振り返る
        codama.joint_trajectory([30,90,angle],30)#起き上がる
        time.sleep(0.5)
        #codama.joint_trajectory([30,90,angle],30)#回って振り返る
        
        #元気ないモーション
        jtalk.jtalk("おかえりなさい。いててて。いてててて。",sp=0.5)
        time.sleep(4)
        codama.joint_trajectory([0,60,angle],50)#疲れて屈む
       
        #ユーザーの音声認識
        #record_text = record2text()
        time.sleep(2)
        jtalk.jtalk("最近ちょっと腰が痛くて。デスクワークのしすぎだよ。",sp=0.8)
        time.sleep(6)
        codama.joint_trajectory([30,90,angle],2)
        jtalk.jtalk("いっちょ体操でもしますか。",sp=1.1)
        time.sleep(4) 
                
        pygame.mixer.init()
        pygame.mixer.music.load("radio_exercise.mp3")
        pygame.mixer.music.play(-1)
        time.sleep(5)
        radio_exercise(codama,15,20)
        time.sleep(20)
        pygame.mixer.music.stop()
        
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




