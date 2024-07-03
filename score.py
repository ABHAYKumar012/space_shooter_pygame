import pygame.font

class score():
    """ to report scoring info"""
    def __init__(self,ai_settings,screen,stats) -> None:
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.ai_settings=ai_settings
        self.stats=stats

        #font setting for scoring
        self.text_color=(30,30,30)
        self.font=pygame.font.SysFont(None,48)
        #prepare the initial score image