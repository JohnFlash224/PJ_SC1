

import random, sys, time, math, pygame
from pygame.locals import *


RED = (255, 0, 0)

def initPlayer(left_standing, STARTSIZE, LEFT, HAFT_WINWIDTH, HAFT_WINHEIGHT, MAXHEALTH, CRYSTAL):
    playerObj = {'surface': pygame.transform.scale(left_standing, (STARTSIZE, STARTSIZE)),
                 'facing': LEFT,
                 'size': STARTSIZE,
                 'x': HAFT_WINWIDTH/2,
                 'y': HAFT_WINHEIGHT,
                 'health': MAXHEALTH,
                 'crystal': str(CRYSTAL)
                 }
    
    
    return playerObj

def initPlayerSysmbol(right_standing, X, Y, STARTSIZE):
    playerObj = {'surface': pygame.transform.scale(right_standing, (STARTSIZE, STARTSIZE)),
                 'x': X,
                 'y': Y,
                 }
        
    return playerObj

def drawPlayerSymbol(DISPLAYSURF, playerObj, tilewidth, tileheight):
    DISPLAYSURF.blit(playerObj['surface'], (playerObj['x']*tilewidth, playerObj['y']*tileheight))

def drawPlayerSymbol_XY(DISPLAYSURF, playerObj):
    DISPLAYSURF.blit(playerObj['surface'], (playerObj['x'], playerObj['y']))


def moveLeft_Player(playerObj,left_walks,anim_left, MOVERATE, LEFT, COLLISIONLEFT):
    
    if COLLISIONLEFT == False:
        playerObj['x'] -= MOVERATE

    if playerObj['facing'] != LEFT: # change player image

        playerObj['facing'] = LEFT

    playerObj['surface'] = left_walks[int(anim_left)]
    if anim_left < 5:
        anim_left += 0.3
    else:
        anim_left = 0
    
    return anim_left


def moveRight_Player(playerObj,right_walks,anim_right,MOVERATE,RIGHT, COLLISIONRIGHT):
    
    if COLLISIONRIGHT == False:
        playerObj['x'] += MOVERATE

    if playerObj['facing'] != RIGHT: # change player image
        playerObj['facing'] = RIGHT

    playerObj['surface'] = right_walks[int(anim_right)]
    if anim_right < 5:
        anim_right += 0.3
    else:
        anim_right = 0

    return anim_right

def jumpLeft_Player(playerObj, MOVERATE, LEFT, COLLISIONLEFT):
    
    if COLLISIONLEFT == False:
        playerObj['x'] -= MOVERATE

    if playerObj['facing'] != LEFT: # change player image

        playerObj['facing'] = LEFT

#     playerObj['surface'] = left_jump
    


def jumpRight_Player(playerObj,MOVERATE,RIGHT, COLLISIONRIGHT):
    
    if COLLISIONRIGHT == False:
        playerObj['x'] += MOVERATE

    if playerObj['facing'] != RIGHT: # change player image
        playerObj['facing'] = RIGHT

#     playerObj['surface'] = right_jump



def drawHealthBar(playerObj, DISPLAYSURF, COLOR, BGCOLOR, TOP, LEFT, SIZEHEALTHBAR, tilewidth, tileheight):
    
    HealthBar_size = (playerObj['health'],SIZEHEALTHBAR)
    HealthBar_rect =  pygame.Surface(HealthBar_size)
    HealthBar_rect.set_alpha(255)
    HealthBar_rect.fill(COLOR)
    DISPLAYSURF.blit(HealthBar_rect, (TOP*tilewidth,LEFT*tileheight))

        
    ShadowHealthBar_size = (10,SIZEHEALTHBAR)
    ShadowHealthBar_rect =  pygame.Surface(ShadowHealthBar_size)
    ShadowHealthBar_rect.set_alpha(255)
    ShadowHealthBar_rect.fill(BGCOLOR)
    DISPLAYSURF.blit(ShadowHealthBar_rect, (TOP*tilewidth, LEFT*tileheight))


