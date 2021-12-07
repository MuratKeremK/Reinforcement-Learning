# pygame template
import pygame
import random

# window size
WIDTH = 900
HEIGHT = 480
FPS = 60 # how fast game is

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0, 0) # RGB
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)



class Player(pygame.sprite.Sprite):
    # sprite for the player
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.radius = 15
        pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 1
        self.speedx = 0
        self.speedy = 0
        
        
    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_LEFT]:
            self.speedx = -4
        elif keystate[pygame.K_RIGHT] :
            self.speedx = 4
        elif keystate[pygame.K_UP]:
            self.speedy = -4
        elif keystate[pygame.K_DOWN]:
            self.speedy = 4
        else:
            self.speedx = 0
            self.speedy = 0

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
            
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
    

    
class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.radius = 15
        pygame.draw.circle(self.image, WHITE, self.rect.center, self.radius)
        self.rect.x = random.randrange(0, 5)
        self.rect.y = random.randrange(200, 290)

        self.speedx = 3
        self.speedy = 0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right > WIDTH + 10:
            self.rect.x = random.randrange(0, 5)
            self.rect.y = random.randrange(210, 280)
            self.speedy = 0
            self.speedx = 3

    def getCoordinates(self):
        return (self.rect.x, self.rect.y)   
    
    
    
    
    

# initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("RL Game")
clock = pygame.time.Clock()

# sprite
all_sprite = pygame.sprite.Group()
player = Player()
all_sprite.add(player)
enemy = Enemy()
all_sprite.add(enemy)




# game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS) 
    
    # process input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # update
    all_sprite.update()
    
    # draw / render(show)
    screen.fill(BLACK)
    all_sprite.draw(screen)
    
    c1=pygame.draw.rect(screen,WHITE,(400,300,5,180))
    c2=pygame.draw.rect(screen,WHITE,(500,300,5,180))
    
    c3=pygame.draw.rect(screen,WHITE,(0,200,400,5))
    c4=pygame.draw.rect(screen,WHITE,(0,300,400,5))
    
    c5=pygame.draw.rect(screen,WHITE,(500,200,900,5))
    c6=pygame.draw.rect(screen,WHITE,(500,300,900,5))
    
    
    park1 = pygame.draw.rect(screen,BLUE,(50,50,100,70))
    park2 = pygame.draw.rect(screen,BLUE,(400,50,100,70))
    park3 = pygame.draw.rect(screen,BLUE,(700,50,100,70))
    
    
    
    
    
    # after drawing flip display
    pygame.display.flip()
    
    # after drawing flip display
    pygame.display.flip()
    
    
pygame.quit() 

