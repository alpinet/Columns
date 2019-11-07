from Settings import *
from Jewel import *
from Grid import *
import random
import math
class Fallers:
    """Class that creates a faller object - 3 jewels stacked onto each other"""
    def __init__(self,screen, settings):
        """Constructor for fallers class"""
        super(Fallers,self).__init__()
        self.screen = screen
        self.settings = settings
        self.jewel = Jewel(self.screen,self.settings) #creates a jewel object from jewel class
        self.falling_list = [] #list of jewels that are currently falling
        self.falling_list_run = [] #list of jewels from falling_list that Run calls on
        self.frozen_list = [] #list of frozen jewels
        self.frozen_list_run = [] #list of frozen jewels that Run calls on
        self.random_color1 = (settings.colors[random.randint(0,9)])
        self.random_color2 = (settings.colors[random.randint(0,9)])
        self.random_color3 = (settings.colors[random.randint(0,9)])
        self.color_list = [self.random_color1,self.random_color2,self.random_color3]
        self.frozen_color_list = [] #list of colors that corresponds to each item in frozen_list
        self.frozen = False
        self.grid = Grid(self.screen,self.settings,390,780) #creates grid object from Grid class
        self.collision = False
        self.left = True
        self.right = True
        self.column = settings.random_column *random.randint(0,5) #picks random column for jewels to fall from


    def make_falling_List(self):
        """creates a falling_list that consists of 3 jewels on top of each other"""
        for x in range(1,4):
            self.ajewel = self.jewel.make_jewel(self.column, self.jewel.row-x*self.settings.grid_row, self.jewel.width, self.jewel.height)
            self.falling_list.append(self.ajewel)


    def make_permanent_jewel_List(self):
        """once jewels stop moving, adds jewels to a frozen list"""
        for x in self.falling_list:
            self.frozen_list.append(x)
        return self.frozen_list

    def make_permanent_color_List(self):
        """once jewels stop moving, adds color of each jewel to a list of colors"""
        for x in self.color_list:
            self.frozen_color_list.append(x)
        return self.frozen_color_list

    def drawPermanentList(self):
        """draws all the items in the frozen list - called each time so they stay on screen"""
        for x in range(len(self.make_permanent_jewel_List())):
            pygame.draw.rect(self.screen,self.make_permanent_color_List()[x],
                             self.make_permanent_jewel_List()[x])

    def moveRight(self):
        """if user hits right key, moves fallers right by a column"""
        if self.right:
            if self.column<self.settings.screen_width - self.settings.grid_column:
                self.column += (self.settings.grid_column)

    def moveLeft(self):
        """if user hits left key, moves fallers left by a column"""
        if self.left:
            if self.column>0:
                self.column -= self.settings.grid_row


    def rotateJewels(self):
        """rotates jewels colors"""
        if self.frozen == False:
            self.color_list = [self.color_list[-1]] + self.color_list [:-1]


    def update(self):
        """updates the drawings on the surface each time clock ticks"""
        self.make_falling_List() #creates list of 3 jewels that are falling
        if self.falling_list[0].bottom < self.settings.screen_height: #if hasn't hit bottom
            self.frozen = False #they aren't frozen
            for x in range(0, 3): #draws the 3 jewels onto the screen
                pygame.draw.rect(self.screen, self.color_list[x], self.falling_list[x])

            if self.falling_list[0].bottom <= self.settings.screen_height - 5:
                self.falling_list_run.append(self.falling_list[0]) #adds jewel 1
                self.falling_list_run.append(self.falling_list[1]) #adds jewel 2
                self.falling_list_run.append(self.falling_list[2]) #adds jewel 3

            self.falling_list[0].y += 0
            self.falling_list[1].y += 0
            self.falling_list[2].y += 0

            if self.collision == True: #if collides with another jewels
                for x in range(len(self.falling_list)):
                    self.falling_list[x].y -= 65 #moves falling jewels back to spot before hit
            if self.collision == False: #if doesn't hit anything
                self.jewel.row += 65/2 #moves jewels down a row
                self.falling_list.clear() #clears falling list each time

            else:
                self.make_permanent_jewel_List() #if hits something or reaches bottom, adds jewels to permanent list
                self.frozen = True #jewels become frozen


        else:
            self.frozen=True

        if self.frozen == True: #if jewels are frozen
            try:
                if self.collision == False:
                    self.drawPermanentList() #draws the permanent list
                self.frozen_list_run.append(self.frozen_list[-3]) #adds permanent jewels to frozen list
                self.frozen_list_run.append(self.frozen_list[-2])
                self.frozen_list_run.append(self.frozen_list[-1])
                self.falling_list.clear()
            except:
                pass
            return "Done"
