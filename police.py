import sys
import os
import random
from pico2d import *
os.chdir('C:\\studyfolder\\mytrolinglife\\plise')
npc = None

class nonplayerable:
    protectableimage = None
    atteckableimage = None

    typeA, typeB = 0, 1

    left, right, leftstop, rightstop = 100,101, 500, 501

    pixel_speed = (10.0/3)
    runspeed = 50.0
    mpm = (runspeed * 1000.0/60.0)
    mps = (mpm / 60.0)
    pps = (pixel_speed * mps)




    def __init__(self):
        self.x, self.y = random.randint(0, 800), random.randint(80, 560)
        self.type = random.randrange(nonplayerable.typeA, nonplayerable.typeB)
        self.life = random.randint(100, 150)
        self.movetime = 0
        self.stoptime = 0
        self.xframe = 0
        self.yfream = 0
        self.movestate = random.randrange(self.left, self.right+1)
        self.emergy = False
        if nonplayerable.protectableimage == None:
            nonplayerable.protectableimage = load_image("makeimage2.png")
        if nonplayerable.atteckableimage == None:
            nonplayerable.atteckableimage = load_image("makeimage2.png")


    def draw(self):
        if self.life > 0:
            if self.type == nonplayerable.typeA:
                self.protectableimage.clip_draw(self.xframe * 35, 455 - (self.yfream + 1) * 45, 35, 45, self.x, self.y,30,40)
            elif self.type == nonplayerable.typeB:
                self.atteckableimage.clip_draw(self.xframe * 35, 455 - (self.yfream + 1) * 45, 35, 45, self.x, self.y,30,40)


    def crashrange(self):
        return self.x - 50, self.y - 50, self.x+50, self.y+50

    def checktime(self):
        if self.movetime < 0:
            self.movetime = 0
            self.stoptime = random.randint(40, 600)
            if self.movestate == self.left:
                self.movestate = self.leftstop
            elif self.movestate == self.right:
                self.movestate = self.rightstop
        elif self.stoptime < 0:
            self.stoptime = 0
            self.movetime = random.randint(30, 400)
            if self.movestate == self.leftstop:
                self.movestate = self.right
            elif self.movestate == self.rightstop:
                self.movestate = self.left
        else:
            pass


    def moveupdate(self, frametime):
        distence = nonplayerable.pps * frametime
        if self.movestate == self.left:
            self.xframe = (self.xframe + 1) % 4
            self.movetime = self.movetime - 1
            self.x = self.x - (distence)
        elif self.movestate == self.right:
            self.xframe = (self.xframe + 1) % 4
            self.movetime = self.movetime - 1
            self.x =  self.x + (distence)
        else:
            self.xframe = 0
            self.stoptime = self.stoptime - 1

    def puttime(self):
        return self.movestate












