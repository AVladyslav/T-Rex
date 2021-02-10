import copy
import random

import pygame

from utils import util
from utils.settings import Settings


class Cactus:
    def __init__(self, speed, scale_factor=0):
        self.cactus_omitted = False
        self.speed = speed
        self.index = 0

        self.images, self.rect = util.load_sprite_sheet(
            image_name=Settings.cactus_large_sheet_name,
            number_x=Settings.cactus_large_n_of_sprites,
            scale_factor=scale_factor)
        self.images_small, self.rect_small = util.load_sprite_sheet(
            image_name=Settings.cactus_small_sheet_name,
            number_x=Settings.cactus_small_n_of_sprites,
            scale_factor=scale_factor)

        self.rects = []
        for _ in range(3):
            self.rects.append(copy.deepcopy(self.rect))

        # Setting up initial positions for cacti
        self.rects[0].left = Settings.screen_size[0]
        self.rects[1].left = Settings.screen_size[0] * 1.5
        self.rects[2].left = Settings.screen_size[0] * 2
        for rect in self.rects:
            rect.bottom = Settings.screen_size[1] - 20

    def update(self):
        # Moving cacti
        for rect in self.rects:
            rect.left += self.speed * Settings.level
        if self.rects[0].right < 0:
            # First cactus
            rect = self.rects.pop(0)
            # rects[1] - last cactus
            rect.left = self.rects[1].right + random.randint(Settings.cactus_min_dist, Settings.cactus_max_dist)
            self.rects.append(rect)

            # Swapping first to last cactus image
            self.images.append(self.images.pop(0))
            
            self.cactus_omitted = True

    def draw(self, screen):
        for i in range(len(self.images)):
            screen.blit(self.images[i], self.rects[i])

    def reset(self):
        self.index = 0
        self.rects[0].left = Settings.screen_size[0]
        self.rects[1].left = Settings.screen_size[0] * 1.5
        self.rects[2].left = Settings.screen_size[0] * 2
