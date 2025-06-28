import pygame
import random
import cv2
import mediapipe as mp

pygame.init()
height=600
width=800
screen=pygame.display.set_mode((width,height)) #create the screen
pygame.display.set_caption("Ping Palm")

#BACKGROUND IMAGE:
background = pygame.image.load("PingPalm_bg.jpg")  
background = pygame.transform.scale(background, (width, height))     #scaled the background image

# Game Elements Initialization
paddlewidth, paddleheight = 10, 100
ballx, bally = 400, 300  # screen center
ballvelocity_x = 7
ballvelocity_y = 5
left_paddle_y = 250
right_paddle_y = 250
ballradius = 10

#for catching fps
fps=pygame.time.Clock()

#OPENCV SETUP
feed = cv2.VideoCapture(0, cv2.CAP_DSHOW) #if you have only one webcam- 0 reads feed fom that one
feed.set(3,640) #setting up its width - id 3 refers to width
feed.set(4,480) #setting up its height - id 4 refers to height

mphands=mp.solutions.hands
hands=mphands.Hands()               #it can contain multiple hands
mpdraw=mp.solutions.drawing_utils  #built in funtion to point hand landmarks for each hand(in this case)

gamerun=True
while gamerun:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gamerun=False
    fps.tick(90)   #we set game fps to 60

    #Setting up MediaPipe
    success,img=feed.read()
    imgrgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)  #Converting BGR color coded img to RGB as it is the one supported!
    results=hands.process(imgrgb)       #"process" is an inbuilt function that gives the necessart details automatically



    #draw background
    screen.blit(background, (0, 0))  #to draw the bgimage on the screen at position (0,0)
    #Basic Ball Movement
    ballx += ballvelocity_x
    bally += ballvelocity_y

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

    #Ball should Bounce off top and bottom
    if bally - ballradius <= 0 or bally + ballradius >= 600:
        ballvelocity_y *= -1
    

    # Collision with left paddle
    if 50 < ballx - ballradius < 60 and left_paddle_y < bally < left_paddle_y + paddleheight:
        ballvelocity_x *= -1
        ballvelocity_y += random.choice([-1, 0, 1])

    # Collision with right paddle
    if 740 < ballx + ballradius < 750 and right_paddle_y < bally < right_paddle_y + paddleheight:
        ballvelocity_x *= -1
        ballvelocity_y += random.choice([-1, 0, 1])

    pygame.display.update()  #to update the frames every second