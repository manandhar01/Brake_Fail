import pygame
from pygame.locals import *
from sys import exit
import car
import obstacle
import road


# Screen Size
screenSize = (1024, 768)


# Images
roadImage = pygame.image.load('images/road.jpg')
carImage = pygame.image.load('images/car.png')
obstacleImages = [
    pygame.image.load('images/hole.png'),
    pygame.image.load('images/rock.png'),
    pygame.image.load('images/box.jpg'),
    pygame.image.load('images/oilBarrel.png'),
    ]

FPS = 60
fpsClock = pygame.time.Clock()

class Game:
    def __init__(self, size):
        self.size = size
        self.R1 = road.Road(roadImage, [0, 0], 5)
        self.R2 = road.Road(roadImage, [0, 0 - roadImage.get_rect().height], 5)
        self.car = car.Car(carImage, [ self.R1.width/2 - carImage.get_rect().width/2, self.R1.height - carImage.get_rect().height - 50 ], 5)
        self.O1 = obstacle.Obstacle(obstacleImages[0], [ 0, 0 ], 5)
        self.O2 = obstacle.Obstacle(obstacleImages[1], [ self.R1.width - obstacleImages[1].get_rect().width, 0 ], 5)
        self.O3 = obstacle.Obstacle(obstacleImages[2], [ self.R1.width/4 , 0 ], 5)
        self.O4 = obstacle.Obstacle(obstacleImages[3], [ 3 * self.R1.width/4 , 0 ], 5)

    def run(self):
        pygame.init
        pygame.display.set_caption('BRAKE FAIL')
        self.screen = pygame.display.set_mode(self.size, 0, 32)
        self.R1.image = self.R1.image.convert()
        self.R2.image = self.R2.image.convert()
        self.car.image = self.car.image.convert_alpha()
        self.O1.image = self.O1.image.convert_alpha()
        self.O2.image = self.O2.image.convert_alpha()
        self.O3.image = self.O3.image.convert_alpha()
        self.O4.image = self.O4.image.convert_alpha()
        while True:
            self.handleEvents()
            self.updateScreen()

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    self.car.isMovingLeft = True
                elif event.key == K_RIGHT:
                    self.car.isMovingRight = True
            elif event.type == KEYUP:
                if event.key == K_LEFT:
                    self.car.isMovingLeft = False
                elif event.key == K_RIGHT:
                    self.car.isMovingRight = False

    def updateScreen(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.R1.image, (self.R1.posx, self.R1.posy))
        self.screen.blit(self.R2.image, (self.R2.posx, self.R2.posy))
        self.screen.blit(self.car.image, (self.car.posx, self.car.posy))
        self.screen.blit(self.O1.image, (self.O1.posx, self.O1.posy))
        self.screen.blit(self.O2.image, (self.O2.posx, self.O2.posy))
        self.screen.blit(self.O3.image, (self.O3.posx, self.O3.posy))
        self.screen.blit(self.O4.image, (self.O4.posx, self.O4.posy))
        pygame.display.update()
        self.R1.move()
        self.R2.move()
        self.car.move()
        self.O1.move()
        self.O2.move()
        self.O3.move()
        self.O4.move()
        fpsClock.tick(FPS)
