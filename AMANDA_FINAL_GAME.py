#########################################
# File Name: dash_game.py
# Description: Runner Game  
# Author: Amanda
# Date: 01/11/2022
#########################################
import pygame
import time
from random import randint

pygame.init()
WIDTH = 800
HEIGHT= 600
gameWindow=pygame.display.set_mode((WIDTH,HEIGHT), pygame.SRCALPHA)

#---------------------------------------#
# functions                             #
#---------------------------------------#
def drawTitleScreen():
    gameWindow.blit(sky1, (0,0))
    DASH_TEXT = FONT_BIG.render("DASH!", 10, WHITE)
    TITLE_TEXT = FONT.render("Press Space to Start", 10, WHITE)
    gameWindow.blit(DASH_TEXT, (280, 100))
    gameWindow.blit(TITLE_TEXT, (280, 530))
    pygame.display.update()

def drawEndScreen():
    gameWindow.blit(sky1, (0,0))
    DASH_TEXT = FONT_BIG.render("GAME OVER!", 10, WHITE)
    TITLE_TEXT = FONT.render("Press Space to Try Again", 10, WHITE)
    gameWindow.blit(DASH_TEXT, (170, 100))
    gameWindow.blit(TITLE_TEXT, (260, 530))
    pygame.display.update()
    
def redrawGameWindow():                
    drawBackground()
    drawObstacles()
    drawCharacter()
    drawScore()
    drawHearts()
    if moveShieldIcon:
        drawShieldIcon()
    if moveHeartIcon:
        drawHeartIcon()
    if shieldUp:
        drawShield()
    pygame.display.update()
    
def drawBackground():
    gameWindow.blit(sky1, (sky1X,sky1Y))
    gameWindow.blit(sky2, (sky2X,sky2Y))

def drawObstacles():
    for i in range (len(obstacleX)):
        gameWindow.blit(obstacleList[i], (obstacleX[i],obstacleY[i]))

def drawCharacter():
    gameWindow.blit(girlPic[girlPicNum], (girlX, girlY))

def drawScore():
    #count digits of score
    digitsScore = len(str(points))
    digitsHiScore = len(str(hiScore))
    #replace previous digits with 0 
    scoreText = FONT.render("SCORE " + "0"*(8-digitsScore)+str(points), 10, WHITE)
    hiScoreText = FONT.render("HI SCORE " + "0"*(8-digitsHiScore)+str(hiScore), 10, WHITE)
    gameWindow.blit(scoreText, (600, 30))
    gameWindow.blit(hiScoreText, (570, 60))
    
