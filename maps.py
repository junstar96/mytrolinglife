import sys
import os
from pico2d import *

class Map:
    image1 = None
    image2 = None

    def __init__(self):
        self.x, self.y = 400,340
        if self.image1 == None:
            self.image1 = load_image("map.png")
        if self.image2 == None:
            self.image2 = load_image("map.png")

    def draw(self):
        self.image1.draw(self.x, self.y, 800, 540)


def mapwall(a):
    ux,uy,dx,dy = a
    if ux < 0: return 1
    if uy < 60: return 2
    if dx > 800: return 3
    if dy > 600: return 4

