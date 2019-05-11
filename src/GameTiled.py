

import random, sys, time, math, pygame
from pygame.locals import *
import pytmx
from pytmx.util_pygame import load_pygame
import SpeechCommandFunction as scf
import SpiteImg as SI
import PlayerPlay as playerP
import MapTiled as mt
import CollisionFunction as cf
import ItemsPlay as itemP
import EnemiesPlay as enemyP
import StartScreen as screen


FPS = 30
WINWIDTH = 640
WINHEIGHT = 512

HAFT_WINWIDTH = int(WINWIDTH/2)
HAFT_WINHEIGHT = int(WINHEIGHT/2)

# define some constants
LEFT = 'left'
RIGHT = 'right'

STARTSIZE = 50   
MAXHEALTH = 1000
CRYSTAL = 0
DAMAGE = 30

MOVERATE = 15
RUNRATE = 12

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BGCOLOR = (100, 50, 50)

NUMFIRE = 3

TYPE = ''

# define some constants
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

INVULNTIME = 2 
GAMEOVERTIME = 4 


VALUECRYSTAL = 10

HEALTH_WASP = 50
HEALTH_GHOST = 90
HEALTH_LEAFBUG = 30



def main():

    global FPSCLOCK,RUNGAME,DISPLAYSURF,BASICFONT,BIGFONT,instructionSurf,instructionRect,left_standing,right_standing,left_jump,right_jump,speechCommand,CRYSTAL_IMG,Flame_IMG, ENEMIES_IMG
    
    pygame.init()
    
    FPSCLOCK = pygame.time.Clock()
    RUNGAME = True
    
#     pygame.display.set_icon(pygame.image.load('gameicon.png'))
    DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
    pygame.display.set_caption("Platform game")
    BASICFONT=pygame.font.Font('freesansbold.ttf',16)
    BIGFONT = pygame.font.Font('freesansbold.ttf', 100)
    
    left_standing, right_standing, left_jump, right_jump = SI.LeftRight()
    Flame_IMG = SI.Fire_img()
    
    CRYSTAL_IMG = itemP.getCrystal_Img()
    
    ENEMIES_IMG = enemyP.getEnemies_Img()
    
    instructionSurf = BASICFONT.render('Speech Command: ', True, WHITE)
    instructionRect = instructionSurf.get_rect()
    instructionRect.bottomleft = (10, WINHEIGHT - 10)

    
    while True:
        
        if RUNGAME == False:
            RUNGAME = screen.showStartScreen('Nova Light', FPSCLOCK, WINWIDTH, WINHEIGHT, DISPLAYSURF, BIGFONT, BASICFONT, INVULNTIME)
        elif RUNGAME == True:
            RUNGAME = runGame(sys.argv)
 
        
def runGame(args):
   
    
    invulnerableMode=False
    invulnerableStartTime=0
    gameOverMode=False
    gameOverStartTime=0
    winMode=False
    startTime=0
#     countTime=0

    # create the surfaces to hold game text
    gameOverSurf = BASICFONT.render('Game Over', True, WHITE)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.center = (HAFT_WINWIDTH, HAFT_WINHEIGHT)
    
    
    LOSEHEALTH = False
    
    speechCommand=''
    r_button = False
    
    moveLeft = moveRight = moveUp = moveDown = False


    left_walks = []
    
    SI.getLeftWalk_img(left_walks,STARTSIZE)
    
    right_walks = []
    
    SI.getRightWalk_img(right_walks, left_walks)
    
   
    # stores the player object:
    playerObj = playerP.initPlayer(left_standing, STARTSIZE, LEFT, HAFT_WINWIDTH, HAFT_WINHEIGHT, MAXHEALTH, CRYSTAL)
    
    
    anim_left=0
    anim_right=0
    
    mic, pDetection = scf.initAudio()
    
    fly = True
    beforeJump = 0
    corJump = 0
    
    playerFire = []
    fire = False
    fireMove = False
    
