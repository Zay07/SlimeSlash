import pygame as pg

import Values

class World():
    
    def __init__(self, gridLengthX, gridLengthY, screenWidth, screenHeight):
        self.gridLengthX = gridLengthX
        self.gridLengthY = gridLengthY
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.world = self.CreateWorld()
        self.tiles = self.LoadImages()

    def LoadImages(self):
        worldTile = pg.image.load("WorldTile/WorldTile.png")
        worldTile = pg.transform.rotozoom(worldTile, 0, 0.1835)
        return {"worldTile" : worldTile}

    def CreateWorld(self):
        # This will make the whole grid for our world
        world = []

        for gridX in range(self.gridLengthX):
            world.append([])
            for gridY in range(self.gridLengthY):
                worldTile = self.GridToWorld(gridX, gridY)
                world[gridX].append(worldTile)
        return world

    def GridToWorld(self, gridX, gridY):
        # This will convert the world to isometric
        rect = [   # all 4 corners of square
            (gridX * Values.tileSizeTop, gridY * Values.tileSizeTop),
            (gridX * Values.tileSizeTop + Values.tileSizeTop , gridY * Values.tileSizeTop),
            (gridX * Values.tileSizeTop + Values.tileSizeTop, gridY * Values.tileSizeTop + Values.tileSizeTop),
            (gridX * Values.tileSizeTop, gridY * Values.tileSizeTop + Values.tileSizeTop)
        ]

        # convert sqaure to isometric coords
        isoPoly = [self.CartToIso(x,y) for x, y in rect]

        minX = min([x for x, y in isoPoly])
        minY = min([y for x, y in isoPoly])

        out = {
            "grid" : [gridX, gridY],
            "cartesianRect" : rect,
            "isoPoly" : isoPoly,
            "renderPos" : [minX, minY]
        }

        return out

    def CartToIso(self,x,y):
        # Convert from cartesian to isometric by formula
        isoX = x-y
        isoY = (x+y)/2
        return isoX, isoY





