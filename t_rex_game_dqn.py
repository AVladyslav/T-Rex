import pygame as pg
from PIL import Image, ImageOps
import numpy as np
import copy

from model.cactus import Cactus
from model.ground import Ground
from model.dino import Dino
from model.text import Text
from utils.settings import Settings


class TRexGame:

    def __init__(self):

        # Reinforcement Learning stuff
        # Position of first cactus, position of second cactus
        self.state_size = 1
        # Do nothing, jump
        self.action_size = 2
        self.DO_NOTHING = 0
        self.JUMP = 1
        # Done - player loosed the game
        self.done = False

        self.display_mode_on = True

        # Game itself
        pg.init()

        self.screen = pg.display.set_mode(Settings.screen_size)
        # Set up the drawing window
        pg.display.set_caption('Run T-Rex Run')

        self.clock = pg.time.Clock()

        self.dino = Dino(jump_velocity=Settings.dino_jump_velocity, scale_factor=Settings.dino_scale)
        self.ground = Ground(speed=Settings.ground_speed)
        self.cactus = Cactus(speed=Settings.ground_speed)
        self.text = Text()

    def _check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE or pg.K_UP:
                    self.dino.jump()

    def _update(self):
        if Settings.level < Settings.max_level:
            if pg.time.get_ticks() % 3000 == 0:
                Settings.level += 0.1

        self.ground.update()
        self.cactus.update()
        self.dino.update()
        self.check_collisions()
        self.text.update()

    def check_collisions(self):
        if self.dino.rect.colliderect(self.cactus.rects[0]):
            self.dino.isDead = True
            self.done = True

    def _draw(self):
        if self.display_mode_on:
            self.screen.fill(Settings.bg_color)
            self.ground.draw(self.screen)
            self.cactus.draw(self.screen)
            self.dino.draw(self.screen)
            self.text.draw(self.screen)
            pg.display.flip()

            # Updating display
            pg.display.update()

    # def run_game(self):
    #
    #     # Run until the user asks to quit
    #     while self.running:
    #         self._check_events()
    #         self._update()
    #         self._draw()
    #         self.clock.tick(Settings.FPS)
    #
    #     # Done! Time to quit.
    #     pg.quit()


    def _get_state(self):

        image = self._make_screenshot()

        # IsJumping, position of first cactus
        dist_to_cactus = Settings.screen_size[0] - self.cactus.rects[0].left
        if dist_to_cactus < 0:
            dist_to_cactus = 1
        else:
            dist_to_cactus /= Settings.screen_size[0]
        state = [dist_to_cactus]
        return state

    def reset(self):

        self.done = False

        Settings.level = Settings.min_level

        self.dino.reset()
        self.cactus.reset()
        self.ground.reset()
        self.text.reset()

        self._update()
        self._draw()
        self.clock.tick(Settings.FPS)

        image_series = []
        self._update()
        self._draw()
        self.clock.tick(Settings.FPS)
        image = self._make_screenshot()
        for _ in range(Settings.n_in_series):
            image_series.append(copy.deepcopy(image))

        state_env = np.array(image_series)
        state_env = state_env.reshape(Settings.thumb_height, Settings.thumb_width, Settings.n_in_series)

        return state_env

    def step(self, action):

        image_series = []

        if action == self.JUMP:
            self.dino.jump()

        for _ in range(Settings.n_in_series):
            self._update()
            self._draw()
            self.clock.tick(Settings.FPS)
            image = self._make_screenshot()
            image_series.append(image)

        next_state_env = np.array(image_series)

        next_state_env = next_state_env.reshape(Settings.thumb_height, Settings.thumb_width, Settings.n_in_series)

        if self.done:
            reward = Settings.negative_reward
        else:
            reward = Settings.positive_reward

        return next_state_env, reward, self.done

    def turn_off_display(self):
        self.display_mode_on = False

    def turn_on_display(self):
        self.display_mode_on = True

    def _make_screenshot(self):
        # Snipping rect of screen
        rect = pg.Rect(0, 0, Settings.rect_width, Settings.rect_height)
        surface = self.screen.subsurface(rect)
        strFormat = 'RGBA'
        raw_str = pg.image.tostring(surface, strFormat, False)
        image = Image.frombytes(strFormat, surface.get_size(), raw_str)
        image.thumbnail((Settings.thumb_width, Settings.thumb_height), Image.ANTIALIAS)
        image = ImageOps.grayscale(image)

        # Inverted treshold
        thresh = Settings.tresh_value
        fn = lambda x: 0 if x > thresh else 255
        image = image.convert('L').point(fn, mode='1')
        image = np.asarray(image)
        image = image.astype(int) * 255
        return image
