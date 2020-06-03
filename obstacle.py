class Obstacle:
    def __init__(self, image, pos, speed):
        self.image = image
        self.posx = pos[0]
        self.posy = pos[1]
        self.speed = speed
        self.height = self.image.get_rect().height
        self.width = self.image.get_rect().width

    def move(self):
        self.posy += self.speed
        if(self.posy > 768):
            self.posy -= 768+self.height