import sys
import os
import random
from pico2d import *
os.chdir('C:\\studyfolder\\mytrolinglife\\plise')

class nonplayerable:
    protectableimage = None
    atteckableimage = None

    typeA, typeB = 0, 1

    left, right, leftstop, rightstop = 100,200,101,201


    def __init__(self):
        self.x, self.y = 0,0
        self.type = random.randrange(nonplayerable.typeA, nonplayerable.typeB)
        self.life = random.randint(100, 150)
        self.movetime = 0
        self.stoptime = 0
        self.movestate = self.leftstop
        self.emergy = False
        if nonplayerable.protectableimage == None:
            nonplayerable.protectableimage.load("makeimage2.png")
        if nonplayerable.atteckableimage == None:
            nonplayerable.atteckableimage.load("makeimage2.png")


    def draw(self):
        if self.life > 0:
            if self.type == nonplayerable.typeA:
                self.protectableimage.draw(self.x, self.y, 40,40)
            elif self.type == nonplayerable.typeB:
                self.atteckableimage.draw(self.x, self.y, 40, 40)


    def crashrange(self):
        return self.x - 20, self.y - 20, self.x+20, self.y+20




    def moveupdate(self):
        if self.movestate == self.left:
            if self.emergy == False:
                self.movetime = max(0, self.movetime - 1)
            self.x = self.x - 10
        elif self.movestate == self.right:
            if self.emergy == False:
                self.movetime = max(0, self.movetime - 1)
            self.x = self.x + 10
        elif self.movestate in (self.leftstop, self.rightstop):
            self.stoptime = max(0, self.stoptime - 1)







