import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """
    A class to represent a single alien in the fleet.
    """
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen=screen
        self.ai_settings=ai_settings
        
        #Load the ship image
        self.image=pygame.image.load("E:\Alien_Invasion\Application\Images\main.bmp")
        self.rect=self.image.get_rect()
        
        #placing it at top left corner
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        
        #store the alien's exact position
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)
        
    def blitme(self):
        """
        Draw the alien at it's current location.
        """
        
        self.screen.blit(self.image, self.rect)
        
    def check_edges(self):
        #Return True if alien is at edge
        screen_rect=self.screen.get_rect()
        if self.rect.x>=screen_rect.right:
            return True
        elif self.rect.x<=0:
            return True
        else:
            return False
    
    def update(self):
        
        #Move the alien down
        self.y+=self.ai_settings.alien_drop_speed*self.ai_settings.move_v
        self.rect.y=self.y
        
        #Move them left and right also
        self.x+=self.ai_settings.alien_speed*self.ai_settings.move_h