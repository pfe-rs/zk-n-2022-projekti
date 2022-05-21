import pygame
import math
import time
from random import randint

pygame.font.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (255,165,0)
YELLOW = (255,255,0)
GREEN = (124,252,0)
BLUE = (0, 0, 255)
PURPLE = (230,230,250)
PINK = (255,192,203)
colors = [RED,ORANGE, YELLOW, GREEN, BLUE, PURPLE, PINK]
BAZEN = (152,251,152)


class Player:
    def __init__(self, color,x, y ,r,Vx,Vy):
        self.color = color
        self.r = r
        self.x = x
        self.y = y
        self.Vx = Vx
        self.Vy = Vy
    def draw(self, surface, x, y):
        pygame.draw.circle(surface, PINK, (self.x, self.y), self.r)
    def Velocity(self):
        x, y = pygame.mouse.get_pos()
        self.Vx = (self.x - x)/75
        self.Vy = (self.y - y)/75
    def BounceX(self):
        self.Vx = -self.Vx * 0.8
    def BounceY(self):
        self.Vy = - self.Vy * 0.8

    def ColX(self, lastBounceX):
        if(int(self.x)-self.r>=screen_w//2 and int(self.x) + self.r <= screen_w//2+400 and screen_h//2+300<=int(self.y)+self.r and screen_h//2+320>=int(self.y)+self.r):
            tr = time.time()
            if(float(tr)-float(lastBounceX)>0.2):
                self.BounceY()
                return tr
            else:
                return lastBounceX
        else:
            return lastBounceX

    def ColY(self, lastBouncey):
        if(screen_h//2+300>=int(self.y) and int(self.y)>=screen_h//2):
            if( self.x+self.r>= screen_w//2 and self.x-self.r<= screen_w//2+20) or (( self.x+self.r>= screen_w//2+380 and self.x-self.r<= screen_w//2+400)):
                tr = time.time()
                if float(tr)-float(lastBouncey)>0.2:
                    self.BounceX()
                    return tr
                else:
                    return lastBounceY
            else:
                return lastBounceY
        else:
            return lastBounceY

    def outOfDis(self):
        return (0>=int(self.x)or int(self.x)>= screen_w or 0>=int(self.y) or int(self.y)>= screen_h)

class Ball:
    def __init__(self, x, y, color, r):
        self.x = x
        self.y = y
        self.color = color
        self.r = r
    def drawBall(self):
        pygame.draw.circle(dis, self.color, (self.x, self.y), self.r)

    def disappear(self, bals):
        bals.remove(self)
    def isDenied(self,  bals):
        a = abs(self.x-player.x)
        b = abs(self.y-player.y)
        c=math.sqrt(a**2+b**2)
        if c<=player.r + self.r:
            self.disappear(bals)

def drawLine():
    x, y = pygame.mouse.get_pos()
    line = [(player.x, player.y), (x, y)]
    a = player.x-x
    b= player.y-y
    c = math.sqrt(a**2 + b**2)
    if(c<110):
        clr=GREEN
    elif(c<170):
        clr = YELLOW
    else:
        clr = RED
    pygame.draw.line(dis, clr, line[0], line[1], 5)
    t = c//3 
    pygame.draw.circle(dis, (200, 200, 200), (player.x + t, player.y +(-1)*t), 15)
    pygame.draw.circle(dis, (150, 150, 150), (player.x + 2*t, player.y+ (-2)*t), 13)
    pygame.draw.circle(dis, (100, 100, 100), (player.x +3*t, player.y +(-3)*t), 10)


game_over = False



def gameOver(): 
    font = pygame.font.SysFont('Corbel',70)
    text = font.render('GAME OVER', True, GREEN)
    dis.blit(text, (100, 100))
    for event in pygame.event.get():
            if event.type == pygame.WINDOWCLOSE or event.type == pygame.QUIT:
                pygame.quit()

game_over = True

def Win():
    font = pygame.font.SysFont('Corbel',70)
    text = font.render('WIN', True, GREEN)
    dis.blit(text, (100, 100))
    for event in pygame.event.get():
            if event.type == pygame.WINDOWCLOSE or event.type == pygame.QUIT:
                pygame.quit()



balls = []
screen_h = 800
screen_w = 900
dis = pygame.display.set_mode((screen_w, screen_h))
player = Player(PINK, screen_w//2-300,screen_h//2+100, 20,0,0)
lastBounceX = 0.0
lastBounceY = 0.0

lineExist = False
Collisioned = False
isIn = True
Winn = False
game_over = False


def spawn():
    under = [randint(1, 4), randint(1, 4), randint(1, 4), randint(1, 4),randint(1, 4),randint(1, 4)]
    s=0;
    
    for i in range(6):
        for j in range(under[i]):
            balls.append(Ball(screen_h//2 +370- i*60+30,screen_w//2 + 250 -j*60-30,colors[randint(0,6)], 30))
            
spawn()
c = 0

while not game_over and not Winn:
    if player.outOfDis():
        game_over = True
    if(len(balls)==0):
        Winn=True
    
    if isIn:
        dis.fill(BLACK)
        pygame.draw.rect(dis, BAZEN, (screen_w//2 , screen_h//2 +300, 400, 20))
        pygame.draw.rect(dis, BAZEN, (screen_w//2 , screen_h//2 , 20, 300))
        pygame.draw.rect(dis, BAZEN, (screen_w//2 +380, screen_h//2 , 20, 300))

        for event in pygame.event.get():
            if event.type == pygame.WINDOWCLOSE or event.type == pygame.QUIT:
                pygame.quit()

        if pygame.mouse.get_pressed()[0]:
            drawLine()
            lineExist = True
        elif lineExist: 
            lineExist = False
            player.Velocity()
        if(not player.Vx == 0):
            player.Vy = player.Vy +0.005

        
        

        lastBounceX = player.ColX(lastBounceX)
        lastBounceY = player.ColY(lastBounceY)

        for i in balls:
            i.drawBall()
            i.isDenied( balls)

        player.x = player.x + player.Vx
        player.y = player.y + player.Vy


        player.draw(dis, player.x, player.y)
        pygame.display.update()
    
while game_over:
    gameOver()
    pygame.display.update()
    player.x = player.x + player.Vx
    player.y = player.y + player.Vy

while Winn:
    Win()
    player.x = player.x + player.Vx
    player.y = player.y + player.Vy
    pygame.display.update()