def drawHearts():
    gameWindow.blit(heart1, ((WIDTH//2)-(heartWidth+(heartWidth//2)),heartX))
    gameWindow.blit(heart2, ((WIDTH//2)-(heartWidth//2),heartX))
    gameWindow.blit(heart3, ((WIDTH//2)+(heartWidth//2),heartX))

def drawShieldIcon():
    gameWindow.blit(SHIELD_ICON, (shieldIconX, iconY))

def drawHeartIcon():
        gameWindow.blit(HEART_ICON, (heartIconX, iconY))

def drawShield():
    pygame.draw.circle(gameWindow, RED, (round(girlX+SHIELD_RADIUS), round(girlY+35)), SHIELD_RADIUS, 5)

def appendNewObstacle():
    if obstacleX[-1]<=200:
        obstacleX.append(WIDTH)
        obstacleNumber = randint(1,5)
        if obstacleNumber == 1:
            obstacleList.append(OBSTACLE1)
            obstacleY.append(obstacle1Y)
            obstacleW.append(obstacle1W)
            obstacleH.append(obstacle1H)
        elif obstacleNumber == 2:
            obstacleList.append(OBSTACLE2)
            obstacleY.append(obstacle2Y)
            obstacleW.append(obstacle2W)
            obstacleH.append(obstacle2H)
        elif obstacleNumber == 3:
            obstacleList.append(OBSTACLE3)
            obstacleY.append(obstacle3Y)
            obstacleW.append(obstacle3W)
            obstacleH.append(obstacle3H)
        elif obstacleNumber == 4:
            obstacleList.append(OBSTACLE4)
            obstacleY.append(obstacle4Y)
            obstacleW.append(obstacle4W)
            obstacleH.append(obstacle4H)
        elif obstacleNumber == 5:
            obstacleList.append(OBSTACLE5)
            obstacleY.append(obstacle5Y)
            obstacleW.append(obstacle5W)
            obstacleH.append(obstacle5H)

def collisionTest(firstX,firstY,firstW,firstH, secondX, secondY, secondW, secondH):
    firstRect = pygame.Rect(firstX,firstY,firstW,firstH)
    secondRect = pygame.Rect(secondX, secondY, secondW, secondH)
    if firstRect.colliderect(secondRect):
        return True

def calculateTime (referenceTime, period):
    elapsed = round((time.time() - referenceTime), 1)
    if elapsed > period:
        return True

#---------------------------------------#
# main program                          #
#---------------------------------------#
# background properties   
sky1 = pygame.image.load("resources/sky.jpg")
sky1W = 960
sky1X = 0
sky1Y = 0
sky2 = pygame.image.load("resources/sky_flipped.jpg")
sky2W = 960
sky2X = sky1W
sky2Y = 0
BASE_SPEED = 9
speed = BASE_SPEED
MAXSPEED = 20

#colour properties
WHITE = (255,255,255)
BLACK = (  0,  0,  0)
BLUE = (102, 178, 255)
RED = (230, 50, 50)

#font properties
FONT_BIG = pygame.font.Font("resources/ARCADECLASSIC.TTF",100)
FONT = pygame.font.Font("resources/ARCADECLASSIC.TTF",24)

#time properties  
PERIOD = 10
pointsPeriod = 0.2
shieldPeriod = 5

#obstacle properties
obstacleX = [WIDTH]
obstacleY = [430]
obstacleW = [50]
obstacleH = [70]

OBSTACLE1 = pygame.image.load("resources/bush.png")
obstacle1Y =(430)
obstacle1W = (50)
obstacle1H = (50)

OBSTACLE2 = pygame.image.load("resources/tree.png")
obstacle2Y = (403)
obstacle2W = (65)
obstacle2H = (80)

OBSTACLE3 = pygame.image.load("resources/bee.png")
obstacle3Y = (380)
obstacle3W = (50)
obstacle3H = (50)
                
OBSTACLE4 = pygame.image.load("resources/tree2.png")
obstacle4Y = (400)
obstacle4W = (60)
obstacle4H = (80)
                
OBSTACLE5 = pygame.image.load("resources/bird1.png")
obstacle5Y = (355)
obstacle5W = (70)
obstacle5H = (70)
                
obstacleList = [OBSTACLE1]

#character properties
GROUND_LEVEL = 415
BASE_JUMP = -18
jumpSpeed = BASE_JUMP
BASE_GRAVITY = 1.3
gravity = BASE_GRAVITY

girl = pygame.image.load("resources/girl1.png")
girlH = 50
girlW = 45
girlX = 120
girlY = GROUND_LEVEL
girlVy = 0
girlPicNum = 1                         
girlPic =[0]*11                       
for i in range(11):                    
    girlPic[i] = pygame.image.load("resources/girl" + str(i) + ".png")

nextRightPic  = [1, 2, 3, 4, 5, 6, 7, 8, 1, 1, 1, 1]

#hearts properties
fullHeart = pygame.image.load("resources/fullheart.png")
emptyHeart = pygame.image.load("resources/emptyheart.png")
heartWidth = 60
heartX = 30

#power-up properties
SHIELD_RADIUS = 40
SHIELD_ICON = pygame.image.load("resources/shield.png")
shieldIconX = WIDTH
iconY = 350
shieldIconW = 40
shieldIconH = 40

HEART_ICON = pygame.image.load("resources/smallheart.png")
heartIconX = WIDTH
heartIconY = 350
heartIconW = 40
heartIconH = 40


#sound properties:
JUMP_SOUND = pygame.mixer.Sound("resources/jump.wav")
JUMP_SOUND.set_volume(0.5)
BOOST_SOUND = pygame.mixer.Sound("resources/boost.wav")
BOOST_SOUND.set_volume(0.5)
HIT_SOUND = pygame.mixer.Sound("resources/hit.wav")
HIT_SOUND.set_volume(0.5)
GAME_OVER_SOUND = pygame.mixer.Sound("resources/lost.wav")
GAME_OVER_SOUND.set_volume(0.5)


#music 
pygame.mixer.music.load("resources/music.ogg")
pygame.mixer.music.set_volume(0.3)

#set fps
clock = pygame.time.Clock()
FPS = 40

#boolean variables
inPlay = True
titleScreen = True
inGame = False
endScreen = False
powerUp = False
shieldUp = False
moveShieldIcon = False
moveHeartIcon = False

#set high score
hiScore = 0

print("Dodge the obstacles! Use UP and DOWN keys to JUMP and DUCK")


#---------------------------------------# 
#main loop
while inPlay:
    #play sound when restarting game
    BOOST_SOUND.play(0)
    
    #open title screen
    while titleScreen:
        pygame.event.get()
        drawTitleScreen()
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # checks x button
                titleScreen = False
                inPlay = False

        #quit
        if keys[pygame.K_ESCAPE]:
            titleScreen = False
            inPlay = False

        #start
        if keys[pygame.K_SPACE]:
            titleScreen=False
            inGame = True
            HIT_SOUND.play(0)
            
    #start music
    pygame.mixer.music.play(-1)

    #reset points
    points = 0

    #reset lives
    lives = 3
    heart1 = fullHeart
    heart2 = fullHeart
    heart3 = fullHeart

    #reset speed
    speed = BASE_SPEED
    jumpSpeed = BASE_JUMP
    gravity = BASE_GRAVITY

    #reset shield variables
    powerUp = False
    moveShieldIcon = False
    moveHeartIcon = False
    shieldUp = False

    #reset time properties  
    BEGIN = time.time()
    referenceTime = BEGIN
    pointsReference = BEGIN

    #in game loop
    while inGame: 
        redrawGameWindow()
        clock.tick(FPS)


        for event in pygame.event.get():
            if event.type == pygame.QUIT: # checks x button
                inGame = False
                inPlay = False

        #quit game
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            inGame=False
            inPlay = False

        # scroll the background
        sky1X = sky1X - speed
        sky2X = sky2X - speed
        if sky1X <= -sky1W: 
            sky1X = sky1W
            sky2X = 0
        elif sky2X <= -sky2W:
            sky2X = sky2W
            sky1X = 0
        
        #add new obstacle
        appendNewObstacle()
                
        #move obstacle
        for i in range(len(obstacleX)):
            obstacleX[i]-=speed
            
        #increase speed of background
        if calculateTime(referenceTime, PERIOD) and speed<MAXSPEED:
            speed+=1
            referenceTime = time.time()

        #incrase gravity as game goes on
        if speed == 12:
            gravity = 1.5
        if speed == 17:
            gravity = 1.8
            jumpSpeed = -19
        if speed == 20:
            gravity = 2

        #increase score        
        if calculateTime(pointsReference, pointsPeriod):
            points+=1
            pointsReference = time.time()

        #girl running animation
        if girlY == GROUND_LEVEL:
            girlPicNum = nextRightPic[girlPicNum]

        #set duck variable
        duck = False

        #jumping animation            
        if keys[pygame.K_UP] and girlY == GROUND_LEVEL:
            girlVy = jumpSpeed
            girlPicNum = 9
            JUMP_SOUND.play(0)

        #ducking animation
        elif keys[pygame.K_DOWN] and girlY == GROUND_LEVEL:
            girlVx = 0
            girlPicNum = 10
            duck = True

        # update girl's vertical velocity
        girlVy = girlVy + gravity 
        # move girl in vertical direction
        girlY = girlY + girlVy
        if girlY > GROUND_LEVEL:
            girlY = GROUND_LEVEL
            girlVy = 0

        #decrease girl's Y position if ducking 
        if duck:
            girlRectY = girlY+30
        else:
            girlRectY = girlY

        #create rectangles for collision detection
        if len(obstacleX)>1:
            if collisionTest(girlX,girlRectY,girlW,girlH, obstacleX[-2],obstacleY[-2],obstacleW[-2],obstacleH[-2]):
                #if shield is not up, lose life
                if not(shieldUp):
                    obstacleX[-2] = -100
                    lives-=1
                    HIT_SOUND.play(0)
                #if shield is up, lose shield
                if shieldUp:
                    obstacleX[-2] = -100
                    shieldUp = False
                    HIT_SOUND.play(0)

        #change hearts based on lives
        if lives ==3:
            heart1 = fullHeart
            heart2 = fullHeart
            heart3 = fullHeart
        if lives == 2:
            heart1 = fullHeart
            heart2 = fullHeart
            heart3 = emptyHeart
        if lives == 1:
            heart1 = fullHeart
            heart2 = emptyHeart
            heart3 = emptyHeart

        #create shield power-up every 100 points
        if points%100==0 and points>10: 
            powerUp = True

        #generate shield icon or heart icon above jumping obstacles and under ducking obstacles
        if powerUp and obstacleX[-1]>=(WIDTH-30):
            randomPowerUp = randint(0,1)
            if randomPowerUp == 0:
                moveShieldIcon = True
            if randomPowerUp == 1:
                moveHeartIcon = True
            refObstacle = obstacleList[-1] 
            if refObstacle==OBSTACLE3 or refObstacle==OBSTACLE5:
                iconY = 430
            else:
                iconY = 350
    
        #move shield icon
        if moveShieldIcon:
            powerUp = False
            shieldIconX -= speed

        #move heart icon
        if moveHeartIcon:
            powerUp = False
            heartIconX -= speed
            
        #reset shield collectible if it passes 0 
        if shieldIconX < -shieldIconW or heartIconX < -heartIconW:
            moveShieldIcon = False
            moveHeartIcon = False
            shieldIconX = WIDTH
            heartIconX = WIDTH

        #detect collision with shield collectible
        if collisionTest(shieldIconX,iconY,shieldIconW,shieldIconH, girlX,girlRectY,girlW,girlH):
            moveShieldIcon = False
            shieldIconX = WIDTH
            shieldUp = True
            shieldReference = time.time()
            BOOST_SOUND.play(0)

        #detect collision with heart collectible
        if collisionTest(heartIconX,iconY,heartIconW,heartIconH, girlX,girlRectY,girlW,girlH):
            moveHeartIcon = False
            heartIconX = WIDTH
            if lives<3:
                lives+=1
            BOOST_SOUND.play(0)

        #shield disappears after certain time 
        if shieldUp: 
            if calculateTime(shieldReference, shieldPeriod):
                shieldUp = False

        #end game if lives deplete
        if lives==0:
            inGame = False
            endScreen = True
            heart1 = emptyHeart
            
            #update high score
            if points>hiScore:
                hiScore = points

            #stop music
            pygame.mixer.music.stop()
            GAME_OVER_SOUND.play(0)

    #open end screen
    while endScreen:
        pygame.event.get()
        drawEndScreen()
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # checks x button
                endScreen = False
                inPlay = False
        
        #quit
        if keys[pygame.K_ESCAPE]:
            endScreen = False
            inPlay = False

        #continue
        if keys[pygame.K_SPACE]:
            inGame = True
            endScreen = False

       
            

    
#---------------------------------------# 
pygame.quit()




  
