import pygame
import random

FPS = 60

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 420

GAME_HEIGHT = 400
GAME_WIDTH = 400

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,255,0)

CAR_WIDTH = 20
CAR_HEIGTH = 20

PARKFIELD_WIDTH = 70
PARKFIELD_HEIGTH = 70

CAR_SPEED_X = 1
CAR_SPEED_Y = 1

screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))


def drawCar(carXPos, carYPos):
    
    car = pygame.Rect(carXPos, carYPos, CAR_WIDTH, CAR_HEIGTH)
        
    pygame.draw.rect(screen, WHITE, car)


def drawParkField(parkXPos, parkYPos):
    
    park = pygame.Rect(parkXPos, parkYPos, PARKFIELD_WIDTH, PARKFIELD_HEIGTH)
    pygame.draw.rect(screen, BLUE, park)

def updateCar(switch, action, carXPos, carYPos):
    
    dft = 7.5 
    
    if switch=="gamer":
        
        if action == 1:
            carXPos = carXPos + CAR_SPEED_X*dft
            carYPos = carYPos
            if carXPos >= 400:
                carXPos=400
            
        elif action == 2:
            carXPos = carXPos - CAR_SPEED_X*dft
            carYPos =carYPos
            if carXPos <= 0:
                carXPos=0
            
        elif action == 3:
            carXPos = carXPos
            carYPos = carYPos + CAR_SPEED_Y*dft
            
            if carYPos >= 400:
                carYPos=400
            
        elif action == 4:
            carXPos = carXPos
            carYPos = carYPos - CAR_SPEED_Y*dft
            
            if carYPos <= 0:
                carYPos=0
            
        elif action == 5:
            carXPos = carXPos
            carYPos = carYPos
        
    elif switch=="otherCar":
        if action == 1:
            pass
            
        elif action == 2:
            pass
        elif action == 3:
            pass
        elif action == 4:
            pass
        
    return [carXPos, carYPos]



def updateParkField(score ,carXPos, carYPos, parkXPos, parkYPos):
    
    if abs(carXPos-parkXPos)< 35 and abs(carYPos - parkYPos) < 35:
        parkXPos = random.randint(100, 300)
        parkYPos = random.randint(100, 300)
        
        
        score = 10000
        
    else:
        parkXPos = parkXPos
        parkYPos = parkYPos
        
        X = abs(carXPos-parkXPos)
        Y = abs(carYPos-parkYPos)
        
        score = -(X + Y)
        
    return [score, parkXPos, parkYPos]





class ParkGame:
    
    def _init_(self):
        pygame.init()
        pygame.display.set_caption("Car Parking Env")
        
        self.parkField_X = random.randint(100, 300)
        self.parkField_Y = random.randint(100, 300)
        
        self.clock = pygame.time.Clock()
        
        self.gamerPos_X = WINDOW_WIDTH/2
        self.gamerPos_Y = GAME_HEIGHT
        
        
        self.otherPos_X = 80
        self.otherPos_Y = random.randint(100,250)
                
        self.GScore = 0.0
    
    def InitialDisplay(self):
        
        pygame.event.pump()
        screen.fill(BLACK)
        
        drawCar(self.gamerPos_X, self.gamerPos_Y)
        
        drawParkField(self.parkField_X, self.parkField_Y)
        
        
        pygame.display.flip()
        
    
    def PlayNextMove(self, action):
        
        DeltaFrameTime = self.clock.tick(FPS)
        
        pygame.event.pump()
        
        score = 0
        
        screen.fill(BLACK)
        
        [self.gamerPos_X, self.gamerPos_Y] = updateCar("gamer", action, self.gamerPos_X, self.gamerPos_Y)
        
        drawCar(self.gamerPos_X, self.gamerPos_Y)
        
        [score, self.parkField_X, self.parkField_Y] = updateParkField(score, self.gamerPos_X, self.gamerPos_Y, self.parkField_X, self.parkField_Y)
        
        drawParkField(self.parkField_X, self.parkField_Y)
    
        if ( score > 0.5 or score < -0.5):
            self.GScore = self.GScore*0.9 + 0.1*score 
            
        ScreenImage = pygame.surfarray.array3d(pygame.display.get_surface())
        
        pygame.display.flip()
        
        return [score, ScreenImage]
    
    
park = ParkGame()
park._init_()
park.InitialDisplay()
 

    
    
    
    
    
    
    
    
    
    