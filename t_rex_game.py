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

        self.dino = Dino(jump_velocity=self.settings.dino_jump_velocity, scale_factor=self.settings.dino_scale)
        self.ground = Ground(speed=self.settings.ground_speed)

    def _check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.dino.jump()

    def _update(self):
        self.ground.update()
        self.dino.update()

    def _draw(self):
        self.screen.fill(self.settings.bg_color)
        self.ground.draw(self.screen)
        self.dino.draw(self.screen)
        self.screen.blit(self.logo_image, self.settings.logo_position)
        # Updating display
        pg.display.update()

    def run_game(self):

        # Run until the user asks to quit
        while self.running:
            self._check_events()
            self._update()
            self._draw()
            self.clock.tick(self.settings.FPS)

        # Done! Time to quit.
        pg.quit()
