import pygame
import random
pygame.init()


# creating a screen
screen_size = width, height = 500, 500
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Snake!")

# size of the grid
square_size = 25

# drawing grid
def draw_lines(square_size, width, height):
    new_square_size = 0
    while new_square_size <= width:
        pygame.draw.line(screen, (50, 50, 50), (new_square_size, 0), (new_square_size, height))
        pygame.draw.line(screen, (50, 50, 50), (0, new_square_size), (width, new_square_size))
        new_square_size += square_size

draw_lines(square_size, width, height)

# creating a snake class
class Snake:
    def __init__(self):
        # position of a snake
        self.x, self.y = square_size, square_size
        # directions (moves to the right by default)
        self.xdir = 1
        self.ydir = 0
        # head, one square block
        self.head = pygame.Rect(self.x, self.y, square_size, square_size)
        # body, type is list
        self.body = [pygame.Rect(self.x - square_size, self.y, square_size, square_size)]
        # tells whether or nor the snake is dead
        self.dead = False

    def moving(self):
        # check if dead
        for square in self.body:
            if self.head.x == square.x and self.head.y == square.y:
                self.dead = True

        if self.dead:
            self.head.x = 2*width
            self.head.y = 2*height
            for i in range(len(self.body) - 1):
                self.body[i].x = 2*width
                self.body[i].y = 2*height

        # to make the head of a snake a part of its body
        self.body.append(self.head)
        # each block of body take a position of the previous block
        for i in range(len(self.body)-1):
            self.body[i].x, self.body[i].y = self.body[i+1].x, self.body[i+1].y
        # snake's head moves
        self.head.x += self.xdir*square_size
        self.head.y += self.ydir*square_size
        # to separate the head from body (because it runs through a different algorithms, and it's more convenient)
        self.body.remove(self.head)
snake = Snake()


# creating an apple class
class Apple:
    def __init__(self):
        self.x = square_size*(random.randrange(0, width/square_size))
        self.y = square_size*(random.randrange(0, height/square_size))
        self.rect = pygame.Rect(self.x, self.y, square_size, square_size)
    def new(self):
        pygame.draw.rect(screen, 'orange', self.rect)
apple = Apple()



FONT = pygame.font.SysFont("arial", square_size*2)

# to create a text that tells the score
score = FONT.render("1", True, "white")
score_rect = score.get_rect(center = (width/2, height/20))

# to create a text that tells if the snake is dead
isdead = FONT.render("1", True, "red")
isdead_rect = isdead.get_rect(center = (width/2 - 120, height/2 - 20))

clock = pygame.time.Clock()

running = True
while running:
    # to color the screen black (before everything)
    screen.fill((0, 0, 0))

    draw_lines(square_size, width, height)

    # to end the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # call the function that moves snake
    snake.moving()

    # call the function that creates a new apple
    apple.new()

    # draw a head
    pygame.draw.rect(screen, 'green', snake.head)

    # goes through every square in the body of a snake and draws it
    for square in snake.body:
        pygame.draw.rect(screen, 'green', square)

    # managing how the snake moves
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake.xdir = -1
        snake.ydir = 0
    if keys[pygame.K_RIGHT]:
        snake.xdir = 1
        snake.ydir = 0
    if keys[pygame.K_UP]:
        snake.ydir = -1
        snake.xdir = 0
    if keys[pygame.K_DOWN]:
        snake.ydir = 1
        snake.xdir = 0

    # collision of snake's head and an apple
    collision = snake.head.colliderect(apple)
    if collision:
        a = random.choice([True, False])
        if a:
            snake.body.append(pygame.Rect(square.x, square.y, square_size, square_size))
            snake.body.append(pygame.Rect(square.x, square.y, square_size, square_size))
        if not a:
            snake.body.append(pygame.Rect(square.x, square.y, square_size, square_size))
        apple = Apple()

    # snake come from opposite side if quieted the screen
    if snake.head.x == 0:
        snake.head.x = width - square_size
    if snake.head.x == width:
        snake.head.x = 0
    if snake.head.y == 0:
        snake.head.y = height - square_size
    if snake.head.y == height:
        snake.head.y = 0

    # to print the score
    score = FONT.render(f"{len(snake.body)+1}", True, 'white')
    screen.blit(score, score_rect)

    # to print if dead
    if snake.dead:
        isdead = FONT.render("Snake's Dead", True, 'red')
        screen.blit(isdead, isdead_rect)

    pygame.display.update()

    if len(snake.body) < 11:
        clock.tick(10)
    if len(snake.body) > 10 and len(snake.body) < 20:
        clock.tick(12)
    if len(snake.body) > 20 and len(snake.body):
        clock.tick(15)

