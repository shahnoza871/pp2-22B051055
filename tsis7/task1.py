import pygame
pygame.init()
size = screen_width, screen_height = 850, 800
screen = pygame.display.set_mode((size))

screen_center = screen_width/2, screen_height/2
image = pygame.image.load("C:\\Users\\DELL\\Desktop\\mikey.png")
img_rect = image.get_rect(center=screen_center)


angle = 5

time = pygame.time.Clock()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill('white')

    part = pygame.Surface((70, 90))
    part.blit(image, (screen_center), (100, 5, 80, 6))
    part_rect = part.get_rect(center=screen_center)

    screen.blit(image, img_rect)
    screen.blit(part, part_rect)
    #screen.blit(rot1, rect1)
    time.tick(15)
    pygame.display.update()

"""    rot1 = pygame.transform.rotate(part, angle) #
    rect1 = rot1.get_rect()
    rect1.center = img_rect.center
    angle += 5"""


