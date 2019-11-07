import pygame
from Settings import *
from Grid import *
from Jewel import *
from Fallers import *

#RUNS THE GAME

def run():
    """method that runs the whole game"""
    pygame.init() #initializes pygame

    # creates objects from Settings class
    settings = Settings()

    # creates screen
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

    # creates object from Grid class
    grid = Grid(screen, settings, settings.screen_height, settings.screen_width)

    # create object from Jewel class
    jewel = Jewel(screen, settings)

    # create object from Fallers class
    faller = Fallers(screen, settings)
    frozen_list = []
    color_list = []
    falling_list_no_use = []
    falling_list = []

    # establishes when the game is running
    running = True
    tick = pygame.USEREVENT + 1
    pygame.time.set_timer(tick, 300)

    # creates Clock object
    clock = pygame.time.Clock()

    #establishes whether object has moved left or right
    click_left = True
    click_right = True
    moved_left = False
    moved_right = False

    #continues running while game is going
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #if user x's out, game quits
                running = False

            if event.type == pygame.KEYUP: #if user presses a key
                if event.key == pygame.K_LEFT: #if user presses left key
                    if click_left == True:
                        for c in range(len(frozen_list)): #checks if there is a frozen jewel to left
                            if falling_list[0].x == frozen_list[c].x + 65:
                                a = c
                                if falling_list[0].y + (c%3)*65 >= frozen_list[a].y:
                                    faller.left = False
                                    moved_left = True
                            else:
                                faller.left = True
                        faller.moveLeft()
                        click_left = False
                    if event.key == tick:
                        click_left = False

                    if moved_left == True:
                        falling_list[0].x -= 65

                if event.key == pygame.K_RIGHT: #if user presses right key
                    if click_right == True:
                        for y in range(len(frozen_list)): #checks if there is a frozen jewel to right
                            print("hi")
                            if falling_list[0].x == frozen_list[y].x - 65:
                                z = y
                                if falling_list[0].y + (y%3)*65 >= frozen_list[z].y:
                                    faller.right = False
                                    moved_right = True
                            else:
                                faller.right = True
                        faller.moveRight()
                        click_right = False
                    if event.key == tick:
                        click_right = False

                    if moved_right == True:
                        falling_list[0].x += 65
                if event.key == pygame.K_SPACE: #if user presses spacebar, rotates jewels colors
                    faller.rotateJewels()
                if event.key == pygame.K_q: #if user presses Q key, game quits
                    running = False

            if event.type == tick:

                faller.update() #calls update function in fallers

                screen.fill(settings.background_color) #fills screen with black
                grid.draw_grid() #draws gird lines

                for x in faller.falling_list_run:
                    falling_list_no_use.append(x)

                falling_list = falling_list_no_use[-3:] #takes last 3 values from falling_list_no_use

                for rect in falling_list:
                    if rect.collidelist(frozen_list) != -1: #if jewel collides with frozen jewel, collision becomes true
                        faller.collision = True

                if faller.update() == "Done": #if falling jewel hits bottom of screen
                    # puts frozen blocks into list

                    for x in faller.frozen_list_run[:3]:  #jewels at bottom get added to frozen_list
                        frozen_list.append(x)
                    for y in faller.color_list: #color of jewels at bottom get added to list of colors
                        color_list.append(y)

                    faller = Fallers(screen, settings) #calls another faller object

                # fills screen and redraws grid everytime
                for x in range(len(frozen_list)):
                    if frozen_list[x].y < 30:
                        running = False

                # for y in range(len(frozen_list)):
                # if falling_list[0].y + 65 == frozen_list[y].y:

                try:
                    for z in range(len(frozen_list)):
                        pygame.draw.rect(screen, color_list[z], frozen_list[z])
                except IndexError:
                    pass

                click_left = True
                click_right = True
                # shows everything onto the surface
                pygame.display.flip()



    pygame.quit()


if __name__ == '__main__':
    run()
