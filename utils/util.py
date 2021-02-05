import os
import pygame as pg

from utils.settings import Settings


def load_sprite_sheet(image_name, number_x, scale_factor=0):
    path = os.path.join(Settings.images_path, image_name)

    sheet = pg.image.load(path)
    sheet = sheet.convert()

    width = sheet.get_width() / number_x
    height = sheet.get_height()

    sprites = []

    for i in range(number_x):
        rect = pg.Rect((i * width, 0, width, height))
        sprite = pg.Surface(rect.size)
        sprite.blit(sheet, (0, 0), rect)

        if scale_factor != 0:
            sprite = pg.transform.scale(sprite, (scale_factor, scale_factor))

        sprite = sprite.convert()
        sprites.append(sprite)

    return sprites, sprites[0].get_rect()

def load_image(image_name, scale_factor=0):

    path = os.path.join(Settings.images_path, image_name)

    image = pg.image.load(path)

    if scale_factor != 0:
        image = pg.transform.scale(image, (scale_factor, scale_factor))

    image = image.convert()

    return image, image.get_rect()

