import pygame
pygame.init()

size = width, height = 600, 500
screen = pygame.display.set_mode(size)

music = [pygame.mixer.Sound("C:\\Users\\DELL\\Music\\Home_Edith_Whiskers.mp3"),
         pygame.mixer.Sound("C:\\Users\\DELL\\Music\\Cliffy.mp3"),
         pygame.mixer.Sound("C:\\Users\\DELL\\Music\\Agnes_Obel_Riverside_(minus).mp3"),
         pygame.mixer.Sound("C:\\Users\\DELL\\Music\\Agnes_Obel_The_Curse_(minus).mp3"),
         pygame.mixer.Sound("C:\\Users\\DELL\\Music\\Daughter-Shallows.mp3")]

i = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #chose one variable for music[i] and make operations only on it (otherwise they play parallel)
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        music[i].play()
    if key[pygame.K_F4]:
        music[i].stop()
    if key[pygame.K_RIGHT]:
        if i!=len(music):
            music[i].play()
        else: music[0].play()
    if key[pygame.K_LEFT]:
        if i != 0:
            music[i-1].play()
        if i==0:
            music[len(music)].play()

    pygame.display.update()





"""    if key[pygame.K_SPACE]:
        music[i].play()
    if key[pygame.K_F4]:
        music[i].stop()
    if key[pygame.K_RIGHT]:
        music[i+1].play()
    if key[pygame.K_LEFT]:
        music[i-1].play()
    i += 1"""
