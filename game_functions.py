from time import sleep
import sys
import pygame
from alien import Alien 
from bullet import Bullet

level = 1
score = 0


def check_keydown_events(event,ai_settings,screen,ship,bullets,stats,aliens):
    if event.key==pygame.K_UP:
        ship.moving_up=True
    if event.key==pygame.K_DOWN:
        ship.moving_down=True  

    if event.key == pygame.K_SPACE:
         # Create a new bullet and add it to the bullets group.
        
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)     

    if event.key == pygame.K_RETURN and not stats.game_active:
        stats.reset_stats()#reset the game statics
        stats.game_active = True
        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)
        
        
        #empty list of aliens and bullets
       
        bullets.empty()
        aliens.empty()
        #create a new fleet and center the ship
        fleet(ai_settings,screen,aliens)
        ship.center_ship()
    if event.key == pygame.K_SPACE and stats.game_active=="over":
        stats.reset_stats()#reset the game statics
        stats.game_active = True
        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)
        
        
        #empty list of aliens and bullets
       
        bullets.empty()
        aliens.empty()
        #create a new fleet and center the ship
        fleet(ai_settings,screen,aliens)
        ship.center_ship()

    if event.key==pygame.K_ESCAPE:
        sys.exit()          
def check_keyup_events(event,ship):
    if event.key==pygame.K_UP:
        ship.moving_up=False
    if event.key==pygame.K_DOWN:
        ship.moving_down=False   
                        
def check_Events(ai_settings,screen,ship,bullets,stats,play_button,aliens):
    """Responses to keyboard and mouse event"""
    for event in pygame.event.get(): #Read the keyboard and mouse events
            if event.type==pygame.QUIT:  #if exit pressed
                sys.exit() #close the game
            elif event.type==pygame.KEYDOWN:
                check_keydown_events(event,ai_settings,screen, ship,bullets,stats,aliens)
 
                        
            elif event.type==pygame.KEYUP:
                check_keyup_events(event, ship)
            
            elif event.type==pygame.MOUSEBUTTONDOWN:
                """checks play click"""
                mouse_x,mouse_y=pygame.mouse.get_pos()
                check_play_button(stats,play_button,mouse_x,mouse_y,aliens,ai_settings,bullets,screen,ship)


def check_play_button(stats,play_button,mouse_x,mouse_y,aliens,ai_settings,bullets,screen,ship):
    """start new game on click play"""

    button_clicked=play_button.rect.collidepoint(mouse_x, mouse_y)
    exit_clicked=play_button.rect1.collidepoint(mouse_x, mouse_y)
    help_clicked=play_button.rect2.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        stats.reset_stats()#reset the game statics
        stats.game_active = True
        ai_settings.speed_settings()
        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)
        
        #empty list of aliens and bullets
       
        bullets.empty()
        aliens.empty()
        #create a new fleet and center the ship
        fleet(ai_settings,screen,aliens)
        ship.center_ship()              
    
    if exit_clicked and not stats.game_active:
        sys.exit()

    if help_clicked and not stats.game_active:
        screen.fill((255,255,255))
        font = pygame.font.Font('freesansbold.ttf', 35)
        text4 = font.render('''HELP: space-key = shoot 🎯  up⬆️-down⬇️-key = move ship  escape📴 = exit''', True,(255,0,0),(0,255,255))
        screen.blit(text4,(0,0))
        pygame.display.update()
        sleep(5)
    

def delet_bullets(ship,bullets):
    for bullet in bullets.copy():
        if bullet.rect.left>=ship.screen_rect.right:
           bullets.remove(bullet)
                           
