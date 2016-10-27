import random
import sys
from pico2d import *
import maps
import item





running = True
xmove = 2
ymove = 2
keymove = False
name = "startstate"
image = None
boy = None
map = None
items = None

class Boy:
    moveimage = None
    deadimage = None
    def __init__(self):
        self.x, self.y = 400, 300
        self.ted = False
        self.frame = 0
        self.xmovepoint = 0
        self.yfream = 0
        self.moveimage = load_image("makeimage2.png")
        self.deadimage = load_image("dead.png")

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
            self.y = 85

    def handle_event(self, event):
        global xmove
        global ymove
        global keymove
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_LEFT:
                keymove = True
                xmove = 0
            elif event.key == SDLK_RIGHT:
                keymove = True
                xmove = 1
            elif event.key == SDLK_UP:
                keymove = True
                ymove = 1
            elif event.key == SDLK_DOWN:
                keymove = True
                ymove = 0
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT or event.key == SDLK_RIGHT:
                xmove = 2
            elif event.key == SDLK_UP or event.key == SDLK_DOWN:
                ymove = 2

    def move_update(self):
        self.frame = (self.frame + 1)%4

    def draw(self):
        if self.ted != True:
            self.moveimage.clip_draw(self.frame * 35, 455 - (self.yfream + 1) * 45, 35, 45, self.x, self.y,30,40)
        else:
            self.deadimage.clip_draw(self.frame * 48, 0, 48, 39, self.x, self.y)


    def get_bb(self):
        return self.x-22, self.y - 20, self.x + 22, self.y + 20

    def dead(self):
        self.ted = True
        self.frame = 0

    def fin(self):
        if self.ted == True and self.frame == 4:
            return True




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
        if event.type == SDL_QUIT:
            running = False
        else:
            boy.handle_event(event)






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

        boy.remap(maps.mapwall(boy.get_bb()))

        delay(0.1)
        update_canvas()
        if boy.fin():
            exit()

    exit()



if __name__ == '__main__':
    main()




