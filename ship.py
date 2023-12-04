import pygame
import random
import helpers

class Ship(pygame.sprite.Sprite):
    def __init__(self,screen):
        super().__init__()
        #self.image = pygame.Surface((150,50))
        #self.image.fill((0,0,220))
        self.image = pygame.image.load('images/ship.png')
        self.image = pygame.transform.scale_by(self.image, 1)
        self.rect = self.image.get_rect()
        self.rect.x = screen.get_width()/2
        self.rect.y = 475
        self.velocity = 0

    def update(self):
        self.rect.x += self.velocity
        self.check_collision()

    def kill_ship(self):
        # get our cannonball location
        grenade_coord = self.rect.center
        # loop over each ship in ship group
        for ship in self.ship_group:
            # calc the distance to that ship from the cannonball
            ship_coord = ship.rect.center
            # if it's close, kill it
            if self.get_distance(grenade_coord,ship_coord)< self.kill_radius:
                # turn that ship into a skeleton!
                ship.skeleton()

    def skeleton(self):
        self.image = pygame.image.load('images/graveyard.png')
        self.dead_timer = pygame.time.get_ticks()
        self.velocity = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def destroy(self):
        self.rect.x
        self.image = pygame.image.load('images/graveyard.png')
        self.velocity = 0

    def check_collision(self):
        # check if ship hits the border. Stop the ship
        buffer = 10
        if self.rect.x < buffer:
            self.velocity = 3
        #tile size is 60 and screen size is 1080
        if self.rect.x > 1080-60- buffer:
            self.velocity = -3