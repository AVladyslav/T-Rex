import pygame as pg

from utils.settings import Settings


class Text:
    def __init__(self):
        pg.font.init()  # you have to call this at the start,
        # if you want to use this module.
        self.myfont = pg.font.SysFont('Comic Sans MS', 34)
        self.score = 0

    def update(self):
        self.score += int(Settings.level * 10 - 10)

    def draw(self, screen):
        text = 'Level: ' + str(int(Settings.level * 10 - 10)) + ' Score: ' + str(self.score)
        textsurface = self.myfont.render(text, False, Settings.text_color)
        screen.blit(textsurface, Settings.text_position)

    def reset(self):
        self.score = 0
