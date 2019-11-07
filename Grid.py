import pygame
class Grid:
    """Establishes the grid of the game"""
    def __init__(self,screen,settings,height,width):
        """Constructor for Grid class"""
        self.screen = screen
        self.settings = settings
        self.height = height
        self.width = width


    def draw_grid(self):
        """Draws the grid onto the screen surface"""
        for x in range(0,7): #6 columns
            for y in range(0,13): #12 rows
                rect = pygame.Rect(x * self.settings.grid_column,
                                   y * self.settings.grid_row,
                                   self.settings.grid_column,
                                   self.settings.grid_row)
                pygame.draw.rect(self.screen, (252,252,252),rect,1) #draws each line onto screen

