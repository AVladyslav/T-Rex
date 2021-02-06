from utils import util
from utils.settings import Settings


class Cactus:
    def __init__(self, speed, scale_factor=0):
        self.speed = speed

        self.images, self.rect = util.load_sprite_sheet(
            image_name=Settings.cactus_large_sheet_name,
            number_x=Settings.cactus_large_n_of_sprites,
            scale_factor=scale_factor)
        self.images_small, self.rect_ducking = util.load_sprite_sheet(
            image_name=Settings.cactus_small_sheet_name,
            number_x=Settings.cactus_small_n_of_sprites,
            scale_factor=scale_factor)
