import pygame

pygame.init()
height=600
width=800
screen=pygame.display.set_mode((width,height)) #create the screen
pygame.display.set_caption("Ping Palm")

#BACKGROUND IMAGE:
background = pygame.image.load("PingPalm_bg.jpg")  
background = pygame.transform.scale(background, (width, height))     #scaled the background image

# Game Elements
paddlewidth, paddleheight = 10, 100
ballx, bally = 400, 300  # screen center
left_paddle_y = 250
right_paddle_y = 250
ballradius = 10

gamerun=True
while gamerun:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gamerun=False

    #draw background
    screen.blit(background, (0, 0))  #to draw the bgimage on the screen at position (0,0)

    #draw paddles:
    pygame.draw.rect(screen,(255,255,255),(50,left_paddle_y,paddlewidth,paddleheight),border_radius=2)
    pygame.draw.rect(screen,(0,0,0),(740,right_paddle_y,paddlewidth,paddleheight),border_radius=2)

    #draw ball:
    # Change ball color based on position
    if ballx > 400:  # right side
        ballcolor = (0, 0, 0)  # black
    else:  # left side
        ballcolor = (255, 255, 255)  # white
    pygame.draw.circle(screen, ballcolor, (ballx, bally), ballradius)



    pygame.display.update()  #to update the frames every second