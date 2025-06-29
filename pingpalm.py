import pygame
import random
import cv2
import mediapipe as mp
import sys
import os

pygame.init()
height=600
width=800
screen=pygame.display.set_mode((width,height)) #create the screen
pygame.display.set_caption("Ping Palm")

# Load background image with PyInstaller support
basedir = getattr(sys, '_MEIPASS', os.path.abspath("."))
background = pygame.image.load(os.path.join(basedir, "PingPalm_bg.jpg"))  
background = pygame.transform.scale(background, (width, height))  # scaled background

# Game Elements Initialization
paddlewidth, paddleheight = 10, 100
ballx, bally = 400, 300  # screen center
default_ballvelocity_x = 15
default_ballvelocity_y = 12
ballvelocity_x = default_ballvelocity_x
ballvelocity_y = default_ballvelocity_y
left_paddle_y = 250
right_paddle_y = 250
ballradius = 10

#SCORE MARKING
left_score = 0
right_score = 0

font = pygame.font.SysFont("Arial", 40, bold=True)


def countdown_screen(screen, background):
    large_font = pygame.font.SysFont("Arial", 100, bold=True)  # Bigger font
    for count in ["3", "2", "1", "GO!"]:
        screen.blit(background, (0, 0))
        color = (0, 255, 0) if count == "GO!" else (255, 0, 0)
        text = large_font.render(count, True, color)
        text_rect = text.get_rect(center=(400, 300))
        screen.blit(text, text_rect)
        pygame.display.update()
        pygame.time.delay(900)  # 900ms delay


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
startingcount=0

while gamerun:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gamerun=False
    fps.tick(60)   #we set game fps to 60

    if startingcount==0:
        countdown_screen(screen, background)
    startingcount=startingcount+1

    #Setting up MediaPipe
    success,img=feed.read()
    img=cv2.flip(img,1)
    imgrgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)  #Converting BGR color coded img to RGB as it is the one supported!
    results=hands.process(imgrgb)       #"process" is an inbuilt function that gives the necessart details automatically
    height,width,_=img.shape  #calculate height and width

    if results.multi_hand_landmarks:
        for handlandmarks,leftrighthand in zip(results.multi_hand_landmarks,results.multi_handedness):
            handlabel=leftrighthand.classification[0].label #it labels left and right hands
            for id,landmarks in enumerate(handlandmarks.landmark): #getting id and landmarks of the hands in the feed [DATA]
                pixelx,pixely=int(landmarks.x*width), int(landmarks.y*height)

                if id==8:
                    y = int(landmarks.y * 600)  # Map to game screen height
                    if handlabel=="Left":
                        left_paddle_y = y - paddleheight // 2
                    elif handlabel=="Right":
                        right_paddle_y = y - paddleheight // 2

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

    #Ball should Bounce off top and bottom
    if bally - ballradius <= 0 or bally + ballradius >= 600:
        ballvelocity_y *= -1
    

    # LEFT paddle collision
    if 30 < ballx < 90 and left_paddle_y < bally < left_paddle_y + paddleheight:
        ballvelocity_x = int(ballvelocity_x * -1.1)
        hit_pos = bally - (left_paddle_y + paddleheight // 2)
        ballvelocity_y = int((hit_pos // 10 + random.choice([-1, 0, 1])) * 1.1)
        max_speed = 30
        ballvelocity_x = max(-max_speed, min(max_speed, ballvelocity_x))
        ballvelocity_y = max(-max_speed, min(max_speed, ballvelocity_y))

    # RIGHT paddle collision
    if 720 < ballx < 770 and right_paddle_y < bally < right_paddle_y + paddleheight:
        ballvelocity_x = int(ballvelocity_x * -1.1)
        hit_pos = bally - (right_paddle_y + paddleheight // 2)
        ballvelocity_y = int((hit_pos // 10 + random.choice([-1, 0, 1])) * 1.1)
        max_speed = 30
        ballvelocity_x = max(-max_speed, min(max_speed, ballvelocity_x))
        ballvelocity_y = max(-max_speed, min(max_speed, ballvelocity_y))

    # SCORE LOGIC
    if ballx < 0:
        right_score += 1
        ballx, bally = 400, 300
        ballvelocity_x = -default_ballvelocity_x
        ballvelocity_y = default_ballvelocity_y
        countdown_screen(screen, background)  

    if ballx > 800:
        left_score += 1
        ballx, bally = 400, 300
        ballvelocity_x = default_ballvelocity_x
        ballvelocity_y = default_ballvelocity_y
        countdown_screen(screen, background) 

    # GAME OVER CHECK
    if left_score == 3 or right_score == 3:
        winner = "Player 1" if left_score == 10 else "Player 2"
        
        # Display background and Game Over text
        screen.blit(background, (0, 0))
        font_big = pygame.font.SysFont("Arial", 60, bold=True)
        font_small = pygame.font.SysFont("Arial", 30, bold=True)

        game_over_text = font_big.render("GAME OVER", True, (255, 0, 0))
        winner_text = font_small.render(f"{winner} WON!", True, (255, 255, 255))
        restart_text = font_small.render("Press R to Restart or Q to Quit", True, (30, 108, 243))

        screen.blit(game_over_text, game_over_text.get_rect(center=(400, 260)))
        screen.blit(winner_text, winner_text.get_rect(center=(400, 300)))
        screen.blit(restart_text, restart_text.get_rect(center=(400, 340)))
        pygame.display.update()

        # Pause game loop and wait for key press
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    paused = False
                    gamerun = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        left_score = 0
                        right_score = 0
                        ballx, bally = 400, 300
                        ballvelocity_x = default_ballvelocity_x
                        ballvelocity_y = default_ballvelocity_y
                        paused = False
                    elif event.key == pygame.K_q:
                        paused = False
                        gamerun = False

    # DRAW BACKGROUND FIRST
    screen.blit(background, (0, 0))

    # DRAW PADDLES
    pygame.draw.rect(screen, (255, 255, 255), (50, left_paddle_y, paddlewidth, paddleheight), border_radius=2)
    pygame.draw.rect(screen, (0, 0, 0), (740, right_paddle_y, paddlewidth, paddleheight), border_radius=2)

    # DRAW BALL
    pygame.draw.circle(screen, ballcolor, (int(ballx), int(bally)), ballradius)

    # DRAW SCORE
    left_score_text = font.render(f"{left_score}", True, (255, 255, 255))
    right_score_text = font.render(f"{right_score}", True, (0, 0, 0))
    screen.blit(left_score_text, (320, 20))
    screen.blit(right_score_text, (450, 20))

    # UPDATE SCREEN
    pygame.display.update()