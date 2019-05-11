

import random, sys, time, math, pygame
from pygame.locals import *

BLACK = (0, 0, 0)
BGCOLOR = (100, 50, 50)
WHITE = (255, 255, 255)
GRAY= (185, 185, 185)
TEXTSHADOWCOLOR = GRAY
TEXTCOLOR = WHITE


def showStartScreen(text, FPSCLOCK, WINWIDTH, WINHEIGHT, DISPLAYSURF, BIGFONT, BASICFONT, INVULNTIME):
    
    DISPLAYSURF.fill(BGCOLOR)
    
    titleSurf, titleRect = makeTextObjs(text, BIGFONT, TEXTSHADOWCOLOR)
    titleRect.center = (int(WINWIDTH / 2), int(WINHEIGHT / 2))
    DISPLAYSURF.blit(titleSurf, titleRect)

    # Draw the text
    titleSurf, titleRect = makeTextObjs(text, BIGFONT, TEXTCOLOR)
    titleRect.center = (int(WINWIDTH / 2) - 3, int(WINHEIGHT / 2) - 3)
    DISPLAYSURF.blit(titleSurf, titleRect)

    # Draw the additional "Press a key to play." text.
    pressKeySurf, pressKeyRect = makeTextObjs('Start', BASICFONT, TEXTCOLOR)
    pressKeyRect.center = (int(WINWIDTH / 2), int(WINHEIGHT / 2) + 100)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

    while True:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
                    
            elif event.type == KEYDOWN:
                if event.key == K_z:
                    print('........................  Play game  ................... ')
                    
                    RUNGAME = True
                    
                    return RUNGAME
        
        pygame.display.update()
        FPSCLOCK.tick()


def showTextScreen(text, FPSCLOCK, WINWIDTH, WINHEIGHT, DISPLAYSURF, BIGFONT, BASICFONT):
    
    # show Big text
    
    titleSurf, titleRect = makeTextObjs(text, BIGFONT, TEXTSHADOWCOLOR)
    titleRect.center = (int(WINWIDTH / 2), int(WINHEIGHT / 2))
    DISPLAYSURF.blit(titleSurf, titleRect)

    # Draw the text
    titleSurf, titleRect = makeTextObjs(text, BIGFONT, TEXTCOLOR)
    titleRect.center = (int(WINWIDTH / 2) - 3, int(WINHEIGHT / 2) - 3)
    DISPLAYSURF.blit(titleSurf, titleRect)

    # Draw the additional "Press a key to play." text.
    pressKeySurf, pressKeyRect = makeTextObjs('Press a key to play.', BASICFONT, TEXTCOLOR)
    pressKeyRect.center = (int(WINWIDTH / 2), int(WINHEIGHT / 2) + 100)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

    while checkForKeyPress() == None:
        pygame.display.update()
        FPSCLOCK.tick()
        

def makeTextObjs(text, font, color):
    surf = font.render(text, True, color)
    return surf, surf.get_rect()

def checkForKeyPress():

    for event in pygame.event.get([KEYDOWN, KEYUP]):
        if event.type == KEYDOWN:
            continue
        return event.key
    return None     


def terminate():
    pygame.quit()
    sys.exit()
    

