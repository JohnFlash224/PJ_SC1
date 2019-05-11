
import random, sys, time, math, pygame
from pygame.locals import *
import pytmx
from pytmx.util_pygame import load_pygame

GRASSCOLOR = (24, 255, 0)

def initMap():
    tiled_map = load_pygame('Map/maptn5.tmx', pixelalpha=True)
    tilewidth = tiled_map.tilewidth
    tileheight = tiled_map.tileheight

    return tiled_map,tilewidth,tileheight



def renderMap(tiled_map, tilewidth, tileheight, DISPLAYSURF, camerax, cameray):
    for layer in tiled_map.layers:
        if isinstance(layer, pytmx.TiledTileLayer):
                
            for x, y, tile in layer.tiles():
                if (tile):
                    DISPLAYSURF.blit(tile, [( x + camerax )*tilewidth,( y + cameray )*tileheight])
                        
                        
def drawRectTerrain(tilewidth, tileheight, WHITE, DISPLAYSURF, camerax, cameray, SET_ALPHA):
    
    tiledGrass1_size = (51*tilewidth,3*tileheight)
    tiledGrass1_rect =  pygame.Surface(tiledGrass1_size)
    tiledGrass1_rect.set_alpha(SET_ALPHA)
    tiledGrass1_rect.fill(WHITE)
    tiledGrass1 = DISPLAYSURF.blit(tiledGrass1_rect, (0*tilewidth + camerax*tilewidth,13*tileheight + cameray*tileheight))
    
    tiledStone1_size = (11*tilewidth,1*tileheight)
    tiledStone1_rect =  pygame.Surface(tiledStone1_size)
    tiledStone1_rect.set_alpha(SET_ALPHA)
    tiledStone1_rect.fill(WHITE)
    tiledStone1 = DISPLAYSURF.blit(tiledStone1_rect, (12*tilewidth + camerax*tilewidth,12*tileheight + cameray*tileheight))
        
    return tiledGrass1, tiledStone1


