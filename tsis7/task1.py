import pygame
import datetime
pygame.init()

size = screen_width, screen_height = 829, 836
screen = pygame.display.set_mode((size))
screen_center = screen_width/2, screen_height/2

image = pygame.image.load("C:\\Users\\DELL\\Desktop\\main_clock.png")
img_rect = image.get_rect(center=screen_center)

right_hand = pygame.image.load("C:\\Users\\DELL\\Desktop\\right_hand.png")
right_hand_rect = right_hand.get_rect(center=screen_center)

left_hand = pygame.image.load("C:\\Users\\DELL\\Desktop\\left_hand.png")
left_hand_rect = left_hand.get_rect(center=screen_center)

l_angle = 5
r_angle = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.blit(image, img_rect)

    time = datetime.datetime.now()
    minutes, seconds = time.minute, time.second

    rot_l = pygame.transform.rotate(left_hand, (-6 * seconds) + 90)
    hand_l = rot_l.get_rect()
    hand_l.center = left_hand_rect.center

    rot_r = pygame.transform.rotate(right_hand, (-6 * minutes) + 90)
    hand_r = rot_r.get_rect()
    hand_r.center = right_hand_rect.center

    l_angle -= 0.66
    r_angle -= 0.0011

    screen.blit(rot_l, hand_l)
    screen.blit(rot_r, hand_r)

    pygame.display.flip()
