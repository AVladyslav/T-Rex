import pygame as pg

from model.cactus import Cactus
from model.ground import Ground
from model.dino import Dino
from model.text import Text
from utils.settings import Settings


class TRexGame:

    def __init__(self):
        pg.init()

        self.settings = Settings()
        self.clock = pg.time.Clock()
        self.running = True
        self.isEndOfGame = False

        self.screen = pg.display.set_mode(self.settings.screen_size)
        # Set up the drawing window
        pg.display.set_caption('Run T-Rex Run')

        self.dino = Dino(jump_velocity=self.settings.dino_jump_velocity, scale_factor=self.settings.dino_scale)
        self.ground = Ground(speed=self.settings.ground_speed)
        self.cactus = Cactus(speed=self.settings.ground_speed)
        self.text = Text()

    def _check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE or pg.K_UP:
                    self.dino.jump()

    def _update(self):
        if Settings.level < 2.5:
            if pg.time.get_ticks() % 3000 == 0:
                Settings.level += 0.1

        self.ground.update()
        self.cactus.update()
        self.dino.update()
        self.check_collisions()
        self.text.update()

    def _draw(self):
        self.screen.fill(self.settings.bg_color)
        self.ground.draw(self.screen)
        self.cactus.draw(self.screen)
        self.dino.draw(self.screen)
        self.text.draw(self.screen)
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

    def check_collisions(self):
        if self.dino.rect.colliderect(self.cactus.rects[0]):
            self.isEndOfGame = True
            self.running = False
