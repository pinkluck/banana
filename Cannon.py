import pygame
from math import sqrt, sin, cos, pi
class Cannonball(pygame.sprite.Sprite):
    def __init__(self,pos, ship_group, x, y):
        super().__init__()
        # attributes  image, rect, velocity
        self.image = pygame.image.load('images/cannonball.png')
        self.image = pygame.transform.scale_by(self.image, .1)
        self.rect = self.image.get_rect()
        self.rect.midtop = pos
        self.velocity_y = 2
        self.velocity_x = 2
        self.boom_time = 0
        #self.creation = pygame.time.set_timer()
        self.ship_group = ship_group
        self.kill_radius = 30
        self.collision_radius = 30
        self.x = x
        self.speed = 10
        self.y = y
        self.theta = 45
        self.rect.center = (x, y)
        self.zoom = 1
        self.x_dot = self.speed * cos(self.theta * pi/180)
        self.y_dot = self.speed * sin(self.theta * pi / 180)

        self.x_ddot = 0
        self.y_ddot = 0

        self.drag = 2e-2
        self.gravity = 2e-2

    def update(self):
        # ball moves up
        #self.rect.y -= self.velocity_y
        #self.rect.x += self.velocity_x
        if self.boom_time:
            if pygame.time.get_ticks() - self.boom_time > 1000:
                # grenade dies
                self.kill()
        # check to see if we hit any fish IF we haven't already boomed!
        self.check_ship_hit()
        # code here for the bullet trajectory
        self.x += self.x_dot
        self.y -= self.y_dot

        # handle the velocity
        self.x_dot += self.x_ddot
        self.y_dot += self.y_ddot

        # handle the acceleration
        self.x_ddot = -self.drag * self.x_dot
        self.y_ddot = -self.drag * self.y_dot - self.gravity

        # Update the bullet's rect
        self.rect.center = (self.x, self.y)
    def check_collision(self):
        # check if  hits the border. Stop the car
        buffer = 50

        if self.x > self.screen.get_width() - 50:
            self.velocity = -0.2

    def get_distance(self, coord1, coord2):
        x1, y1 = coord1
        x2, y2 = coord2
        return sqrt( (x2-x1)**2 + (y2-y1)**2 )

    def get_sprite_distance(self, sprite1, sprite2):
        coord1 = sprite1.rect.center
        coord2 = sprite2.rect.center
        return (self.get_distance(coord1,coord2) < self.collision_radius)
    def check_ship_hit(self):
        # check for collisions with the fish group use spritecollide
        hit_ship_list = pygame.sprite.spritecollide(self, self.ship_group, 0,  collided=self.get_sprite_distance )
        # if we find a collision, call fish.skeleton()
        for s in hit_ship_list:
            s.skeleton()