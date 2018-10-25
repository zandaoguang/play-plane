#coding=utf-8
import pygame
import random
import time
from pygame.locals import *


class HeroPlane(object):
    def __init__(self,screen):
        #设置飞机默认的xy值
        self.x=180
        self.y=600
        self.screen=screen
        self.imageName='./feiji/hero.gif'
        self.image=pygame.image.load(self.imageName).convert()
        self.bulletList=[]
        self.needRemoveList=[]
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        for bullet in self.bulletList:
            bullet.display()
            bullet.move()
        for bullet in self.bulletList:
            if bullet.judgeOut():
                self.needRemoveList.append(bullet)
        for bullet in self.bulletList:
            if bullet in self.needRemoveList:
                self.bulletList.remove(bullet)
    def move(self,opt):
        if opt=='left':
            self.x-=15
        elif opt=='right':
            self.x+=15
        elif opt=='up':
            self.y-=15
        elif opt=='down':
            self.y+=15
    def shoot(self):
        newBullet=Bullet(self.screen,self.x,self.y)
        newBulletLeft=BulletSmall(self.screen,self.x,self.y)
        newBulletRight=BulletSmall(self.screen,self.x+64,self.y+20)
        self.bulletList.append(newBulletLeft)
        self.bulletList.append(newBulletRight)
        self.bulletList.append(newBullet)

class EnemyPlane(object):
    def __init__(self,screen):
        #设置飞机默认的xy值
        self.x=random.randint(0,420)    
        self.y=0
        self.screen=screen
        self.imageName='./feiji/enemy-1.gif'
        self.image=pygame.image.load(self.imageName).convert()
        self.bulletList=[]
        self.needRemoveList=[]
        self.direction='right'
    def move(self):
        if self.direction=='right':
            self.x+=2
        elif self.direction=='left':
            self.x-=2
        if self.x>420:
            self.direction='left'
        elif self.x<10:
            self.direction='right'
        
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        for bullet in self.bulletList:
            bullet.display()
            bullet.move()
        for bullet in self.bulletList:
            if bullet.judgeOut():
                self.needRemoveList.append(bullet)
        for bullet in self.bulletList:
            if bullet in self.needRemoveList:
                self.bulletList.remove(bullet)


    def shoot(self):
        num=random.randint(1,30)
        if num==22:
            enemyBullet=EnemyBullet(self.screen,self.x,self.y)
            self.bulletList.append(enemyBullet)
        
class EnemyBullet(object):
    def __init__(self,screen,x,y):
        self.x=x+20
        self.y=y+28
        self.screen=screen
        self.imageName='./feiji/bullet-2.gif'
        self.image=pygame.image.load(self.imageName).convert()
    def display(self):
        self.screen.blit(self.image,(self.x,self.y)) 
    def move(self):
        self.y+=5
    def judgeOut(self):
        if self.y<-980:
            return True
        else:
            return False

class Bullet(object):
    def __init__(self,screen,x,y):
        self.x=x+40
        self.y=y-20
        self.screen=screen
        self.imageName='./feiji/bullet-3.gif'
        self.image=pygame.image.load(self.imageName).convert()
    def display(self):
        self.screen.blit(self.image,(self.x,self.y)) 
    def move(self):
        self.y-=2
    def judgeOut(self):
        if self.y<0:
            return True
        else:
            return False
class BulletSmall(object):
    def __init__(self,screen,x,y):
        self.x=x+16
        self.y=y+20
        self.screen=screen
        self.imageName='./feiji/bullet-1.gif'
        self.image=pygame.image.load(self.imageName).convert()
    def display(self):
        self.screen.blit(self.image,(self.x,self.y)) 
    def move(self):
        self.y-=6
    def judgeOut(self):
        if self.y<0:
            return True
        else:
            return False

if __name__ == "__main__":

    #1. 创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((480,890),0,32)

    #2. 创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load("./feiji/background.png").convert()
    #hero = pygame.image.load("./feiji/hero.gif").convert()
    heroPlane=HeroPlane(screen) 
    enemyPlane=EnemyPlane(screen)
    enemyPlane2=EnemyPlane(screen)

    #3. 把背景图片放到窗口中显示
    while True:

    #设定需要显示的背景图
        screen.blit(background,(0,0))
        #screen.blit(hero,(x,y))
        heroPlane.display()
        enemyPlane.shoot()
        enemyPlane.display()
        enemyPlane.move()
        
        enemyPlane2.shoot()
        enemyPlane2.display()
        enemyPlane2.move()
        #获取事件，比如按键等
        for event in pygame.event.get():

        #判断是否是点击了退出按钮
            if event.type == QUIT:
                print("exit")
                exit()
            #判断是否是按下了键
            elif event.type == KEYDOWN:
            #检测按键是否是a或者left
                if event.key == K_a or event.key == K_LEFT:
                    print('left')
                    heroPlane.move('left')    
            #检测按键是否是d或者right
                elif event.key == K_d or event.key == K_RIGHT:
                    heroPlane.move('right')
                    print('right')
                   
            #检测按键是否是空格键
                elif event.key == K_w or event.key == K_UP:
                    heroPlane.move('up')
                    print('up')
                elif event.key == K_s or event.key == K_DOWN:
                    heroPlane.move('down')
                    print('down')


                elif event.key == K_SPACE:
                    print('space')
                    heroPlane.shoot()
        time.sleep(0.01)        
        #更新需要显示的内容
        pygame.display.update()
