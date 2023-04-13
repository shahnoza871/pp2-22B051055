import sys
import pygame
import random
from pygame.locals import *
pygame.init()

n = 25

# to print "Game over!"
play = True

# set time
clock = pygame.time.Clock()

# set screen (size and caption)
screen_size = width, height = 400, 600
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Race")

# street
street = pygame.image.load("AnimatedStreet.png")
street_rect = street.get_rect()
# background noise
noise = pygame.mixer.Sound("background.wav")

class Player:
    def __init__(self):
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width-40), height - 80)
    def update(self):
        keys = pygame.key.get_pressed()
        if self.rect.left > 0 and keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right > 0 and keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
    def draw(self, screen):
        screen.blit(self.image, self.rect)

score = 0
class Enemy:
    def __init__(self):
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width-40), 0)
    def update(self):
        self.rect.move_ip(0, 10)
        if self.rect.bottom > height:
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def draw(self, screem):
        screen.blit(self.image, self.rect)

class Coins:
    def __init__(self):
        self.image = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width-40), 0)
    def update(self):
        self.rect.move_ip(0, 10)
        if self.rect.bottom > height:
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def draw(self, screem):
        screen.blit(self.image, self.rect)

# define objects
p1 = Player()
e1 = Enemy()
coins = Coins()

# to end the game, print "Game over"
FONT = pygame.font.SysFont("arial", 80)
end = FONT.render("1", True, "red")
end_rect = end.get_rect(center = (width/2 - 160, height/2 - 20))


# sound
crash = pygame.mixer.Sound("crash.wav")

# coins
coinAddCounter = 0


running = True
while running:
    # prints the background street image
    screen.blit(street, street_rect)

    # plays background noise
    noise.play()

    # to end the game
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # to print "Game over" and stop updating
    if play:
        # call car moving functions
        p1.update()
        e1.update()
        coins.update()

        p1.draw(screen)
        e1.draw(screen)
        coins.draw(screen)

    # score
    if e1.rect.bottom >= p1.rect.bottom:
        score += 1
        n += 2

    # Pint the score
    FONT_2 = pygame.font.SysFont("arial", 30)
    final_score = int(score/3)
    printscore = FONT_2.render(f"{final_score}", True, "black")
    printscore_rect = printscore.get_rect(center=(20, 30))
    # prints the score
    screen.blit(printscore, printscore_rect)


    # collision
    collision = p1.rect.colliderect(e1.rect)
    if collision:
        noise.stop()
        crash.play()
        screen.fill('red')
        end = FONT.render("Game over!", True, 'white')
        screen.blit(end, end_rect)
        # prints the score
        screen.blit(printscore, printscore_rect)
        play = False


    if p1.rect.colliderect(coins.rect):
        score += random.randint(1, 2)
        coins.rect.bottom = 1000

        


    clock.tick(n)
    pygame.display.update()
