import pygame
from random import randint

# this function will take 2 surface and center the 2nd surface on the first one
def center_surfaces(bg, fg):
    # get the bg width and height
    bg_width = bg.get_width()
    bg_height = bg.get_height()
    # get the front surface width and height
    fg_width = fg.get_width()
    fg_height = fg.get_height()
    # blit the text on the surface
    bg.blit(fg, (bg_width/2 - fg_width/2, bg_height/2-fg_height/2 ))

def make_background(screen):
    WIDTH = screen.get_width()
    HEIGHT = screen.get_height()
    parchment = pygame.image.load('images/parchmentFolded.png')
    watertext = pygame.image.load('images/textureWater.png')
    parchment_width = parchment.get_width()
    parchment_height = parchment.get_height()
    tile_width = watertext.get_width()
    tile_height = watertext.get_height()
    # make a background
    background = pygame.Surface((WIDTH,HEIGHT))
    # draw parchment background
    for x in range(0,WIDTH,parchment_width):
        for y in range(0,HEIGHT,parchment_height):
            background.blit(parchment, (x,y))
    # draw water tile
    for x in range(0,WIDTH,tile_width):
        background.blit(watertext, (x,HEIGHT-2*tile_height))
    # draw water top tile
    for x in range(0,WIDTH,tile_width):
        background.blit(watertext, (x,HEIGHT-3*tile_height))
    return background