import pygame
from pygame.locals import *
from sys import exit
from modules import car
from modules import obstacle
from modules import road
import random

# Screen Size
screenSize = (1024, 768)

# Speed
speed = 7
count = 0

# Images
roadImage = pygame.image.load('images/road.jpg')
carImage = pygame.image.load('images/car.png')
obstacleImages = [
    pygame.image.load('images/hole.png'),
    pygame.image.load('images/rock.png'),
    pygame.image.load('images/box.jpg'),
    pygame.image.load('images/oilBarrel.png'),
    ]

class Game:
    def __init__(self, size):
        global speed
        global roadImage
        global carImage
        self.fpsClock = pygame.time.Clock()
        self.size = size
        self.R1 = road.Road(roadImage, [0, 0], speed)
        self.R2 = road.Road(roadImage, [0, 0 - roadImage.get_rect().height], speed)
        self.car = car.Car(carImage, [ self.R1.width/2 - carImage.get_rect().width/2, self.R1.height - carImage.get_rect().height - 50 ], speed)
        self.obstacles = []
        self.pause = False
        self.score = 0

    def run(self):
        global obstacleImages
        global speed
        y = 150
        pygame.init()
        pygame.display.set_caption('BRAKE FAIL')
        self.font = pygame.font.Font('fonts/comic.ttf', 50)
        self.screen = pygame.display.set_mode(self.size, 0, 32)
        self.R1.image = self.R1.image.convert()
        self.R2.image = self.R2.image.convert()
        self.car.image = self.car.image.convert_alpha()
        for images in obstacleImages:
            images = images.convert_alpha()
        for i in range(3):
            image = obstacleImages[random.randint(0, 3)]
            self.obstacles.append(obstacle.Obstacle(image,  [random.randint(0, 1024 - image.get_rect().width), -y], speed))
            y += 319
        while True:
            self.handleEvents()
            self.detectCollisions()
            self.updateScreen()

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.pause = True
                    self.paused()
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
        for ob in self.obstacles:
            self.screen.blit(ob.image, (ob.posx, ob.posy))
        self.screen.blit(self.car.image, (self.car.posx, self.car.posy))
        self.screen.blit(self.font.render(f'Score: {self.score}', True, (255, 255, 255)), (20, 0))
        pygame.display.update()
        self.R1.move()
        self.R2.move()
        self.car.move()
        for ob in self.obstacles:
            ob.move()
            if ob.posy > 768:
                ob.image = obstacleImages[random.randint(0, 3)]
                ob.width = ob.image.get_rect().width
                ob.posy = -189
                ob.posx = random.randint(0, 1024 - ob.width)
                ob.isRecorded = False
        self.fpsClock.tick(60)

    def paused(self):
        while self.pause:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.pause = False
                elif event.type == KEYUP:
                    if event.key == K_LEFT:
                        self.car.isMovingLeft = False
                    elif event.key == K_RIGHT:
                        self.car.isMovingRight = False

    def detectCollisions(self):
        for ob in self.obstacles:
            if ob.posy + 0.8*ob.height >= self.car.posy and ob.posy + 0.2*ob.height <= self.car.posy + self.car.height:
                if ob.posx <= self.car.posx:
                    if ob.posx + 0.8*ob.width >= self.car.posx:
                            self.pause = True
                            self.paused()
                else:
                    if self.car.posx + self.car.width >= ob.posx + 0.2*ob.width:
                        self.pause = True
                        self.paused()
                return 0
            elif ob.posy + 0.2*ob.height > self.car.posy + self.car.height:
                if not ob.isRecorded:
                    ob.isRecorded = True
                    self.score += 1