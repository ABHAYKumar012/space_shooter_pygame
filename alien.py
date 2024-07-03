import pygame
from pygame.sprite import Sprite

class Alien(Sprite):    #alien class inherited with sprite class 
    """A class for single alien ship"""
    def __init__(self , ai_settings,screen) -> None:
        """initilizing alien"""
        super().__init__()
        self.screen=screen
        self.ai_settings=ai_settings

        self.image=pygame.image.load("alienship1.jpg")   #load meteor image
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.topright=self.screen_rect.topright
        

        self.x=float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image,self.rect)  

    def update(self):
        self.rect.y+=(self.ai_settings.alien_speed*self.ai_settings.direction)

    def check_edges(self):
        """return true if alien is at edge of screen"""
        
        if self.rect.bottom>=self.screen_rect.bottom:
            return True
        if self.rect.top<=0:
            return True

                


