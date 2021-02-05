from utils import util
from utils.settings import Settings


class Ground:
    def __init__(self, speed):
        self.speed = speed
        self.image, self.rect = util.load_image(image_name=Settings.ground_image_name)
        pass
    pass
