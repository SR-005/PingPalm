import pygame

pygame.init()
screen=pygame.display.set_mode((800,600)) #create the screen
pygame.display.set_caption("Ping Palm")
background = pygame.image.load("PingPalm_bg.jpg")  
background = pygame.transform.scale(background, (800, 600))


gamerun=True
while gamerun:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gamerun=False
    screen.blit(background, (0, 0))
    pygame.display.update()