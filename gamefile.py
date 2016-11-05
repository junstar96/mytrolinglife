import random
import sys
from pico2d import *
import maps
import item
import os
import json
os.chdir('C:\\studyfolder\\mytrolinglife\\plise')




running = True
name = "startstate"
boy = None
map = None
items = None

class Boy:
    moveimage = None
    deadimage = None

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
        self.first_x = 0
        self.first_y = 0
        self.life = 5

    def remap(self, a):
        if a == 1:
            self.x = 750
        elif a == 2:
            self.y = 550
        elif a == 3:
            self.x = 25
        elif a == 4:
            self.y = 85

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


    def update(self):
        if self.first_y != 0 or self.first_x != 0:
              self.xframe = (self.xframe + 1) % 4
        if self.first_x == 1:
            self.x = self.x - 10
        elif self.first_x == 2:
            self.x = self.x + 10
        if self.first_y == 1:
            self.y = self.y + 10
        elif self.first_y == 2:
            self.y = self.y - 10

    def draw(self):
        if self.ted != True:
            self.moveimage.clip_draw(self.xframe * 35, 455 - (self.yfream + 1) * 45, 35, 45, self.x, self.y,30,40)
        else:
            self.deadimage.clip_draw(self.xframe * 48, 0, 48, 39, self.x, self.y)


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




def enter():
    global boy
    global map
    global items
    open_canvas()
    boy = Boy()
    map = maps.Map()
    items = item.Item()

def exit():
    global boy
    global map
    global items
    del(boy)
    del(map)
    del(items)
    close_canvas()

def movestop():
    global keymove
    if xmove == 2 and ymove == 2:
        keymove = False

def handle_events():
    global running
    global boy
    events = get_events()
    for event in events:
        boy.handle_event(event)
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False


def main():
    global xmove, ymove
    global running, keymove
    global boy
    global map
    global items

    enter()

    while (running):
        handle_events()
        clear_canvas()
        map.draw()
        items.draw()

        boy.draw()
        boy.update()

        boy.remap(maps.mapwall(boy.get_bb()))
        boy.getdamage(maps.mapwall(boy.get_bb()))

        delay(0.1)
        update_canvas()
        if boy.fin():
            exit()

    exit()

if __name__ == '__main__':
    main()




