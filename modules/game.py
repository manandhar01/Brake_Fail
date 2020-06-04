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
        self.pause = True
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
        self.paused('BRAKE FAIL', 'PLAY')
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
                    self.paused('GAME PAUSED', 'Resume')
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
        self.screen.blit(self.font.render(f'SCORE: {self.score}', True, (250, 70, 85)), (20, 0))
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

    def paused(self, title, string, gameOver = False):
        select = 0
        font = pygame.font.Font('fonts/comic.ttf', 100)
        text = font.render(f'{title}', True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (screenSize[0]/2, screenSize[1]/6)
        font = pygame.font.Font('fonts/comic.ttf', 60)
        _score = font.render(f'Final Score: {self.score}', True, (0, 0, 0))
        _scoreRect = _score.get_rect()
        _scoreRect.center = (screenSize[0]/2, screenSize[1]/3)
        resume = font.render(f'{string}', True, (0, 0, 0))
        resumeRect = resume.get_rect()
        resumeRect.center = (screenSize[0]/2, screenSize[1]/2)
        _quit = font.render('Quit', True, (0, 0, 0))
        _quitRect = _quit.get_rect()
        _quitRect.center = (screenSize[0]/2, 3*screenSize[1]/4)
        font = pygame.font.Font('fonts/comic.ttf', 20)
        guide = font.render('Use Up and Down arrow keys to navigate. Press Return to select.', True, (0, 0, 0))
        guideRect = guide.get_rect()
        guideRect.center = (screenSize[0]/2, 9*screenSize[1]/10)
        while self.pause:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.pause = False
                    elif event.key == K_DOWN:
                        select = 1
                    elif event.key == K_UP:
                        select = 0
                    elif event.key == K_RETURN:
                        if select == 0:
                            self.pause = False
                            if gameOver:
                                self.playAgain()
                        else:
                            exit()
                elif event.type == KEYUP:
                    if event.key == K_LEFT:
                        self.car.isMovingLeft = False
                    elif event.key == K_RIGHT:
                        self.car.isMovingRight = False
            self.screen.fill((220, 230, 110))
            self.screen.blit(text, textRect)
            if gameOver:
                self.screen.blit(_score, _scoreRect)
            pygame.draw.rect(self.screen, (0, 175, 90), (screenSize[0]/2 - 150, screenSize[1]/2 - 50, 300, 100))
            pygame.draw.rect(self.screen, (180, 0, 40), (screenSize[0]/2 - 120, 3*screenSize[1]/4 - 50, 240, 100))
            if select == 0:
                pygame.draw.rect(self.screen, (0, 0, 0), (screenSize[0]/2 - 150, screenSize[1]/2 - 50, 300, 100), 10)
            else:
                pygame.draw.rect(self.screen, (0, 0, 0), (screenSize[0]/2 - 120, 3*screenSize[1]/4 - 50, 240, 100), 10)
            self.screen.blit(resume, resumeRect)
            self.screen.blit(_quit, _quitRect)
            self.screen.blit(guide, guideRect)
            pygame.display.update()

    def detectCollisions(self):
        global speed
        for ob in self.obstacles:
            if ob.posy + 0.8*ob.height >= self.car.posy and ob.posy + 0.2*ob.height <= self.car.posy + self.car.height:
                if ob.posx <= self.car.posx:
                    if ob.posx + 0.8*ob.width >= self.car.posx:
                        self.pause = True
                        self.paused('GAME OVER!!!', 'Play Again', True)
                else:
                    if self.car.posx + self.car.width >= ob.posx + 0.2*ob.width:
                        self.pause = True
                        self.paused('GAME OVER!!!', 'Play Again', True)
                return 0
            elif ob.posy + 0.2*ob.height > self.car.posy + self.car.height:
                if not ob.isRecorded:
                    ob.isRecorded = True
                    self.score += 1
                    if self.score % 20 == 0:
                        self.R1.speed += 1
                        self.R2.speed += 1
                        self.car.speed += 1
                        for obj in self.obstacles:
                            obj.speed += 1

    def playAgain(self):
        global obstacleImages
        global speed
        self.obstacles = []
        self.score = 0
        self.R1.speed = speed
        self.R2.speed = speed
        self.car.speed = speed
        y = 150
        for i in range(3):
            image = obstacleImages[random.randint(0, 3)]
            self.obstacles.append(obstacle.Obstacle(image,  [random.randint(0, 1024 - image.get_rect().width), -y], speed))
            y += 319
        self.car.posx = screenSize[0]/2 - self.car.width/2