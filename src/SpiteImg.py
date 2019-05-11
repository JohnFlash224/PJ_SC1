

import random, sys, time, math, pygame
from pygame.locals import *
import pytmx
from pytmx.util_pygame import load_pygame


def LeftRight():
    left_standing = pygame.image.load('img/crono_left_walk.000.gif')
    right_standing = pygame.transform.flip(left_standing, True, False)
    left_jump = pygame.image.load('img/crono_left_run.001.gif')
    right_jump = pygame.transform.flip(left_jump, True, False)
    
    return left_standing, right_standing, left_jump, right_jump



def getLeftWalk_img(left_walks,STARTSIZE):
    left_walks.append(pygame.transform.scale(pygame.image.load('img/crono_left_walk.000.gif'), (STARTSIZE, STARTSIZE)))
    left_walks.append(pygame.transform.scale(pygame.image.load('img/crono_left_walk.001.gif'), (STARTSIZE, STARTSIZE)))
    left_walks.append(pygame.transform.scale(pygame.image.load('img/crono_left_walk.002.gif'), (STARTSIZE, STARTSIZE)))
    left_walks.append(pygame.transform.scale(pygame.image.load('img/crono_left_walk.003.gif'), (STARTSIZE, STARTSIZE)))
    left_walks.append(pygame.transform.scale(pygame.image.load('img/crono_left_walk.004.gif'), (STARTSIZE, STARTSIZE)))
    left_walks.append(pygame.transform.scale(pygame.image.load('img/crono_left_walk.005.gif'), (STARTSIZE, STARTSIZE)))


def getRightWalk_img(right_walks,left_walks):
    for i in range(6):
        right_walks.append(pygame.transform.flip(left_walks[i], True, False))


def Fire_img():
    Flame_IMG=pygame.image.load('img3/flame_a_0001.png')
    
    return Flame_IMG




        