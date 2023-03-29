import pygame as pg 

pg.init()

fps = pg.time.Clock()
VINDU = pg.display.set_mode((800,800))
pg.display.set_caption("Pong")

svart = (0,0,0)
hvit = (255,255,255)

Spiller = pg.Rect(375,750,150,10)
Ball = pg.Rect(385,385,15,15)

spiller_poeng = 0 
spill_font = pg.font.Font("freesansbold.ttf",20)
pause_button = pg.image.load("pause.png")

Pause = pg.transform.scale(pause_button)

s = 7

ball_x = 5
ball_y = 5

def tegn():
    fps.tick(60)
    VINDU.fill(svart)
    pg.draw.rect(VINDU,hvit,Spiller)
    pg.draw.ellipse(VINDU,hvit,Ball)

def beveg():
    if keys[pg.K_RIGHT] or keys[pg.K_a]:
        Spiller.x += s
    if keys[pg.K_LEFT] or keys[pg.K_s]:
        Spiller.x -= s

def Spiller_grense():
    if Spiller.x >= 645:
        s = 0
        Spiller.x = 644
    if Spiller.x <= 5:
        s = 0
        Spiller.x = 6





while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        
    Ball.x += ball_x
    Ball.y += ball_y

    if Ball.top <= 0 or Ball.bottom >= 800: 
        ball_y *=-1
    if Ball.left <= 0 or Ball.left >= 800: 
        ball_x *=-1

    if Ball.colliderect(Spiller):
        ball_y *=-1
        s += 0.8

    keys = pg.key.get_pressed()

    tegn()
    beveg()
    Spiller_grense()

    pg.display.update()



