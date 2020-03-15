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

#class instance
codama = set_joint_trajectory.robot_pose([0,60,0])#5,4,6
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
        codama.joint_trajectory([30,90,0],30)#起き上がる
        #time.sleep(0.5)
        codama.joint_trajectory([0,90,angle],20)#回って振り返る
        codama.joint_trajectory([40,90,angle],20)#回って振り返る
        
        #おかえり
        jtalk.jtalk("おかえりなさい。もうねむくなっちゃった。",sp=0.5)
        codama.joint_trajectory([30,90,angle],20)#回って振り返る
        codama.joint_trajectory([50,90,angle],20)#回って振り返る
        codama.joint_trajectory([30,90,angle],20)#回って振り返る
        codama.joint_trajectory([50,90,angle],20)#回って振り返る
        codama.joint_trajectory([30,90,angle],20)#回って振り返る
        
        time.sleep(5)
        #倒れる
        codama.joint_trajectory([90,0,angle],2)#倒れる
        time.sleep(1)
        #おやすみ
        jtalk.jtalk("おやすみなさい。",sp=1.1)
        time.sleep(2)
        codama.joint_trajectory([0,0,angle],2)#倒れる

                
        #####################

        break
    #print("not detected")




