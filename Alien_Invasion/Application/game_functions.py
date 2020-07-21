import sys

import pygame

from bullet import Bullet

from alien import Alien

from time import sleep

import score

def get_number_aliensx(ai_settings,alien_width):
    """
    Return the number of aliens that can fit to the screen width at a time.
    """
    available_spacex=ai_settings.screen_width-2*alien_width
    number_aliensx=int(available_spacex/(2*alien_width))
    return number_aliensx


def create_alien(ai_settings, screen, aliens, alien_number):
    """
    create an alien, add it to group aliens and update dimensions.
    """

    alien=Alien(ai_settings, screen)
    alien_width=alien.rect.width
    alien.x=alien_width+2*alien_width*alien_number
    alien.rect.x=alien.x
    alien.rect.y=alien.rect.height
    aliens.add(alien)
    
    
def create_fleet(ai_settings, screen, aliens, ship):
    """
    create a group of alien sprites.
    """
    alien=Alien(ai_settings, screen)
    number_aliensx=get_number_aliensx(ai_settings, alien.rect.width)
    
    #create a row of aliens
    for alien_number in range(number_aliensx):
        create_alien(ai_settings, screen, aliens, alien_number)
        
        
        
def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """
    Watch for various keydown events.
    """
    
    if event.key==pygame.K_RIGHT:
        ship.moving_right=True
    elif event.key==pygame.K_LEFT:
        ship.moving_left=True
    elif event.key==pygame.K_SPACE:
        if len(bullets)<ai_settings.bullets_allowed:
            new_bullet=Bullet(ai_settings,screen,ship)
            bullets.add(new_bullet)
    elif event.key==pygame.K_q:
        sys.exit()
        
        
        
def check_keyup_events(event,ship):
    """
    Watch for various key up events.
    """
    if event.key==pygame.K_RIGHT:
        ship.moving_right=False
    elif event.key==pygame.K_LEFT:
        ship.moving_left=False

    
    

def check_events(ai_settings,screen,ship,bullets, stats, button,aliens, sb):
    """
    Respond various user's events during game.
    """
    
    for event in  pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
            
        elif event.type==pygame.KEYUP:
            check_keyup_events(event, ship)
        
        elif event.type== pygame.MOUSEBUTTONDOWN:
            
            mouse_x, mouse_y=pygame.mouse.get_pos()
            
            if button[0].rect.collidepoint(mouse_x, mouse_y):
                check_play_button(ai_settings, ship, aliens, bullets, screen,
                                  stats, button[0],sb)
                
            elif button[1].rect.collidepoint(mouse_x, mouse_y):
                check_about_button(screen, button[4], button[1])
                
            elif button[2].rect.collidepoint(mouse_x, mouse_y):
                check_best_score_button(screen, button[4], button[2])
                
            elif button[3].rect.collidepoint(mouse_x, mouse_y):
                sys.exit(0)
                
   
                
def check_play_button(ai_settings, ship, aliens, bullets, screen, stats,
                      play_button,sb):
    
    """
    Run when user press play_button.
    
    Empty the aliens and bullets group.
    intialize init dynamic setting.
    """

    stats.reset_stats()
    stats.game_active=True
    
        
    #empty the list of aliens and bulets
    aliens.empty()
    bullets.empty()
        
    #initialize dynamic settings
    ai_settings.init_dynamic_settings()
        
    #display no. of ships
    sb.prep_ships()
        
    #create new fleet and center the ship
    create_fleet(ai_settings, screen, aliens, ship)
    ship.center_ship()
   

     
        
def check_about_button(screen, back_button, about_button):
    """
    Run when user press about button.
    
    Show the game info by drawing an image.
    Created a back button.
    Remain in the same screen configuration till user press back button.
    """
    
    check_image=pygame.image.load("E:\Alien_Invasion\Application\Images\ma.png")
    check_image_rect=check_image.get_rect()
    screen_rect=screen.get_rect()
    check_image_rect.center=screen_rect.center
    back_flag=True
    while(back_flag):
        screen.fill((230,230,230))
        back_button.draw_button()
        screen.blit(check_image, check_image_rect)
        pygame.display.flip()
        for event2 in pygame.event.get():
            if event2.type==pygame.MOUSEBUTTONDOWN:
                mx,my=pygame.mouse.get_pos()
                if back_button.rect.collidepoint(mx,my):
                    back_flag=False
 
    
 