def drawRectTerrainList(tilewidth, tileheight, WHITE, DISPLAYSURF, camerax, cameray, SET_ALPHA):
    
    tiledColisions = []
    tiledColisions2 = []
    tiledColisions3 = []
    tiledColisions4 = []
    tiledColisions5 = []
    tiledColisions6 = []
    
    # Area 1 
    
    tileStart1 = { 'area': 1, 'type': 'ground', 'X': 0,'Y': 0, 'sizeX': 1,'sizeY': 16 }
    tileStart1_size = (tileStart1['sizeX']*tilewidth,tileStart1['sizeY']*tileheight)
    tileStart1_rect =  pygame.Surface(tileStart1_size)
    tileStart1_rect.set_alpha(SET_ALPHA)
    tileStart1_rect.fill(WHITE)
    tileStart1['rect'] = DISPLAYSURF.blit(tileStart1_rect, (tileStart1['X']*tilewidth + camerax*tilewidth,tileStart1['Y']*tileheight + cameray*tileheight))
    
    tiledGrass1 = { 'area':1, 'type': 'ground', 'X': 0,'Y': 13, 'sizeX': 51,'sizeY': 3   }
    tiledGrass1_size = (tiledGrass1['sizeX']*tilewidth,tiledGrass1['sizeY']*tileheight)
    tiledGrass1_rect =  pygame.Surface(tiledGrass1_size)
    tiledGrass1_rect.set_alpha(SET_ALPHA)
    tiledGrass1_rect.fill(WHITE)
    tiledGrass1['rect'] = DISPLAYSURF.blit(tiledGrass1_rect, (tiledGrass1['X']*tilewidth + camerax*tilewidth,tiledGrass1['Y']*tileheight + cameray*tileheight))
    
    tiledStone1={ 'area':1, 'type': 'ground', 'X': 12,'Y': 12, 'sizeX': 11,'sizeY': 1  }
    tiledStone1_size = (tiledStone1['sizeX']*tilewidth,tiledStone1['sizeY']*tileheight)
    tiledStone1_rect =  pygame.Surface(tiledStone1_size)
    tiledStone1_rect.set_alpha(SET_ALPHA)
    tiledStone1_rect.fill(WHITE)
    tiledStone1['rect'] = DISPLAYSURF.blit(tiledStone1_rect, (tiledStone1['X']*tilewidth + camerax*tilewidth,tiledStone1['Y']*tileheight + cameray*tileheight))
    
    tiledStone2={ 'area':1, 'type': 'ground', 'X': 13,'Y': 11, 'sizeX': 9,'sizeY': 1   }
    tiledStone2_size = (tiledStone2['sizeX']*tilewidth,tiledStone2['sizeY']*tileheight)
    tiledStone2_rect =  pygame.Surface(tiledStone2_size)
    tiledStone2_rect.set_alpha(SET_ALPHA)
    tiledStone2_rect.fill(WHITE)
    tiledStone2['rect'] = DISPLAYSURF.blit(tiledStone2_rect, (tiledStone2['X']*tilewidth + camerax*tilewidth,tiledStone2['Y']*tileheight + cameray*tileheight))
    
    tiledStone3={ 'area':1, 'type': 'ground', 'X': 14,'Y': 10, 'sizeX': 7,'sizeY': 1   }
    tiledStone3_size = (tiledStone3['sizeX']*tilewidth,tiledStone3['sizeY']*tileheight)
    tiledStone3_rect =  pygame.Surface(tiledStone3_size)
    tiledStone3_rect.set_alpha(SET_ALPHA)
    tiledStone3_rect.fill(WHITE)
    tiledStone3['rect'] = DISPLAYSURF.blit(tiledStone3_rect, (tiledStone3['X']*tilewidth + camerax*tilewidth,tiledStone3['Y']*tileheight + cameray*tileheight))
    
    tiledStone4={ 'area':1, 'type': 'ground', 'X': 15,'Y': 9, 'sizeX': 5,'sizeY': 1   }
    tiledStone4_size = (tiledStone4['sizeX']*tilewidth,tiledStone4['sizeY']*tileheight)
    tiledStone4_rect =  pygame.Surface(tiledStone4_size)
    tiledStone4_rect.set_alpha(SET_ALPHA)
    tiledStone4_rect.fill(WHITE)
    tiledStone4['rect'] = DISPLAYSURF.blit(tiledStone4_rect, (tiledStone4['X']*tilewidth + camerax*tilewidth,tiledStone4['Y']*tileheight + cameray*tileheight))
    
    tiledStone5={ 'area':1, 'type': 'ground', 'X': 16,'Y': 8, 'sizeX': 3,'sizeY': 1   }
    tiledStone5_size = (tiledStone5['sizeX']*tilewidth,tiledStone5['sizeY']*tileheight)
    tiledStone5_rect =  pygame.Surface(tiledStone5_size)
    tiledStone5_rect.set_alpha(SET_ALPHA)
    tiledStone5_rect.fill(WHITE)
    tiledStone5['rect'] = DISPLAYSURF.blit(tiledStone5_rect, (tiledStone5['X']*tilewidth + camerax*tilewidth,tiledStone5['Y']*tileheight + cameray*tileheight))
    
    tiledSnow1={ 'area':1, 'type': 'ground', 'X': 25,'Y': 8, 'sizeX': 5,'sizeY': 2   }
    tiledSnow1_size = (tiledSnow1['sizeX']*tilewidth,tiledSnow1['sizeY']*tileheight)
    tiledSnow1_rect =  pygame.Surface(tiledSnow1_size)
    tiledSnow1_rect.set_alpha(SET_ALPHA)
    tiledSnow1_rect.fill(WHITE)
    tiledSnow1['rect'] = DISPLAYSURF.blit(tiledSnow1_rect, (tiledSnow1['X']*tilewidth + camerax*tilewidth,tiledSnow1['Y']*tileheight + cameray*tileheight))
    
    
    tiledSnow2={ 'area':1, 'type': 'ground', 'X': 33,'Y': 6, 'sizeX': 6,'sizeY': 2   }
    tiledSnow2_size = (tiledSnow2['sizeX']*tilewidth,tiledSnow2['sizeY']*tileheight)
    tiledSnow2_rect =  pygame.Surface(tiledSnow2_size)
    tiledSnow2_rect.set_alpha(SET_ALPHA)
    tiledSnow2_rect.fill(WHITE)
    tiledSnow2['rect'] = DISPLAYSURF.blit(tiledSnow2_rect, (tiledSnow2['X']*tilewidth + camerax*tilewidth,tiledSnow2['Y']*tileheight + cameray*tileheight))
    
    tiledSnow3={ 'area':1, 'type': 'ground', 'X': 38,'Y': 12, 'sizeX': 6,'sizeY': 1   }
    tiledSnow3_size = (tiledSnow3['sizeX']*tilewidth,tiledSnow3['sizeY']*tileheight)
    tiledSnow3_rect =  pygame.Surface(tiledSnow3_size)
    tiledSnow3_rect.set_alpha(SET_ALPHA)
    tiledSnow3_rect.fill(WHITE)
    tiledSnow3['rect'] = DISPLAYSURF.blit(tiledSnow3_rect, (tiledSnow3['X']*tilewidth + camerax*tilewidth,tiledSnow3['Y']*tileheight + cameray*tileheight))
    
    tiledTyp1={ 'area':1, 'type': 'ground', 'X': 44,'Y': 9, 'sizeX': 3,'sizeY': 4   }
    tiledTyp1_size = (tiledTyp1['sizeX']*tilewidth,tiledTyp1['sizeY']*tileheight)
    tiledTyp1_rect =  pygame.Surface(tiledTyp1_size)
    tiledTyp1_rect.set_alpha(SET_ALPHA)
    tiledTyp1_rect.fill(WHITE)
    tiledTyp1['rect'] = DISPLAYSURF.blit(tiledTyp1_rect, (tiledTyp1['X']*tilewidth + camerax*tilewidth,tiledTyp1['Y']*tileheight + cameray*tileheight))
    
   
    
    # Area 2 
    
    tiledGrass2 = { 'area':2, 'type': 'ground', 'X': 53,'Y': 10, 'sizeX': 6,'sizeY': 2   }
    tiledGrass2_size = (tiledGrass2['sizeX']*tilewidth,tiledGrass2['sizeY']*tileheight)
    tiledGrass2_rect =  pygame.Surface(tiledGrass2_size)
    tiledGrass2_rect.set_alpha(SET_ALPHA)
    tiledGrass2_rect.fill(WHITE)
    tiledGrass2['rect'] = DISPLAYSURF.blit(tiledGrass2_rect, (tiledGrass2['X']*tilewidth + camerax*tilewidth,tiledGrass2['Y']*tileheight + cameray*tileheight))
    
    tiledGrass3 = { 'area':2, 'type': 'ground', 'X': 61,'Y': 8, 'sizeX': 7,'sizeY': 2   }
    tiledGrass3_size = (tiledGrass3['sizeX']*tilewidth,tiledGrass3['sizeY']*tileheight)
    tiledGrass3_rect =  pygame.Surface(tiledGrass3_size)
    tiledGrass3_rect.set_alpha(SET_ALPHA)
    tiledGrass3_rect.fill(WHITE)
    tiledGrass3['rect'] = DISPLAYSURF.blit(tiledGrass3_rect, (tiledGrass3['X']*tilewidth + camerax*tilewidth,tiledGrass3['Y']*tileheight + cameray*tileheight))
    
    tiledSea1 = { 'area':2, 'type': 'sea', 'X': 51,'Y': 14, 'sizeX': 19,'sizeY': 2   }
    tiledSea1_size = (tiledSea1['sizeX']*tilewidth,tiledSea1['sizeY']*tileheight)
    tiledSea1_rect =  pygame.Surface(tiledSea1_size)
    tiledSea1_rect.set_alpha(SET_ALPHA)
    tiledSea1_rect.fill(WHITE)
    tiledSea1['rect'] = DISPLAYSURF.blit(tiledSea1_rect, (tiledSea1['X']*tilewidth + camerax*tilewidth,tiledSea1['Y']*tileheight + cameray*tileheight))
    
    tiledSand1 = { 'area':2, 'type': 'ground', 'X': 70,'Y': 13, 'sizeX': 52,'sizeY': 3   }
    tiledSand1_size = (tiledSand1['sizeX']*tilewidth,tiledSand1['sizeY']*tileheight)
    tiledSand1_rect =  pygame.Surface(tiledSand1_size)
    tiledSand1_rect.set_alpha(SET_ALPHA)
    tiledSand1_rect.fill(WHITE)
    tiledSand1['rect'] = DISPLAYSURF.blit(tiledSand1_rect, (tiledSand1['X']*tilewidth + camerax*tilewidth,tiledSand1['Y']*tileheight + cameray*tileheight))
    
    tiledGrass4 = { 'area':2, 'type': 'ground', 'X': 72,'Y': 5, 'sizeX': 6,'sizeY': 2   }
    tiledGrass4_size = (tiledGrass4['sizeX']*tilewidth,tiledGrass4['sizeY']*tileheight)
    tiledGrass4_rect =  pygame.Surface(tiledGrass4_size)
    tiledGrass4_rect.set_alpha(SET_ALPHA)
    tiledGrass4_rect.fill(WHITE)
    tiledGrass4['rect'] = DISPLAYSURF.blit(tiledGrass4_rect, (tiledGrass4['X']*tilewidth + camerax*tilewidth,tiledGrass4['Y']*tileheight + cameray*tileheight))
    
    tiledStone6={ 'area':2, 'type': 'ground', 'X': 85,'Y': 10, 'sizeX': 4,'sizeY': 1   }
    tiledStone6_size = (tiledStone6['sizeX']*tilewidth,tiledStone6['sizeY']*tileheight)
    tiledStone6_rect =  pygame.Surface(tiledStone6_size)
    tiledStone6_rect.set_alpha(SET_ALPHA)
    tiledStone6_rect.fill(WHITE)
    tiledStone6['rect'] = DISPLAYSURF.blit(tiledStone6_rect, (tiledStone6['X']*tilewidth + camerax*tilewidth,tiledStone6['Y']*tileheight + cameray*tileheight))
    
    tiledStone7={ 'area':2, 'type': 'ground', 'X': 85,'Y': 11, 'sizeX': 8,'sizeY': 2   }
    tiledStone7_size = (tiledStone7['sizeX']*tilewidth,tiledStone7['sizeY']*tileheight)
    tiledStone7_rect =  pygame.Surface(tiledStone7_size)
    tiledStone7_rect.set_alpha(SET_ALPHA)
    tiledStone7_rect.fill(WHITE)
    tiledStone7['rect'] = DISPLAYSURF.blit(tiledStone7_rect, (tiledStone7['X']*tilewidth + camerax*tilewidth,tiledStone7['Y']*tileheight + cameray*tileheight))
    
    tiledStone8={ 'area':2, 'type': 'ground', 'X': 101,'Y': 12, 'sizeX': 1,'sizeY': 1   }
    tiledStone8_size = (tiledStone8['sizeX']*tilewidth,tiledStone8['sizeY']*tileheight)
    tiledStone8_rect =  pygame.Surface(tiledStone8_size)
    tiledStone8_rect.set_alpha(SET_ALPHA)
    tiledStone8_rect.fill(WHITE)
    tiledStone8['rect'] = DISPLAYSURF.blit(tiledStone8_rect, (tiledStone8['X']*tilewidth + camerax*tilewidth,tiledStone8['Y']*tileheight + cameray*tileheight))
    
    tiledStone9={ 'area':2, 'type': 'ground', 'X': 104,'Y': 11, 'sizeX': 1,'sizeY': 2   }
    tiledStone9_size = (tiledStone9['sizeX']*tilewidth,tiledStone9['sizeY']*tileheight)
    tiledStone9_rect =  pygame.Surface(tiledStone9_size)
    tiledStone9_rect.set_alpha(SET_ALPHA)
    tiledStone9_rect.fill(WHITE)
    tiledStone9['rect'] = DISPLAYSURF.blit(tiledStone9_rect, (tiledStone9['X']*tilewidth + camerax*tilewidth,tiledStone9['Y']*tileheight + cameray*tileheight))
    
    tiledStone10={ 'area':2, 'type': 'ground', 'X': 107,'Y': 10, 'sizeX': 1,'sizeY': 3   }
    tiledStone10_size = (tiledStone10['sizeX']*tilewidth,tiledStone10['sizeY']*tileheight)
    tiledStone10_rect =  pygame.Surface(tiledStone10_size)
    tiledStone10_rect.set_alpha(SET_ALPHA)
    tiledStone10_rect.fill(WHITE)
    tiledStone10['rect'] = DISPLAYSURF.blit(tiledStone10_rect, (tiledStone10['X']*tilewidth + camerax*tilewidth,tiledStone10['Y']*tileheight + cameray*tileheight))
    
    tiledStone11={ 'area':2, 'type': 'ground', 'X': 110,'Y': 9, 'sizeX': 1,'sizeY': 4   }
    tiledStone11_size = (tiledStone11['sizeX']*tilewidth,tiledStone11['sizeY']*tileheight)
    tiledStone11_rect =  pygame.Surface(tiledStone11_size)
    tiledStone11_rect.set_alpha(SET_ALPHA)
    tiledStone11_rect.fill(WHITE)
    tiledStone11['rect'] = DISPLAYSURF.blit(tiledStone11_rect, (tiledStone11['X']*tilewidth + camerax*tilewidth,tiledStone11['Y']*tileheight + cameray*tileheight))
    
    tiledStone12={ 'area':2, 'type': 'ground', 'X': 113,'Y': 10, 'sizeX': 1,'sizeY': 3   }
    tiledStone12_size = (tiledStone12['sizeX']*tilewidth,tiledStone12['sizeY']*tileheight)
    tiledStone12_rect =  pygame.Surface(tiledStone12_size)
    tiledStone12_rect.set_alpha(SET_ALPHA)
    tiledStone12_rect.fill(WHITE)
    tiledStone12['rect'] = DISPLAYSURF.blit(tiledStone12_rect, (tiledStone12['X']*tilewidth + camerax*tilewidth,tiledStone12['Y']*tileheight + cameray*tileheight))
    
    tiledStone13={ 'area':2, 'type': 'ground', 'X': 116,'Y': 11, 'sizeX': 1,'sizeY': 2   }
    tiledStone13_size = (tiledStone13['sizeX']*tilewidth,tiledStone13['sizeY']*tileheight)
    tiledStone13_rect =  pygame.Surface(tiledStone13_size)
    tiledStone13_rect.set_alpha(SET_ALPHA)
    tiledStone13_rect.fill(WHITE)
    tiledStone13['rect'] = DISPLAYSURF.blit(tiledStone13_rect, (tiledStone13['X']*tilewidth + camerax*tilewidth,tiledStone13['Y']*tileheight + cameray*tileheight))
    
    tiledStone14={ 'area':2, 'type': 'ground', 'X': 118,'Y': 12, 'sizeX': 1,'sizeY': 1   }
    tiledStone14_size = (tiledStone14['sizeX']*tilewidth,tiledStone14['sizeY']*tileheight)
    tiledStone14_rect =  pygame.Surface(tiledStone14_size)
    tiledStone14_rect.set_alpha(SET_ALPHA)
    tiledStone14_rect.fill(WHITE)
    tiledStone14['rect'] = DISPLAYSURF.blit(tiledStone14_rect, (tiledStone14['X']*tilewidth + camerax*tilewidth,tiledStone14['Y']*tileheight + cameray*tileheight))
    
    
    # Area 3
    
    
    tiledSea2 = { 'area':3, 'type': 'sea', 'X': 122,'Y': 14, 'sizeX': 48,'sizeY': 2   }
    tiledSea2_size = (tiledSea2['sizeX']*tilewidth,tiledSea2['sizeY']*tileheight)
    tiledSea2_rect =  pygame.Surface(tiledSea2_size)
    tiledSea2_rect.set_alpha(SET_ALPHA)
    tiledSea2_rect.fill(WHITE)
    tiledSea2['rect'] = DISPLAYSURF.blit(tiledSea2_rect, (tiledSea2['X']*tilewidth + camerax*tilewidth,tiledSea2['Y']*tileheight + cameray*tileheight))
    
    tiledSnow4={ 'area':3, 'type': 'ground', 'X': 124,'Y': 10, 'sizeX': 5,'sizeY': 2   }
    tiledSnow4_size = (tiledSnow4['sizeX']*tilewidth,tiledSnow4['sizeY']*tileheight)
    tiledSnow4_rect =  pygame.Surface(tiledSnow4_size)
    tiledSnow4_rect.set_alpha(SET_ALPHA)
    tiledSnow4_rect.fill(WHITE)
    tiledSnow4['rect'] = DISPLAYSURF.blit(tiledSnow4_rect, (tiledSnow4['X']*tilewidth + camerax*tilewidth,tiledSnow4['Y']*tileheight + cameray*tileheight))
    
    tiledSnow5={ 'area':3, 'type': 'ground', 'X': 131,'Y': 7, 'sizeX': 5,'sizeY': 2   }
    tiledSnow5_size = (tiledSnow5['sizeX']*tilewidth,tiledSnow5['sizeY']*tileheight)
    tiledSnow5_rect =  pygame.Surface(tiledSnow5_size)
    tiledSnow5_rect.set_alpha(SET_ALPHA)
    tiledSnow5_rect.fill(WHITE)
    tiledSnow5['rect'] = DISPLAYSURF.blit(tiledSnow5_rect, (tiledSnow5['X']*tilewidth + camerax*tilewidth,tiledSnow5['Y']*tileheight + cameray*tileheight))
    
    tiledSnow6={ 'area':3, 'type': 'ground', 'X': 139,'Y': 5, 'sizeX': 6,'sizeY': 2   }
    tiledSnow6_size = (tiledSnow6['sizeX']*tilewidth,tiledSnow6['sizeY']*tileheight)
    tiledSnow6_rect =  pygame.Surface(tiledSnow6_size)
    tiledSnow6_rect.set_alpha(SET_ALPHA)
    tiledSnow6_rect.fill(WHITE)
    tiledSnow6['rect'] = DISPLAYSURF.blit(tiledSnow6_rect, (tiledSnow6['X']*tilewidth + camerax*tilewidth,tiledSnow6['Y']*tileheight + cameray*tileheight))
    
    tiledSnow7={ 'area':3, 'type': 'ground', 'X': 148,'Y': 11, 'sizeX': 6,'sizeY': 2   }
    tiledSnow7_size = (tiledSnow7['sizeX']*tilewidth,tiledSnow7['sizeY']*tileheight)
    tiledSnow7_rect =  pygame.Surface(tiledSnow7_size)
    tiledSnow7_rect.set_alpha(SET_ALPHA)
    tiledSnow7_rect.fill(WHITE)
    tiledSnow7['rect'] = DISPLAYSURF.blit(tiledSnow7_rect, (tiledSnow7['X']*tilewidth + camerax*tilewidth,tiledSnow7['Y']*tileheight + cameray*tileheight))
    
    tiledSnow8={ 'area':3, 'type': 'ground', 'X': 155,'Y': 8, 'sizeX': 6,'sizeY': 2   }
    tiledSnow8_size = (tiledSnow8['sizeX']*tilewidth,tiledSnow8['sizeY']*tileheight)
    tiledSnow8_rect =  pygame.Surface(tiledSnow8_size)
    tiledSnow8_rect.set_alpha(SET_ALPHA)
    tiledSnow8_rect.fill(WHITE)
    tiledSnow8['rect'] = DISPLAYSURF.blit(tiledSnow8_rect, (tiledSnow8['X']*tilewidth + camerax*tilewidth,tiledSnow8['Y']*tileheight + cameray*tileheight))
    
    tiledSnow9={ 'area':3, 'type': 'ground', 'X': 163,'Y': 6, 'sizeX': 2,'sizeY': 2   }
    tiledSnow9_size = (tiledSnow9['sizeX']*tilewidth,tiledSnow9['sizeY']*tileheight)
    tiledSnow9_rect =  pygame.Surface(tiledSnow9_size)
    tiledSnow9_rect.set_alpha(SET_ALPHA)
    tiledSnow9_rect.fill(WHITE)
    tiledSnow9['rect'] = DISPLAYSURF.blit(tiledSnow9_rect, (tiledSnow9['X']*tilewidth + camerax*tilewidth,tiledSnow9['Y']*tileheight + cameray*tileheight))
    
    tiledSnow10={ 'area':3, 'type': 'ground', 'X': 167,'Y': 4, 'sizeX': 2,'sizeY': 2   }
    tiledSnow10_size = (tiledSnow10['sizeX']*tilewidth,tiledSnow10['sizeY']*tileheight)
    tiledSnow10_rect =  pygame.Surface(tiledSnow10_size)
    tiledSnow10_rect.set_alpha(SET_ALPHA)
    tiledSnow10_rect.fill(WHITE)
    tiledSnow10['rect'] = DISPLAYSURF.blit(tiledSnow10_rect, (tiledSnow10['X']*tilewidth + camerax*tilewidth,tiledSnow10['Y']*tileheight + cameray*tileheight))
    
    
    # ----------------------------------------------------------
    
    # Area 1
    tiledColisions.append(tileStart1)
    tiledColisions.append(tiledGrass1)
    tiledColisions.append(tiledStone1)
    tiledColisions.append(tiledStone2)
    tiledColisions.append(tiledStone3)
    tiledColisions.append(tiledStone4)
    tiledColisions.append(tiledStone5)
    tiledColisions.append(tiledSnow1)
    tiledColisions.append(tiledSnow2)
    tiledColisions.append(tiledSnow3)
    tiledColisions.append(tiledTyp1)
    
    # Area 2
    tiledColisions2.append(tiledGrass2)
    tiledColisions2.append(tiledGrass3)
    tiledColisions2.append(tiledSea1)
    tiledColisions2.append(tiledSand1)
    tiledColisions2.append(tiledGrass4)
    tiledColisions2.append(tiledStone6)
    tiledColisions2.append(tiledStone7)
    tiledColisions2.append(tiledStone8)
    tiledColisions2.append(tiledStone9)
    tiledColisions2.append(tiledStone10)
    tiledColisions2.append(tiledStone11)
    tiledColisions2.append(tiledStone12)
    tiledColisions2.append(tiledStone13)
    tiledColisions2.append(tiledStone14)
    
    
    # Area 3
    
    tiledColisions3.append(tiledSea2)
    tiledColisions3.append(tiledSnow4)
    tiledColisions3.append(tiledSnow5)
    tiledColisions3.append(tiledSnow6)
    tiledColisions3.append(tiledSnow7)
    tiledColisions3.append(tiledSnow8)
    tiledColisions3.append(tiledSnow9)
    tiledColisions3.append(tiledSnow10)

    
    
    return tiledColisions, tiledColisions2, tiledColisions3


# def drawRectCrystal(crystalObj, DISPLAYSURF, SET_ALPHA, camerax, cameray, tilewidth, tileheight):
#     
#     # Area 1 
#     
#     crystal={ 'area':1, 'type': 'crytal' }
#     crystal_size = (30,30)
#     crystal_rect =  pygame.Surface(crystal_size)
#     crystal_rect.set_alpha(SET_ALPHA)
#     crystal_rect.fill(GRASSCOLOR)
#     crystal['rect'] = DISPLAYSURF.blit(crystal_rect, (crystalObj['x']*tilewidth + camerax*tilewidth,crystalObj['y']*tileheight + cameray*tileheight))
# 
#     
# #         print(crystalList)
#     return crystal




    



                        
                        