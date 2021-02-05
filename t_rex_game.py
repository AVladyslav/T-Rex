import os
import pygame as pg

from model.ground import Ground
from model.dino import Dino
from utils.settings import Settings


class TRexGame:

    def __init__(self):
        pg.init()

        self.settings = Settings()
        self.clock = pg.time.Clock()
        self.running = True

        self.screen = pg.display.set_mode(self.settings.screen_size)
        # Set up the drawing window
        pg.display.set_caption('Run T-Rex Run')

        self.logo_image = pg.image.load(os.path.join('images', 'logo.png'))

        self.t_rex = Dino(speed=self.settings.dino_speed, scale_factor=self.settings.dino_scale)
        self.ground = Ground(speed=self.settings.ground_speed)

    def _check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def _update(self):
        self.ground.update()
        self.t_rex.update()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ground.draw(self.screen)
        self.t_rex.draw(self.screen)
        self.screen.blit(self.logo_image, self.settings.logo_position)
        # Updating display
        pg.display.update()

    def run_game(self):

        # Run until the user asks to quit
        while self.running:
            self._check_events()
            self._update()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

        # Done! Time to quit.
        pg.quit()
