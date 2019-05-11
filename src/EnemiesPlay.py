
import random, sys, time, math, pygame
from pygame.locals import *

GRASSCOLOR = (24, 255, 0)



def initEnemy(ENEMY_IMG, STARTSIZE, FACE, MOVE, X, Y, MAXHEALTH):
    enemyObj = {'surface': pygame.transform.scale(ENEMY_IMG, (STARTSIZE, STARTSIZE)),
                 'facing':FACE,
                 'size': STARTSIZE,
                 'x': X,
                 'y': Y,
                 'health':MAXHEALTH,
                 'move': MOVE, 
                 'type': ''
                 }
    
    return enemyObj

def editEnemyFace(enemyObj, ENEMY_IMG, STARTSIZE):
    enemyObj['surface'] = pygame.transform.scale(ENEMY_IMG, (STARTSIZE, STARTSIZE))
    

def getEnemies_Img():
    
    ENEMIES_IMG = []
    
    R_WASP_IMG = pygame.image.load('img4/spr_wasp_idle_anim.gif')
    L_WASP_IMG = pygame.transform.flip(R_WASP_IMG, True, False)
    
    R_GHOST_IMG = pygame.image.load('img4/pipo-enemy010a.png')
    L_GHOST_IMG = pygame.transform.flip(R_GHOST_IMG, True, False)
    
    R_LEAFBUG_IMG = pygame.image.load('img4/spr_leafbug_idle_anim.gif')
    L_LEAFBUG_IMG = pygame.transform.flip(R_LEAFBUG_IMG, True, False)
    
    # Add to List
    ENEMIES_IMG.append(L_WASP_IMG)
    ENEMIES_IMG.append(R_WASP_IMG)
    
    ENEMIES_IMG.append(L_GHOST_IMG)
    ENEMIES_IMG.append(R_GHOST_IMG)
    
    ENEMIES_IMG.append(L_LEAFBUG_IMG)
    ENEMIES_IMG.append(R_LEAFBUG_IMG)
    
    return ENEMIES_IMG


def drawEnemiesRect(DISPLAYSURF, ENEMIES_IMG, enemyObjs1, tilewidth, tileheight, camerax, cameray, STARTSIZE, RIGHT, LEFT):
    
#     print('.............moi......................')
    
    enemyCollision1 = []
    MOVERATEX = 0
    MOVERATEY = 0
    
    i = 0
    for x,y,z,w,mx,my,sx,sy,face,move in enemyObjs1:
        
#         print('w0: ',w)
        
        if z == 'wasp':
            
            enemyObj = initEnemy(ENEMIES_IMG[0], STARTSIZE, face, move, x, y, w)
            
            if enemyObj['facing'] == LEFT:
#                 enemyObj = initEnemy(ENEMIES_IMG[0], STARTSIZE, RIGHT, LEFT, x, y, w)
                editEnemyFace(enemyObj, ENEMIES_IMG[0], STARTSIZE)
            elif enemyObj['facing'] == RIGHT:
#                 enemyObj = initEnemy(ENEMIES_IMG[1], STARTSIZE, RIGHT, LEFT, x, y, w)
                editEnemyFace(enemyObj, ENEMIES_IMG[1], STARTSIZE)
            
            enemyObj['type'] = z
            
            MOVERATEX = 0
            MOVERATEY = 0.1
            
#             print('w000000: ',w)
        elif z == 'ghost':
            
#             print('w1: ',w)
            enemyObj = initEnemy(ENEMIES_IMG[2], STARTSIZE, face, move, x, y, w)
            
            if enemyObj['facing'] == LEFT:
#                 enemyObj = initEnemy(ENEMIES_IMG[2], STARTSIZE, RIGHT, LEFT, x, y, w)
                editEnemyFace(enemyObj, ENEMIES_IMG[2], STARTSIZE)
            elif enemyObj['facing'] == RIGHT:
#                 enemyObj = initEnemy(ENEMIES_IMG[3], STARTSIZE, RIGHT, LEFT, x, y, w)
                editEnemyFace(enemyObj, ENEMIES_IMG[3], STARTSIZE)
            
#             print('w2: ',w)
            enemyObj['type'] = z
            
            MOVERATEX = 0.05
            
#             print('w3: ',w)
            
        elif z == 'leafbug':
            enemyObj = initEnemy(ENEMIES_IMG[4], STARTSIZE, face, move, x, y, w)
            
            if enemyObj['facing'] == LEFT:
#                 enemyObj = initEnemy(ENEMIES_IMG[4], STARTSIZE, RIGHT, LEFT, x, y, w)
                editEnemyFace(enemyObj, ENEMIES_IMG[4], STARTSIZE)
            elif enemyObj['facing'] == RIGHT:
#                 enemyObj = initEnemy(ENEMIES_IMG[5], STARTSIZE, RIGHT, LEFT, x, y, w)
                editEnemyFace(enemyObj, ENEMIES_IMG[5], STARTSIZE)
            
            enemyObj['type'] = z
            
            MOVERATEX = 0.1
            
        # change something of enemies
        
#         print('sx: ',sx)
#         print('sy: ',sy)
#         print('eo before face: ', face)
#         print('enemyObj facing',enemyObj['facing'])
        
#         enemyObj['x'], STARTPOINT = moveEnemies(enemyObj, RIGHT, LEFT, MOVERATE, x, STARTPOINT)
        
