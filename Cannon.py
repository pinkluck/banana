import pygame
class Cannonball(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        # attributes  image, rect, velocity
        self.image = pygame.image.load('images/cannonball.png')
        self.image = pygame.transform.scale_by(self.image, .1)
        self.rect = self.image.get_rect()
        self.rect.midtop = pos
        self.velocity_y = 0
        self.velocity_x = 2
        self.boom_time = 0

    def update(self):
        # ball moves up
        self.rect.y -= self.velocity_y
        self.rect.x += self.velocity_x
        # check if the ball has been boomed, then delete after 1 second
        if self.boom_time:
            if pygame.time.get_ticks() - self.boom_time > 1000:
                # grenade dies
                self.kill()
    def boom(self):
        self.boom_time = pygame.time.get_ticks()
        # ball changes its image
        self.image = pygame.image.load('images/splat00.png')
        self.velocity = 0