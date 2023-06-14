#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 12 21:08:57 2023

@author: liuzhining
"""
#arialunicode
#songti
import os
import pygame
import random
import pandas as pd
import requests
from bs4 import BeautifulSoup
import sys
py=pygame

pygame.init()
running=True
WIDTH=900
HEIGHT=700
g_WIDTH=WIDTH*3/8
g_HEIGHT=HEIGHT/2
FPS=60
all_map=[]
clock=py.time.Clock()
window = pygame.display.set_mode((WIDTH,HEIGHT ))
class pos:
    result= [
    ["在路上撿到一張樂透",150],
    ["報名奧運獲得金牌",200],
    ["路過動物園遇到獅子出逃 損失門票錢",-100],
    ["被卡車司機送去轉生",-150],
   [ "去非洲投資晶圓廠失敗",-150],
   [ "投資虛擬貨幣獲利",150],
   [ "投資蘋果股票獲利",150],
   [ "早餐電奶茶喝到中午 食物中毒",-200],
   [ "投資小美人魚真人版 損失慘重",-200],
   [ "見義勇為舉發捷運色狼",150],
   [ "接到詐騙集團“你女兒在我手上”的電話",-300],
   [ "爬金字塔頂端被罰款",-200],
   [ "在西馬拉雅山煮火鍋 被罰款",-150],
   [ "走在路上遇到 Mr.Beast發錢",400],
   [ "馬麻發零用錢",350],
   [ "在路上遇到貓貓 買飼料罐頭",-100]
]
    current=0
    width=WIDTH
    height=HEIGHT
    center=(width/2,height/2)
    width_block_num=4
    height_block_num=5#*****************************************************************
    corner_1=width_block_num+1
    corner_2=width_block_num + height_block_num + 2
    corner_3=2 * width_block_num + height_block_num + 3
    corners=[0,corner_1,corner_2,corner_3]
    font1 = "arialunicode"
    font2="songti"
    
    block_width=g_WIDTH/(width_block_num)
    block_height=g_HEIGHT/(height_block_num)
    all_block_num=4+2*(width_block_num+height_block_num)
    grass_size=(g_WIDTH,g_HEIGHT)
    g_t = height / 2 - grass_size[1] / 2
    g_b = height / 2 + grass_size[1] / 2
    g_l = width / 2 - grass_size[0] / 2
    g_r = width / 2 + grass_size[0] / 2
    dice_left_position=((g_l-block_width)/2,height*3/4)
    dice_right_position=(width-((g_l-block_width)/2),height*3/4)
    
    left_center=(g_l-block_width)/2
    right_center=width-left_center
    last_question="default_q"
    last_word=["default1","default2","default3"]
    last_ans=0
    roundd=["first","second","third","forth","final"]
    combo_dollar=[20,25,30,35,40]
    voc_data=['vocabulary/vocabulary1200.csv','vocabulary/4000_7000.csv','my_vocabulary.xlsx']
    current_voc="vocabulary/vocabulary1200.csv"
    
    url='https://dictionary.cambridge.org/zht/詞典/英語/'
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }
    
class image:
    temp=pygame.image.load("pic/background.png").convert()
    background=pygame.transform.scale(temp,(WIDTH,HEIGHT))
    
    temp=pygame.image.load("pic/back2.jpg").convert()
    background2=pygame.transform.scale(temp,(WIDTH,HEIGHT))
    
    temp=pygame.image.load("pic/grass2.jpg").convert()
    grass=pygame.transform.scale(temp,pos.grass_size)
    
    destiny_width=pos.grass_size[0]*(9/10)
    temp = pygame.image.load("pic/destiny.png").convert_alpha()
    temp1 = temp.get_rect()
    destiny = pygame.transform.scale(temp, (destiny_width, destiny_width * (temp1.height / temp1.width)))
    
    destiny_height=destiny_width * (temp1.height / temp1.width)
    temp = pygame.image.load("pic/chance.png").convert_alpha()
    temp1 = temp.get_rect()
    chance = pygame.transform.scale(temp, (destiny_width, destiny_height))
    
    temp = pygame.image.load("pic/word_voc.png").convert_alpha()
    temp1 = temp.get_rect()
    word_voc= pygame.transform.scale(temp, (pos.block_height*(temp1.width/temp1.height),pos.block_height))
    
    temp = pygame.image.load("pic/voc_finish.png").convert_alpha()
    temp1 = temp.get_rect()
    voc_finish= pygame.transform.scale(temp, (pos.block_height*(temp1.width/temp1.height),pos.block_height))
    
    buttons=[]
    destiny_height=destiny_width * (temp1.height / temp1.width)
    temp = pygame.image.load("pic/button.jpg").convert_alpha()
    temp1 = temp.get_rect()
    button_r = pygame.transform.scale(temp, (pos.block_width, pos.block_height))
    buttons=[pygame.transform.rotate(button_r,-90),pygame.transform.rotate(button_r,90),pygame.transform.rotate(button_r,180),button_r]
    
    word_width=pos.block_width*(8/10)
    temp = pygame.image.load("pic/word_start.png").convert_alpha()
    temp1 = temp.get_rect()
    word_start = pygame.transform.scale(temp, (word_width, word_width * (temp1.height / temp1.width)))
    word_start.set_colorkey((255, 255, 255))

    temp = pygame.image.load("pic/word_built.png").convert_alpha()
    temp1 = temp.get_rect()
    word_built = pygame.transform.scale(temp, (word_width, word_width * (temp1.height / temp1.width)))
    word_built.set_colorkey((255, 255, 255))

    temp = pygame.image.load("pic/word_battle.png").convert_alpha()
    temp1 = temp.get_rect()
    word_battle = pygame.transform.scale(temp, (word_width, word_width * (temp1.height / temp1.width)))
    word_battle.set_colorkey((255, 255, 255))

    temp = pygame.image.load("pic/word_destiny.png").convert_alpha() 
    temp1 = temp.get_rect()
    word_destiny = pygame.transform.scale(temp, (word_width, word_width * (temp1.height / temp1.width)))
    word_destiny.set_colorkey((255, 255, 255))

    temp = pygame.image.load("pic/word_chance.png").convert_alpha()
    temp1 = temp.get_rect()
    word_chance = pygame.transform.scale(temp, (word_width, word_width * (temp1.height / temp1.width)))
    word_chance.set_colorkey((255, 255, 255))
    word_height=word_width * (temp1.height / temp1.width)
    
    temp = pygame.image.load("pic/gameover2.png").convert_alpha()
    temp1 = temp.get_rect()
    gameover = pygame.transform.scale(temp, (pos.block_width*4/3, pos.block_width*4/3 * (temp1.height / temp1.width)))
    
    building_height=(pos.block_height-word_height)/2
    
    player=['1','2','3']
    books=[]
    reminder=[0,0]
    player_width=pos.block_width
    
    temp2="player/"+player[0]+".png"
    temp = pygame.image.load(temp2).convert_alpha()
    temp1 = temp.get_rect()
    player_height=player_width * (temp1.height / temp1.width)
    while pos.g_t-pos.block_height/2-player_height < 0:
        player_width = player_width-10
        player_height=player_width * (temp1.height / temp1.width)
        
        
    buildings=[0,0]
    for i in range(3):
        temp2="player/"+player[i]+".png"
        temp = pygame.image.load(temp2).convert_alpha()
        temp1 = temp.get_rect()
        player[i] = pygame.transform.scale(temp, (player_width, player_height))
    book_height=pos.height/5
    for i in range(3):
        temp2="pic/book"+str(i)+".png"
        temp = pygame.image.load(temp2).convert_alpha()
        temp1 = temp.get_rect()
        books.append(pygame.transform.scale(temp, (book_height* (temp1 .width / temp1 .height),book_height)))
        
    
    reminder_width=(pos.g_l-pos.block_width)*(8/10)
    for i in range(2):
        temp2="pic/reminder"+str(i)+".png"
        temp = pygame.image.load(temp2).convert_alpha()
        temp1 = temp.get_rect()
        reminder[i] = pygame.transform.scale(temp, (reminder_width,reminder_width* (temp1.height / temp1.width)))
        
        temp2="pic/building"+str(i)+".png"
        temp = pygame.image.load(temp2).convert_alpha()
        temp1 = temp.get_rect()
        buildings[i] = pygame.transform.scale(temp, ( building_height* (temp1.width / temp1.height),building_height))
    building_width=  building_height* (temp1.width / temp1.height)
        
    #dice=['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg']
    dice=['1.png','2.png','3.png','4.png','5.png','6.png']
    dice_width=pos.g_l*(1/3)
    for i in range(6):
        temp2="dice3/"+dice[i]
        temp = pygame.image.load(temp2).convert_alpha()
        temp1 = temp.get_rect()
        dice[i]= pygame.transform.scale(temp,( dice_width, dice_width*(temp1.height / temp1.width)))
        
        
    
    
class color:
    WHITE=(255,255,255)
    GREEN=(0,255,0)
    RED=(255,0,0)
    YELLOW=(255,255,0)
    BLACK=(0,0,0)
    GROUND1=(238 ,221 ,130)
    GROUND2=(238, 197 ,145)
    QA=(245 ,245, 220)
    QAQ=(255 ,245 ,238)
    QA_WRONG=(220 ,220, 220)
    QA_CORRECT=(84 ,255 ,159)
    Yes_No_Q=(255, 240 ,245)

class Block(pygame.sprite.Sprite):
    def __init__(self,place):
        py.sprite.Sprite.__init__(self)
        self.place=place
        self.image=pygame.Surface((pos.block_width,pos.block_height))
        if self.place%2==0 :
            self.image.fill(color.GROUND1)
        else:
            self.image.fill(color.GROUND2)
        self.rect = self.image.get_rect()
        self.place_block()
        self.bl=[self.rect.centerx-pos.block_width/2,self.rect.centery+pos.block_height/2]
        
        
    def update(self):
        

        # 更新畫面，等所有操作完成後一次更新（若沒更新，則元素不會出現）
        pygame.display.update()
    def place_block(self):
      n = pos.width_block_num#5 
      m = pos.height_block_num#4

      if self.place == 0:
          self.rect.bottomright = (pos.g_l,pos.g_t)
          
      elif self.place >= 1 and self.place <= n:
          self.rect.bottomleft=(pos.g_l+pos.block_width*(self.place-1),pos.g_t)

      elif self.place == n + 1:
          self.rect.bottomleft = (pos.g_r,pos.g_t)

      elif self.place >= n + 2 and self.place <= n + m + 1:
        self.rect.topleft = (pos.g_r,pos.g_t+pos.block_height*(self.place-(n+2)))
        
      elif self.place == n + m + 2:
        self.rect.topleft = (pos.g_r,pos.g_b)

      elif self.place >= n + m + 3 and self.place <= 2 * n + m + 2:
        self.rect.topright = (pos.g_r-pos.block_width*(self.place-(n+m+3)),pos.g_b)

      elif self.place == 2 * n + m + 3:
        self.rect.topright = (pos.g_l,pos.g_b)

      elif self.place >= 2 * n + m + 4 and self.place <= 2 * (n + m) + 3:
        self.rect.topright = (pos.g_l,pos.g_t+((n+m)*2+3-self.place)*pos.block_height)
     
      
class Block_word(pygame.sprite.Sprite):
    def __init__(self,place):
        py.sprite.Sprite.__init__(self)
        self.place=place
        
        self.set_image()
        
        
    def update(self):
        

        # 更新畫面，等所有操作完成後一次更新（若沒更新，則元素不會出現）
        pygame.display.update()
    def set_image(self):
        n = pos.width_block_num
        m = pos.height_block_num
        if self.place == 0:
            self.image=image.word_start
        elif self.place == n+1 or self.place == 2 * n + m + 3 or self.place == n + m + 2:
            self.image=image.word_battle
            all_map[i]=1
        else:#1 battle 2 built 3 chance 4 destiny
            temp=[2,3,4]
            r=random.choices(temp, weights=(3,2,2), k=1)[0]
            #r=3
            if r==2:
                self.image=image.word_built
                all_map[i]=2
            elif r==3:
                self.image=image.word_chance
                all_map[i]=3
            else:
                self.image=image.word_destiny
                all_map[i]=4
        self.rect = self.image.get_rect()
        self.rect.center=all_block[self.place].rect.center
       
     
           
class Dice(pygame.sprite.Sprite):
    def __init__(self,player_num):
        py.sprite.Sprite.__init__(self)
        self.image=image.dice[3]
        self.rect = self.image.get_rect()
        self.player_num=player_num
        
        if player_num==0:
            self.rect.center=pos.dice_left_position
        else:
            self.rect.center=pos.dice_right_position
        
        
    def event(self):
       
        events=pygame.event.get()
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: 
                        if build_QA():
                            players[pos.current].money+=20
                        else:
                            players[pos.current].money-=20
                        for i in range(6):
                            self.image=image.dice[i]
                            redraw_everything()
                            pygame.display.update()
                            delay(0.15)
                        r=random.randint(1, 6)
                        
                        self.image=image.dice[r-1]
                        if self.player_num==0:
                            players[0].move(r)
                            pos.current= 1
                        else:
                            players[1].move(r)
                            pos.current= 0
                        redraw_everything()
                        delay(0.3)
        elif Gameover.rect.collidepoint(mouse_pos):
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: 
                        build_end()
                

class GameOver(pygame.sprite.Sprite):
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.image=image.gameover
        self.rect = self.image.get_rect()
        self.rect.bottom=pos.height-10 
        self.rect.centerx=pos.width/2
    #def word_gameover(self):
                                                 
class Player(pygame.sprite.Sprite):
    def __init__(self,player_num):
        py.sprite.Sprite.__init__(self)
        self.player_num=player_num
        self.other_num=(player_num+1)%2
        self.image=image.player[player_num]
        self.rect = self.image.get_rect()
        self.rect.center=all_block[0].rect.center
        self.rect.bottom=all_block[0].rect.centery-all_block_word[0].rect.height/2
        if player_num==0:
            self.rect.left=all_block[0].rect.centerx
        else:
            self.rect.right=all_block[0].rect.centerx
        self.position=0    
        self.money=300
        self.tested_word=0
        self.wrong_word=0
        self.not_init=False
        self.tested=[]
        self.voc=[]
        self.wrong=[]

    def move(self,step):
        #1 battle 2 built 3 chance 4 destiny
        self.move_to_center()
        for i in range(step):
            
            if self.position in pos.corners and self.not_init:
                self.image = pygame.transform.rotate(self.image, -90)
                self.rect=self.image.get_rect()
                self.place_player_to_block_position(self.position)
            self.not_init=True
            self.position+=1
            if self.position <= pos.corner_1:
                self.rect.centerx+=pos.block_width
            elif self.position<=pos.corner_2:
                self.rect.centery+=pos.block_height
            elif self.position<=pos.corner_3:
                self.rect.centerx-=pos.block_width
            else:
                self.rect.centery-=pos.block_height
                
            if self.position>=pos.all_block_num:
                self.money+=300       
            self.position%=pos.all_block_num
            redraw_everything()   
            delay(0.25)
            
        if players[0].position==players[1].position:
           self.players_using_same_block(self.position,self.player_num)
           redraw_everything() 
        #1 battle 2 built 3 chance 4 destiny
        if all_map[self.position]==1:
            self.on_battle()
        elif all_map[self.position]==2:
            self.on_build()
        elif all_map[self.position]==3:
            self.on_chance()
        elif all_map[self.position]==4:
            self.on_destiny()
            
    def on_build(self):  
        reminders[pos.current].build_or_not()
        if self.position in buildings[self.player_num]:
            reminders[pos.current].my_building()
            delay(1.5)
        elif self.position in buildings[(self.player_num+1)%2]:
            reminders[pos.current].not_my_building()
            delay(1.5)
            reminders[pos.current].common("收租200元")
            delay(1.5)
            self.money-=200
            players[self.other_num].money+=200
        else:
            reminders[pos.current].build_or_not()
            if build_Yes_NO("耗費金幣200建造房子？"):
                redraw_everything()
                if build_QA():
                    buildings[self.player_num].append(self.position)
                    self.money-=160
                    redraw_everything()
                    reminders[pos.current].common("房價打8折！" )
                else:
                    buildings[self.player_num].append(self.position)
                    self.money-=200
                    redraw_everything()
                    reminders[pos.current].common("房價維持原價！" )
                delay(1.5)
    def get_card(self):
        r = random.randint(0,len(pos.result)-1)
        font = pygame.font.SysFont(pos.font1, 20)
        text=pos.result[r][0][0:8]
        question_img=font.render(text, True, color.BLACK)
        question_img_rect=question_img.get_rect()
        question_img_rect.center=(pos.width/2,pos.height/2-image.destiny_height*1/3)
        window.blit(question_img,question_img_rect)
        
        question_img=font.render(str(pos.result[r][1])+" Coins", True, color.BLACK)
        question_img_rect=question_img.get_rect()
        question_img_rect.center=(pos.width/2,pos.height/2+image.destiny_height*1/5)        
       
        
        if len(pos.result[r][0])>8:
            text=pos.result[r][0][8:]
            temp_img=font.render(text, True, color.BLACK)
            temp_img_rect=temp_img.get_rect()
            temp_img_rect.center=(pos.width/2,pos.height/2)
            window.blit(temp_img,temp_img_rect)
            question_img_rect.centery=pos.height/2+image.destiny_height*1/3
        
        window.blit(question_img,question_img_rect)   
        return pos.result[r][1]
        
    def on_destiny(self):
        c_image=image.destiny
        rect = c_image.get_rect()
        rect.center=(pos.width/2,pos.height/2)
        window.blit(c_image,rect)
        self.money+=self.get_card()
        pygame.display.update()
        a=0
        while True:
            clock.tick(60)
            events=pygame.event.get()
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 : 
                        a=1
            if a==1:
                break
                          
        
    def on_chance(self):
        c_image=image.chance
        rect = c_image.get_rect()
        rect.center=(pos.width/2,pos.height/2)
        window.blit(c_image,rect)
        temp=self.get_card()
        pygame.display.update()
        a=0
        while True:
            clock.tick(60)
            events=pygame.event.get()
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 : 
                        a=1
            if a==1:
                break
        redraw_everything()
        if build_Yes_NO("再抽一次?"):
            redraw_everything()
            
            if build_QA():
                #redraw_everything()
                c_image=image.chance
                rect = c_image.get_rect()
                rect.center=(pos.width/2,pos.height/2)
                redraw_everything()
                window.blit(c_image,rect)
                self.money+=self.get_card()
            else:
                self.money+=temp
                reminders[self.player_num].common("重新抽牌失敗")
                delay(1)
                return 0
        else:
            self.money+=temp
            return 0
        pygame.display.update()
        a=0
        while True:
            clock.tick(60)
            events=pygame.event.get()
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 : 
                        a=1
            if a==1:
                break
        
    def on_battle(self):
        combo=0
        for i in range(5):
            reminders[self.player_num].common(pos.roundd[i]+" round")
            delay(1)
            redraw_everything()
            if build_QA(2):
                combo+=1
                reminders[self.player_num].common("Combo x"+str(combo))
                delay(1)
                redraw_everything()
                reminders[self.player_num].common(" +"+str(pos.combo_dollar[i])+"Coin")
                self.money+=pos.combo_dollar[i]
                delay(1)
                redraw_everything()
            else:
                redraw_everything()
                if build_QA(1):
                    reminders[self.other_num].common("搶答成功")
                    delay(1)
                    redraw_everything()
                    reminders[self.other_num].common(" +"+str(pos.combo_dollar[i]-10)+"Coin")
                    players[self.other_num].money+=(pos.combo_dollar[i]-10)
                    delay(1)
                    redraw_everything()
                else:
                    reminders[self.other_num].common("搶答失敗")
                    delay(0.7)
                    redraw_everything()
                combo=0
  
        # 更新畫面，等所有操作完成後一次更新（若沒更新，則元素不會出現）
    def move_to_center(self):
        if self.position <= pos.corner_1:
            self.rect.centerx=all_block[self.position].rect.centerx
        elif self.position<pos.corner_2:
            self.rect.centery=all_block[self.position].rect.centery
        elif self.position<pos.corner_3:
            self.rect.centerx=all_block[self.position].rect.centerx
        else:
            self.rect.centery=all_block[self.position].rect.centery
                         
        redraw_everything()   
    def players_using_same_block(self,place,second):
        if second==1:
            first=0
            second=1
        else:
            first=1
            second=0
        if place<=pos.corner_1:
            players[first].rect.left=all_block[self.position].rect.centerx
            players[second].rect.right=all_block[self.position].rect.centerx
        elif place<=pos.corner_2:
            players[first].rect.top=all_block[self.position].rect.centery
            players[second].rect.bottom=all_block[self.position].rect.centery
        elif place<=pos.corner_3:
            players[second].rect.left=all_block[self.position].rect.centerx
            players[first].rect.right=all_block[self.position].rect.centerx
        else :
            players[second].rect.top=all_block[self.position].rect.centery
            players[first].rect.bottom=all_block[self.position].rect.centery
            
    def place_player_to_block_position(self,place):
        if place<pos.corner_1:
            self.rect.center=all_block[place].rect.center
            self.rect.bottom=all_block[place].rect.centery-image.word_height/2
        elif place<pos.corner_2:
            self.rect.center=all_block[place].rect.center
            self.rect.left=all_block[place].rect.centerx+image.word_width/2
        elif place<pos.corner_3:
            self.rect.center=all_block[place].rect.center
            self.rect.top=all_block[place].rect.centery+image.word_height/2
        else :
            self.rect.center=all_block[place].rect.center
            self.rect.right=all_block[place].rect.centerx-image.word_width/2
  
class Reminder(pygame.sprite.Sprite):
    def __init__(self,player_num):
        py.sprite.Sprite.__init__(self)
        self.player_num=player_num
        self.image=image.reminder[player_num]
        self.rect = self.image.get_rect()
        if player_num==0:
            self.rect.centerx=pos.left_center
        else:
            self.rect.centerx=pos.right_center
        self.rect.centery=pos.height/2
        
        
    def roll_dice(self):
        talk="請擲骰子"
        self.show(talk)
        
    def anwser(self):
        self.show("請回答")
    
    def correct(self):
        self.show("回答正確")
    
    def wrong(self):
        self.show("回答錯誤")
    
    def build_or_not(self):
        self.show("買房嗎？")
    
    def my_building(self):
        self.show("經過自己家")
        
    def not_my_building(self):
        self.show("經過別人家")
    
    def build_success(self):
        talk="房子建造成功"
        self.show(talk)
    
    def common(self,inn):
        self.show(inn)
    
    def show(self,word):
        font = pygame.font.SysFont(pos.font1, 20)
        img=font.render(word, True, color.BLACK)
        rect=img.get_rect()
        rect.center=self.rect.center
        window.blit(self.image, self.rect)
        window.blit(img, rect)
        pygame.display.update()

def build_scoreboard(player):
    #0 for first player
    player_num=player.player_num
    texts=["Coin: ","Tested: ","Incorrect: "]
    if player_num==0:
        texts.insert(0, "Player 1")
    else:
        texts.insert(0, "Player 2")
    texts[1]+=str(player.money)
    texts[2]+=str(player.tested_word)
    texts[3]+=str(player.wrong_word)
            
    font = pygame.font.SysFont("Arial", 20)
    temp=pos.g_t-pos.block_height
    for text in texts:
        image=font.render(text, True, color.WHITE)
        rect = image.get_rect()
        rect.centerx=dices[player_num].rect.centerx
        rect.top=temp
        window.blit(image,rect)
        temp+=rect.height*(4/3)
        
def place_caracter_in_corner(player):    
    
    c_image=image.player[player.player_num]
    rect = c_image.get_rect()
    c_image=pygame.transform.scale(c_image,(image.dice_width/3,image.dice_width*(rect.width /rect.height)))
    rect=c_image.get_rect()
    rect.bottom=pos.height-image.dice_width/2
    if player.player_num==0:
        rect.left=image.dice_width/3
    else:
        rect.right=pos.width-image.dice_width/3
    window.blit(c_image,rect)

def build_Yes_NO(text,c_color=color.BLACK):
    yes_no=[0,0]
    yesno_texts=["Yes","NO"]
    font2 = pygame.font.SysFont(pos.font2, 25)
    font = pygame.font.SysFont(pos.font1, 25)
    text_img=font.render(text, True, c_color)
    text_img_rect=text_img.get_rect()
    text_img_rect.centerx=pos.width/2
    text_img_rect.centery=pos.g_t+pos.grass_size[1]/4
    text_background=py.Surface((text_img_rect.width+10,text_img_rect.height+10))
    text_background.fill(color.Yes_No_Q)
    text_background_rect=text_background.get_rect()
    text_background_rect.center=text_img_rect.center
    window.blit(text_background,text_background_rect)
    window.blit(text_img,text_img_rect)
    for i in [0,1]:
       yes_no[i]=Yes_No(i)
       temp=font2.render(yesno_texts[i],True,color.BLACK)
       temp_rect=temp.get_rect()
       temp_rect.center=yes_no[i].rect.center
       window.blit(temp, temp_rect)
    pygame.display.update()
    a=0
    while not (a):
        events=pygame.event.get()
        mouse_pos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for x in yes_no:
                    if x.rect.collidepoint(mouse_pos):
                        if event.button == 1: 
                            a=1
                           
                            if x.index==0:
                                return True
                            else:
                                return False

class Yes_No(pygame.sprite.Sprite):
    def __init__(self,index):
        py.sprite.Sprite.__init__(self)
        self.index=index
        self.image=py.Surface((g_WIDTH*2/5,pos.block_height))
        self.image.fill(color.WHITE)
        self.rect = self.image.get_rect()
        if self.index==0:
            self.rect.centerx=pos.g_l+pos.grass_size[0]*1/4
        else:
            self.rect.centerx=pos.g_r-pos.grass_size[0]*1/4
        self.rect.centery=pos.height/2+pos.grass_size[1]*1/5
        window.blit(self.image,self.rect)
        
class Voc:
    def __init__(self):
        
        d=[]
        if not pos.current_voc==pos.voc_data[2]:
            d = pd.read_csv(pos.current_voc,header=None,encoding='utf-8-sig')
            for i in range(0,len(d)):#####
                players[0].voc.append(d.loc[i][0])
                players[1].voc.append(d.loc[i][0])
        else :
            for j in [1,2]:
                edata = pd.read_excel('Player'+str(j)+'_vocabulary.xlsx', engine='openpyxl')
                d = edata['English'].astype(str) + '@' + edata['Chinese'].astype(str)
                for i in range(0,len(d)):#####
                    players[j-1].voc.append(d.loc[i])

        
    def get_vol(self,player):
        
        temp=[]#index
        temp2=[]#voc
        if len(player.voc)<4:
            player.voc+=player.tested
            player.tested=[]
        temp= random.sample(range(len(player.voc)), 4)
        for i in range(4):
            temp2.append(player.voc[temp[i]].split('@')[0])
        self.ans=random.randint(0, 2)
        self.ans_word=player.voc[temp[self.ans]].split('@')[1]
        player.tested.append(player.voc.pop(temp[self.ans]))
        return temp2
    
    def add_wrong(self,player,english,chinese):
        temp=english+'@'+chinese
        if temp not in player.wrong:
            player.wrong.append(temp)
        player.wrong_word+=1
            
def build_QA(same=0):
    #purpose0 for dice roll
    answering=pos.current
    answering_player=players[answering]
    question=""
    words=""
    ans=""
    if same==1:
        question=pos.last_question
        words=pos.last_word
        ans=pos.last_ans
        answering=(answering+1)%2
        answering_player=players[answering]
    else:
        words=voc.get_vol(answering_player)
        question=voc.ans_word
        ans=voc.ans
    answering_player.tested_word+=1
    temp=question.split('，')
    question=temp[0]
    for i in temp[1:]:
        
        if len(question+i)<15:
            question=question+','+i
    reminders[answering].anwser()
    pos.last_question=question
    pos.last_word=words
    pos.last_ans=ans
    
    words_img=[0,1,2]
    words_img_rect=[0,0,0]
    font = pygame.font.SysFont(pos.font2, 20)
    font_question=pygame.font.SysFont(pos.font1, 22)
    question_img=font_question.render(question, True, color.BLACK)
    question_img_rect=question_img.get_rect()
    
    big=question_img_rect.width
    for i in range(3):
        words[i]=words[i][:27]
        words_img[i]=font.render(words[i], True, color.BLACK)
        words_img_rect[i]=font.render(words[i], True, color.BLACK).get_rect()
        if words_img_rect[i].width > big:
            big=words_img_rect[i].width 
    if big+20>g_WIDTH*(9/10)-10 :
        big=g_WIDTH*(9/10)-20-10
    qa=[QA(0,big),QA(1,big),QA(2,big)]
    for i in range(3):
        words_img_rect[i].centery=qa[i].rect.center[1]
        words_img_rect[i].left=qa[i].rect.left+10
        window.blit(qa[i].image,qa[i].rect )
        window.blit(words_img[i], words_img_rect[i])
    question_img_rect.centery=(pos.g_t+qa[0].rect.top)/2
    question_img_rect.left=words_img_rect[0].left
    
    b_image=py.Surface((big+20,(pos.grass_size[1]/4)-15))
    b_image.fill(color.QAQ)
    b_image_rect = b_image.get_rect()
    b_image_rect.center=question_img_rect.center
    b_image_rect.left=pos.g_l+pos.grass_size[0]*(1/10)
    b_image_rect.height-=10
    window.blit(b_image,b_image_rect)
    window.blit(question_img, question_img_rect)
    pygame.display.update()
    a=0
    while not (a):
        events=pygame.event.get()
        mouse_pos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for x in qa:
                    if x.rect.collidepoint(mouse_pos):
                        if event.button == 1: 
                            a=1
                            if x.index==ans:
                                qa[ans].change_color_correct()
                                window.blit(words_img[ans], words_img_rect[ans])
                                reminders[answering].correct()
                                pygame.display.update()
                                delay(1)
                                return True
                            else:
                                voc.add_wrong(answering_player, words[ans],question)
                                if not same==2:
                                    qa[ans].change_color_correct()
                                qa[x.index].change_color_wrong()
                                reminders[answering].wrong() 
                                window.blit(words_img[ans], words_img_rect[ans])
                                window.blit(words_img[x.index], words_img_rect[x.index])
                                pygame.display.update()
                                delay(2)
                                
                                return False
                                                            
    
class QA(pygame.sprite.Sprite):
    def __init__(self,index,big):
        py.sprite.Sprite.__init__(self)
        self.image=py.Surface((big+20,(pos.grass_size[1]/4)-15))
        self.index=index
        self.image.fill(color.QA)
        self.rect = self.image.get_rect()
        self.rect.left=pos.g_l+pos.grass_size[0]*(1/10)
        self.rect.y=pos.g_t+pos.grass_size[1]*(1/10)+(pos.grass_size[1]*(9/40)*(index+1))
        self.rect.height-=10
    def change_color_correct(self):
        self.image.fill(color.QA_CORRECT)
        window.blit(self.image, self.rect)
        
    def change_color_wrong(self):
        self.image.fill(color.QA_WRONG)
        window.blit(self.image, self.rect)
        
class Choice_Caracter(pygame.sprite.Sprite):
    def __init__(self,image,index):
        py.sprite.Sprite.__init__(self)
        self.index=index
        self.image=image
        self.rect = self.image.get_rect()
        self.image= pygame.transform.scale(self.image,(pos.height/5* (self.rect.width / self.rect.height),pos.height/5))
        self.rect = self.image.get_rect()
        self.rect.centery=pos.height*2/3

class Choice_Voc_book(pygame.sprite.Sprite):
    def __init__(self,image,index):
        py.sprite.Sprite.__init__(self)
        self.index=index
        self.image=image
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect()
        self.rect.centery=pos.height*1/2

class Button(pygame.sprite.Sprite):
    def __init__(self,index,image):
        py.sprite.Sprite.__init__(self)
        self.image=image
        self.index=index
        self.rect = self.image.get_rect()
       
        
def add_sentance():
    for i in [1,2]:
        filename='Player'+str(i)+'_vocabulary.xlsx'
        df_vocabulary = pd.read_excel(filename)
        for index, row in df_vocabulary.iterrows():
            if pd.isna(row['Example']):
                try:
                    response = requests.get(pos.url+row['English'],headers=pos.headers)
                    soup = BeautifulSoup(response.content, "html.parser")
                    df_vocabulary.at[index, 'Example'] = soup.find(class_="eg deg").text
                except:
                    df_vocabulary.at[index, 'Example'] = "*"

    
        writer = pd.ExcelWriter(filename, engine='xlsxwriter')
        df_vocabulary['English'].to_excel(writer, sheet_name='vocabulary', index=False, startcol=0)
        df_vocabulary['Chinese'].to_excel(writer, sheet_name='vocabulary', index=False, startcol=1)
        df_vocabulary['Example'].to_excel(writer, sheet_name='vocabulary', index=False, startcol=2)
        writer.save()
    '''
    df_fault = pd.read_excel('Player2_fault.xlsx')
    df_vocabulary = pd.read_excel('Player2_vocabulary.xlsx')
    combined_df = pd.concat([df_fault[['Chinese', 'English']], df_vocabulary[['Chinese', 'English']]], ignore_index=True)
    combined_df = combined_df.drop_duplicates()
    combined_df.to_excel('Player2_vocabulary.xlsx', index=False)
    '''
    
    
def delay(sec):
    p=pygame.time.get_ticks()
    sec*=1000
    a=0
    while True:
        if pygame.time.get_ticks()-p>sec:
            a=1
        if a==1:
            break

def redraw_everything(): 
    
    window.blit(image.background,(0,0))
    window.blit(image.grass,((pos.width-g_WIDTH) /2,(pos.height-g_HEIGHT)/2) )
    window.blit(Gameover.image,Gameover.rect) 
    for i in range(pos.all_block_num):
        window.blit(all_block[i].image,all_block[i].rect)
        window.blit(all_block_word[i].image,all_block_word[i].rect)
    for g in [0,1]:
        for i in buildings[g]:
           window.blit(image.buildings[g],(all_block[i].bl[0],all_block[i].bl[1]-image().building_height))
    for i in [0,1]:
        window.blit(dices[i].image,dices[i].rect)
        build_scoreboard(players[i])
        place_caracter_in_corner(players[i])
        window.blit(players[i].image,players[i].rect)     
    pygame.display.update()
     
def build_end():
    win=0
    window.fill(color.BLACK)
    if players[0].money==players[1].money:
        win="兩位玩家平手"
        img=image.player[0]
        c_rect=image.player[0].get_rect()
        c_rect.centery=pos.height*1/3
        c_rect.centerx=pos.width*1/3
        window.blit(img,c_rect)
        img=image.player[1]
        c_rect=image.player[1].get_rect()
        c_rect.centery=pos.height*1/3
        c_rect.centerx=pos.width*2/3
        window.blit(img,c_rect)
    elif players[0].money>players[1].money:
        win="恭喜玩家1獲勝！"
        img=image.player[0]
        c_rect=image.player[0].get_rect()
        c_rect.centery=pos.height*1/3
        c_rect.centerx=pos.width*1/3
        window.blit(img,c_rect)
    else:
        win="恭喜玩家2獲勝！"
        img=image.player[1]
        c_rect=image.player[1].get_rect()
        c_rect.centery=pos.height*1/3
        c_rect.centerx=pos.width*1/3
        window.blit(img,c_rect)
        
    font = pygame.font.SysFont(pos.font1, 40)
    question_img=font.render(win, True, color.WHITE)
    question_img_rect=question_img.get_rect()
    question_img_rect.center=(pos.width/2,pos.height/2)
    window.blit(question_img,question_img_rect)
    
    
    pygame.display.update()
    a=0
    while True:
        clock.tick(60)
        events=pygame.event.get()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 : 
                    a=1
        if a==1:
            break     
    
    for i in [0,1]:
        en=[]
        ch=[]
        ex=[]
        for g in players[i].wrong:
            g=g.split('@')
            if g[0] not in en:
                en.append(g[0])
                ch.append(g[1])
                try:
                    response = requests.get(pos.url+g[0],headers=pos.headers)
                    soup = BeautifulSoup(response.content, "html.parser")
                    outer_class = soup.find(class_="eg deg")
                    ex.append(outer_class.text)
                except:
                    ex.append('*')
            
        data={'English':en,'Chinese':ch,'Example':ex}
        df = pd.DataFrame(data)
        filename='Player'+str(i+1)+ '_fault.xlsx'
        writer = pd.ExcelWriter(filename, engine='xlsxwriter')
        df['English'].to_excel(writer, sheet_name='vocabulary', index=False, startcol=0)
        df['Chinese'].to_excel(writer, sheet_name='vocabulary', index=False, startcol=1)
        df['Example'].to_excel(writer, sheet_name='vocabulary', index=False, startcol=2)
        writer.save()
        if os.name == 'nt':  # For Windows
            os.startfile(filename)
        elif os.name == 'posix':  # For macOS and Linux
            os.system('open ' + filename)
    pygame.quit()
    sys.exit()

pygame.display.set_caption('英語單字大富翁')


###################
font = pygame.font.SysFont(pos.font1, 26)
question_img=font.render("請選擇第一位角色圖案", True, color.WHITE)
question_img_rect=question_img.get_rect()
question_img_rect.center=(pos.width/2,pos.height/3)

temp=[]
for i in range(3):
    temp.append(Choice_Caracter(image.player[i],i))
    temp[i].rect.centerx=pos.width*(1/4)*(i+1)
    window.blit(temp[i].image,temp[i].rect)
window.blit(question_img,question_img_rect)
temp.append(Button(5,image.word_voc))
temp[3].rect.topright=(WIDTH,0)
window.blit(temp[3].image,temp[3].rect)

pygame.display.update()
a=0
while not (a):
    events=pygame.event.get()
    mouse_pos = pygame.mouse.get_pos()
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            for x in temp:
                if x.rect.collidepoint(mouse_pos):
                    if event.button == 1: 
                        if x.index!=5:
                            a=1
                            temp2=image.player[0]
                            image.player[0]=image.player[x.index]
                            image.player[x.index]=temp2
                            del temp[3]
                            del temp[x.index]
                        else:
                            add_sentance()
                            window.fill(color.BLACK)
                            for i in range(3):
                                window.blit(temp[i].image,temp[i].rect)
                            window.blit(question_img,question_img_rect)
                            temp[3].image=image.voc_finish
                            window.blit(temp[3].image,temp[3].rect)
                            pygame.display.update()
                            
                            
                        
window.fill(color.BLACK)
font = pygame.font.SysFont(pos.font1, 26)
question_img=font.render("請選擇第二位角色圖案", True, color.WHITE)
question_img_rect=question_img.get_rect()
question_img_rect.center=(pos.width/2,pos.height/3)

for i in range(2):
    window.blit(temp[i].image,temp[i].rect)
window.blit(question_img,question_img_rect)
pygame.display.update()
a=0
while not (a):
    events=pygame.event.get()
    mouse_pos = pygame.mouse.get_pos()
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            for x in temp:
                if x.rect.collidepoint(mouse_pos):
                    if event.button == 1: 
                        a=1
                        temp2=image.player[1]
                        image.player[1]=image.player[x.index]
                        image.player[x.index]=temp2
#################################################                        
window.fill(color.BLACK)
font = pygame.font.SysFont(pos.font1, 26)
question_img=font.render("請選擇單字庫", True, color.WHITE)
question_img_rect=question_img.get_rect()
question_img_rect.center=(pos.width/2,pos.height/4)
window.blit(question_img,question_img_rect)

    
font = pygame.font.SysFont(pos.font1, 20)
book_font=['國中基礎單字','高中基礎單字','自訂單字本']
for i in range(3):
    temp=font.render(book_font[i], True, color.WHITE)
    temp2=temp.get_rect()
    temp2.centerx=pos.width*(1/4)*(i+1)
    temp2.centery=pos.height*2/3
    window.blit(temp,temp2)
    
temp=[]
for i in range(3):
    temp.append(Choice_Voc_book(image.books[i], i))
    temp[i].rect.centerx=pos.width*(1/4)*(i+1)
    window.blit(temp[i].image,temp[i].rect)

pygame.display.update()
a=0
while not (a):
    events=pygame.event.get()
    mouse_pos = pygame.mouse.get_pos()
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            for x in temp:
                if x.rect.collidepoint(mouse_pos):
                    if event.button == 1: 
                        a=1
                        pos.current_voc=pos.voc_data[x.index]
                         
                            

####################################################
window.fill(color.BLACK)
if build_Yes_NO("是否要將錯誤單字匯到單字庫"):
    df_fault = pd.read_excel('Player1_fault.xlsx')
    df_vocabulary = pd.read_excel('Player1_vocabulary.xlsx')
    combined_df = pd.concat([df_fault[['Chinese', 'English','Example']], df_vocabulary[['Chinese', 'English','Example']]], ignore_index=True)
    combined_df = combined_df.drop_duplicates()
    combined_df.to_excel('Player1_vocabulary.xlsx', index=False)
    
    df_fault = pd.read_excel('Player2_fault.xlsx')
    df_vocabulary = pd.read_excel('Player2_vocabulary.xlsx')
    combined_df = pd.concat([df_fault[['Chinese', 'English','Example']], df_vocabulary[['Chinese', 'English','Example']]], ignore_index=True)
    combined_df = combined_df.drop_duplicates()
    combined_df.to_excel('Player2_vocabulary.xlsx', index=False)

###########################################
all_block=[]
all_block_word=[]
for i in range(pos.all_block_num):
    all_map.append(0)
    all_block.append(Block(i))
    all_block_word.append(Block_word(i))
#print(all_map)e
players=[]
dices=[]
scorebroads=[]
reminders=[]
buildings=[[],[]]


Gameover=GameOver()
for i in [0,1]:
    players.append(Player(i))
    dices.append(Dice(i))
    build_scoreboard( players[i])
    reminders.append(Reminder(i))

redraw_everything()
pygame.display.update()
voc=Voc()
pos_l=(0,0)
i=0

while running:
    clock.tick(FPS)
    
    if pos.current==0:
        reminders[0].roll_dice()
        dices[0].event()   
        
    else:
        reminders[1].roll_dice()
        dices[1].event()
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running=False
    
    
pygame.quit()
sys.exit()