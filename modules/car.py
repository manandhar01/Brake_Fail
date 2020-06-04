class Car:
    def __init__(self, image, pos, speed):
        self.image = image
        self.height = self.image.get_rect().height
        self.width = self.image.get_rect().width
        self.speed = speed
        self.posx = pos[0]
        self.posy = pos[1]
        self.isMovingLeft = False
        self.isMovingRight = False

    def move(self):
        if self.isMovingLeft:
            self.posx -= self.speed
        if self.isMovingRight:
            self.posx += self.speed
        if self.posx < 0:
            self.posx += self.speed
        if self.posx + self.width > 1024:
            self.posx -= self.speed