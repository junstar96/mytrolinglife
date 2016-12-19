import random
import sys
import myframe
from pico2d import *
from maps import Map
from item import Item
import maps
import os
from canplay import Boy
import json
from police import nonplayerable

from soundfile import backgroundsound
os.chdir('C:\\studyfolder\\mytrolinglife\\plise')




running = True
name = "startstate"
boy = None
map = None
items = None
current_time = 0.0
font = None
line = None
background = None

def get_frame_time():

    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time


def enter():
    global boy
    global map
    global items, font
    global line
    global background
    open_canvas()
    boy = Boy()
    map = [Map() for i in range(0, 25)]
    items = Item()
    background = backgroundsound()



    line = 4
    font = load_font('ENCR10B.TTF', 30)

def exit():
    global boy
    global map
    global items
    global font
    del(boy)
    del(map)
    del(items)
    del(font)
    close_canvas()

def check():
    global boy
    global map

    checkpoint = 0

    for mapcheck in map:
        for re in mapcheck.returnnpc():
            checkpoint = checkpoint + re.livecheck()

    boy.killcheck(checkpoint)








def handle_events(frametime):
    global running
    global boy, items
    events = get_events()
    for event in events:
        boy.handle_event(event)
        items.handle_event(event)
        if event.type == SDL_QUIT:
            myframe.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False

def linewall():
    global boy, map, line
    if maps.mapwall(boy.get_bb()) == 1:
        if line > 0:
            line = line - 1
            boy.remap(maps.mapwall(boy.get_bb()))
        else:
            boy.notmove(maps.mapwall(boy.get_bb()))
    elif maps.mapwall(boy.get_bb()) == 2:
        if line/5 < 4:
            line = line + 5
            boy.remap(maps.mapwall(boy.get_bb()))
        else:
            boy.notmove(maps.mapwall(boy.get_bb()))
    elif maps.mapwall(boy.get_bb()) == 3:
        if line < 24:
            line = line + 1
            boy.remap(maps.mapwall(boy.get_bb()))
        else:
            boy.notmove(maps.mapwall(boy.get_bb()))
    elif maps.mapwall(boy.get_bb()) == 4:
        if line/5 > 1:
            line = line - 5
            boy.remap(maps.mapwall(boy.get_bb()))
        else:
            boy.notmove(maps.mapwall(boy.get_bb()))

def update(frametime):
    global boy
    global map
    global items
    global background

    boy.update(frametime)
    map[line].update(frametime)

    if boy.killtimer > 1200:
        myframe.quit()

    linewall()

    check()


    map[line].playercheck(boy)

def draw(frametime):
    global boy
    global map
    global items

    clear_canvas()
    map[line].draw()
    items.draw()
    boy.draw()

    update_canvas()