#     coliRight = False
    
    global COLLISION, COLLISIONRIGHT, COLLISIONLEFT, COLLISIONBOTTOM, COLLISIONTOP
    global GRAVITY
    GRAVITY = 9
    ACCERATION = 0
    
    COLLISION = False
    COLLISIONRIGHT = False
    COLLISIONLEFT = False
    COLLISIONBOTTOM = False
    COLLISIONTOP = False
#     COLLISIONCRYSTAL = False
    
    #map tiled
    tiled_map,tilewidth,tileheight = mt.initMap()
    
    SET_ALPHA = 255
    
    # camerax and cameray are the top left of where the camera view is
    camerax = 0
    cameray = 0
    
    crystalObjs1 = [[4,12],[28,7],[39,11],[40,11],[41,11],[42,11],[43,11]]
    crystalCollision1 = []

    enemyObjs1 = [[28,11,'wasp',HEALTH_WASP,20,5,28,11,'left','left'],[38,11,'ghost',HEALTH_GHOST,20,0,30,11,'left','left'], [30,9,'leafbug',HEALTH_LEAFBUG,20,10,38,8,'left','left']]
    enemiesCollision1 = []
#     ENEMYLIVE = False
    
    STARTPOINT = False
      
    while True:
    
        DISPLAYSURF.fill(BGCOLOR)
        
        if invulnerableMode and time.time() - invulnerableStartTime > INVULNTIME:
            invulnerableMode = False
            LOSEHEALTH = False
        
        mt.renderMap(tiled_map, tilewidth, tileheight, DISPLAYSURF, camerax, cameray)
        
        #draw Crystal and enemy
        
#         print('Startpoint: ', STARTPOINT)
        
        crystalCollision1 = itemP.drawCrystalsRect(DISPLAYSURF, crystalObjs1, tilewidth, tileheight, camerax, cameray, CRYSTAL_IMG, STARTSIZE - 20, VALUECRYSTAL)
        enemiesCollision1 = enemyP.drawEnemiesRect(DISPLAYSURF, ENEMIES_IMG, enemyObjs1, tilewidth, tileheight, camerax, cameray, STARTSIZE, RIGHT, LEFT)
      
#         print('Startpoint: ', STARTPOINT)
        
#         for enemiesCollision in enemiesCollision1:
#             print('ec: ',enemiesCollision)
        
        #draw terrain
        tiledColisions = []
        tiledColisions2 = []
        tiledColisions3 = []
        tiledColisions4 = []
        tiledColisions5 = []
        tiledColisions6 = []
        tiledColisions, tiledColisions2, tiledColisions3 = mt.drawRectTerrainList(tilewidth, tileheight, WHITE, DISPLAYSURF, camerax, cameray, SET_ALPHA)
#         tiledColisions.extend(crystalRectList)
        
        
        # draw the player 
        flashIsOn = round(time.time(), 1) * 10 % 2 == 1
        if not gameOverMode and not (invulnerableMode and flashIsOn):
            playerObj['rect'] = pygame.Rect( (HAFT_WINWIDTH,
                                              playerObj['y'],
                                              playerObj['size'],
                                              playerObj['size']) )
            playerObj['rectRight'] = pygame.Rect( (HAFT_WINWIDTH+playerObj['size'],
                                                    playerObj['y'],
                                                    playerObj['size']/4,
                                                    playerObj['size']-8) )
            playerObj['rectLeft'] = pygame.Rect( (HAFT_WINWIDTH-15,
                                                    playerObj['y'],
                                                    playerObj['size']/4,
                                                    playerObj['size']-8) )
            playerObj['rectTop'] = pygame.Rect( (HAFT_WINWIDTH+10,
                                                    playerObj['y']-10,
                                                    playerObj['size']/2,
                                                    playerObj['size']/4) )
            
            playerObj['rectBottom'] = pygame.Rect( (HAFT_WINWIDTH+20,
                                                    playerObj['y']+playerObj['size'],
                                                    playerObj['size']-30,
                                                    playerObj['size']/8) )
            
            DISPLAYSURF.blit(playerObj['surface'], playerObj['rect'])
