import pygame

pygame.init()
screen=pygame.display.set_mode((800,600)) #create the screen

gamerun=True
while gamerun:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gamerun=False