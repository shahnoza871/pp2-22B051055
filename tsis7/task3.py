import pygame
size = screen_width, screen_height = 625, 425
pygame.init()
screen = pygame.display.set_mode(size)
run = True

x = 25
y = 25
vel = 20

speed = pygame.time.Clock()

while run:
    screen.fill('white')
    c = pygame.draw.circle(screen, (150, 0, 0), (x, y), 25)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>25 :
        x -= vel
    if keys[pygame.K_RIGHT] and x<screen_width-25:
        x += vel
    if keys[pygame.K_UP] and y>25:
        y -= vel
    if keys[pygame.K_DOWN] and y<screen_height-25:
        y+=vel

    speed.tick(30)
    pygame.display.update()

