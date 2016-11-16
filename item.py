import sys
import os
import random
from pico2d import *
import os


os.chdir('C:\\studyfolder\\mytrolinglife\\plise')




class Item:
    image1 = None
    image2 = None
    boardimage = None
    font = None

    def __init__(self):
        self.x = 30
        self.y = 30
        self.wcount = 5
        self.bcount = 5
        self.type = 0
        if Item.image1 == None:
            Item.image1 = load_image("wateritem.png")
        if Item.image2 == None:
            Item.image2 = load_image("breaditem.png")
        if Item.boardimage == None:
            Item.boardimage = load_image("board.png")
        if Item.font == None:
            Item.font = load_font("ENCR10B.TTF", 25)

    def draw(self):
        for i in range(0, 11):
            self.boardimage.draw(80*i, 30, 80, 60)
        if self.wcount >= 0:
            self.image1.draw(self.x, self.y, 60,60)
            self.font.draw(self.x - 5, self.y, "%d" % self.wcount)
        if self.bcount >= 0:
            self.image2.draw(self.x + 60, self.y, 60,60)
            self.font.draw(self.x + 60, self.y, "%d" % self.bcount)

    def gettype(self):
        self.type = random.randint(-4, 3)

    def dropdraw(self, a,b):
        point_x, point_y = a,b
        if self.type == 0:
            self.image1.draw(point_x, point_y, 30,20)
        elif self.type == 1:
            self.image2.draw(point_x, point_y, 30,30)


    def eatwater(self):
        if self.wcount > 0:
            self.wcount = self.wcount - 1;

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_1:
                self.wcount = self.wcount - 1
            elif event.key == SDLK_2:
                self.bcount = self.bcount - 1
