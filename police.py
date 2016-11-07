import sys
import os
import random
import math
from pico2d import *
os.chdir('C:\\studyfolder\\mytrolinglife\\plise')
npc = None

class nonplayerable:
    protectableimage = None
    atteckableimage = None
    checkmove = None

    typeA, typeB = 0, 1

    left, right, leftstop, rightstop = 100,101, 500, 501
    up, down, stop = 10, 11, 12

    pixel_speed = (10.0/3)
    runspeed = 8.0
    mpm = (runspeed * 1000.0/60.0)
    pps = (pixel_speed * mpm)




    def __init__(self):
        self.x, self.y = random.randint(100, 700), random.randint(80, 560)
        self.type = random.randrange(nonplayerable.typeA, nonplayerable.typeB)
        self.life = random.randint(100, 150)
        self.movetime = 0
        self.ymovetime = 0
        self.ystoptime = 0
        self.stoptime = 0
        self.xframe = 0
        self.yfream = 0
        self.movestate = random.randrange(self.left, self.right+1)
        self.ymove = self.stop
        self.emergy = False
        if nonplayerable.protectableimage == None:
            nonplayerable.protectableimage = load_image("makeimage2.png")
        if nonplayerable.atteckableimage == None:
            nonplayerable.atteckableimage = load_image("makeimage2.png")
        if nonplayerable.checkmove == None:
            nonplayerable.checkmove = load_image("find.png")


    def draw(self):
        if self.life > 0:
            if self.type == nonplayerable.typeA:
                self.protectableimage.clip_draw(self.xframe * 35, 455 - (self.yfream + 1) * 45, 35, 45, self.x, self.y,30,40)
            elif self.type == nonplayerable.typeB:
                self.atteckableimage.clip_draw(self.xframe * 35, 455 - (self.yfream + 1) * 45, 35, 45, self.x, self.y,30,40)
        if self.emergy == True:
            self.checkmove.draw(self.x, self.y + 40, 20, 20)


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

        if self.ymovetime < 0:
            self.ymovetime = 0
            self.ymove = self.stop
            self.ystoptime = random.randint(40, 600)
        elif self.ystoptime < 0:
            self.ystoptime = 0
            if self.y < 340:
                self.ymove = self.up
            else:
                self.ymove = self.down
            self.ymovetime = random.randint(30, 400)




    def moveupdate(self, frametime):
        distence = nonplayerable.pps * frametime
        if self.movestate == self.left:
            self.xframe = (self.xframe + 1) % 4
            self.movetime = self.movetime - 1
            if self.x > 0:
                self.x = self.x - (distence)
        elif self.movestate == self.right:
            self.xframe = (self.xframe + 1) % 4
            self.movetime = self.movetime - 1
            if self.x < 800:
                self.x =  self.x + (distence)
        else:
            self.xframe = 0
            self.stoptime = self.stoptime - 1
        if self.ymove == self.up:
            self.yfream = 4
            if self.y <= 600:
                self.y = self.y + (distence)
            self.ymovetime = self.ymovetime - 1
        elif self.ymove == self.down:
            self.yfream = 0
            if self.y >= 60:
                self.y = self.y - (distence)
            self.ymovetime = self.ymovetime - 1
        elif self.ymove == self.stop:
            self.ystoptime = self.ystoptime - 1



    def puttime(self):
        return self.ymove

    def escape(self, player):
        downx, downy, upx, upy = player
        xcheck = (self.x - downx + 15)*(self.x - downx + 15)
        ycheck = (self.y - downy + 20)*(self.y - downy + 20)

        r = math.sqrt(xcheck + ycheck)
        if r < 100:
            self.emergy = True















