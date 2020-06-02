import pygame
from pygame.locals import *
from sys import exit
import car
# import obstacle
import road


# Screen Size
screenSize = (1024, 768)


# Images
roadImage = pygame.image.load('images/road.jpg')
carImage = pygame.image.load('images/car.png')

FPS = 30
fpsClock = pygame.time.Clock()

class Game:
    def __init__(self, size):
        self.size = size
        self.R1 = road.Road(roadImage, [0, 0], 5)
        self.R2 = road.Road(roadImage, [0, 0 - roadImage.get_rect().height], 5)
        self.car = car.Car(carImage, [ screenSize[0]/2 - carImage.get_rect().width/2, screenSize[1] - carImage.get_rect().height-10 ], 0)


    def run(self):
        pygame.init
        pygame.display.set_caption('BRAKE FAIL')
        self.screen = pygame.display.set_mode(self.size, 0, 32)
        self.R1.image = self.R1.image.convert()
        self.R2.image = self.R2.image.convert()
        self.car.image = self.car.image.convert_alpha()
        while True:
            self.handleEvents()
            self.updateScreen()

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

    def updateScreen(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.R1.image, (self.R1.posx, self.R1.posy))
        self.screen.blit(self.R2.image, (self.R2.posx, self.R2.posy))
        self.screen.blit(self.car.image, (self.car.posx, self.car.posy))
        pygame.display.update()
        self.R1.move()
        self.R2.move()
        fpsClock.tick(FPS)
