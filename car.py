class Car:
    def __init__(self, image, pos, speed):
         self.image = image
         self.speed = speed
         self.posx = pos[0]
         self.posy = pos[1]

    def move(self):
         self.posx += self.speed
         
