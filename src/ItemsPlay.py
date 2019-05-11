
import random, sys, time, math, pygame
from pygame.locals import *

GRASSCOLOR = (24, 255, 0)

def getCrystal_Img():
    CRYSTAL_IMG = pygame.image.load('img3/CrystalExtract2.gif')
    
    return CRYSTAL_IMG

def initCrystal(CRYSTAL_IMG, STARTSIZE, TOP, LEFT, VALUECRYSTAL):
    crystalObj = {'surface': pygame.transform.scale(CRYSTAL_IMG, (STARTSIZE, STARTSIZE)),
                 'size': STARTSIZE,
                 'x': TOP,
                 'y': LEFT,
                 'valueCrystal': VALUECRYSTAL
                 }
    
    return crystalObj

def drawCrystalSymbol(DISPLAYSURF, crystalObj, tilewidth, tileheight):
    DISPLAYSURF.blit(crystalObj['surface'], (crystalObj['x']*tilewidth, crystalObj['y']*tileheight))


def drawCrystal(DISPLAYSURF, crystalObj, tilewidth, tileheight, camerax, cameray):
    DISPLAYSURF.blit(crystalObj['surface'], (crystalObj['x']*tilewidth + camerax*tilewidth, crystalObj['y']*tileheight + cameray*tileheight))

def drawCrystalsRect(DISPLAYSURF, crystalObjs1, tilewidth, tileheight, camerax, cameray, CRYSTAL_IMG, STARTSIZE, VALUECRYSTAL):
    
    crystalCollision1 = []
    
    for x,y in crystalObjs1:
    
        crystalObj = {'surface': pygame.transform.scale(CRYSTAL_IMG, (STARTSIZE, STARTSIZE)),
                 'size': STARTSIZE,
                 'x': x,
                 'y': y,
                 'valueCrystal': VALUECRYSTAL
                 }
    
        crystalObj['rect'] = pygame.Rect( (crystalObj['x']*tilewidth + camerax*tilewidth,
                                                  crystalObj['y']*tileheight  + cameray*tileheight,
                                                  crystalObj['size'],
                                                  crystalObj['size']) )
        
    #     DISPLAYSURF.blit(crystalObj['surface'], (crystalObj['x']*tilewidth + camerax*tilewidth, crystalObj['y']*tileheight + cameray*tileheight))
        DISPLAYSURF.blit(crystalObj['surface'], crystalObj['rect'])
#         pygame.draw.rect(DISPLAYSURF, GRASSCOLOR, crystalObj['rect'])
                
        crystalCollision1.append(crystalObj)
        
    return crystalCollision1