def update_screen(ai_settings,screen,ship,bullets,aliens,play_button,stats):
    screen.fill(ai_settings.bg_color) #set screen background colour
    
    font = pygame.font.Font('freesansbold.ttf', 35)
    font2 = pygame.font.Font('freesansbold.ttf', 55)
    text = font.render('Level:'+str(level), True,(255,0,0),(0,0,255))
    text2 = font.render('Score:'+str(score), True,(255,0,0),(0,0,255))
    text3 = font.render('Ship left:'+str(stats.ships_left), True,(255,0,0),(0,0,255))
    space=pygame.image.load("space.jpg").convert()
    screen.blit(space,(0,0))
    screen.blit(text,(0,0))
    screen.blit(text2,(550,0))
    screen.blit(text3,(1025,0))
    
        
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # Draw the play button if the game is inactive.
    if stats.game_active == False:
       screen.fill(ai_settings.bg_color) #set screen background colour
       play_button.draw_button()
       
    if stats.game_active=="over":
        screen.fill(ai_settings.bg_color) #set screen background colour
        text5 = font2.render('Game over !!! ', True,(255,0,0),(255,255,255))
        text6 = font.render('Press SPACE to continue.. Esc To EXIT.. ', True,(255,0,0),(0,255,255))
        screen.blit(text5,(250,265))
        screen.blit(text6,(200,365))



    pygame.display.flip() #update the screen actions

def get_aliens(ai_settings,alien_width):
    """determine space between ship and alien"""
    available_apace_x=ai_settings.s_width
    number_alien=int(available_apace_x/(1.5*alien_width))
    return number_alien

def get_number_aliens_y(ai_settings,alien_height):
    """Determine the number of aliens that fits """
    available_space_y=ai_settings.s_height-4*alien_height
    number_alien_y=int(available_space_y/(alien_height))
    return number_alien_y

def create_alien(ai_settings,screen,aliens,alien_number,number_al):
    """create an alien and place in on screen""" 
    alien=Alien(ai_settings,screen)
    alien_height=alien.rect.height
    alien.y=alien_height+alien_height*alien_number
    alien.rect.y=alien.y
    alien.rect.x=alien.rect.width+2*alien.rect.width*number_al
    aliens.add(alien)

def fleet(ai_settings,screen,aliens):
    """create a full fleet of aliens"""
    
    alien=Alien(ai_settings,screen)
    number_aliens_y =get_number_aliens_y(ai_settings,alien.rect.height)
    number_alien=get_aliens(ai_settings,alien.rect.width)
    for number_al in range(3,number_alien):
        for alien_number in range (number_aliens_y):
            create_alien(ai_settings,screen,aliens,alien_number,number_al)

def change_alien_direction(ai_settings,aliens):
    """"change direction"""
    for alien in aliens.sprites():
        alien.rect.x -= ai_settings.drop_speed
    ai_settings.direction *=-1

def check_alien_edge(ai_settings,aliens):
    """Respond appropriately if any alien reched an adge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_alien_direction(ai_settings,aliens)
            break

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """Respond to ship being hit by alien."""
    # Decrement ships_left.
    stats.ships_left -= 1

    if(stats.ships_left>0):
        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()
       
        # Create a new fleet and center the ship.
        fleet(ai_settings, screen, aliens)
        ship.center_ship()
       
        # Pause.
        sleep(0.5)
    else: 
        stats.game_active="over"
        #visible mouse cursor.
        global level,score
        level=1
        score=0
        pygame.mouse.set_visible(True)
            

def update_aliens(ai_settings,aliens,ship,stats,screen,bullets):
    """check if alien  is at an edge ,
        , then update the position of all aliens"""
    check_alien_edge(ai_settings,aliens)
    aliens.update()
    #look for alien ship collision.
    if pygame.sprite.spritecollideany(ship,aliens):
        #print("ship hit")
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    check_aliens_bottom(ai_settings,ship,screen,stats,bullets,aliens)

    
def update_fleet(ai_settings,screen,aliens,bullets):
    a=pygame.sprite.groupcollide(bullets,aliens,True,True)
    
    if a:
        global score
        score +=10
        
    

    
    if len(aliens)==0:
        #create new fleet of aliens and destroy existing bullets
        bullets.empty() 
        ai_settings.speedup()
        global level 
        level+= 1
        fleet(ai_settings,screen,aliens)   
    return a
def check_aliens_bottom(ai_settings,ship,screen,stats,bullets,aliens):
    """check if any alien touches biootm of ship """
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.left <= screen_rect.left:
            #same as if ship got hit
            ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
            break


