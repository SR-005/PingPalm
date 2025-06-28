import pygame

pygame.init()
height=600
width=800
screen=pygame.display.set_mode((width,height)) #create the screen
pygame.display.set_caption("Ping Palm")
background = pygame.image.load("PingPalm_bg.jpg")  
background = pygame.transform.scale(background, (width, height))     #scaled the background image

gamerun=True
while gamerun:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gamerun=False
    screen.blit(background, (0, 0))
    pygame.display.update()