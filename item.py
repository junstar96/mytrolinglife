import sys
import os
from pico2d import *

num = None
def get():
    global num
    num = num + 1;



class Item:
    image1 = None
    image2 = None

    def __init__(self):
        self.x = 30
        self.y = 40
        self.wcount = 5
        self.bcount = 5
        if self.image1 == None:
            self.image1 = load_image("wateritem.png")
        if self.image2 == None:
            self.image2 = load_image("breaditem.png")

    def draw(self):
        if self.wcount >= 0:
            self.image1.draw(self.x, self.y, 40,60)
        if self.bcount >= 0:
            self.image2.draw(self.x + 40, self.y, 40,60)

    def eatwater(self):
        if self.wcount > 0:
            self.wcount = self.wcount - 1;
