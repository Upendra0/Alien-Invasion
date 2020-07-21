class Settings():
    """
    A class to store all settings of my game.
    """
    
    def __init__(self):
        #screen settings
        self.screen_width=800
        self.screen_height=800
        self.caption='Alien Invasion'
        self.bg_color=(230,230,230)
        

        #bullet settings
        self.bullet_width=5
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        self.bullets_allowed=6
        
        #alien settings
        self.alien_speed=0.0003
        
        #1 means right,-1 means left directions
        self.move_h=1
        self.move_v=1
        
        #stats_settings
        self.ship_limit=3
        
        self.ship_speed=0.8
        
        #Game speedup's settings
        self.speedup_scale=1.05
        self.score_speed=2
    
        
        self.init_dynamic_settings()
        
    def init_dynamic_settings(self):
        """
        initialize the settings that will change as game progresses.
        """

        self.bullet_speed=3
        self.alien_drop_speed=0.1
        self.alien_point=1
        
    def increase_speed(self):
        """
        increase the dyanmic  settings each time by speedup_scale factor.
        """
        
        self.bullet_speed*=self.speedup_scale
        self.alien_drop_speed*=self.speedup_scale
        self.alien_point+=self.score_speed
        
        
        
        
        
        
        
        
        