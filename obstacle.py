import random

class Obstacle:
    def __init__(self, image, posy, speed):
        self.image = image
        self.height = self.image.get_rect().height
        self.width = self.image.get_rect().width
        self.posx = random.randint(0, 1024 - self.width)
        self.posy = posy
        self.speed = speed

    def move(self):
        self.posy += self.speed