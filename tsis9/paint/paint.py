import pygame

# Making canvas
screen = pygame.display.set_mode((900, 700))

# Setting Title
pygame.display.set_caption('GFG Paint')

draw_on = False
last_pos = (0, 0)

eraser_width = 50

# Radius of the Brush
radius = 5

# My code: setting up colors and their boxes
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (255, 128, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)

COLOR_BUTTONS = [
    {"color": RED, "rect": pygame.Rect(10, 10, 50, 50)},
    {"color": WHITE, "rect": pygame.Rect(70, 10, 50, 50)},
    {"color": YELLOW, "rect": pygame.Rect(130, 10, 50, 50)},
    {"color": GREEN, "rect": pygame.Rect(190, 10, 50, 50)},
    {"color": BLUE, "rect": pygame.Rect(250, 10, 50, 50)},
    {"color": PURPLE, "rect": pygame.Rect(310, 10, 50, 50)}
]

# eraser and its box
eraser = pygame.image.load('data/3672876_education_eraser_erasing_rubber_stationery_icon.png')
eraser_img_resize = pygame.transform.scale(eraser, (eraser_width, eraser_width))


eraser_rect = pygame.Rect(360, 10, 50, 50)


# ends here

def roundline(canvas, color, start, end, radius=1):
    Xaxis = end[0] - start[0]
    Yaxis = end[1] - start[1]
    dist = max(abs(Xaxis), abs(Yaxis))
    for i in range(dist):
        x = int(start[0] + float(i) / dist * Xaxis)
        y = int(start[1] + float(i) / dist * Yaxis)
        pygame.draw.circle(canvas, color, (x, y), radius)

# My Code
color = WHITE
initial_pos = None
final_pos = None
figure = None

# ends here
try:
    while True:
        e = pygame.event.wait()

        if e.type == pygame.QUIT:
            raise StopIteration

        # My code
        if e.type == pygame.MOUSEBUTTONDOWN: # check if mouse button was clicked on the boxes' position and change the color the new one
            if eraser_rect.collidepoint(e.pos):
                color = BLACK
            for button in COLOR_BUTTONS:
                if button["rect"].collidepoint(e.pos):
                    color = button['color']
        if e.type == pygame.KEYDOWN:
            radius = 0 # check if keys were pressed and save the figure form
            if e.key == pygame.K_r:
                initial_pos = pygame.mouse.get_pos()
                figure = 'rect'
            elif e.key == pygame.K_c:
                initial_pos = pygame.mouse.get_pos()
                figure = 'circle'
            elif e.key == pygame.K_s:
                initial_pos = pygame.mouse.get_pos()
                figure = 'sqr'
            elif e.key == pygame.K_t:
                initial_pos = pygame.mouse.get_pos()
                figure = 'r_t'
            elif e.key == pygame.K_e:
                initial_pos = pygame.mouse.get_pos()
                figure = 'e_t'
            elif e.key == pygame.K_w:
                initial_pos = pygame.mouse.get_pos()
                figure = 'rhombus'
        if e.type == pygame.KEYUP:
            initial_pos = None
            final_pos = None
            radius = 5
        # get position of mouse cursor as mouse left button is up
        if e.type == pygame.MOUSEBUTTONUP:
            final_pos = pygame.mouse.get_pos()
        # drawing figures
        if final_pos is not None and initial_pos is not None and figure == 'rect':
            rect_size = (final_pos[0] - initial_pos[0], final_pos[1] - initial_pos[1])
            rect_pos = initial_pos
            pygame.draw.rect(screen, color, (rect_pos, rect_size))
        elif final_pos is not None and initial_pos is not None and figure == 'circle':
            circle_rad = (final_pos[0] - initial_pos[0])/2
            circle_pos = initial_pos[0] + circle_rad, initial_pos[1] + circle_rad
            pygame.draw.circle(screen, color, circle_pos, circle_rad)
        elif final_pos is not None and initial_pos is not None and figure == 'sqr':
            sqr_size = (final_pos[0] - initial_pos[0], final_pos[0] - initial_pos[0])
            sqr_pos = initial_pos
            pygame.draw.rect(screen, color, (sqr_pos, sqr_size))
        elif final_pos is not None and initial_pos is not None and figure == 'r_t':
            r_t_left_bottom = initial_pos[0], final_pos[1]
            r_t_right = final_pos
            r_t_pos = initial_pos
            pygame.draw.polygon(screen, color, (r_t_pos, r_t_right, r_t_left_bottom))
        elif final_pos is not None and initial_pos is not None and figure == 'e_t':
            e_t_left = initial_pos[0], final_pos[1]
            e_t_right = final_pos
            e_t_top = (initial_pos[0] + final_pos[0])/2, initial_pos[1]
            pygame.draw.polygon(screen, color, (e_t_top, e_t_left, e_t_right))
        elif final_pos is not None and initial_pos is not None and figure == 'rhombus':
            r_top = (initial_pos[0] + final_pos[0])/2, initial_pos[1]
            r_left = initial_pos[0], (initial_pos[1] + final_pos[1])/2
            r_right = final_pos[0], (initial_pos[1] + final_pos[1])/2
            r_bottom = (initial_pos[0] + final_pos[0])/2, final_pos[1]

            pygame.draw.polygon(screen, color, (r_left,r_top, r_right, r_bottom))

        # ends here

        if e.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.circle(screen, color, e.pos, radius)
            draw_on = True
        # When mouse button released it will stop drawing
        if e.type == pygame.MOUSEBUTTONUP:
            draw_on = False
        # It will draw a continuous circle with the help of roundline function.
        if e.type == pygame.MOUSEMOTION:
            if draw_on:
                pygame.draw.circle(screen, color, e.pos, radius)
                roundline(screen, color, e.pos, last_pos, radius)
            last_pos = e.pos

        # My code
        for button in COLOR_BUTTONS:
            pygame.draw.rect(screen, button["color"], button["rect"])

        screen.blit(eraser_img_resize, (370, 10))

        # ends here
        pygame.display.flip()


except StopIteration:
    pass

# Quit
pygame.quit()
