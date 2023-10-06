
import pygame as pg
import sys
import random

from World import World
import Values

class Game:

    def __init__(self,screen,clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()

        self.world = World(Values.worldLength, Values.worldLength, self.width, self.height)

    def run(self):
        self.gameActive = True
        while self.gameActive:
            self.clock.tick(60)
            self.events()
            self.update()
            # self.draw()
            self.GenerateWorld()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()

    def update(self):
        # pg.display.update()
        pass

    def draw(self):
        # Want to draw the grid for the world
        self.screen.fill((0,0,0))

        for x in range(self.world.gridLengthX):
            for y in range(self.world.gridLengthY):
                # draw cartesian grid on screen
                square = self.world.world[x][y]["cartesianRect"]
                rect = pg.Rect(square[0][0], square[0][1], Values.tileSizeTop, Values.tileSizeTop)
                # pg.draw.rect(self.screen, (0,0, 255), rect, 1)

                # import worldtile into game
                renderPos = self.world.world[x][y]["renderPos"]
                # self.screen.blit(self.world.tiles["worldTile"], ((renderPos[0] + self.width/2) * 0.93, (renderPos[1] + self.height/4) * 1.075 ))

                # draw iso grid on screen
                p = self.world.world[x][y]["isoPoly"]
                p = [(x + self.width/2, y + self.height/4) for x,y in p]
                # pg.draw.polygon(self.screen, (255,0,0), p, 1)

        pg.display.flip()

    def GenerateWorld(game):
        # Create a list to store the positions of the tiles
        tilePositions = []

        for x in range(game.world.gridLengthX):
            for y in range(game.world.gridLengthY):
                renderPos = game.world.world[x][y]["renderPos"]

                # 65% chance of adding the tile position to the list
                if random.random() < 0.65:
                    tilePositions.append(((renderPos[0] + game.width / 2) * 0.93, (renderPos[1] + game.height / 4) * 1.075))

        return tilePositions
