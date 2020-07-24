import pygame
from pygame.sprite import Group

from settings import Settings

import game_functions as gf

from ship import Ship

from game_stats import GameStats

from button import Button
 
from scoreboard import Scoreboard

def run_game():
    """
    This is main function to run game.
    """
    
    
    pygame.init()
    
    #intialise pygame setting instance
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.caption)
    bg_color=ai_settings.bg_color
    screen.fill(bg_color)
    
    #make a ship object
    ship=Ship(ai_settings,screen)
    
    #make a bullets group to store various bullet sprites
    bullets=Group()
    
    #make an aliens sprites to store various alien sprites
    aliens=Group()
    
    gf.create_fleet(ai_settings,screen,aliens,ship)
    
    #create a stat instance
    stats=GameStats(ai_settings)
    
    #created various buttons for menu.
    play_button=Button(ai_settings, screen, 'PLAY', 200, 100, 250, 60)
    info_button=Button(ai_settings, screen, 'About', 200, 200, 250, 60)
    best_score_button=Button(ai_settings, screen, 'Best Score',200,300,250,60)
    exit_button=Button(ai_settings, screen, 'Exit', 200, 400, 250, 60)
    back_button=Button(ai_settings, screen,'BACK', 100, 50,150,50)
    
    #Too many buttons, so used mapping technique
    button=[play_button,info_button,best_score_button,exit_button,back_button]
    
    #Make a scoreboard instance
    sb=Scoreboard(ai_settings, screen, stats)
    
    #added the background music to game
    pygame.mixer.music.load("E:\Alien_Invasion\Application\Music\ms.mp3")
    pygame.mixer.music.play(-1)

    
    #main loop of game
    while True:
        
        #Watch for events
        gf.check_events(ai_settings,screen,ship,bullets,stats,button,aliens,sb) 
        
        if stats.game_active:
            ship.update()
        
            gf.update_bullets(aliens,bullets,ai_settings,screen,ship, stats,sb)
        
            gf.update_aliens(ai_settings,aliens,ship,screen,stats, bullets, sb)
        
        #redraw the screen at each loop
        gf.update_screen(ai_settings,screen,ship,bullets,aliens,stats,button,sb)
 
        
run_game()
        