from copy import deepcopy

from utils import util
from utils.settings import Settings


class Dino:
    def __init__(self, jump_velocity, scale_factor=0):
        self.jump_velocity = jump_velocity
        self.current_velocity = 0
        self.counter = 0

        self.images_running, self.rect = util.load_sprite_sheet(
            image_name=Settings.dino_sheet_name,
            number_x=Settings.dino_n_of_sprites,
            scale_factor=scale_factor)
        self.images_ducking, self.rect_ducking = util.load_sprite_sheet(
            image_name=Settings.dino_ducking_sheet_name,
            number_x=Settings.dino_ducking_n_of_sprites,
            scale_factor=scale_factor)

        self.rect.bottom = deepcopy(Settings.dino_position['y'])
        self.rect.left = deepcopy(Settings.dino_position['x'])

        self.image = self.images_running[0]
        self.isJumping = False
        self.isDead = False
        self.isDucking = False
        self.index = 0
        self.delta_t = 1 / Settings.FPS

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        if not self.isDead:
            if self.isJumping:

                # Calculating new position
                y_pos = self.rect.bottom
                y_pos = y_pos + self.delta_t * self.current_velocity * abs(Settings.ground_speed) * 4 * Settings.level

                # Calculating new velocity
                self.current_velocity = \
                    self.current_velocity + self.delta_t * abs(Settings.ground_speed) * Settings.level

                # If dino landed - finishing jump
                if y_pos > Settings.dino_position['y']:
                    self.isJumping = False
                    y_pos = Settings.dino_position['y']

                # Setting new dino position
                self.rect.bottom = y_pos
            else:
                self.counter += 1
                if self.counter % 4 == 0:
                    self.index += 1

                # 2 last sprites of dead t-rex
                if self.index is Settings.dino_n_of_sprites - 2:
                    self.index = 2
                self.image = self.images_running[self.index]
        else:
            # Image of dead dino
            self.image = self.images_running[4]

    def jump(self):
        if not self.isJumping:
            self.isJumping = True
            self.current_velocity = self.jump_velocity
            # Jumping dino
            self.image = self.images_running[0]

    def duck(self):
        # TODO: Finish it later
        pass

    def reset(self):
        self.current_velocity = 0
        self.counter = 0

        self.rect.bottom = deepcopy(Settings.dino_position['y'])

        self.image = self.images_running[0]
        self.isJumping = False
        self.isDead = False
        self.isDucking = False
        self.index = 0