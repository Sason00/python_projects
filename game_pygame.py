import pygame
import time
import random

screen_width = 600
screen_height = 600
x = 50
y = screen_height - 75
stone_x = 585
stone_y = 520
game_over = False
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))

def update():
    pygame.draw.rect(screen,(0, 0, 255), (x, y, 25, 25))
    pygame.draw.rect(screen,(255, 255, 255), (0, 550, 600, 75))
    pygame.display.update()
    pygame.draw.rect(screen, (0, 0, 0), (x, y, screen_width, screen_height))

def stone():
    global stone_x
    stone_width = 10
    stone_height = 10
    pygame.draw.rect(screen,(125, 125, 125), (stone_x, stone_y, stone_width, stone_height))
    stone_x -= 2
    update()     

while not game_over:
    update()
    for event in pygame.event.get():
        print(event.type)
        if event.type == pygame.MOUSEBUTTONDOWN:
            y -= 50
            update()
            time.sleep(1.5)
            y += 50
    r = random.random() * 100
    if r < 5:
        #print(r)
        stone()
    update()


