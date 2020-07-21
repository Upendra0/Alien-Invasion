import pygame

from pygame.sprite import Sprite

class Ship(Sprite):
    """
    This class creates a ship instance, draw it to screen and move it as user
    keypress events during game.
    """
    
    def __init__(self,ai_settings,screen):
        super().__init__()
        
        #initialize the ship and set its starting position.
        self.screen=screen
        self.ai_settings=ai_settings
        
        #load the ship image and get its rect
        self.image=pygame.image.load("E:\Alien_Invasion\Application\Images\ship.bmp.bmp")
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        
        #start each ship at bottom center of screen
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        
        #store center variable for movement of ship
        self.center=float(self.rect.centerx)
        
        #movement flags
        self.moving_right=False
        self.moving_left=False
        
    def update(self):
        #update the ship's position
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.center+=self.ai_settings.ship_speed
            
        if self.moving_left and self.rect.left>0:
            self.center-=self.ai_settings.ship_speed
            
        #change ship centerx
        self.rect.centerx=self.center
        
    def blitme(self):
        #render the ship image on screen
        self.screen.blit(self.image,self.rect)
        
    def center_ship(self):
        self.center=self.screen_rect.centerx