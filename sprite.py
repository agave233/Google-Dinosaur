# -*- coding: utf-8 -*-
import pygame
import element
import random
from pygame.locals import *
from sys import exit

#update flame of background
def floor_update(move_speed):
    global floor_start,floor_len1,floor_len2
    floor_start = floor_start + move_speed
    if floor_start > 1500:
        if floor_start > 2300:
            floor_start = 0
            floor_len1 = 800
            floor_len2 = 0
        else:
            floor_len1 = 2300 - floor_start
            floor_len2 = 800 - floor_len1

#update flame of birds
def bird_update(time_passed,speed):
    global bird_time_record,bird_frame
    if time_passed > bird_time_record + speed:
        bird_frame = bird_frame + 1
        if bird_frame > 1:
            bird_frame = 0
        bird_time_record = time_passed

#update flame of sprite while standing
def sprite_std_update(time_passed,speed):
    global sprite_std_time_record,sprite_std_frame
    if time_passed > sprite_std_time_record + speed:
        sprite_std_frame = sprite_std_frame + 1
        if sprite_std_frame > 3:
            sprite_std_frame = 0
        sprite_std_time_record = time_passed

#update flame of sprite while squating
def sprite_down_update(time_passed,speed):
    global sprite_down_time_record,sprite_down_frame
    if time_passed > sprite_down_time_record + speed:
        sprite_down_frame = sprite_down_frame + 1
        if sprite_down_frame > 1:
            sprite_down_frame = 0
        sprite_down_time_record = time_passed

#update position of sprite while jumping
def sprite_up_update(max_h):
    global sprite_up_pos,sprite_up_state,sprite_up_step
    if sprite_up_state == 1:
        if sprite_up_pos > 330 - max_h:
            sprite_up_pos = sprite_up_pos - sprite_up_step
        else:
            sprite_up_state = 0
            sprite_up_pos = sprite_up_pos + sprite_up_step
        sprite_up_step -= 0.5
    else:
        sprite_up_pos = sprite_up_pos + sprite_up_step
        if sprite_up_pos > 330:
            sprite_up_state = -1
        sprite_up_step += 0.5

def block_update(move_speed):
    global block_number,block_type,block_start,last_dist,now_dist,block
    block_dist = [400,600,800]
    #update position of each block
    block_start = [start - move_speed for start in block_start]
    #check if disappear
    if block_number:
        if block_start[0] + block[block_type[0]].get_rect().width < 0:
            block_number -= 1
            del block_start[0]
            del block_type[0]
    if now_dist < last_dist:
        now_dist += move_speed
    else:
        last_dist = block_dist[random.randint(0,2)]
        block_type.append(random.randint(0,5))
        block_start.append(800)
        block_number += 1
        now_dist = 0

def cloud_update(move_speed):
    global cloud,cloud_start,cloud_last,cloud_now,cloud_number
    cloud_dist = [400, 600, 800]
    #update position of each block
    cloud_start = [start - move_speed for start in cloud_start]
    #check if disappear
    if cloud_number:
        if cloud_start[0] + cloud.get_rect().width < 0:
            cloud_number -= 1
            del cloud_start[0]
            del cloud_height[0]
    if cloud_now < cloud_last:
        cloud_now += move_speed
    else:
        cloud_height.append(random.randint(100,250))
        cloud_last = cloud_dist[random.randint(0,2)]
        cloud_start.append(800)
        cloud_number += 1
        cloud_now = 0



pygame.init()

screen = pygame.display.set_mode((800, 600), 0, 32)
sprite = pygame.image.load("resource/sprite.png").convert_alpha()
f = open("score.txt", "r")
best_score = f.read()
f.close()
pygame.display.set_caption("Google Dinosaur")
clock = pygame.time.Clock()

#get basic png
sprite_std,sprite_down,block,bird,floor,dead,restart,cloud = element.get(sprite)


#all vars of game
score = 0
best_score_temp = int(best_score)
speed = 60
move_speed = 8
action = -1
state = 0

sprite_std_frame = 0
sprite_down_frame = 0
sprite_up_pos = 330
sprite_up_state = -1
sprite_up_step = 0
max_h = 240
bird_frame = 0

block_start = []
block_type = []
block_number = 0
last_dist = 1000
now_dist = 0

cloud_start = []
cloud_height = []
cloud_number = 0
cloud_last = 0
cloud_now = 0

