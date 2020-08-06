#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame


class Ship(object):

    def __init__(self, settings, screen):
        """初始化飞船，包括其关联的窗口、图像、图像位置"""
        self.screen = screen
        self.ai_settings = settings

        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        self.rect.centerx = self.screen.get_rect().centerx
        self.rect.bottom = self.screen.get_rect().bottom
        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        """更新飞船状态"""
        if self.moving_right and self.rect.right < self.screen.get_rect().right:
            self.center = self.rect.centerx + self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center = self.rect.centerx - self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
