from pico2d import *

map = None
mapnum = None

class Map:
    image = None

    def __init__(self):
        self.x, self.y = 0,0
        image = load_image("큐링온라인.png")

    def get_bb(self):
        return self.x, self.y, self.x + 800, self.y + 600

    def draw(self):
        self.image.draw(self.x, self.y)


def mapdef():
    global map
    global mapnum
    map = [Map for i in range(9)]
    mapnum = 0

def crash(a,b):
    p1,p2,p3,p4 = a.get_bb()
    map1,map2,map3,map4 = b.get_bb()

    if p1 >= map1: return 1
    if p2 >= map2: return 2
    if p3 <= map3: return 3
    if p4 <= map4: return 4

    return 0

def mapwall(a):
    global map
    global mapnum
    if a == 1 and mapnum > 0:
        mapnum = mapnum - 1
        return 1
    if a == 2 and mapnum/3 > 0:
        mapnum = mapnum - 3
        return 2
    if a == 3 and mapnum < 8:
        mapnum = mapnum + 1
        return 3
    if a == 4 and mapnum/3 < 2:
        mapnum = mapnum + 3
        return 4
    return 0




