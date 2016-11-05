import sys
import os
from pico2d import *
import os
os.chdir('C:\\studyfolder\\mytrolinglife\\plise')


num = None
def get():
    global num
    num = num + 1;



class Item:
    image1 = None
    image2 = None
    boardimage = None

    def __init__(self):
        self.x = 30
        self.y = 40
        self.wcount = 5
        self.bcount = 5
        if Item.image1 == None:
            Item.image1 = load_image("wateritem.png")
        if Item.image2 == None:
            Item.image2 = load_image("breaditem.png")
        if Item.boardimage == None:
            Item.boardimage = load_image("board.png")

    def draw(self):
        if self.wcount >= 0:
            self.image1.draw(self.x, self.y, 60,40)
        if self.bcount >= 0:
            self.image2.draw(self.x + 60, self.y, 60,60)
        for i in range(0, 10):
            self.boardimage.draw(40*i, 40, 40, 40)

    def eatwater(self):
        if self.wcount > 0:
            self.wcount = self.wcount - 1;

    def handle_event(self, event):
        pass
