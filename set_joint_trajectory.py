#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import numpy as np

#servo可動範囲: 4 11

class robot_pose:
    def __init__(self, init_pose = [90, 90, 90], io_pins = [4, 5, 6]):
        self.io_pins = io_pins
        joints = self.deg_to_com(init_pose)
        self.pose = joints

        GPIO.setmode(GPIO.BCM)
        self.pwm_out = []

        for pin_i, pin in enumerate(self.io_pins):
            # PWM出力の設定
            GPIO.setup(pin, GPIO.OUT)
            self.pwm_out.append(GPIO.PWM(pin, 50))
            self.pwm_out[-1].start(0)

            # 初期姿勢の設定
            self.pwm_out[-1].ChangeDutyCycle(self.pose[pin_i])

    def deg_to_com(self, angles):
        joints = []

        for angle in angles:
            joints.append(11 - 7 * angle / 180)

        return joints

    def joint_trajectory(self, angles, flame_num):
        jt = [0, 0, 0]

        joints = self.deg_to_com(angles)

        for i, joint in enumerate(joints):
            jt[i] = np.linspace(self.pose[i], joint, flame_num)

        for i in range(flame_num):
            for pin_i, pin in enumerate(self.io_pins):
                self.pwm_out[pin_i].ChangeDutyCycle(jt[pin_i][i])
            time.sleep(0.03)

        self.pose = joints
        
    def servo_off(self):
        for pin_i, pin in enumerate(self.io_pins):
            self.pwm_out[pin_i].ChangeDutyCycle(0)

"""
codama = robot_pose()
codama.joint_trajectory([4, 4, 4], 30)
codama.joint_trajectory([11, 11, 11], 60)
codama.joint_trajectory([7, 7, 7], 30)
codama.servo_off()
"""
