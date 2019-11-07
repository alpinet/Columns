import random
class Settings:
    def __init__(self):
        """Class that has all the settings needed to run the game"""
        #Screen settings
        self.screen_width = 390
        self.screen_height = 780
        self.background_color = (0,0,0) #background color is black

        #Grid settings
        self.grid_column = self.screen_width/6
        self.grid_row = self.screen_height/12

        self.random_column = self.grid_column

        #colors
        self.colors = [(255,128,128),(255,42,0),(255,140,25),(255,255,0),(43,255,0),(0,255,255),(51,119,255),(128,0,255),(255,0,255),(13,0,77)]
        #list of possible colors ^
        self.x = random.randint(0,9)
        self.random_color = self.colors[self.x]
