import pygame, time, random, psycopg2
from config import  host, user, password, db_name, port_id

pygame.init()

window_x = 720
window_y = 480
font = pygame.font.Font(None, 25)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

pygame.display.set_caption('Змейка')
game_window = pygame.display.set_mode((window_x, window_y))
pause = False


def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, 'white')
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def paused(pause, user_nick, score, level):
    pygame.init()

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pause = False
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_v:
                    pause = False
                if event.key == pygame.K_s:
                    get_user_info(user_nick, score, level)


        pygame.draw.rect(game_window, 'lightskyblue3', (window_x/2-300, window_y/2-120, 600, 240))

        drawText('Paused', font, game_window, window_x/2-20, window_y/2-100)
        drawText('Press S to save', font, game_window, 120, window_y/2)
        drawText('Press V to continue', font, game_window, 450, window_y/2)


        pygame.display.flip()


def get_user_info(user_name, score, level):
    connection = None
    cursor = None
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name,
            port = port_id
        )
        connection.autocommit = True

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT user_name FROM SnakeGame WHERE user_name = '%s' 
            """ % (user_name,)
        )

        user_exists = cursor.fetchone()

        if user_exists is not None:
            cursor.execute(
                """
                SELECT user_score FROM SnakeGame WHERE user_name = (%s)
                """, (user_name,)
            )

            max_score = cursor.fetchone()[0]
            # print(max_score)

            if int(max_score) < score:
                max_score = score

            cursor.execute(
                """
                UPDATE SnakeGame
                SET user_score = %s, user_level = %s
                WHERE user_name = %s
                """, (str(max_score), str(level), (user_name,))
            )
        else:
            cursor.execute(
                """
                INSERT INTO SnakeGame(user_name, user_score, user_level)
                VALUES (%s, %s, %s)
                """, (user_name, str(score), str(level))
            )

    except Exception as _ex:
        print("[INFO] Error working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            cursor.close()

def show_user_info(user_name, score, level):
        connection = None
        cursor = None
        user_score = score
        user_level = level

        try:
            connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=db_name, 
                port = port_id
            )
            connection.autocommit = True

            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT user_name FROM SnakeGame WHERE user_name = %s
                """, (user_name,)
            )

            user_exists = cursor.fetchone()

            if user_exists is not None:
                cursor.execute(
                    """
                    SELECT user_score FROM SnakeGame WHERE user_name = %s
                    """, (user_name,)
                )

                user_score = cursor.fetchone()[0]

                cursor.execute(
                    """
                    SELECT user_level FROM SnakeGame WHERE user_name = %s
                    """, (user_name,)
                )

                user_level = cursor.fetchone()[0]

        except Exception as _ex:
            print("[INFO] Error while connecting to PostgreSql", _ex)
        finally:
            if connection:
                connection.close()
                cursor.close()

        return user_score, user_level