#             pygame.draw.rect(DISPLAYSURF, RED,playerObj['rectRight'])
#             pygame.draw.rect(DISPLAYSURF, RED,playerObj['rectBottom'])
#             pygame.draw.rect(DISPLAYSURF, RED,playerObj['rectLeft'])
#             pygame.draw.rect(DISPLAYSURF, RED,playerObj['rectTop'])
        
        # draw the bars
        playerSymbol = playerP.initPlayerSysmbol(right_standing, 0, 1, STARTSIZE - 20)
        playerP.drawPlayerSymbol(DISPLAYSURF, playerSymbol, tilewidth, tileheight)
        playerP.drawHealthBar(playerObj, DISPLAYSURF, RED, BGCOLOR, 1, 1, 15, tilewidth, tileheight)
        playerP.drawCrystalAmount(BASICFONT, DISPLAYSURF, WHITE, playerObj, 18, 1, tilewidth, tileheight)
        crystalSymbol = itemP.initCrystal(CRYSTAL_IMG, STARTSIZE - 35, 17, 1, VALUECRYSTAL)
        itemP.drawCrystalSymbol(DISPLAYSURF, crystalSymbol, tilewidth, tileheight)
        
        
        # check Area 
        
        if playerObj['x'] < 1600:
            
            GRAVITY, COLLISION, COLLISIONBOTTOM, COLLISIONRIGHT, COLLISIONLEFT, COLLISIONTOP, fly, LOSEHEALTH = cf.CollisionObject(tiledColisions, playerObj, LEFT, RIGHT, left_standing, right_standing, GRAVITY, COLLISION, COLLISIONBOTTOM, COLLISIONRIGHT, COLLISIONLEFT, COLLISIONTOP, fly, LOSEHEALTH)
            crystalCollision1, crystalObjs1 = cf.CollisionCrystal(crystalCollision1, crystalObjs1, playerObj)
            cf.CollisionFirePlayer(playerFire, tiledColisions, WINWIDTH)
            enemiesCollision1, enemyObjs1 = cf.CollisionFirePlayer_Enemies(playerFire, enemiesCollision1, enemyObjs1)
            enemiesCollision1, LOSEHEALTH = cf.CollisionEnemies(enemiesCollision1, playerObj, LOSEHEALTH)
            
        elif playerObj['x'] > 1600 and playerObj['x'] < 3900:
            print('va 2')
            
            GRAVITY, COLLISION, COLLISIONBOTTOM, COLLISIONRIGHT, COLLISIONLEFT, COLLISIONTOP, fly, LOSEHEALTH = cf.CollisionObject(tiledColisions2, playerObj, LEFT, RIGHT, left_standing, right_standing, GRAVITY, COLLISION, COLLISIONBOTTOM, COLLISIONRIGHT, COLLISIONLEFT, COLLISIONTOP, fly, LOSEHEALTH)
            
            cf.CollisionFirePlayer(playerFire, tiledColisions2, WINWIDTH)
            
        elif playerObj['x'] >= 3900:
            print('va 3')
            
            GRAVITY, COLLISION, COLLISIONBOTTOM, COLLISIONRIGHT, COLLISIONLEFT, COLLISIONTOP, fly, LOSEHEALTH = cf.CollisionObject(tiledColisions3, playerObj, LEFT, RIGHT, left_standing, right_standing, GRAVITY, COLLISION, COLLISIONBOTTOM, COLLISIONRIGHT, COLLISIONLEFT, COLLISIONTOP, fly, LOSEHEALTH)
            
            cf.CollisionFirePlayer(playerFire, tiledColisions3, WINWIDTH)
        
        if COLLISIONBOTTOM == False:
    
            GRAVITY = 5
            playerObj['y'] +=  ACCERATION
            if ACCERATION < 3:
                ACCERATION += 0.1
        
        
        
        fire, fireMove = playerP.firePlayer(playerObj, fire, fireMove, playerFire, DISPLAYSURF, RIGHT, LEFT, MOVERATE)
        
#         print('lenFire: ',len(playerFire))
        
        playerObj['y'] += GRAVITY
        
