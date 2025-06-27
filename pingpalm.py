import cv2
import mediapipe as mp

feed = cv2.VideoCapture(0, cv2.CAP_DSHOW) #if you have only one webcam- 0 reads feed fom that one
feed.set(3,640) #setting up its width - id 3 refers to width
feed.set(4,480) #setting up its height - id 4 refers to height
feed.set(10,100) #id 10 is for BRIGHTNESS 

#Building the ball
ballx,bally=320,240
ballvelocityx,ballvelocityy=5,4
ballradius=10

leftpaddle_y = 240
rightpaddle_y = 240
paddlewidth = 10
paddleheight = 100


#DEFAULT FORMALITY!!!!
mphands=mp.solutions.hands
hands=mphands.Hands()               #it can contain multiple hands
mpdraw=mp.solutions.drawing_utils  #built in funtion to point hand landmarks for each hand(in this case)

while True:
    success,img=feed.read()
    imgrgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)  #Converting BGR color coded img to RGB as it is the one supported!
    results=hands.process(imgrgb)       #"process" is an inbuilt function that gives the necessart details automatically
    height,width,channel=img.shape  #calculate height and width
    leftpaddle_y=height//2
    rightpaddle_y=height//2      #if no hand is detected

    if results.multi_hand_landmarks:
        for handlandmarks,leftrighthand in zip(results.multi_hand_landmarks,results.multi_handedness):
            handlabel=leftrighthand.classification[0].label #it labels left and right hands
            for id,landmarks in enumerate(handlandmarks.landmark): #getting id and landmarks of the hands in the feed [DATA]
                pixelx,pixely=int(landmarks.x*width), int(landmarks.y*height)

                if id==8:
                    if leftrighthand=="left":
                        leftpaddle_y=pixely
                    elif leftrighthand=="right":
                        rightpaddle_y=pixely

            mpdraw.draw_landmarks(img,handlandmarks,mphands.HAND_CONNECTIONS) #in the "img" it will set landmarks for each hand in the feed and set connections

    # Draw ball
    cv2.circle(img, (ballx, bally), ballradius, (255, 255, 0), -1)

    # Draw paddles
    cv2.rectangle(img, (50, leftpaddle_y - paddleheight // 2),
                  (50 + paddlewidth, leftpaddle_y + paddleheight // 2), (0, 255, 0), -1)

    cv2.rectangle(img, (width - 60, rightpaddle_y - paddleheight // 2),
                  (width - 60 + paddlewidth, rightpaddle_y + paddleheight // 2), (255, 0, 0), -1)
    
    #Ball Movement
    ballx=ballx+ballvelocityx
    bally=bally+ballvelocityy

    #if it goes over the upper or lower boundary-stop the ball
    if bally<=0 or bally>=height:
        ballvelocityy=-1

    # Collision with paddles
    #If paddle center is at y = 200, and paddle_height = 100, you want:
    #Top edge at 200 - 50 = 150
    #Bottom edge at 200 + 50 = 250
    #So the paddle is from y = 150 to y = 250.
    if 50 < ballx < 60 and leftpaddle_y - paddleheight//2 < bally < leftpaddle_y + paddleheight//2:
        ballvelocityx *= -1
    if width - 60 < ballx < width - 50 and rightpaddle_y - paddleheight//2 < bally < rightpaddle_y + paddleheight//2:
        ballvelocityx *= -1

    # Ball reset if missed
    if ballx <= 0 or ballx >= width:
        ballx, bally = width // 2, height // 2
        ballvelocityx *= -1


    img=cv2.flip(img,1)
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

feed.release()
cv2.destroyAllWindows()