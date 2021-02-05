from utils import util
from utils.settings import Settings


class TRex:
    def __init__(self, speed, scale_factor=0):
        self.speed = speed
        self.images_running, self.rect = util.load_sprite_sheet(
            image_name=Settings.t_rex_sheet_name,
            number_x=Settings.t_rex_n_of_sprites,
            scale_factor=scale_factor)
        self.images_ducking, self.rect_ducking = util.load_sprite_sheet(
            image_name=Settings.t_rex_ducking_sheet_name,
            number_x=Settings.t_rex_ducking_n_of_sprites,
            scale_factor=scale_factor)
        pass
    pass
