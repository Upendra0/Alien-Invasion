import pygame.font

from pygame.sprite import Group

from ship import Ship

class Scoreboard():
    """
    A class to display score, no. of ship user has left during game time.
    """
    
    def __init__(self, ai_settings, screen, stats):
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.ai_settings=ai_settings
        self.stats=stats
        
        #Font creation and it's settings
        self.text_color=(30,30,30)
        self.font=pygame.font.SysFont(None, 48)
        
        #Prepare the score
        self.prep_score()
        
        #Prepare the ships
        self.prep_ships()
        
    def prep_ships(self):
        """
        Show how many ship a player has left.
        """
        
        self.ships=Group()
        for ship_number in range(self.stats.ships_left):
            ship=Ship(self.ai_settings, self.screen)
            ship.rect.x=10+ship_number*ship.rect.width
            ship.rect.y=10
            self.ships.add(ship)
        
    def prep_score(self):
        """
        Turn the score into image to later render it.
        """
        rounded_score= round(self.stats.score, -1)
        score_str="{:,}".format(rounded_score)
        self.score_image=self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
        
        #display the score at top right of screen
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right-20
        self.score_rect.top=20
        
    def show_score(self):
        """
        Draw the score to screen.
        """
        
        self.screen.blit(self.score_image, self.score_rect)
        
        #Draw the ship
        self.ships.draw(self.screen)