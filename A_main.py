import pygame
from settings import Settings
from game_stats import Gamestats
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from button import Button
#from alien import Alien



def run_Game():
    
    pygame.init()    #Initialize backgroun settings that pygame needs to work properly
    ai_settings=Settings()     #object of settings class
    
    screen=pygame.display.set_mode((ai_settings.s_width,ai_settings.s_height))    #create display
    pygame.display.set_caption("Space Shooter")  #set display name
    ship=Ship(ai_settings,screen)   #make the ship
    #alien=Alien(ai_settings,screen,ship)
    clock=pygame.time.Clock() #to set fps
    bullets = Group()   #groupiing bullets
    aliens=Group()  #grouping alien fleet
    #make play button
    play_button=Button(screen,"Play","Exit","Help") #object of button class
    gf.fleet(ai_settings,screen,aliens) #fleet function call
    stats=Gamestats(ai_settings)    #an instance to store game statistics

    while True:       #Start main loop of game
        gf.check_Events(ai_settings,screen,ship,bullets,stats,play_button,aliens)
        if stats.game_active: 
            ship.update()   #update function fron ship class 
            bullets.update()    #update function from bullet class
            gf.delet_bullets(ship,bullets)
            gf.update_fleet(ai_settings,screen,aliens,bullets)        
            gf.update_aliens(ai_settings,aliens,ship,stats,screen,bullets) 
            
        gf.update_screen(ai_settings,screen,ship,bullets,aliens,play_button,stats)
        clock.tick(60)  #set fps
        

run_Game()
