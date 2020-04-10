#Year 1 Programming Fundamental Assignment 2 : Python Game
#Author : Adam Zaim Chua
#Up960074


import pygame
import random
import math

#initialization of pygame
pygame.init()

#Window dimensions
win = pygame.display.set_mode((1000,800))

#Setting title and icon
pygame.display.set_caption("Shoot the Aliens")
pygame.display.set_icon(pygame.image.load('rocket.png'))

#Background
bg = pygame.image.load('nasa.jpg')

#Score count
score = 0
font = pygame.font.Font('BADABB__.ttf',32)

#player
playericon = pygame.image.load('space-invaders.png')
Px = 450
Py = 550
Update_X = 0
Update_Y = 0

#alien
alienicon = []
Ax = []
Ay = []
Update_Ax = []
Update_Ay = []
NumAliens = 5

#Fin
finFont = pygame.font.Font('BADABB__.ttf',64)

for i in range(NumAliens):
    alienicon.append(pygame.image.load('alien.png'))
    Ax.append(random.randint(0,935))
    Ay.append(random.randint(50,150))
    Update_Ax.append(2)
    Update_Ay.append(40)

#bullet
Bulleticon = pygame.image.load('bullet.png')
Bx = 0
By = 550
Update_Bx = 0
Update_By = 10
b_state = "ready"

def showScore(x,y):
    show = font.render("Score :" + str(score),True, (255,255,255))
    win.blit(show, (x,y))

def player(x,y):
    win.blit(playericon, (x,y))

def alien(x,y, i):
    win.blit(alienicon[i], (x,y))
    
def fire_bullet(x,y):
    global b_state
    b_state = "fire"
    win.blit(Bulleticon, (x + 16, y + 10))

def collision(Ax,Ay,Bx,By):
    distance = math.sqrt((math.pow(Ax - Bx, 2)) + ( math.pow ((Ay - By),2)))
    if distance < 30 :
        return True
    else:
        return False

def gameOver():
    text = finFont.render("Game Over", True, (255,255,255))
    win.blit(text, (380, 380))

#Main Loop
run = True
while run == True:
    win.fill((0,0,0))  
    win.blit(bg,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Update_X = -5

            elif event.key == pygame.K_RIGHT:
                Update_X = 5

            elif event.key == pygame.K_SPACE:
                if b_state == "ready":
                    Bx = Px
                    fire_bullet(Bx,By)

                else :
                    pass

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                Update_X = 0

            elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                Update_Y = 0

    #Player Boundaries------------------

    Px += Update_X
    Py += Update_Y

    if Px <= 0 :
        Px = 0

    elif Px >= 936:
        Px = 936


    #Alien Boundaries-------------------
    for i in range(NumAliens):

        if Ay[i] > 500:
            for j in range(NumAliens):
                Ay[i] = 2000

            gameOver()
            break

        Ax[i] += Update_Ax[i]

        if Ax[i] <= 0 :
            Update_Ax[i] = 4
            Ay[i] += Update_Ay[i]

        elif Ax[i] >= 936:
            Update_Ax[i] = -4
            Ay[i] += Update_Ay[i]

        col = collision(Ax[i],Ay[i],Bx,By)

        if col:
            By = 550
            b_state = "fire"
            score += 1
            Ax[i] = random.randint(0,935)
            Ay[i] = random.randint(50,150)

        alien(Ax[i],Ay[i], i)
        
    #Bullet movement-------------------
    if By <= 0:
        By = 550
        b_state = 'ready'

    if b_state == "fire":
        fire_bullet(Bx,By)
        By -= Update_By

               
    #-----------------------------------

    player(Px,Py)
    showScore(7,7)

    pygame.display.update()