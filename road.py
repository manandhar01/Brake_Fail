class Road:
    def __init__(self, image, pos, speed):
        self.image = image
        self.height = self.image.get_rect().height
        self.width = self.image.get_rect().width
        self.speed = speed
        self.posx = pos[0]
        self.posy = pos[1]

    def move(self):
        self.posy += self.speed
        if(self.posy > 768):
            self.posy -= 768+self.height
        
