import random
import sys
from pico2d import *
import maps

import os

running = True
xmove = 2
ymove = 2
keymove = False
name = "startstate"
image = None
boy = None


class Boy:
    def __init__(self):
        self.x, self.y = 400, 300
        self.frame = 0
        self.yfream = random.randint(0,4)
        self.moveimage = load_image("makeimage2.png")

    def x_move_right(self):
        self.x = self.x + 10

    def x_move_left(self):
        self.x = self.x - 10

    def y_move_up(self):
        self.yfream = 4
        self.y = self.y + 10

    def y_move_down(self):
        self.yfream = 0
        self.y = self.y -10

    def remap(self, a):
        if a == 1:
            self.x = 750
        elif a == 2:
            self.y = 550
        elif a == 3:
            self.x = 25
        elif a == 4:
            self.y = 25

    def move_update(self):
        self.frame = (self.frame + 1)%4

    def draw(self):
        self.moveimage.clip_draw(self.frame*35,455 - (self.yfream+1)*45,35,45,self.x, self.y)

    def get_bb(self):
        return self.x, self.y, self.x + 35, self.y + 45

def enter():
    global boy
    open_canvas()
    boy = Boy()

def exit():
    global boy
    del(boy)
    close_canvas()

def movestop():
    global keymove
    if xmove == 2 and ymove == 2:
        keymove = False



def handle_events():
    global running
    global xmove
    global ymove
    global keymove
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            keymove = True
            if event.key == SDLK_ESCAPE:
               running = False
            elif event.key == SDLK_LEFT:
                xmove = 0
            elif event.key == SDLK_RIGHT:
                xmove = 1
            elif event.key == SDLK_UP:
                ymove = 1
            elif event.key == SDLK_DOWN:
                ymove = 0
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT or event.key == SDLK_RIGHT:
                xmove = 2
            elif event.key == SDLK_UP or event.key == SDLK_DOWN:
                ymove = 2





def main():
    global xmove, ymove
    global running, keymove
    global boy

    enter()



    while (running):
        handle_events()
        clear_canvas()

        boy.draw()
        if (keymove):
            boy.move_update()

        if (xmove == 0):
            boy.x_move_left()
        elif xmove == 1:
            boy.x_move_right()

        if ymove == 0:
            boy.y_move_down()
        elif ymove == 1:
            boy.y_move_up()



        movestop()

        delay(0.1)
        update_canvas()

    close_canvas()


if __name__ == '__main__':
    main()