def drawCrystalAmount(BASICFONT, DISPLAYSURF, WHITE, playerObj, LEFT, TOP, tilewidth, tileheight):
    
    CrystalAmount = BASICFONT.render(playerObj['crystal'], True, WHITE)
    DISPLAYSURF.blit(CrystalAmount, (LEFT*tilewidth, TOP*tileheight))
    

def firePlayer(playerObj, fire, fireMove, playerFire, DISPLAYSURF, RIGHT, LEFT, MOVERATE):
    if fire == True:

        if fireMove == False:
            for playerBulletM in playerFire:
                playerBulletM['x'] = playerObj['x']
                playerBulletM['y'] = playerObj['y']
        fireMove = True
        
        if fireMove == True:

            for playerBulletM in playerFire:
                    
                print('pBM: ',playerBulletM)
                playerBulletM['rect'] = pygame.Rect( (playerBulletM['x'],
                                                  playerBulletM['y'],
                                                  playerBulletM['size'],
                                                  playerBulletM['size']) )
                DISPLAYSURF.blit(playerBulletM['surface'], playerBulletM['rect'])
                
#                 pygame.draw.rect(DISPLAYSURF, RED,playerBulletM['rect'])
                
                if playerBulletM['move'] == True:
                    
                    if playerBulletM['fly'] == False:
                    
                        if playerObj['facing'] == RIGHT:
                            playerBulletM['facing'] = RIGHT 
                            playerBulletM['x'] += MOVERATE + 5
            
                        elif playerObj['facing'] == LEFT:
                            playerBulletM['facing'] = LEFT
                            playerBulletM['x'] -= MOVERATE + 5
                        
                        playerBulletM['fly'] = True
                        
                    elif playerBulletM['fly'] == True:
                        
                        if playerBulletM['facing'] == LEFT:
                            playerBulletM['x'] -= MOVERATE + 5 
                        elif playerBulletM['facing'] == RIGHT:
                            playerBulletM['x'] += MOVERATE + 5 
                        
    
    return fire, fireMove


def genFire(playerObj, playerFire, NUMFIRE, Flame_IMG, STARTSIZE, LEFT, RIGHT, MAXHEALTH, DAMAGE, HAFT_WINWIDTH):
    
    fire = True
                    
    if len(playerFire) < NUMFIRE:
        
        if playerObj['facing'] == RIGHT:
            playerBulletM={'surface':pygame.transform.scale(Flame_IMG, (STARTSIZE, STARTSIZE)),
                                           'facing':LEFT,
                                           'x': HAFT_WINWIDTH + 15,
                                           'y':playerObj['y'],
                                           'size': STARTSIZE - 15,
                                           'health':MAXHEALTH,
                                           'damage': DAMAGE,
                                           'move': True,
                                           'fly': False,
                                           'rect': pygame.Rect( (HAFT_WINWIDTH + 25,
                                                      playerObj['y'] + 20,
                                                      STARTSIZE - 15,
                                                      STARTSIZE - 15) )                                              
                                           }
            
        elif playerObj['facing'] == LEFT:
            playerBulletM={'surface':pygame.transform.scale(Flame_IMG, (STARTSIZE, STARTSIZE)),
                                           'facing':LEFT,
                                           'x': HAFT_WINWIDTH,
                                           'y':playerObj['y'],
                                           'size': STARTSIZE - 15,
                                           'health':MAXHEALTH,
                                           'damage': DAMAGE,
                                           'move': True,
                                           'fly': False,
                                           'rect': pygame.Rect( (HAFT_WINWIDTH + 25,
                                                      playerObj['y'] + 20,
                                                      STARTSIZE - 15,
                                                      STARTSIZE - 15) )                                              
                                           }
        
        playerFire.append(playerBulletM)
#         print('fire')
    
    return fire


    


