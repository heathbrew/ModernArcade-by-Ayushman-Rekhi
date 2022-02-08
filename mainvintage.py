import pygame
import random
import math
from pygame import mixer
from pygame.locals import *
#initialize the game
pygame.init()
#create the screen
screen = pygame.display.set_mode((800,600))
b1 = pygame.image.load("Vintage2.jpg")
# create the screen
screen = pygame.display.set_mode((800, 600))  # width,height
#title and icon
pygame.display.set_caption("Main Menu")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

#game loop
running = True
if running == True:
    mixer.music.load("squidgame.wav")
    mixer.music.play(-1)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_2:
                # create game loop
                pingpong = True
                mixer.music.stop()
                mixer.music.load("DeathNote.wav")
                mixer.music.play(-1)
                screen_width = 800
                screen_height = 600

                fpsClock = pygame.time.Clock()
                screen = pygame.display.set_mode((screen_width, screen_height))
                pygame.display.set_caption('Main menu')

                # font
                font = pygame.font.SysFont('Constantia', 25)

                # game variables
                margin = 50
                cpuscore = 0
                player_score = 0
                fps = 60
                live_ball = False
                winner = 0

                # screen colours
                bg = (0, 0, 0)
                white = (255, 255, 255)


                def draw_board():
                    screen.fill(bg)
                    pygame.draw.line(screen, white, (0, margin), (screen_width, margin), 2)


                def draw_text(text, font, text_col, x, y):
                    img = font.render(text, True, text_col)
                    screen.blit(img, (x, y))


                class paddle():
                    def __init__(self, x, y):
                        self.x = x
                        self.y = y
                        self.rect = Rect(x, y, 20, 100)
                        self.speed = 5
                        self.ai_speed = 5

                    def move(self):
                        key = pygame.key.get_pressed()
                        if key[pygame.K_UP] and self.rect.top > margin:
                            self.rect.move_ip(0, -1 * self.speed)
                        if key[pygame.K_DOWN] and self.rect.bottom < screen_height:
                            self.rect.move_ip(0, self.speed)

                    def draw(self):
                        pygame.draw.rect(screen, white, self.rect)

                    def ai(self):
                        # ai to move the paddle automatically
                        if self.rect.centery < pong.rect.top and self.rect.bottom < screen_height:
                            self.rect.move_ip(0, self.ai_speed)
                        if self.rect.centery > pong.rect.bottom and self.rect.top > margin:
                            self.rect.move_ip(0, -1 * self.ai_speed)


                class ball():
                    def __init__(self, x, y):
                        self.reset(x, y)

                    def move(self):

                        # check collision
                        if self.rect.top < margin:
                            self.speed_y *= -1

                        if self.rect.bottom > screen_height:
                            self.speed_y *= -1
                        if self.rect.colliderect(player_paddle) or self.rect.colliderect(cpu_paddle):
                            self.speed_x *= -1

                        # check for out of bounds
                        if self.rect.left < 0:
                            self.winner = 1
                        if self.rect.left > screen_width:
                            self.winner = -1

                        # update ball position
                        self.rect.x += self.speed_x
                        self.rect.y += self.speed_y

                        return self.winner

                    def draw(self):
                        pygame.draw.circle(screen, white, (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad),
                                           self.ball_rad)

                    def reset(self, x, y):
                        self.x = x
                        self.y = y
                        self.ball_rad = 8
                        self.rect = Rect(x, y, self.ball_rad * 2, self.ball_rad * 2)
                        self.speed_x = -4
                        self.speed_y = 4
                        self.winner = 0  # 1 is the player and -1 is the CPU


                # create paddles
                player_paddle = paddle(screen_width - 40, screen_height // 2)
                cpu_paddle = paddle(20, screen_height // 2)

                # create pong ball
                pong = ball(screen_width - 60, screen_height // 2 + 50)
                while pingpong:
                    fpsClock.tick(fps)
                    draw_board()
                    draw_text('CPU: ' + str(cpuscore), font, white, 20, 15)
                    draw_text('P1: ' + str(player_score), font, white, screen_width - 100, 15)
                    draw_text('BALL SPEED: ' + str(abs(pong.speed_x)), font, white, screen_width // 2 - 100, 15)

                    # draw paddles
                    player_paddle.draw()
                    cpu_paddle.draw()

                    if live_ball == True:
                        winner = pong.move()
                        if winner == 0:
                            pong.draw()
                            player_paddle.move()
                            cpu_paddle.ai()
                        else:
                            live_ball = False
                            if winner == 1:
                                player_score += 1
                            elif winner == -1:
                                cpuscore += 1

                    # player instructions
                    if live_ball == False:
                        if winner == 0:
                            draw_text('CLICK ANYWHERE TO START', font, white, 100, screen_height // 2 - 100)
                        if winner == 1:
                            draw_text('YOU SCORED!', font, white, 220, screen_height // 2 - 100)
                            draw_text('CLICK ANYWHERE TO START', font, white, 100, screen_height // 2 - 50)
                        if winner == -1:
                            draw_text('CPU SCORED!', font, white, 220, screen_height // 2 - 100)
                            draw_text('CLICK ANYWHERE TO START', font, white, 100, screen_height // 2 - 50)

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pingpong = False
                        if event.type == pygame.MOUSEBUTTONDOWN and live_ball == False:
                            live_ball = True
                            pong.reset(screen_width - 60, screen_height // 2 + 50)
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_q:
                                pingpong = False
                                mixer.music.stop()
                                mixer.music.load("squidgame.wav")
                                mixer.music.play(-1)
                    pygame.display.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    space = True
                    mixer.music.stop()
                    background = pygame.image.load("dead-2.jpg")
                    # baground music

                    # title and icon
                    pygame.display.set_caption("Space Invaders")
                    ufo = pygame.image.load("ufo.png")
                    pygame.display.set_icon(ufo)
                    # player
                    playerImg = pygame.image.load("Thor.png")
                    playerX = 370
                    playerY = 480
                    playerX_change = 0
                    playerY_change = 0
                    # enemy
                    enemyImg = []
                    enemyX = []
                    enemyY = []
                    enemyX_change = []
                    enemyY_change = []
                    num_of_enemies = 6

                    for i in range(num_of_enemies):
                        enemyImg.append(pygame.image.load("Ultron.png"))
                        enemyX.append(random.randint(0, 736))
                        enemyY.append(random.randint(50, 150))
                        enemyX_change.append(0.3)
                        enemyY_change.append(40)

                    # bullet
                    # Ready - You can't see the bullet on the screen
                    # Fire - The bullet is currently moving
                    bulletImg = pygame.image.load("hammer.png")
                    bulletX = 0
                    bulletY = 0
                    bulletX_change = 0
                    bulletY_change = 1
                    bullet_state = "ready"
                    # score
                    score_value = 0
                    font = pygame.font.Font("freesansbold.ttf", 32)
                    textX = 10
                    textY = 10

                    # Game Over text
                    over_font = pygame.font.Font("freesansbold.ttf", 64)


                    def player(x, y):
                        screen.blit(playerImg, (x, y))


                    def enemy(x, y, i):
                        screen.blit(enemyImg[i], (x, y))


                    def fire_bullet(x, y):
                        global bullet_state
                        bullet_state = "fire"
                        screen.blit(bulletImg, (x + 21, y - 21))


                    def isCollision(enemyX, enemyY, bulletX, bulletY):
                        distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
                        if distance < 27:
                            return True


                    def show_score(x, y):
                        score = font.render("Score : " + str(score_value), True, (255, 255, 255))  # RGB for white
                        screen.blit(score, (x, y))


                    def game_over_text():
                        f = over_font.render("GAME OVER", True, (255, 255, 255))  # RGB for white
                        screen.blit(f, (200, 250))

                    if space == True:
                        mixer.music.load("jojoth.wav")
                        mixer.music.play(-1)
                    while space:
                        # RGB - red, green , blue
                        # 0-255
                        screen.fill((0, 255, 255))
                        # background image
                        screen.blit(background, (0, 0))
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                running = False
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_q:
                                    space = False
                                    mixer.music.stop()
                                    mixer.music.load("squidgame.wav")
                                    mixer.music.play(-1)

                                if event.key == pygame.K_LEFT:
                                    playerX_change -= 0.3
                                if event.key == pygame.K_RIGHT:
                                    playerX_change += 0.3
                                if event.key == pygame.K_UP:
                                    playerY_change -= 0.3
                                if event.key == pygame.K_DOWN:
                                    playerY_change += 0.3
                                if event.key == pygame.K_SPACE:
                                    if bullet_state == "ready":
                                        bullet_Sound = mixer.Sound("laser.wav")
                                        bullet_Sound.play()
                                        bulletX = playerX
                                        bulletY = playerY
                                        fire_bullet(bulletX, bulletY)
                            if event.type == pygame.KEYUP:
                                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                                    playerX_change = 0
                                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                                    playerY_change = 0
                        # player movement
                        playerX += playerX_change
                        if playerX <= 0:
                            playerX = 0
                        if playerX >= 736:
                            playerX = 736
                        """
                        playerY += playerY_change
                        if playerY <=0:
                            playerY=0
                        elif playerY >=536:
                            playerY=536
                        """
                        player(playerX, playerY)
                        # enemy movement
                        for i in range(num_of_enemies):

                            if enemyY[i] >= 430:
                                for j in range(num_of_enemies):
                                    enemyY[j] = 2000
                                game_over_text()
                                break
                            enemyX[i] += enemyX_change[i]
                            # enemyY[i] += enemyY_change[i]
                            if enemyX[i] <= 0:
                                enemyX_change[i] = +0.3
                                enemyY[i] += enemyY_change[i]
                            elif enemyX[i] >= 736:
                                enemyX_change[i] = -0.3
                                enemyY[i] += enemyY_change[i]
                            if enemyY[i] >= 536:
                                enemyY[i] = random.randint(50, 150)
                            # Collision
                            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
                            if collision == True:
                                explosion_Sound = mixer.Sound("ora.wav")
                                explosion_Sound.play()
                                bulletY = playerY
                                bullet_state = "ready"
                                score_value += 1
                                # print(score)
                                enemyX[i] = random.randint(0, 736)
                                enemyY[i] = random.randint(50, 150)
                            enemy(enemyX[i], enemyY[i], i)
                        # bullet movement
                        if bulletY <= 0:
                            bulletY = playerY
                            bullet_state = "ready"
                        if bullet_state == "fire":
                            fire_bullet(bulletX, bulletY)
                            bulletY -= bulletY_change
                        show_score(textX, textY)
                        pygame.display.update()
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_4:
                        superman = True
                        mixer.music.stop()
                        mixer.music.load("Stamina Airborne OST.wav")
                        mixer.music.play(-1)
                        fps = 32
                        """screenwidth = 289
                        screenheight = 511"""
                        screenwidth = 800
                        screenheight = 600
                        screen = pygame.display.set_mode((screenwidth, screenheight))
                        groundy = screenheight * 0.8
                        g_sprites = {}
                        g_sound = {}
                        player = 'gallery/sprites/superman1.png'
                        background = 'metropolis.jpeg'
                        pipe = 'gallery/sprites/pipe.png'


                        def isCollide(playerx, playery, upperPipes, lowerPipes):
                            if playery > groundy - 25 or playery < 0:
                                g_sound['hit'].play()
                                return True
                            for pipe in upperPipes:
                                pipeHeight = g_sprites['pipe'][0].get_height()
                                if (playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < g_sprites['pipe'][
                                    0].get_width()):
                                    g_sound['hit'].play()
                                    return True
                            for pipe in lowerPipes:
                                if (playery + g_sprites['player'].get_height() > pipe['y']) and abs(
                                        playerx - pipe['x']) < g_sprites['pipe'][0].get_width():
                                    g_sound['hit'].play()
                                    return True
                            return False


                        def getRandomPipe():
                            pipeHeight = g_sprites['pipe'][0].get_height()
                            offset = screenheight / 3
                            y2 = offset + random.randrange(0, int(screenheight - g_sprites[
                                'base'].get_height() - 1.2 * offset))
                            pipeX = screenwidth + 10
                            y1 = pipeHeight - y2 + offset
                            pipe = [{'x': pipeX, 'y': -y1}, {'x': pipeX, 'y': y2}]
                            return pipe


                        pygame.init()
                        FPSCLOCK = pygame.time.Clock()
                        pygame.display.set_caption('Superman by Vintage Developpers')
                        g_sprites['numbers'] = (pygame.image.load('gallery/sprites/0.png').convert_alpha(),
                                                pygame.image.load('gallery/sprites/1.png').convert_alpha(),
                                                pygame.image.load('gallery/sprites/2.png').convert_alpha(),
                                                pygame.image.load('gallery/sprites/3.png').convert_alpha(),
                                                pygame.image.load('gallery/sprites/4.png').convert_alpha(),
                                                pygame.image.load('gallery/sprites/5.png').convert_alpha(),
                                                pygame.image.load('gallery/sprites/6.png').convert_alpha(),
                                                pygame.image.load('gallery/sprites/7.png').convert_alpha(),
                                                pygame.image.load('gallery/sprites/8.png').convert_alpha(),
                                                pygame.image.load('gallery/sprites/9.png').convert_alpha(),)
                        g_sprites['message'] = pygame.image.load('gallery/sprites/start3.png').convert_alpha()
                        g_sprites['base'] = pygame.image.load('gallery/sprites/base.png').convert_alpha()
                        g_sprites['pipe'] = (pygame.transform.rotate(pygame.image.load(pipe).convert_alpha(), 180),
                                             pygame.image.load(pipe).convert_alpha())
                        g_sound['die'] = pygame.mixer.Sound('gallery/audio/die.wav')
                        g_sound['hit'] = pygame.mixer.Sound('gallery/audio/hit.wav')
                        g_sound['point'] = pygame.mixer.Sound('gallery/audio/point.wav')
                        g_sound['swoosh'] = pygame.mixer.Sound('gallery/audio/swoosh.wav')
                        g_sound['wing'] = pygame.mixer.Sound('gallery/audio/wing.wav')
                        g_sprites['background'] = pygame.image.load(background).convert()
                        g_sprites['player'] = pygame.image.load(player).convert_alpha()
                        while superman:
                            playerx = int(screenwidth / 5)
                            playery = int((screenheight - g_sprites['player'].get_height()) / 2)
                            messagex = int((screenwidth - g_sprites['message'].get_width()) / 2)
                            messagey = int(screenheight * 0.13)
                            basex = 0
                            while superman:
                                for event in pygame.event.get():
                                    if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
                                        superman = False
                                        mixer.music.stop()
                                        mixer.music.load("squidgame.wav")
                                        mixer.music.play(-1)
                                    elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                                        score = 0
                                        playerx = int(screenwidth / 5)
                                        playery = int(screenwidth / 2)
                                        basex = 0
                                        newPipe1 = getRandomPipe()
                                        newPipe2 = getRandomPipe()
                                        upperPipes = [{'x': screenwidth + 200, 'y': newPipe1[0]['y']},
                                                      {'x': screenwidth + 200 + (screenwidth / 2),
                                                       'y': newPipe2[0]['y']}, ]
                                        lowerPipes = [{'x': screenwidth + 200, 'y': newPipe1[1]['y']},
                                                      {'x': screenwidth + 200 + (screenwidth / 2),
                                                       'y': newPipe2[1]['y']}, ]
                                        pipeVelX = -4
                                        playerVelY = -9
                                        playerMaxVelY = 10
                                        playerMinVelY = -8
                                        playerAccY = 1
                                        playerFlapAccv = -8
                                        playerFlapped = False

                                        while True:
                                            for event in pygame.event.get():
                                                if event.type == QUIT:
                                                    superman = False
                                                if event.type == KEYDOWN and (
                                                        event.key == K_SPACE or event.key == K_UP):
                                                    if playery > 0:
                                                        playerVelY = playerFlapAccv
                                                        playerFlapped = True
                                                        g_sound['wing'].play()
                                            crashTest = isCollide(playerx, playery, upperPipes, lowerPipes)
                                            if crashTest:
                                                break
                                            playerMidPos = playerx + g_sprites['player'].get_width() / 2
                                            for pipe in upperPipes:
                                                pipemidpos = pipe['x'] + g_sprites['pipe'][0].get_width() / 2
                                                if pipemidpos <= playerMidPos < pipemidpos + 4:
                                                    score += 1
                                                    print(f"Your score is {score}")
                                                    g_sound['point'].play()
                                            if playerVelY < playerMaxVelY and not playerFlapped:
                                                playerVelY += playerAccY
                                            if playerFlapped:
                                                playerFlapped = False
                                            playerHeight = g_sprites['player'].get_height()
                                            playery = playery + min(playerVelY, groundy - playery - playerHeight)
                                            for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
                                                upperPipe['x'] += pipeVelX
                                                lowerPipe['x'] += pipeVelX
                                            if 0 < upperPipes[0]['x'] < 5:
                                                newpipe = getRandomPipe()
                                                upperPipes.append(newpipe[0])
                                                lowerPipes.append(newpipe[1])
                                            if upperPipes[0]['x'] < -g_sprites['pipe'][0].get_width():
                                                upperPipes.pop(0)
                                                lowerPipes.pop(0)
                                            screen.blit(g_sprites['background'], (0, 0))
                                            for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
                                                screen.blit(g_sprites['pipe'][0], (upperPipe['x'], upperPipe['y']))
                                                screen.blit(g_sprites['pipe'][1], (lowerPipe['x'], lowerPipe['y']))
                                            screen.blit(g_sprites['base'], (basex, groundy))
                                            screen.blit(g_sprites['player'], (playerx, playery))
                                            myDigits = [int(x) for x in list(str(score))]
                                            width = 0
                                            for digit in myDigits:
                                                width += g_sprites['numbers'][digit].get_width()
                                            Xoffset = (screenwidth - width) / 2
                                            for digit in myDigits:
                                                screen.blit(g_sprites['numbers'][digit], (Xoffset, screenheight * 0.12))
                                                Xoffset += g_sprites['numbers'][digit].get_width()
                                            pygame.display.update()
                                            FPSCLOCK.tick(fps)
                                    else:
                                        screen.blit(g_sprites['background'], (0, 0))
                                        screen.blit(g_sprites['player'], (playerx, playery))
                                        screen.blit(g_sprites['message'], (messagex, messagey))
                                        screen.blit(g_sprites['base'], (basex, groundy))
                                        pygame.display.update()
                                        FPSCLOCK.tick(fps)
            if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_3:
                       DBZ = True
                       mixer.music.stop()
                       win = pygame.display.set_mode((800, 600))
                       pygame.display.set_caption("Battle of Saiyans : Goku v Vegeta")
                       # we add 3 elements in both of the lists below
                       ''' 0: large stride
                           1: small stride
                           2: jump'''
                       walkRight = [pygame.image.load('pics\\GokuR2x.png'), pygame.image.load('pics\\GokuR3x.png'),
                                    pygame.image.load('pics\\GokuR1x.png')]
                       walkLeft = [pygame.image.load('pics\\GokuL2x.png'), pygame.image.load('pics\\GokuL3x.png'),
                                   pygame.image.load('pics\\GokuL1x.png')]

                       bg = pygame.image.load('pics\\bodybg.jpg')
                       stan = pygame.image.load('pics\\GokuSx.png')

                       Gh = pygame.image.load('pics\\gh1-modified.png')
                       Vh = pygame.image.load('pics\\Vh.png')

                       bgm = pygame.mixer.music.load(
                           "pics\\Royal Blue (Vegeta's Limit Breaker Theme) - Dragon Ball Super (Extended Version).wav")
                       hitSound = pygame.mixer.Sound("pics\\kiblast.wav")
                       collisionSound = pygame.mixer.Sound("pics\\punch.wav")
                       pygame.mixer.music.play()
                       Clock = pygame.time.Clock()


                       class player():
                           def __init__(self, x, y, width, height):
                               self.x = x
                               self.y = y
                               self.width = width
                               self.height = height
                               self.speed = 10
                               self.isjump = False  # if it is in jumping
                               self.jumpheight = 10
                               self.left = False
                               self.right = False
                               self.walkCount = 0
                               self.standing = True
                               self.hitbox = (self.x + 10, self.y + 5, 80, 80)  # for collision purposes
                               self.health = 200  # player health

                           def draw(self, win):

                               if self.health > 0:

                                   if self.walkCount + 1 > 6:  # if we exceed 6 it will show length error
                                       self.walkCount = 0

                                   if not (self.standing):

                                       if self.left:  # run in left w/o jumping
                                           win.blit(walkLeft[self.walkCount // 2], (
                                               self.x,
                                               self.y))  # divide by 2 because we are flipping two images it would be //3 for 3 images
                                           self.walkCount += 1  # to flip the imgs

                                       elif self.right:  # run in right w/o jumping
                                           win.blit(walkRight[self.walkCount // 2], (self.x, self.y))
                                       self.walkCount += 1  # to flip the imgs

                                   else:
                                       if self.right:
                                           win.blit(pygame.image.load('pics\\GokuR1x.png'), (self.x, self.y))
                                       else:
                                           win.blit(pygame.image.load('pics\\GokuSx.png'), (self.x, self.y))

                                   self.hitbox = (self.x + 10, self.y + 5, 80, 80)
                                   Gbar2 = pygame.draw.rect(win, (255, 0, 0),
                                                            (80, 40, 210, 25))  # health bar background
                                   Gbar = pygame.draw.rect(win, (255, 255, 0), (80, 45, self.health, 15))  # health bar
                                   # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

                               else:
                                   # Remind me to add picture here
                                   # text = font.render('Vegeta Wins', True, (255, 255, 255), (255, 0, 0))
                                   win.blit(pygame.image.load('pics\\VegetaW.jpeg'), (200, 200))
                                   # win.blit(text, (100, 200))
                                   win.blit(pygame.image.load('pics\\GokuDx.png'), (self.x, self.y))

                           def hit(self):  # health decreasing logic
                               if self.health > 0:
                                   self.health -= 5
                                   # print("Goku Damage")
                               else:
                                   print("Goku Died")


                       class weapons():

                           def __init__(self, x, y, width, height, facing):
                               self.x = x
                               self.y = y
                               self.width = width
                               self.height = height
                               self.facing = facing
                               self.velocity = 8 * facing
                               self.hitbox = (self.x, self.y, 40, 40)

                           def draw(self, win):
                               win.blit(pygame.image.load('pics\\Daco_2529631.png'), (self.x, self.y))  # ki blast img
                               self.hitbox = (self.x, self.y, 40, 40)
                               # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


                       # vegeta class
                       class enemy():
                           # loading vegeta sprites
                           walkRightV = [pygame.image.load('pics\\VR2.png'), pygame.image.load('pics\\VR3.png'),
                                         pygame.image.load("pics\\VR1.png")]
                           walkLeftV = [pygame.image.load('pics\\VL2cs.png'), pygame.image.load('pics\\VL3cs.png'),
                                        pygame.image.load('pics\\VL1cs.png')]

                           def __init__(self, x, y, width, height,end):  # end is just to tell the enemy to flip after touching borders
                               self.x = x
                               self.y = y
                               self.width = width
                               self.height = height
                               self.end = end
                               self.path = [self.x, self.end]
                               self.speed = 8
                               self.walkCount = 0
                               self.hitbox = (self.x + 10, self.y + 5, 80, 80)
                               self.health = 200


                           def draw(self, win):
                               self.move()

                               if self.health > 0:

                                   if self.walkCount + 1 >= 6:
                                       self.walkCount = 0

                                   if self.speed > 0:
                                       win.blit(self.walkRightV[self.walkCount // 2], (
                                       self.x, self.y))  # self.walkCount is put in a list cuz we made it inside a class
                                       self.walkCount += 1

                                   else:
                                       win.blit(self.walkLeftV[self.walkCount // 2], (
                                       self.x, self.y))  # self.walkCount is put in a list cuz we made it inside a class
                                       self.walkCount += 1

                                   self.hitbox = (self.x + 10, self.y + 5, 80, 80)
                                   Vbar2 = pygame.draw.rect(win, (0, 0, 0), (550, 40, 210, 25))  # health bar background
                                   Vbar = pygame.draw.rect(win, (255, 255, 0),
                                                           (550, 45, -self.health, 15))  # health bar

                                   # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

                               else:
                                   self.speed = 0
                                   # text = font.render('Goku Wins',True,(0,0,255),(255,100,10))
                                   win.blit(pygame.image.load('pics\\GokuW.jpeg'), (200, 200))
                                   win.blit(pygame.image.load('pics\\vd1raw-removebg-preview.png'), (self.x, self.y))

                           # func for enemy movement
                           def move(self):

                               if self.speed > 0:

                                   if self.x + self.speed < self.path[1]:
                                       self.x += self.speed
                                   else:
                                       self.speed = self.speed * -1  # in pygame multiply by 1 and -1 means going in positive and negative direction respectively
                                       self.walkCount = 0

                               else:
                                   if self.x - self.speed > self.path[0]:
                                       self.x += self.speed

                                   else:
                                       self.speed = self.speed * -1
                                       self.walkCount = 0

                           def hit(self):  # collison/hit purposes
                               if self.health > 0:
                                   self.health -= 10

                               else:
                                   print('vegeta died ')
                               # print("Hit")  # so as to whenever goku n vegeta collide hit prints in our console
                            #RGB - red, green , blue


                       def Redrawgamewindow():
                           win.blit(bg, (0, 0))
                           goku.draw(win)
                           vegeta.draw(win)
                           win.blit(Gh, (10, 10))
                           win.blit(Vh, (490, 10))

                           for kiblast in kiblasts:
                               kiblast.draw(win)

                           pygame.display.update()  # update it shifted upwards to make the code cleaner


                       '''
                           global left
                           global right
                           global walkCount '''
                       # globalizing the variable to update the values in the whole program

                       font = pygame.font.SysFont('comicsans', 60, True)

                       goku = player(30, 400, 100, 100)
                       vegeta = enemy(120, 400, 100, 100, 700)
                       kiblasts = []
                       throwSpeed = 0

                       while DBZ:

                           ### FRAME RATE ###
                           Clock.tick(25)
                           #############

                           # putting limits in kiblast speeds
                           if throwSpeed > 0:
                               throwSpeed += 1
                           if throwSpeed > 3:
                               throwSpeed = 0

                           for event in pygame.event.get():
                               if event.type == pygame.QUIT:
                                   DBZ = False
                               if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_q:
                                        DBZ = False
                                        mixer.music.stop()
                                        mixer.music.load("squidgame.wav")
                                        mixer.music.play(-1)

                           if goku.health > 0 and vegeta.health > 0:
                               if goku.hitbox[1] < vegeta.hitbox[1] + vegeta.hitbox[3] and goku.hitbox[1] + goku.hitbox[
                                   3] > vegeta.hitbox[1]:
                                   if goku.hitbox[0] + goku.hitbox[2] > vegeta.hitbox[0] and goku.hitbox[0] < \
                                           vegeta.hitbox[0] + vegeta.hitbox[2]:
                                       goku.hit()
                                       collisionSound.play()

                           else:
                               if goku.health == 0:
                                   goku.speed = 0

                           # making boundaries for ki blast below
                           for kiblast in kiblasts:

                               if vegeta.health > 0:

                                   if kiblast.hitbox[1] + round(kiblast.hitbox[3] / 2) > vegeta.hitbox[1] and \
                                           kiblast.hitbox[1] + round(kiblast.hitbox[3] / 2) < vegeta.hitbox[1] + \
                                           vegeta.hitbox[3]:
                                       if kiblast.hitbox[0] + kiblast.hitbox[2] > vegeta.hitbox[0] and kiblast.hitbox[
                                           0] + kiblast.hitbox[2] < vegeta.hitbox[0] + vegeta.hitbox[2]:
                                           vegeta.hit()  # calling hit function
                                           hitSound.play()  # plays ki blast sound
                                           kiblasts.pop(kiblasts.index(kiblast))

                               else:
                                   vegeta.speed = 0  # when player dies(i.e. health turns to zero) his speed turns into zero and he stops moving

                               if kiblast.x < 699 and kiblast.x > 0:
                                   kiblast.x += kiblast.velocity

                               else:
                                   kiblasts.pop(kiblasts.index(kiblast))

                           ### KEYS ###
                           keys = pygame.key.get_pressed()
                           # the code after and" in the next two if conditions are used to create boundaries
                           # we use the object 'goku' instead of self because we cannot use self outside the class

                           ###SHOOTING###

                           if keys[pygame.K_SPACE] and throwSpeed == 0:
                               if goku.left == True:
                                   facing = -1

                               else:
                                   facing = 1

                               if len(kiblasts) < 5:
                                   kiblasts.append(weapons(round(goku.x + 10), round(goku.y + 30), 40, 40, facing))
                               throwSpeed = 1
                               # 'goku.width//2' is done so as to make the ki blast shoot from the centre of is body i.e. half of his body(//2)
                               # 40,40 is the dimensions of the ki blast

                           ### LEFT DIRECTION ###
                           if keys[pygame.K_LEFT] and goku.x > goku.speed:
                               """x > speed is a logic used to make boundary 
                               in the left side of the window """
                               goku.x -= goku.speed
                               goku.left = True
                               goku.right = False
                               goku.standing = False

                           ### RIGHT DIRECTION ###
                           elif keys[pygame.K_RIGHT] and goku.x < 690 - goku.width - goku.speed:
                               """To make the right most boundary i used  little
                                different logic because pygame marks the coordinate (0,0) 
                               from the top left of the window and so as to make the character stop at the boundary 
                               i had to subract it with width and then speed"""
                               goku.x += goku.speed
                               goku.left = False
                               goku.right = True
                               goku.standing = False

                           # For K_LEFT Left is true and right is false and vice versa for K_RIGHT

                           else:
                               goku.standing = True
                               '''
                               goku.left = False
                               goku.right = False
                               '''
                               goku.walkCount = 0
                           # this is done tp stop the legs during jump and also stop the legs when button is released
                           # same is done in the code down below

                           ####JUMP LOGIC ####
                           if goku.isjump == False:
                               if keys[pygame.K_UP]:
                                   goku.isjump = True
                                   goku.left = False
                                   goku.right = False
                                   goku.walkCount = 0  # this is done tp stop the legs during jump and also stop the legs when button is released

                           else:
                               if goku.jumpheight >= -10:
                                   neg = 1

                                   if goku.jumpheight < 0:
                                       neg = -1

                                   goku.y -= (goku.jumpheight ** 2) * 0.5 * neg  # eqn of y during free fall
                                   goku.jumpheight -= 1
                               else:
                                   goku.isjump = False
                                   goku.jumpheight = 10

                           # win.fill((0,0,0))
                           # we wont be needing winfill as we are adding a background image
                           # we will remove this rectangle because we dont need this as we are adding characters instead
                           # pygame.draw.rect(win,(255,255,255),(x,y,width,height))

                           Redrawgamewindow()
    #0-255
    screen.fill((0,255,255))
    screen.blit(b1,(0,0))
    pygame.display.update()

