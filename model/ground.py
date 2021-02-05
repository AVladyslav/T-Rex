from utils import util
from utils.settings import Settings


class Ground:
    def __init__(self, speed):
        self.speed = speed
        self.image1, self.rect1 = util.load_image(image_name=Settings.ground_image_name)
        self.image2, self.rect2 = util.load_image(image_name=Settings.ground_image_name)

        self.is1InFront = False
        # Positioning, -20: bias
        self.rect1.bottom = Settings.screen_size[1] - 20
        self.rect2.bottom = Settings.screen_size[1] - 20
        self.rect2.left = self.rect1.right

    def draw(self, screen):
        screen.blit(self.image1, self.rect1)
        screen.blit(self.image2, self.rect2)

    def update(self):
        # Moving ground
        self.rect1.left += self.speed
        self.rect2.left += self.speed

        # Swapping grounds
        if self.is1InFront:
            if self.rect1.left < 0:
                self.is1InFront = False
                self.rect2.left = self.rect1.right
        else:
            if self.rect2.left < 0:
                self.is1InFront = True
                self.rect1.left = self.rect2.right
