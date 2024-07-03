import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    """ class to manage bullet fired form ship"""
    def __init__(self,ai_settings,screen,ship) -> None:
        """creating bullet object at ship current position"""
        super().__init__()  
        self.screen=screen

        #creating bullet at initial position(0,0) , then setting position

        self.rect=pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centery = ship.rect.centery
        self.rect.left = ship.rect.right
         

        # Store the bullet's position as a decimal value.
        self.x = float(self.rect.x)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed


    def update(self):
        """MOving bullet"""
        #update decimal position of bullet
        self.x+=self.speed_factor
        # updaet rect position
        self.rect.x=self.x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)  