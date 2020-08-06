#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import sys
from bullet import Bullet


def check_keydown_events(event, ship, ai_settings, screen, bullets):
    """响应键盘按下操作"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ship, ai_settings, screen, bullets)


def check_keyup_events(event, ship):
    """响应键盘按下操作"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship, ai_settings, screen, bullets):
    """响应鼠标和键盘事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, ai_settings, screen, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(screen, settings, ship, bullets):
    """更新窗口，并重绘窗口内容"""
    # 更新窗口
    screen.fill(settings.bg_color)
    # 重绘飞船
    ship.blitme()

    # 重绘子弹序列
    for bullet in bullets:
        bullet.draw_bullet()

    # 重绘屏幕
    pygame.display.flip()


def update_bullets(bullets):
    """更新子弹位置并删除消失的子弹"""
    # 更新子弹位置
    bullets.update()
    # 删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(ship, ai_settings, screen, bullets):
    """如果子弹个数没超过限制，则发射（创建）新子弹"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)