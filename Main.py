# I would like to thank Arachnid56 as his tutorial has helped me alot.

import pygame as pg
import sys
import random

from Game import Game

screenWidth = 1280
screenHeight = 720
worldDrawn = False

def GenerateWorld2(game):
    # Create a list to store the positions of the tiles
    tilePositions = []

    for x in range(game.world.gridLengthX):
        for y in range(game.world.gridLengthY):
            renderPos = game.world.world[x][y]["renderPos"]

            # 65% chance of adding the tile position to the list
            if random.random() < 0.65:
                tilePositions.append(((renderPos[0] + game.width / 2) * 0.91, (renderPos[1] + game.height / 4) * 1.075))

    return tilePositions

def main():
    global worldDrawn
    running = True
    gameActive = True

    pg.init()
    screen = pg.display.set_mode((screenWidth, screenHeight))
    clock = pg.time.Clock()
    # implement menus

    # implement game
    game = Game(screen,clock)
    tilePositions = GenerateWorld2(game)

    while running:
        # start menu here

        # create world
        for pos in tilePositions:
            game.screen.blit(game.world.tiles["worldTile"], pos)
        pg.display.update()

        while gameActive:
            # game loop here

            game.run()
    
            pg.display.update()

if __name__ == "__main__":
    main()








