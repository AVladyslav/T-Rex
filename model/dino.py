from utils import util
from utils.settings import Settings


class Dino:
    def __init__(self, speed, scale_factor=0):
        self.speed = speed

        self.images_running, self.rect = util.load_sprite_sheet(
            image_name=Settings.dino_sheet_name,
            number_x=Settings.dino_n_of_sprites,
            scale_factor=scale_factor)
        self.images_ducking, self.rect_ducking = util.load_sprite_sheet(
            image_name=Settings.dino_ducking_sheet_name,
            number_x=Settings.dino_ducking_n_of_sprites,
            scale_factor=scale_factor)

        self.rect.bottom = Settings.dino_position['y']
        self.rect.left = Settings.dino_position['x']

        self.image = self.images_running[0]
        self.isJumping = False
        self.isDead = False
        self.isDucking = False
        self.index = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.index += 1

        if not self.isDead:
            if not self.isJumping:
                # 2 last sprites of dead t-rex
                if self.index is Settings.dino_n_of_sprites - 2:
                    self.index = 0
                self.image = self.images_running[self.index]