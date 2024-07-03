class Gamestats():
    """Track statics of the game"""

    def __init__(self,ai_settings) -> None:
        """initialize statics"""
        self.ai_settings=ai_settings
        self.reset_stats()
        #start game in an active state
        self.game_active=False

    def reset_stats(self):     
        """intialize statics that can be change during the game"""
        self.ships_left=self.ai_settings.ship_limit

        self.score=0