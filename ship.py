import pygame

class Ship():

    def __init__(self,ai_settings,screen) -> None:
        
        self.screen=screen
        self.ai_settings=ai_settings
        self.image=pygame.image.load('ship11.jpg') #returns surface erfresenting the ship image
        self.rect=self.image.get_rect() #to treat image(element) like an rectangle
        self.screen_rect=screen.get_rect()

        #positioning the ship image

        self.rect.centery=self.screen_rect.centery
        

        #store a decimal value for ship,s center
        self.center=float(self.rect.centery)

        # Movement flag
        self.moving_up = False
        self.moving_down = False
    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.center -= self.ai_settings.ship_speed
        if self.moving_down and self.rect.bottom <self.screen_rect.bottom :
            self.center += self.ai_settings.ship_speed

        #update rect object feom self.center
        self.rect.centery=self.center
    def blitme(self):

        self.screen.blit(self.image,self.rect)  #to draw the image on screen   
    
    def center_ship(self):
        """center the ship on screen"""
        self.center=self.screen_rect.centery
