from pico2d import *
import os
os.chdir('C:\\studyfolder\\mytrolinglife\\plise')

class backgroundsound:

    def __init__(self):
        self.backgroundsound = load_music("Arctic+Void+-+On+the+Padded+Wall.mp3")
        self.backgroundsound.set_volume(32)
        self.backgroundsound.repeat_play()


    def __del__(self):
        del self.backgroundsound