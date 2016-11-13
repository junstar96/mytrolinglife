import random
import sys
import myframe
from pico2d import *
from maps import Map
from item import Item
import maps
import os
import json
os.chdir('C:\\studyfolder\\mytrolinglife\\plise')


class Boy:
    moveimage = None
    deadimage = None
    attackleft = None
    attackright = None
    attackup = None
    attackdown = None

    pixel_speed = (10.0 / 3)
    runspeed = 10.0
    mpm = (runspeed * 1000.0 / 60.0)
    pps = (pixel_speed * mpm)

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND = 0, 1, 2, 3
    UP_RUN, DOWN_RUN, STAND = 4, 5, 6

    def __init__(self):
        self.x, self.y = 400, 300
        self.ted = False
        self.xframe = 0
        self.yfream = 0
        self.left, self.right = self.LEFT_STAND, self.RIGHT_STAND
        self.up, self.down = self.STAND, self.STAND
        self.moveimage = load_image("makeimage2.png")
        self.deadimage = load_image("dead.png")
        self.attacktime = 0
        self.first_x = 0
        self.first_y = 0
        self.life = 5
        if Boy.attackleft == None:
            Boy.attackleft = load_image("left.png")
        if Boy.attackright == None:
            Boy.attackright = load_image("right.png")
        if Boy.attackup == None:
            Boy.attackup = load_image("up.png")
        if Boy.attackdown == None:
            Boy.attackdown = load_image("down.png")




    def remap(self, a):
        if a == 1:
             self.x = 799
        elif a == 2:
            self.y = 600
        elif a == 3:
            self.x = 1
        elif a == 4:
            self.y = 60

    def notmove(self, a):
        if a == 1:
             self.x = 1
        elif a == 2:
            self.y = 60
        elif a == 3:
            self.x = 799
        elif a == 4:
            self.y = 600





    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                self.left = self.LEFT_RUN
                if self.first_x == 0:
                    self.first_x = 1
            if event.key == SDLK_RIGHT:
                self.right = self.RIGHT_RUN
                if self.first_x == 0:
                    self.first_x = 2
            if event.key == SDLK_UP:
                self.up = self.UP_RUN
                self.yfream = 4
                if self.first_y == 0:
                    self.first_y = 1
            if event.key == SDLK_DOWN:
                self.down = self.DOWN_RUN
                self.yfream = 0
                if self.first_y == 0:
                    self.first_y = 2
            if event.key == SDLK_x:
                self.attacktime = 5

        if event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                self.left = self.LEFT_STAND
                if self.right == self.RIGHT_RUN:
                    self.first_x = 2
                else:
                    self.first_x = 0
            if event.key == SDLK_RIGHT:
                self.right = self.RIGHT_STAND
                if self.left == self.LEFT_RUN:
                    self.first_x = 1
                else:
                    self.first_x = 0
            if event.key == SDLK_UP:
                self.up = self.STAND
                if self.down == self.DOWN_RUN:
                    self.first_y = 2
                else:
                    self.first_y = 0
            if event.key == SDLK_DOWN:
                self.down = self.STAND
                if self.up == self.UP_RUN:
                    self.first_y = 1
                else:
                    self.first_y = 0


    def update(self, frametime):
        global line
        distence = Boy.pps * frametime
        if self.first_y != 0 or self.first_x != 0:
              self.xframe = (self.xframe + 1) % 4
        if self.first_x == 1:
            self.x = self.x - (distence)
        elif self.first_x == 2:
            self.x = self.x + (distence)
        if self.first_y == 1:
            self.y = self.y + (distence)
        elif self.first_y == 2:
            self.y = self.y - (distence)

        if self.attacktime > 0:
            self.attacktime = self.attacktime - 0.3

    def draw(self):
        if self.ted != True:
            self.moveimage.clip_draw(self.xframe * 35, 455 - (self.yfream + 1) * 45, 35, 45, self.x, self.y,40,48)
        else:
            self.deadimage.clip_draw(self.xframe * 48, 0, 48, 39, self.x, self.y)
        if self.attacktime > 0:
            if self.first_x == 1 and self.first_y == 0:
                self.attackleft.draw(self.x - 20, self.y, 10, 20)
            elif self.first_x == 2 and self.first_y == 0:
                self.attackright.draw(self.x + 20, self.y, 10, 20)
            elif self.yfream == 0:
                self.attackdown.draw(self.x, self.y - 20, 20, 10)
            elif self.yfream == 4:
                self.attackup.draw(self.x, self.y + 20, 20, 10)








    def get_bb(self):
        return self.x-15, self.y - 20, self.x + 15, self.y + 20

    def dead(self):
        self.ted = True
        self.xframe = 0

    def fin(self):
        if self.ted == True:
            return True

    def getdamage(self, a):
        self.life = self.life - 0.5 and self.xframe == 0
        if self.life < 0:
           self.dead()
