from dataclasses import dataclass
import pygame as pg
import noise
#angle between extremes of vision
viewport_angle = 90

@dataclass
class Block:
    typeid: str
    x: int
    y: int
    color: tuple
    
class Player:
    def __init__(self, x , y):
        #2d --- 2 coords
        self.x = x
        self.y = y
        #2d --- 2 look axies
        self.xlook = 0
        self.ylook = 0
        self.look_angle = 0
        
        #returns color value for checked spot. Pix goes from 0 (top) to N (bottom)
    def raycast(self, pix):
        relative_angle = (pix/height - 0.5) * max #bottom is 1, top is 0
        absolute_angle = self.look_angle + relative_angle
        
        
class Game:
    def __init__(self, width, height):
        pg.init()
        self.width = width
        self.height = height
        self.terrain = []
        self.screen = pg.display.set_mode(width, height)

    def run(self):
        for event in pg.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                return
        self.render()
    #send rays for each pixel in the stip
    def render(self):
        #look around
        pg.display.flip()
    

        