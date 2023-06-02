from pygame import *
from random import randrange

mixer.init()
mixer.music.load('backmusic.mp3')
mixer.music.play()
bite = mixer.Sound('bite87.ogg')

class GameSprite(sprite.Sprite):
    def __init__(self, picture, x, y, size_x, size_y, speed):
        super().__init__()
        self.image = transform.scale(
            image.load(picture),
            (size_x, size_y)
            )       
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def show(self): 
        window.blit(self.image,(self.rect.x,self.rect.y))

window = display.set_mode((1000,700))
background = transform.scale(
    image.load("background.png"),
    (1000,700)
)

RES = 700
SIZE = 50
x, y = 250, 250
apple = GameSprite('apple.png', randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE), 50, 50, None)
lenth = 1
score = 0
snake = [(x, y)]
dx, dy = 0, 0

font.init()
text = font.Font(None, 50).render('SCORE:', True, (189, 172, 19))

FPS = 8
clock = time.Clock()
gameon = True
finish = False

while gameon:
    for e in event.get():
        if e.type == QUIT:
            gameon = False

    if not finish:
        window.blit(background,(0,0))
        [draw.rect(window, Color('green'), (i, j, SIZE - 1, SIZE - 1)) for i, j in snake]
        apple.show()   
        #движение
        x += dx * SIZE
        y += dy * SIZE
        snake.append((x, y))
        snake = snake[-lenth:]
    
        #еда
        if snake[-1][0] < apple.rect.x + 50 and snake[-1][0] > apple.rect.x - 50 and snake[-1][1] < apple.rect.y + 50 and snake[-1][1] > apple.rect.y - 50:
            apple.rect.x = randrange(SIZE, RES - SIZE, SIZE)
            apple.rect.y = randrange(SIZE, RES - SIZE, SIZE)
            lenth += 1
            score += 1
            bite.play()

        #конец игры
        if x < 0 or x > 1000 or y < 0 or y > 650 or len(snake) != len(set(snake)):
            finish = True
            fin_text = font.Font(None, 100).render(('Столкновение! Счёт: ' + str(score)), True, (189, 172, 19))
            window.blit(fin_text, (100, 300))
            
        #управление
        keys = key.get_pressed()
        if keys[K_UP]:
            dx, dy = 0, -1
        elif keys[K_DOWN]:
            dx, dy = 0, 1
        elif keys[K_LEFT]:
            dx, dy = -1, 0
        elif keys[K_RIGHT]:
            dx, dy = 1, 0  

        window.blit(text, (20, 40))
        score_text = font.Font(None, 50).render(str(score), True, (189, 172, 19))
        window.blit(score_text, (170, 40))

        display.update()
        clock.tick(FPS)
        