floor_start = 0
floor_len1 = 800
floor_len2 = 0
bird_time_record = 0
sprite_std_time_record = 0
sprite_down_time_record = 0
time_record = 0
key_up_pressed = False

font = pygame.font.SysFont("rial", 40)
text1 = font.render("Unconnected to the Internet", True, (96, 96, 96))
game_over =  font.render("Game Over!", True, (96, 96, 96))
font = pygame.font.SysFont("rial", 30)
text2 = font.render("Please try the following method", True, (96, 96, 96))
text3 = font.render("   *Reconnect to the WiFi network", True, (96, 96, 96))
text4 = font.render("   *Check network lines, modem, and routers", True, (96, 96, 96))

while True:

    #just enter game
    if action == -1:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    action = 1
                if event.key == K_ESCAPE:
                    exit()
        screen.fill((255,255,255))
        screen.blit(sprite_std[0],(100,250))
        screen.blit(text1, (300, 200))
        screen.blit(text2, (300, 250))
        screen.blit(text3, (300, 300))
        screen.blit(text4, (300, 350))
        pygame.display.update()
        continue

    #event handle
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if action == 3 and event.type == KEYDOWN:
            if event.key == K_SPACE:
                action = 1
                speed = 60
                move_speed = 8
                block_start = []
                block_type = []
                block_number = 0
                last_dist = 1000
                now_dist = 0
                score = 0
        elif event.type == KEYDOWN:
            if (event.key == K_SPACE or event.key == K_UP) and action != 2:
                sprite_up_pos = 330
                sprite_up_state = 1
                sprite_up_step = 18
                key_up_pressed = True
                action = 2
            if event.key == K_DOWN:
                action = 0
        elif event.type == KEYUP:
            if event.key == K_DOWN:
                action = 1
            if event.key == K_UP or event.key == K_SPACE:
                key_up_pressed = False


    clock.tick(60)
    time_passed = pygame.time.get_ticks()

    screen.fill((255,255,255))
    bird_update(time_passed, speed * 2)
    floor_part1 = floor.subsurface((floor_start, 0, floor_len1, 26))
    floor_part2 = floor.subsurface((0, 0, floor_len2, 26))

    #check collision
    for index in range(block_number):
        sprite_rect = pygame.Rect(20, sprite_up_pos, 70, 50)
        if action == 0:
            sprite_rect = pygame.Rect(20, sprite_up_pos, 120, 66)
        block_rect = pygame.Rect(block_start[index], 356 - 16 * block_type[index] / 3, block[block_type[index]].get_width(),block[block_type[index]].get_height())
        if sprite_rect.colliderect(block_rect) == True:
            best_score = best_score_temp
            move_speed = 0
            speed = 0
            action = 3
            f = open("score.txt", "w")
            f.write(str(best_score_temp))
            f.close()

    #show cloud
    cloud_update(move_speed)
    for index in range(cloud_number):
        screen.blit(cloud, (cloud_start[index], cloud_height[index]))

    #FSM under the control of player
    if action == 0:
        sprite_down_update(time_passed, speed * 2)
        screen.blit(sprite_down[sprite_down_frame], (20, 330))
    if action == 1:
        sprite_std_update(time_passed, speed)
        screen.blit(sprite_std[sprite_std_frame], (20, 330))
    if action == 2:
        sprite_up_update(max_h)
        screen.blit(sprite_std[0], (20, sprite_up_pos))
        if sprite_up_state == -1:
            if not key_up_pressed:
                action = 1
            else:
                sprite_up_pos = 330
                sprite_up_state = 1
                sprite_up_step = 18
    if action == 3:
        screen.blit(dead, (18, sprite_up_pos - 5))
        screen.blit(game_over,(380,250))
        screen.blit(restart,(400,300))
    if action != 3:
        score += 1

    #show score
    if best_score_temp < score / 10:
        best_score_temp = score / 10
    screen.blit(font.render("HIGH  " + str(int(best_score)), True, (96, 96, 96)), (600, 20))
    screen.blit(font.render(str(score / 10), True, (96, 96, 96)),(750,20))
    #screen.blit(bird[bird_frame], (0, 200))
    #show every block
    for index in range(block_number):
        screen.blit(block[block_type[index]], (block_start[index], 356 - 16 * block_type[index] / 3))
    #display background
    screen.blit(floor_part1,(0,400))
    screen.blit(floor_part2, (floor_len1, 400))

    block_update(move_speed)
    floor_update(move_speed)

    pygame.display.update()