def start_game(user_nick):


    snake_speed = 15
    pygame.init()
    fps = pygame.time.Clock()
    snake_position = [100, 50]
    snake_body = [[100, 50],
                  [90, 50],
                  [80, 50],
                  [70, 50]
                  ]

    # fruit position
    fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                      random.randrange(1, (window_y // 10)) * 10]

    fruit_spawn = True

    t_fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                        random.randrange(1, (window_y // 10)) * 10]

    t_fruit_spawn = True
    t_fruit_weight = 25

    # установка направления змеи по умолчанию к
    # право
    direction = 'RIGHT'
    change_to = direction

    # начальная оценка
    score = 0

    level = 1

    # My code
    if int(show_user_info(user_nick, score, level)[1]) > 1:
        level = int(show_user_info(user_nick, score, level)[1])
    else:
        level = 1


    # ends here

    # отображение функции Score
    def show_score(choice, color, font, size):
        # создание объекта шрифта score_font
        score_font = pygame.font.SysFont(font, size)

        # создать объект поверхности отображения
        # score_surface
        score_surface = score_font.render('Score : ' + str(score), True, color)

        # создаем прямоугольный объект для текста
        # поверхностный объект
        score_rect = score_surface.get_rect()

        # отображение текста
        game_window.blit(score_surface, score_rect)

    # функция завершения игры
    def game_over():
        # создание объекта шрифта my_font
        my_font = pygame.font.SysFont('times new roman', 50)

        # создание текстовой поверхности, на которой текст
        # будет нарисовано
        game_over_surface = my_font.render(
            'Your Score is : ' + str(score), True, red)
        game_over_surface_level = my_font.render(
            'You level is: ' + str(level), True, red)

        # создать прямоугольный объект для текста
        # surface object
        game_over_rect = game_over_surface.get_rect()
        game_over_surface_level_rect = game_over_surface_level.get_rect()
        # установка положения текста
        game_over_rect.midtop = (window_x / 2, window_y / 4)
        game_over_surface_level_rect.midtop = (window_x/2, window_y/4 + 100)
        # blit нарисует текст на экране
        game_window.blit(game_over_surface, game_over_rect)
        game_window.blit(game_over_surface_level, game_over_surface_level_rect)
        pygame.display.flip()

        # через 2 секунды мы выйдем из программы
        time.sleep(2)

        # деактивация библиотеки pygame
        get_user_info(user_nick, score, level)
        pygame.quit()

        # quit the program
        quit()

    # My code
    counter = 7
    timer_event = pygame.USEREVENT + 1
    pygame.time.set_timer(timer_event, 1000)
    foo = False
    fruit_weight_list = [10, 15, 20]
    global pause
    pause = False
    # Ends here

    # Main Function
    while True:

        # обработка ключевых событий
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'
                if event.key == pygame.K_c:
                    pause = True
                    paused(pause, user_nick, score, level)


            # My code
            elif event.type == timer_event:
                counter -= 1
                if counter >= 8:
                    foo = True
                else:
                    foo = False

                if counter == 0:
                    counter = 12
                # Ends here

        # Если две клавиши нажаты одновременно
        # мы не хотим, чтобы змея разделялась на две
        # направлений одновременно
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Перемещение змеи
        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10

        # Механизм роста тела змеи
        # если фрукты и змеи сталкиваются, то очки
        # будет увеличено на 10
        snake_body.insert(0, list(snake_position))
        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            score += random.choice(fruit_weight_list)
            fruit_spawn = False
        else:
            snake_body.pop()

        if not fruit_spawn:
            fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                              random.randrange(1, (window_y // 10)) * 10]

        fruit_spawn = True
        game_window.fill(black)

        # My code
        if foo:
            if snake_position[0] == t_fruit_position[0] and snake_position[1] == t_fruit_position[1]:
                counter = 7
                score += t_fruit_weight
                t_fruit_spawn = False
            pygame.draw.rect(game_window, 'orange', (t_fruit_position[0], t_fruit_position[1], 10, 10))

            if not t_fruit_spawn:
                counter = 7
                t_fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                                    random.randrange(1, (window_y // 10)) * 10]

            t_fruit_spawn = True
        # ends here

        for pos in snake_body:
            pygame.draw.rect(game_window, green,
                             pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(game_window, white, pygame.Rect(
            fruit_position[0], fruit_position[1], 10, 10))

        # Game Over conditions
        if snake_position[0] < 0 or snake_position[0] > window_x - 10:
            get_user_info(user_nick, score, level)
            game_over()
        if snake_position[1] < 0 or snake_position[1] > window_y - 10:
            get_user_info(user_nick, score, level)
            game_over()

        # Touching the snake body
        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                get_user_info(user_nick, score, level)
                game_over()

        # My code
        if score >= level * 30:
            level += 1
            snake_speed += (level * 6)

        if level >= 3:
            pygame.draw.rect(game_window, white, (0, 0, window_x, 10))
            pygame.draw.rect(game_window, white, (0, 0, 10, window_y))
            pygame.draw.rect(game_window, white, (window_x - 10, 0, 10, window_y))
            pygame.draw.rect(game_window, white, (0, window_y - 10, window_x, 10))

            pygame.draw.rect(game_window, white, (100, 140, 520, 20))
            pygame.draw.rect(game_window, white, (100, 290, 520, 20))

            if snake_position[0] < 10 or snake_position[0] > window_x - 30:
                get_user_info(user_nick, score, level)
                game_over()
            if snake_position[1] < 10 or snake_position[1] > window_y - 30:
                get_user_info(user_nick, score, level)
                game_over()

            if snake_position[1] < 160 and snake_position[1] > 140 and snake_position[0] > 90 and snake_position[0] < 620:
                get_user_info(user_nick, score, level)
                game_over()

            if snake_position[1] < 310 and snake_position[1] > 280 and snake_position[0] > 90 and snake_position[0] < 620:
                get_user_info(user_nick, score, level)
                game_over()


            if fruit_position[0] < 10 or fruit_position[0] > window_x - 30:
                fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                                  random.randrange(1, (window_y // 10)) * 10]
            if fruit_position[1] < 10 or fruit_position[1] > window_y - 30:
                fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                              random.randrange(1, (window_y // 10)) * 10]

            if fruit_position[1] < 160 and snake_position[1] > 140 and fruit_position[0] > 90 and fruit_position[0] < 620:
                fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                                  random.randrange(1, (window_y // 10)) * 10]

            if fruit_position[1] < 310 and fruit_position[1] > 280 and fruit_position[0] > 90 and fruit_position[0] < 620:
                fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                                  random.randrange(1, (window_y // 10)) * 10]



        drawText('Level %s' % (level), font, game_window, 640, 10)
        drawText('Player: %s' % (user_nick), font, game_window, 10, 30)
        drawText('Max Score: %s' % (show_user_info(user_nick, score, level)[0]), font, game_window, 10, 50)
        # ends here

        drawText('Score %s' % (score), font, game_window, 10, 10)


        # Refresh game screen
        pygame.display.update()

        # Frame Per Second /Refresh Rate
        fps.tick(snake_speed)


def get_user_name():
    nickname = ""
    input_box = pygame.Rect(window_x // 2 - 100, window_y // 2 - 25, 200, 50)
    active_color = pygame.Color('dodgerblue2')
    inactive_color = pygame.Color('lightskyblue3')
    color = inactive_color
    input_active = True

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    input_active = True
                else:
                    input_active = False
                color = active_color if input_active else inactive_color
            if event.type == pygame.KEYDOWN:
                if input_active:
                    if event.key == pygame.K_BACKSPACE:
                        nickname = nickname[:-1]
                    elif event.key == pygame.K_RETURN:
                        start_game(nickname)

                        return nickname
                    else:
                        nickname += event.unicode

        # Fill the background
        game_window.fill((255, 255, 255))

        # Render the text
        text_surface = font.render("Enter your nickname:", True, (0, 0, 0))
        game_window.blit(text_surface, (window_x // 2 - text_surface.get_width() // 2, window_y // 4))

        # Render the input box
        pygame.draw.rect(game_window, color, input_box, 2)

        # Render the nickname text
        nickname_surface = font.render(nickname, True, (0, 0, 0))
        game_window.blit(nickname_surface, (input_box.x + 5, input_box.y + 5))

        pygame.display.update()

    pygame.quit()


get_user_name()