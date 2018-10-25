#!/usr/bin/python
#coding=utf-8
import pygame

if __name__ =="__main__":
    #创建一个窗口
    screen=pygame.display.set_mode((480,890),0,32)
    #图片导入窗口
    background =pygame.image.load('./feiji/background.png').convert()
    #图片放入窗口显示
    i=1
    while i<1000:
        screen.blit(background,(0,0))
        pygame.display.update()
        i+=1

