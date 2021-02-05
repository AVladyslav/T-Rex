import os
import pygame as pg

from model.ground import Ground
from model.t_rex import TRex
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

        self.t_rex = TRex(speed=self.settings.t_rex_speed, scale_factor=self.settings.t_rex_scale)
        self.ground = Ground(speed=self.settings.ground_speed)

        pass

    def _check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
        pass

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.logo_image, self.settings.logo_position)
        # Updating display
        pg.display.update()
        pass

    def run_game(self):

        # Run until the user asks to quit
        while self.running:
            self._check_events()
            self._update_screen()
            self.clock.tick(1)

        # Done! Time to quit.
        pg.quit()
        pass

    pass
