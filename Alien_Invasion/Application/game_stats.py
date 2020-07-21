class GameStats():
    """
    Track statistics of game.
    """
    def __init__(self, ai_settings):
        self.ai_settings=ai_settings
        self.reset_stats()
        self.game_active=False
    
    def reset_stats(self):
        """
        all the statistics which will change at each new game.
        """
        self.ships_left=self.ai_settings.ship_limit
        self.score=0