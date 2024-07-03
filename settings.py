class Settings():
    """A class to store all settings for game (Alien Invasion)"""

    def __init__(self):
        self.s_width=1200
        self.s_height=600
        self.bg_color = (230, 230, 230)

        #ship settngs
        
        self.ship_limit=3

        #bullet settings
        
        self.bullet_width=25
        self.bullet_height=10
        self.bullet_color=(245,16,92)

        #Alien settings
        
        self.drop_speed=20
        

        #level up
        self.speed_up=1.5

        self.speed_settings()

    def speed_settings(self):

        #speed settings
        self.ship_speed=8
        self.bullet_speed=15
        self.alien_speed=2

        #fleet direction
        self.direction=1

    def speedup(self):
        """increasing speed"""
        self.ship_speed *= self.speed_up
        self.bullet_speed *= self.speed_up
        self.drop_speed += 10
        self.alien_speed += 1
    





 