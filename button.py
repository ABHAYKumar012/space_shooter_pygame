import pygame.font

class Button():

    def __init__(self,screen,msg,msg_1,msg_2) -> None:
        """initialize button attributes"""
        self.screen=screen
        self.screen_rect=screen.get_rect()

        #set dimensions and properties of button
        self.width ,self.height=200,50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
       
        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect1 = pygame.Rect(0, 0, self.width, self.height)
        self.rect2 = pygame.Rect(0, 0, self.width, self.height)
        #play
        self.rect.top = self.screen_rect.top
        self.rect.centerx = self.screen_rect.centerx
        #exit
        self.rect1.bottom = self.screen_rect.bottom
        self.rect1.centerx = self.screen_rect.centerx
        #help
        self.rect2.center = self.screen_rect.center

       
        # The button message needs to be prepped only once.
        self.pre_msg(msg)
        self.ex_msg(msg_1)
        self.h_msg(msg_2)

    def pre_msg(self,msg):
        """Turn msg into render image and center text on button"""
        self.msg_image=self.font.render(msg, True, self.text_color,self.button_color)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.top=self.rect.top
        self.msg_image_rect.centerx=self.rect.centerx
    
    def ex_msg(self,msg_1):
        """Turn msg into render image and center text on button"""
        self.msg_image_1=self.font.render(msg_1, True, self.text_color,self.button_color)
        self.msg_image_rect_1=self.msg_image_1.get_rect()
        self.msg_image_rect_1.bottom=self.rect1.bottom
        self.msg_image_rect_1.centerx=self.rect1.centerx

    def h_msg(self,msg_2):
        """Turn msg into render image and center text on button"""
        self.msg_image_2=self.font.render(msg_2, True, self.text_color,self.button_color)
        self.msg_image_rect_2=self.msg_image_2.get_rect()
        self.msg_image_rect_2.center=self.rect2.center
        


    def draw_button(self):
        """draw a black button than message"""    
        self.screen.fill(self.button_color,self.rect)
        self.screen.fill(self.button_color,self.rect1)
        self.screen.fill(self.button_color,self.rect2)
        self.screen.blit(self.msg_image,self.msg_image_rect)
        self.screen.blit(self.msg_image_1,self.msg_image_rect_1)
        self.screen.blit(self.msg_image_2,self.msg_image_rect_2)
        