def check_best_score_button(screen, back_button, about_button):
    """
    Run when user press best score button.
    
    Show user's thair best score and return to original menu when user press 
    back button.
    """
    
    back_flag=True
    with open("E:\Alien_Invasion\Application\\best_score.txt",'r') as fp:
        msg=fp.read()
    text_color=(0,0,230)
    buttom_color=(230,230,230)
    font=pygame.font.SysFont(None, 48)
    text_image=font.render(msg, True, text_color, buttom_color)
    text_rect=text_image.get_rect()
    screen_rect=screen.get_rect()
    text_rect.center=screen_rect.center
    while back_flag:
        screen.fill((230,230,230))
        back_button.draw_button()
        screen.blit(text_image, text_rect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                mx,my=pygame.mouse.get_pos()
                if back_button.rect.collidepoint(mx,my):
                    back_flag=False



            
def update_bullets(aliens,bullets,ai_settings,screen,ship, stats, sb):
    #update bullets position
    bullets.update()
    
    #delete old bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)
            
    #delete collided bullets and ships
    collision=pygame.sprite.groupcollide(bullets,aliens,True,True)
    
    #score for each aliens shoot
    if collision:
        stats.score+=ai_settings.alien_point
        sb.prep_score()
    #repopulate fleets
    if(len(aliens)==0):
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, aliens, ship)




def update_screen(ai_settings,screen,ship,bullets,aliens,stats, button,sb):
    """
    Updates the images on the screen and flip to new screen
    """
    
    screen.fill(ai_settings.bg_color)
        
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        
    ship.blitme()
    aliens.draw(screen)

    #Draw the menu button when game is not active
    if not stats.game_active:
        for i in range(4):
            button[i].draw_button()
            
    #off mouse cursor when game become active
    if stats.game_active:
        pygame.mouse.set_visible(False)
    else:
        pygame.mouse.set_visible(True)
        
    sb.show_score()
        
    pygame.display.flip()
    
    
    
    
def ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb):
    """
    Run when ship is hitted.
    
    Played the blast sound.
    Reduce the no. of ship user has left by 1.
    """
    
    crash_sound=pygame.mixer.Sound("E:\Alien_Invasion\Application\Music\crsh.wav")
    pygame.mixer.Sound.play(crash_sound)
    
    blast(ship, screen)
    if stats.ships_left>1:
        stats.ships_left-=1
        #Update the no. of ships
        sb.prep_ships()
        
        aliens.empty()
        bullets.empty()
    
        #create a new fleet
        create_fleet(ai_settings, screen, aliens, ship)
        ship.center_ship()
    
        #pause for a moment
        sleep(1)
    else:
        score.update(str(sb.stats.score))
        stats.game_active=False
        
        
        
    
def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets,sb):
    #check if any ship hit the bottom of screen.If yes end the current game.
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom>= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb)
            break
        
        
    
def update_aliens(ai_settings,aliens, ship,screen, stats, bullets, sb):
    #Update the aliens rect.
    for alien in aliens.sprites():
        alien.update()
    
    #check for collisons
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb)
        
    #check for a ship enter into bottom
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets, sb)
    
 
    
def blast(ship, screen):
    #Draw the blast image after ship get hit
    
    blast=pygame.image.load("E:\Alien_Invasion\Application\Images\m.bmp")
    blast_rect=blast.get_rect()
    screen_rect=screen.get_rect()
    blast_rect.centerx=screen_rect.centerx
    blast_rect.bottom=screen_rect.bottom
    screen.blit(blast, blast_rect)
    pygame.display.flip()