#         if camerax > 0.5:
        camerax = - ( playerObj['x'] - HAFT_WINWIDTH ) /32
        
        
        print(playerObj['x'] )
        print(playerObj['y'])
#         print(camerax)
        
        if LOSEHEALTH == True:
            if not invulnerableMode:
                # player is flash when takes damage
                invulnerableMode = True
                invulnerableStartTime = time.time()
        
        
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
                
            
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    print('pause')

    
                if event.key == K_UP:
#                     moveUp = True
                    if playerObj['facing'] == LEFT: # change player image
                        playerObj['surface'] = pygame.transform.scale(left_jump, (playerObj['size'], playerObj['size']))
                    elif playerObj['facing'] == RIGHT:
                        playerObj['surface'] = pygame.transform.scale(right_jump, (playerObj['size'], playerObj['size']))
                    
                    moveDown = False
                    
                    
                    if fly == False:
                        moveUp = True
                    
                    if beforeJump == 0:
                        corJump = playerObj['y']
#                         print('cJ: ',corJump)
                        beforeJump = 1
#                         print('bj: ',beforeJump)
                    
                    
                    fly = True
                    COLLISIONBOTTOM = False
                    
                if event.key == K_LEFT:
                    
                    moveLeft = True
                    moveRight = False
                    anim_left=0
                    
                    if playerObj['facing'] != LEFT: # change player image
                        playerObj['surface'] = pygame.transform.scale(left_standing, (playerObj['size'], playerObj['size']))
                    playerObj['facing'] = LEFT
                    
#                     playerObj['x'] -= MOVERATE
                    
                elif event.key == K_RIGHT:
                    moveRight = True
                    moveLeft = False
                    anim_right=0
                    
                    if playerObj['facing'] != RIGHT: # change player image
                        playerObj['surface'] = pygame.transform.scale(right_standing, (playerObj['size'], playerObj['size']))
                    playerObj['facing'] = RIGHT
                    
#                     speechCommand = ''
                
                elif event.key == K_DOWN:
                    moveDown = True
                    moveUp = False
                    
                elif event.key == K_z:
                    print('z')
                    
                    fire = playerP.genFire(playerObj, playerFire, NUMFIRE, Flame_IMG, STARTSIZE - 10, LEFT, RIGHT, MAXHEALTH, DAMAGE, HAFT_WINWIDTH)

                elif event.key == K_r:
                    
                    r_button = True
                    
                    speechCommand = scf.SpeechRecognition(mic, pDetection)
                    
                    
            elif event.type == KEYUP:
    
                if event.key == K_UP:
                    moveUp = False
                    
                if event.key == K_LEFT:
                    moveLeft = False
                    anim_left = 0
                    playerObj['surface'] = pygame.transform.scale(left_standing, (playerObj['size'], playerObj['size']))

                elif event.key == K_RIGHT:
                    moveRight = False
                    anim_right = 0
                    playerObj['surface'] = pygame.transform.scale(right_standing, (playerObj['size'], playerObj['size']))
                    
                elif event.key == K_DOWN:
                    moveDown = False
                
                elif event.key == K_r:
                    r_button = False
#                     speechCommand = ''
                    if speechCommand == 'back':
                        moveLeft = False
                        anim_left = 0
                        playerObj['surface'] = pygame.transform.scale(left_standing, (playerObj['size'], playerObj['size']))
                    elif speechCommand == 'go':
                        moveRight = False
                        anim_right = 0
                        playerObj['surface'] = pygame.transform.scale(right_standing, (playerObj['size'], playerObj['size']))
                    
                    elif speechCommand == 'jump':
                        moveUp = False
                        
                    
                    speechCommand = ''
                    
                elif event.key == K_ESCAPE:
#                     DISPLAYSURF.fill(BGCOLOR)
                    screen.showTextScreen('Pause', FPSCLOCK, WINWIDTH, WINHEIGHT, DISPLAYSURF, BIGFONT, BASICFONT)
    
