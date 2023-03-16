import pygame
import random
import math
import winsound

pygame.init()
pygame.display.set_caption("SIMON")
screen = pygame.display.set_mode((800, 800))

def collision(xpos, ypos):
    if math.sqrt((xpos - 400)**2 + (ypos - 400)**2)>200 or math.sqrt((xpos - 200)**2 + (ypos - 400)**2)<100:
        print("outside of ring")
    else:
        print("inside of ring")
#game variables 
xpos = 0
ypos = 0
mousePos = (xpos, ypos)
hasClicked = False #used to get user input
pattern = [] #holds random pattern
playyerPattern = [] #eventually holds player pattern
playerTurn = True
pi = 3.1415
ded = False # if player clicks wrong pattern, this resets everything


#gameloop##############################################################
while True:

    event = pygame.event.wait()#event queue

    #input section-------------------------------------------------------------

    if event.type == pygame.QUIT:
        break

    if event.type == pygame.MOUSEBUTTONDOWN:
        hadClicked =  True
        print("click")

    if event.type == pygame.MOUSEBUTTONUP:
        hasClicked = False
    
    if event.type == pygame.MOUSEMOTION:
        mousePos = event.pos
    
    #update section---------------------------------------------------------
    pattern.append(random.randrange(0, 2))
    collision(xpos, ypos)
    #play computer pattern
    for i in range(len(pattern)):
        if pattern[i] == 0: #RED
            #make brighter
            pygame.draw.arc(screen, (255, 0, 0), (200, 200, 400, 400), pi / 2, pi, 100)
            pygame.display.flip()
            #winsound.Beep(440, 500) 
        
        elif pattern[i] == 1: #GREEN
            #make brighter
            pygame.draw.arc(screen, (0, 255, 0), (200, 200, 400, 400), pi, (3 * pi / 2), 100)
            pygame.display.flip()
            #winsound.Beep(640, 500) 

        elif pattern[i] == 2: #BLUE
            #make brighter
            pygame.draw.arc(screen, (0, 0, 255), (200, 200, 400, 400), 3 * pi / 2, (2 * pi), 100)
            pygame.display.flip()
            #winsound.Beep(540, 500) 
        
        elif pattern[i] == 3: #YELLOW
            #make brighter
            pygame.draw.arc(screen, (255, 255, 0), (200, 200, 400, 400), 2 * pi, (pi / 2), 100)
            pygame.display.flip()
            #winsound.Beep(340, 500)
    #render section------------------------------------------------------
    
    #game board
    pygame.draw.arc(screen, (155, 0, 0), (200, 200, 400, 400), pi / 2, pi, 100)
    pygame.draw.arc(screen, (0, 155, 0), (200, 200, 400, 400), pi, (3 * pi / 2), 100)
    pygame.draw.arc(screen, (0, 0, 155), (200, 200, 400, 400), 3 * pi / 2, (2 * pi), 100)
    pygame.draw.arc(screen, (155, 155, 0), (200, 200, 400, 400), 2 * pi, (pi / 2), 100)

    #pygame.time.wait(800)
    pygame.display.flip()

pygame.quit()
