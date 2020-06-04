class Obstacle:
    def __init__(self, image, pos, speed):
        self.image = image
        self.height = self.image.get_rect().height
        self.width = self.image.get_rect().width
        self.posx = pos[0]
        self.posy = pos[1]
        self.speed = speed
        self.isRecorded = False

    def move(self):
        self.posy += self.speed