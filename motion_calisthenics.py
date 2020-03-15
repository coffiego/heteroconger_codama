#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#servo可動範囲: 0 180

import set_joint_trajectory
#codama = set_joint_trajectory.robot_pose([0, 90, 90])

#rhythm = 15
#rhythm2 = 20
# 前奏
def radio_exercise(codama,rhythm, rhythm2): 
    codama.joint_trajectory([30, 90, 90], rhythm)
    codama.joint_trajectory([0, 90, 90], rhythm)
    codama.joint_trajectory([30, 90, 90], rhythm)
    codama.joint_trajectory([0, 90, 90], rhythm)
    codama.joint_trajectory([30, 90, 90], rhythm)
    codama.joint_trajectory([0, 90, 90], rhythm)
    codama.joint_trajectory([30, 90, 90], rhythm)
    codama.joint_trajectory([0, 90, 90], rhythm)

    codama.joint_trajectory([60, 130, 90], rhythm2)
    codama.joint_trajectory([60, 110, 90], rhythm2)
    codama.joint_trajectory([60, 130, 90], rhythm2)

    codama.joint_trajectory([0, 80, 90], rhythm2)
    codama.joint_trajectory([0, 60, 90], rhythm2)
    codama.joint_trajectory([0, 80, 90], rhythm2)

    codama.joint_trajectory([60, 130, 90], rhythm2)
    codama.joint_trajectory([60, 110, 90], rhythm2)
    codama.joint_trajectory([60, 130, 90], rhythm2)

    codama.joint_trajectory([0, 80, 90], rhythm2)
    codama.joint_trajectory([0, 60, 90], rhythm2)
    codama.joint_trajectory([0, 80, 90], rhythm2)
    codama.joint_trajectory([60, 130, 90], rhythm2)
    codama.joint_trajectory([60, 110, 90], rhythm2)
    codama.joint_trajectory([60, 130, 90], rhythm2)

    codama.joint_trajectory([0, 80, 90], rhythm2)
    codama.joint_trajectory([0, 60, 90], rhythm2)
    codama.joint_trajectory([0, 80, 90], rhythm2)

    codama.joint_trajectory([60, 130, 90], rhythm2)
    codama.joint_trajectory([60, 110, 90], rhythm2)
    codama.joint_trajectory([60, 130, 90], rhythm2)

    codama.joint_trajectory([0, 80, 90], rhythm2)
    codama.joint_trajectory([0, 60, 90], rhythm2)
    codama.joint_trajectory([0, 80, 90], rhythm2)

