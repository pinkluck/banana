# Example file showing a basic pygame "game loop"
#import pygame
import pygame

from helpers import *
from ship import Ship
from Cannon import *

# pygame setup
pygame.init()
# make a clock
clock = pygame.time.Clock()
# set the resolution of our game window
WIDTH = 1080
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Make my background once!
background = make_background(screen)

#declare a Font
game_font = pygame.font.SysFont('flanella', 120)

#set up music with auido file
pygame.mixer.music.load('images/drunkensailor.mp3')
pygame.mixer.music.set_volume(.5)
pygame.mixer.music.play(-1)
cannonsound = pygame.mixer.Sound('images/explosion-91872.wav')
#makes cannonball sprite group
cannonball_group = pygame.sprite.Group()
ship_group = pygame.sprite.Group()
# make a boat instance
ship1 = Ship(screen)
ship_group.add(ship1)
#make a 2nd boat
ship2 = Ship(screen)
ship_group.add(ship2)

running = True
while running:
    # pygame.QUIT event means the user clicked X to close your window

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship2.velocity += 1
            if event.key == pygame.K_LEFT:
                ship2.velocity -= 1
            if event.key == pygame.K_d:
                ship1.velocity += 1
            if event.key == pygame.K_a:
                ship1.velocity -=1
            if event.key == pygame.K_DOWN:
                #if less than 1 cannonballs exist drop a grenade if you get a space
                    cannonsound.play()
                    cannonball_group.add(Cannonball(ship2.rect.midtop, ship_group, ship2.rect.centerx, ship2.rect.centery-50))

            if event.key == pygame.K_s:
                cannonsound.play()
                cannonball_group.add(Cannonball(ship1.rect.midbottom,ship_group, ship1.rect.centerx, ship1.rect.centery-50))

    # update my groups
    ship_group.update()
    cannonball_group.update()

    # draw the background on the screen
    screen.blit(background, (0, 0))
    # only draw words in first 3 seconds of game
    if pygame.time.get_ticks() < 3000:
        # draw text
        font_surface = game_font.render('Hello There',1,(0, 0, 0))
        center_surfaces(screen, font_surface)

    #draw cannonball
    cannonball_group.draw(screen)
    # draw the boat
    ship_group.draw(screen)


    clock.tick(60) # run at 60 FPS

    pygame.display.set_caption(f"Hello There {clock.get_fps():.0}")

    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()