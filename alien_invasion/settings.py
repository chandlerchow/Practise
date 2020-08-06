#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Settings(object):
    """存储游戏的所有设置的类"""

    def __init__(self):
        """存储游戏的相关参数设置"""
        # 窗口的设置
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_speed_factor = 1.1

        # 子弹的设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_speed_factor = 2
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 20
