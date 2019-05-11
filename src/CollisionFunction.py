
import random, sys, time, math, pygame
from pygame.locals import *


def CollisionObject(tiledColisionsN, playerObj, LEFT, RIGHT, left_standing, right_standing, GRAVITY, COLLISION, COLLISIONBOTTOM, COLLISIONRIGHT, COLLISIONLEFT, COLLISIONTOP, fly, LOSEHEALTH):
    
    for tiledColision in tiledColisionsN:
        if playerObj['rectBottom'].colliderect(tiledColision['rect']):
            
            if tiledColision['type'] == 'ground':
            
                COLLISIONBOTTOM = True
                GRAVITY = 0
                
                fly = False
                        
#                 print('va cham bottom: ',tiledColision)

                        
                if fly == False:
                    if playerObj['facing'] == LEFT: # change player image
                        playerObj['surface'] = pygame.transform.scale(left_standing, (playerObj['size'], playerObj['size']))
                    elif playerObj['facing'] == RIGHT:
                        playerObj['surface'] = pygame.transform.scale(right_standing, (playerObj['size'], playerObj['size']))
                
                
                break
            
            elif tiledColision['type'] == 'sea':
            
                COLLISIONBOTTOM = True
                
                playerObj['y'] -= 50
                
                if LOSEHEALTH == False:
                    if playerObj['health'] >= 10:
                        playerObj['health'] -= 10
                        LOSEHEALTH = True
                        
#                 print('va cham bottom: SEA ',tiledColision)

                    
                break

            
        elif playerObj['rectBottom'].colliderect(tiledColision['rect']) == False:
            COLLISIONBOTTOM = False
    #                 print('Not va bottom')
            
    for tiledColision in tiledColisionsN:
            
        if playerObj['rectRight'].colliderect(tiledColision['rect']):
            if tiledColision['type'] == 'ground':
                COLLISIONRIGHT = True
#                 print('va right: ',tiledColision)
                        
                break
                    
        elif playerObj['rectRight'].colliderect(tiledColision['rect']) == False:
            COLLISIONRIGHT = False
    #                 print('Not va right')
               
    for tiledColision in tiledColisionsN:
                
        if playerObj['rectLeft'].colliderect(tiledColision['rect']):
            if tiledColision['type'] == 'ground':
                COLLISIONLEFT = True
#                 print('va left: ',tiledColision)
                        
                break
                    
        elif playerObj['rectLeft'].colliderect(tiledColision['rect']) == False:
            COLLISIONLEFT = False
    #                 print('Not va left')
                       
    for tiledColision in tiledColisionsN:
                
        if playerObj['rectTop'].colliderect(tiledColision['rect']):
            if tiledColision['type'] == 'ground':
                COLLISIONTOP = True
#                 print('va top: ',tiledColision)
                        
                break
                
        elif playerObj['rectTop'].colliderect(tiledColision['rect']) == False:
            COLLISIONTOP = False
    #                 print('Not va top')
    
#     for tiledColision in tiledColisionsN:
#                 
#         if playerObj['rect'].colliderect(tiledColision['rect']):
#             if tiledColision['type'] == 'ground':
#                 COLLISION = True
#                 print('va rect: ',tiledColision)
#                 if COLLISIONLEFT == True:
#                     playerObj['x'] = tiledColision['X']*tilewidth + tiledColision['sizeX']*tilewidth
#                 elif COLLISIONRIGHT == True:
#                     playerObj['x'] = tiledColision['X']*tilewidth
#                         
#                 break
#                 
#         elif playerObj['rect'].colliderect(tiledColision['rect']) == False:
#             COLLISION = False
#             print('Not va rect')
    
    return GRAVITY, COLLISION, COLLISIONBOTTOM, COLLISIONRIGHT, COLLISIONLEFT, COLLISIONTOP, fly, LOSEHEALTH


def CollisionCrystal(crystalColisionsN, crystalObjs1, playerObj):
    
    i = 0
    
    for crystalColision in crystalColisionsN:
        
        if playerObj['rect'].colliderect(crystalColision['rect']):
            
            playerObj['crystal'] = int(playerObj['crystal'])
            playerObj['crystal'] += crystalColision['valueCrystal']
            playerObj['crystal'] = str(playerObj['crystal'])
            
#             print('get crystal')
            
            crystalColisionsN.remove(crystalColision)
            del crystalObjs1[i]
            
#             print('remove crystal')
            
#             i -= 1
            
            break
        
        i += 1
        
#         print('i: ',i)
        
    return crystalColisionsN, crystalObjs1



def CollisionFirePlayer(playerFire, tiledColisionsN, WINWIDTH):
    
    for playerBulletM in playerFire:
               
        for tiledColision in tiledColisionsN:
            
            if tiledColision['type'] == 'ground':
                if playerBulletM['rect'].colliderect(tiledColision['rect']):
                    playerBulletM['move'] = False
#                     print('bullet', playerBulletM)
                    playerFire.remove(playerBulletM)
    
                    break


        if playerBulletM['x'] < - 100 or playerBulletM['x'] > WINWIDTH + 100:
#             print('bullet', playerBulletM)
            playerFire.remove(playerBulletM)
            


def CollisionFirePlayer_Enemies(playerFire, enemiesColisionsN, enemyObjs1):
    
    i = 0
    
    for playerBulletM in playerFire:
               
        for enemiesColision in enemiesColisionsN:
            
            if playerBulletM['rect'].colliderect(enemiesColision['rect']):
                playerBulletM['move'] = False
#                 print('bullet', playerBulletM)
                playerFire.remove(playerBulletM)
                
                enemiesColision['health'] -= playerBulletM['damage']
                
                
                if enemiesColision['health'] > 0:
                    enemyObjs1[i][3] = enemiesColision['health']
                 
#                     print('e health: ',enemyObjs1[i][3], ' type: ', enemiesColision['type'])
#                     print('enemy health: ',enemyObjs1[i], ' type: ', enemiesColision['type'])
                elif enemiesColision['health'] <= 0:
                    
                    try:
                        
                        enemiesColisionsN.remove(enemiesColision)
#                         print('e o : ',enemyObjs1[i])
                        del enemyObjs1[i]
                    
                    except KeyError:
                        print('Error: ',KeyError)
                    
#                 print('enemy health 2 : ',enemyObjs1[i], ' type: ', enemiesColision['type'])
                
                break
            
            i += 1
                
    return enemiesColisionsN, enemyObjs1


            
def CollisionEnemies(enemiesColisionsN, playerObj, LOSEHEALTH):
    
    for enemiesColision in enemiesColisionsN:
        
        if playerObj['rect'].colliderect(enemiesColision['rect']):
            
            if LOSEHEALTH == False:
                if playerObj['health'] >= 10:
                    playerObj['health'] -= 10
                    LOSEHEALTH = True
                        
                    print('va cham enemies: ',enemiesColision)
                    
            break
        
        
    return playerObj, LOSEHEALTH












