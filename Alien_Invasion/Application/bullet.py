import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """
     A class to create bullet sprite and contain bullet instances methods.
    """
    
    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.screen=screen
        
        #create a bullet rect 
        self.rect=pygame.Rect(0, 0, ai_settings.bullet_width, 
                              ai_settings.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top
        
        #store bullet y in decimal to later customize with speed
        self.y=float(self.rect.y)
        
        self.color=ai_settings.bullet_color
        self.speed=ai_settings.bullet_speed
        
    def update(self):
        """
        Move the bullet up the screen.
        """
        self.y-=self.speed
        self.rect.y=self.y
        
    def draw_bullet(self):
        # Draw the bullet.
        pygame.draw.rect(self.screen, self.color, self.rect)
        
    