import sys
import os
import random
import math

from item import Item
from pico2d import *
os.chdir('C:\\studyfolder\\mytrolinglife\\plise')
npc = None

class nonplayerable:
    protectableimage = None
    atteckableimage = None
    checkmove = None
    item = None
    attackleft = None
    attackright = None
    attackup = None
    attackdown = None
    sound = None
    deadimage = None


    typeA, typeB = 0, 1

    left, right, leftstop, rightstop = 100,101, 500, 501
    up, down, stop = 10, 11, 12

    pixel_speed = (10.0/3)
    runspeed = 8.0
    mpm = (runspeed * 1000.0/60.0)
    pps = (pixel_speed * mpm)




    def __init__(self):
        self.x, self.y = random.randint(100, 700), random.randint(80, 560)
        self.type = random.randrange(nonplayerable.typeA, nonplayerable.typeB + 1)
        self.life = random.randint(100, 150)
        self.movetime = 0
        self.ymovetime = 0
        self.ystoptime = 0
        self.stoptime = 0
        self.xframe = 0
        self.yfream = 0
        self.countkill = 0
        self.countsafe = 0
        self.attacktime = 1
        self.attackdelay = 1
        self.movestate = random.randrange(self.left, self.right+1)
        self.ymove = self.stop
        self.emergy = False
        self.item = Item()
        self.speak = False
        self.attackvector = 0 # 0은 밑 1은 위 2는 왼쪽, 3은 오른쪽

        if nonplayerable.sound == None:
            nonplayerable.sound = load_music("The+Very+First+Wilhelm+Scream.mp3")
            nonplayerable.sound.set_volume(32)

        self.targetx, self.targety = 0,0
        if nonplayerable.protectableimage == None:
            nonplayerable.protectableimage = load_image("makeimage2.png")
        if nonplayerable.atteckableimage == None:
            nonplayerable.atteckableimage = load_image("makeimage2.png")
        if nonplayerable.checkmove == None:
            nonplayerable.checkmove = load_image("find.png")
        self.item.gettype()

        if nonplayerable.attackleft == None:
            nonplayerable.attackleft = load_image("left.png")
        if nonplayerable.attackright == None:
            nonplayerable.attackright = load_image("right.png")
        if nonplayerable.attackup == None:
            nonplayerable.attackup = load_image("up.png")
        if nonplayerable.attackdown == None:
            nonplayerable.attackdown = load_image("down.png")

        if nonplayerable.deadimage == None:
            nonplayerable.deadimage = load_image("dead.png")





    def putpoint(self):
        return self.x, self.y

    def checklife(self):
        return self.life


    def draw(self):
        if self.type == nonplayerable.typeA:
            if self.life > 1:
                self.protectableimage.clip_draw(self.xframe * 35, 455 - (self.yfream + 1) * 45, 35, 45, self.x, self.y,
                                                30, 40)
                if self.emergy == True:
                    if self.attacktime > 0:
                        if self.attackvector == 0:
                            self.attackdown.draw(self.x, self.y - (50 - self.attacktime), 18, 9)
                        elif self.attackvector == 1:
                            self.attackup.draw(self.x, self.y + (50 - self.attacktime), 18, 9)
            else:
                self.item.dropdraw(self.x, self.y)
        elif self.type == nonplayerable.typeB:
            if self.life > 1:
                self.atteckableimage.clip_draw(self.xframe * 35, 455 - (self.yfream + 1) * 45, 35, 45, self.x, self.y,
                                               30, 40)

            else:
                self.item.dropdraw(self.x, self.y)
        if self.emergy == True:
            if self.life > 0:
                self.checkmove.draw(self.x, self.y + 40, 20, 20)





    def deadsound(self):
        if self.speak == False:
            self.sound.play(1)
            self.speak = True


    def vec(self):
        return self.attackvector





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

        if self.attacktime >= 0:
            self.attacktime -= 0.5
            if self.attacktime == 0:
               self.attackdelay = 25
        elif self.attackdelay >= 0:
            self.attackdelay -= 0.5
            if self.attackdelay == 0:
               self.attacktime = 25
               if self.targety > self.y:
                   self.attackvector = 1
               elif self.targety < self.y:
                   self.attackvector = 0







    def moveupdate(self, frametime):
        distence = nonplayerable.pps * frametime
        if self.life > 0:
            if self.emergy == False:
                if self.movestate == self.left:
                    self.xframe = (self.xframe + 1) % 4
                    self.movetime = self.movetime - 1
                    if self.x > 0:
                        self.x = self.x - (distence)
                elif self.movestate == self.right:
                    self.xframe = (self.xframe + 1) % 4
                    self.movetime = self.movetime - 1
                    if self.x < 800:
                        self.x = self.x + (distence)
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
            elif self.emergy == True:
               if self.type == self.typeA:
                   if self.targetx < self.x:
                       self.xframe = (self.xframe + 1) % 4
                       if self.x > 0:
                           self.x = self.x - (distence)
                   elif self.targetx > self.x:
                       self.xframe = (self.xframe + 1) % 4
                       if self.x < 800:
                           self.x = self.x + (distence)
                   if self.targety > self.y:
                       self.yfream = 4
                       if self.y <= 600:
                           self.y = self.y + (distence)
                   elif self.targety < self.y:
                       self.yfream = 0
                       if self.y >= 60:
                           self.y = self.y - (distence)
               elif self.type == self.typeB:
                   if self.targetx < self.x:
                       self.xframe = (self.xframe + 1) % 4
                       if self.x < 800:
                           self.x = self.x + (distence)
                   elif self.targetx > self.x:
                       self.xframe = (self.xframe + 1) % 4
                       if self.x > 0:
                           self.x = self.x - (distence)
                   if self.targety > self.y:
                       self.yfream = 0
                       if self.y >= 60:
                           self.y = self.y - (distence)
                   elif self.targety < self.y:
                       self.yfream = 4
                       if self.y <= 600:
                           self.y = self.y + (distence)





        else:
            pass


    def puttime(self):
        return self.ymove

    def escape(self, player):
        downx, downy, upx, upy = player.get_bb()
        mathx = (self.x - (downx + 15))*(self.x - (downx + 15))
        mathy = (self.y - (downy + 20))*(self.y - (downy + 20))
        self.targetx = downx + 15
        self.targety = downy + 20


        r = math.sqrt(mathx + mathy)
        if r < 100:
            self.emergy = True
            if r < 30 and player.getattack() > 0:
                self.life = 0

    def checkpoint(self, a):
        self.countkill, self.countsafe = a

    def livecheck(self):
        if self.life > 0:
            return 0
        else:
            return 1



















