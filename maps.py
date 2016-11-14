import sys
import os


from police import nonplayerable


from pico2d import *
os.chdir('C:\\studyfolder\\mytrolinglife\\plise')

class Map:
    image1 = None
    image2 = None

    def __init__(self):
        self.x, self.y = 400,340
        self.npc = [nonplayerable() for i in range(0, 9)]
        if Map.image1 == None:
            Map.image1 = load_image("tileboard.png")
        if Map.image2 == None:
            Map.image2 = load_image("map.png")

    def draw(self):
        for i in range(0,21):
            for j in range(0, 16):
                self.image1.draw(i*40, j*40, 40,40)
        for monster in self.npc:
            monster.draw()


    def update(self, frametime):
        for monster in self.npc:
            monster.moveupdate(frametime)
            monster.checktime()


    def playercheck(self, a):
        for monster in self.npc:
            monster.escape(a)



def mapwall(a):
    dx, dy, ux, uy = a
    if dx < -20: return 1
    if dy < 40: return 2
    if ux > 820: return 3
    if uy > 620: return 4