#         print('fly: ',fly)
        
        if not gameOverMode:
            # actually move the player
            
            if r_button == True:
                print('rrrrrrrrrrrrrrr', speechCommand)
                
                if speechCommand == 'back':
                    moveLeft = True
                    moveRight = False
                    anim_left=0
                
                        
                    if playerObj['facing'] != LEFT: # change player image
                        playerObj['surface'] = pygame.transform.scale(left_standing, (playerObj['size'], playerObj['size']))
                    playerObj['facing'] = LEFT
                    
                elif speechCommand == 'go':
                    moveRight = True
                    moveLeft = False
                    anim_right=0

                    print('gooooooooo')
                    
                    if playerObj['facing'] != RIGHT: # change player image
                        playerObj['surface'] = pygame.transform.scale(right_standing, (playerObj['size'], playerObj['size']))
                    playerObj['facing'] = RIGHT
                
                elif speechCommand == 'jump':
                    if playerObj['facing'] == LEFT: # change player image
                        playerObj['surface'] = pygame.transform.scale(left_jump, (playerObj['size'], playerObj['size']))
                    elif playerObj['facing'] == RIGHT:
                        playerObj['surface'] = pygame.transform.scale(right_jump, (playerObj['size'], playerObj['size']))
                    
                    moveDown = False
                    
                    if fly == False:
                        moveUp = True
                    
                    if beforeJump == 0:
                        corJump = playerObj['y']
#                         print('cJ: ',corJump)
                        beforeJump = 1
#                         print('bj: ',beforeJump)
                         
                    fly = True
                    COLLISIONBOTTOM = False
                
                elif speechCommand == 'fire':
                    print('z')
                    
                    fire = playerP.genFire(playerObj, playerFire, NUMFIRE, Flame_IMG, STARTSIZE - 10, LEFT, RIGHT, MAXHEALTH, DAMAGE, HAFT_WINWIDTH)
            
            
            if moveLeft:
                if fly == False:
                    anim_left = playerP.moveLeft_Player(playerObj, left_walks, anim_left, MOVERATE, LEFT, COLLISIONLEFT)
                elif fly == True:
                    playerP.jumpLeft_Player(playerObj, MOVERATE, LEFT, COLLISIONLEFT)
    
            if moveRight:
                if fly == False:
                    anim_right = playerP.moveRight_Player(playerObj, right_walks, anim_right, MOVERATE, RIGHT, COLLISIONRIGHT)
                elif fly == True:
                    playerP.jumpRight_Player(playerObj, MOVERATE, RIGHT, COLLISIONRIGHT)
                
                
            if moveUp:
    #             playerObj['y'] -= MOVERATE
                if COLLISIONTOP == False:
                    if corJump - playerObj['y'] <= 120:
        #                     moveUp = True
                        playerObj['y'] -= MOVERATE + 12 + ACCERATION
                        if ACCERATION < 3:
                            ACCERATION += 0.1
        #                 print('up: ', corJump - playerObj['y'])
                    elif corJump - playerObj['y'] > 120:
                        moveUp = False
        #                 print('not up: ', corJump - playerObj['y'])
        #                     if fly == False:
                        beforeJump = 0
        #                 print('bJ = 0: ',beforeJump)
                elif COLLISIONTOP == True:
                    moveUp = False
                    beforeJump = 0
            
            if moveDown:
                if COLLISIONBOTTOM == False:
                    playerObj['y'] += MOVERATE
            
            displaySpeechCommand = 'Speech Command: ' + speechCommand
            instructionSurf = BASICFONT.render(displaySpeechCommand, True, WHITE)
            
            DISPLAYSURF.blit(instructionSurf, instructionRect)
    
            if playerObj['health'] < 60:
                gameOverMode = True # turn on "game over mode"
                gameOverStartTime = time.time()
            
        
        else:
            # game is over, show "game over" text
            DISPLAYSURF.blit(gameOverSurf, gameOverRect)
            if time.time() - gameOverStartTime > GAMEOVERTIME:
                RUNGAME = False
                return RUNGAME # end the current game
    
    
    
        pygame.display.update()
        FPSCLOCK.tick(FPS)
    
    

def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
    
    

    




