import pygame
import random
class Jewel:
    """Class that creates a Jewel object"""
    def __init__(self,screen, settings):
        """Constructor of Jewel class"""
        super(Jewel,self).__init__()
        self.screen = screen
        self.settings = settings #creates settings object from settings class
        self.width = settings.grid_column
        self.height = settings.grid_row
        self.col = settings.random_column
        self.row = 65/2
        self.jewel_list = [] #list of jewels

    def make_jewel(self,column,row,width,height):
        """returns a Jewel rectangle"""
        self.jewel = pygame.Rect(column,row,width,height)
        return self.jewel

    def add_to_jewel_list(self):
        """adds jewel to the jewel_list"""
        self.jewel_list.append(self.jewel)

    def update(self):
        self.add_to_jewel_list()
        for x in self.jewel_list:
            pygame.draw.rect(self.screen,(231,212,121),x)
        print(self.jewel_list)
        self.jewel_list.clear()
        print(self.jewel_list)