#         if STARTPOINT == False:
#             enemyObj['startPointX'] = x
#             enemyObj['startPointY'] = y
            
        
        enemyObj = moveEnemies(enemyObj, RIGHT, LEFT, MOVERATEX, MOVERATEY, x, y, mx, my, sx, sy)
        enemyObjs1[i][0] = enemyObj['x']
        enemyObjs1[i][1] = enemyObj['y']
        enemyObjs1[i][8] = enemyObj['facing']
        enemyObjs1[i][9] = enemyObj['move']
#         print('eo face: ',enemyObjs1[i][8])
        
        enemyObj['rect'] = pygame.Rect( (enemyObj['x']*tilewidth + camerax*tilewidth,
                                                  enemyObj['y']*tileheight  + cameray*tileheight,
                                                  enemyObj['size'],
                                                  enemyObj['size']) )
        
    #     DISPLAYSURF.blit(enemyObj['surface'], (enemyObj['x']*tilewidth + camerax*tilewidth, enemyObj['y']*tileheight + cameray*tileheight))
        DISPLAYSURF.blit(enemyObj['surface'], enemyObj['rect'])
#         pygame.draw.rect(DISPLAYSURF, GRASSCOLOR, enemyObj['rect'])
                
        enemyCollision1.append(enemyObj)
        
        i += 1
        
#     STARTPOINT = True
        
    return enemyCollision1


def moveEnemies(enemyObj, RIGHT, LEFT, MOVERATEX, MOVERATEY, x, y, mx, my, sx, sy):
    
#     print('e facing before :', enemyObj['facing'])
    
    if MOVERATEX > 0:
        
#         print('move x: ', MOVERATEX)
        
        if enemyObj['facing'] == LEFT:
            
            if ( ( x - mx ) / mx ) >= 0:        
                enemyObj['move'] = LEFT
                
#                 print('111111111111')
            elif ( ( x - mx ) / mx ) < 0:
                if enemyObj['x'] < sx:         
                    enemyObj['facing'] = RIGHT
                    enemyObj['move'] = RIGHT
                    
#                     print('22222222222222')
                
        elif enemyObj['facing'] == RIGHT:
            if enemyObj['x'] < sx:
                enemyObj['move'] = RIGHT
                
#                 print('3333333333333333')
            elif enemyObj['x'] >= sx:
                enemyObj['facing'] = LEFT
                enemyObj['move'] = LEFT
                
#                 print('444444444444444444')
        
#         print('e facing :', enemyObj['facing'])
        
        if enemyObj['move'] == LEFT:
            enemyObj['x'] -= MOVERATEX
        if enemyObj['move'] == RIGHT:
            enemyObj['x'] += MOVERATEX
        
    elif MOVERATEY > 0:
        
#         print('move y: ', MOVERATEY)
        
        if enemyObj['facing'] == LEFT:
            
            if ( ( y - my ) / my ) >= 0:        
                enemyObj['move'] = LEFT
                
#                 print('5555555555555')
            elif ( ( y - my ) / my ) < 0:
                if enemyObj['y'] < sy:         
                    enemyObj['facing'] = RIGHT
                    enemyObj['move'] = RIGHT
                    
#                     print('666666666666666')
                
        elif enemyObj['facing'] == RIGHT:
            if enemyObj['y'] < sy:
                enemyObj['move'] = RIGHT
                
#                 print('77777777777777777')
            elif enemyObj['y'] >= sy:
                enemyObj['facing'] = LEFT
                enemyObj['move'] = LEFT
                
#                 print('88888888888888888')
        
#         print('e facing :', enemyObj['facing'])
        
        if enemyObj['move'] == LEFT:
            # UP 
            enemyObj['y'] -= MOVERATEY
        if enemyObj['move'] == RIGHT:
            # DOWN 
            enemyObj['y'] += MOVERATEY
            
#         enemyObj['y'] -= MOVERATEY
#         m -= MOVERATE
#     elif m < 0:
#         enemyObj['x'] += MOVERATE
#         m += MOVERATE
        
    return enemyObj

# def moveEnemies(enemyObj, RIGHT, LEFT, MOVERATE, x, STARTPOINT):
#     
# #     enemyObjStartPoint = 0
#     
#     if STARTPOINT == False:
#         enemyObjStartPoint = x
#         STARTPOINT = True
#     
#     print('e sp: ', enemyObjStartPoint)
#     
#     if enemyObj['facing'] == RIGHT:
#         if enemyObj['x'] - enemyObjStartPoint <= x:
#             enemyObj['move'] = RIGHT
#         elif enemyObj['x'] - enemyObjStartPoint > x:
# #                     enemyObjStartPoint = enemyObj['x']
#             enemyObj['facing'] = LEFT
#             enemyObj['move'] = LEFT
#                      
#     elif enemyObj['facing'] == LEFT:
#         if enemyObj['x'] - enemyObjStartPoint <= x and enemyObj['x'] - enemyObjStartPoint >= 0:
#             enemyObj['move'] = LEFT
#         elif enemyObj['x'] - enemyObjStartPoint < 0:
# #                     enemyObjStartPoint = enemyObj['x']
#             enemyObj['facing'] = RIGHT
#             enemyObj['move'] = RIGHT
#             
# #     print('e f : ', enemyObj['facing'])
#     print('e x: ', enemyObj['x'])
#     print('tru: ',enemyObj['x'] - enemyObjStartPoint)
#             
#     if enemyObj['move'] == RIGHT:
#         enemyObj['x'] -= MOVERATE
#     elif enemyObj['move'] == LEFT:
#         enemyObj['x'] -= MOVERATE - 3       
# 
#     return enemyObj['x'], STARTPOINT



