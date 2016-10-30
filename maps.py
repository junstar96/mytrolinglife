import sys
import os
from pico2d import *
os.chdir('C:\\studyfolder\\mytrolinglife\\plise')

class Map:
    image1 = None
    image2 = None

    def __init__(self):
        self.x, self.y = 400,340
        if self.image1 == None:
            self.image1 = load_image("tileboard.png")
        if self.image2 == None:
            self.image2 = load_image("map.png")

    def draw(self):
        for i in range(0,21):
            for j in range(0, 16):
                self.image1.draw(i*40, j*40, 40,40)


def mapwall(a):
    ux,uy,dx,dy = a
    if ux < 0: return 1
    if uy < 60: return 2
    if dx > 800: return 3
    if dy > 600: return 4

