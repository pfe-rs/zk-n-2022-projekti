import pygame
import time
import random
import math
#import numpy as np

G=0.0667
dt=0.01 
class Planeta:
    def __init__(self,x,y,r,color):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.m = 4*(r**3)*3.14/3
        self.vx = 0
        self.vy = 0
    def draw(self,surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.r)
    def sila(self, other):
        if self!=other:
            d=math.sqrt((self.x-other.x)**2+(self.y-other.y)**2)
            if d>self.r+other.r:
                ax=G*other.m*(other.x-self.x)/(d**3) #a=Fg/m
                self.vx+=ax*dt
                ay=G*other.m*(other.y-self.y)/(d**3) #a=Fg/m
                self.vy+=ay*dt
            #else sudar

class ja:
    def __init__(self,x,y,r,color):
        self.x=x
        self.y=y
        self.r=r
        self.m=4*(r**3)*3.14/3
        self.color=color
        self.visible = True
    def draw(self,surface):
        if self.visible:
            pygame.draw.circle(surface, self.color, (self.x, self.y), self.r)
    def movex(self,dx):
        self.x+=dx
    def movey(self,dy):
        self.y+=dy
    def eat(self,other):
        self.m=self.m+other.m
        self.r=(3*self.m/(4*3.14))**(1./3)




pygame.init()
screen_w = 900
screen_h = 720
dis=pygame.display.set_mode((screen_w,screen_h))
pygame.display.update()
pygame.display.set_caption('agar.io')
game_over=False

BLACK = (0, 0, 0)
WHITE = (255,255,255)
RED = (255, 0, 0)
BLUE = (0,0,255)

r_igraca1 = 12
r_igraca2 = 12
player1=ja(r_igraca1*3,screen_h-r_igraca1*3,r_igraca1,RED)
player2=ja(screen_w-r_igraca2*3,screen_h-r_igraca2*3,r_igraca2,BLUE)
planets = []






def random_color():
    levels = range(32,256,32)
    return tuple(random.choice(levels) for _ in range(3))

for i in range(15):
    r=random.randint(7,11)
    planets.append(Planeta(random.randint(r,screen_w-r),random.randint(r,screen_h-r),r,random_color()))
for i in range(5):
    r=random.randint(11,21)
    planets.append(Planeta(random.randint(r,screen_w-r),random.randint(r,screen_h-r),r,random_color()))
for i in range(5):
    r=random.randint(21,29)
    planets.append(Planeta(random.randint(r,screen_w-r),random.randint(r,screen_h-r),r,random_color()))


font = pygame.font.Font('freesansbold.ttf', 20)

while not game_over:
    for event in pygame.event.get():
        #print(event)   
        if event.type == pygame.WINDOWCLOSE or event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_RIGHT]:
        player2.movex(2)
    if keys_pressed[pygame.K_LEFT]:
        player2.movex(-2)
    if keys_pressed[pygame.K_UP]:
        player2.movey(-2)
    if keys_pressed[pygame.K_DOWN]:
        player2.movey(2)  
    
    if keys_pressed[pygame.K_d]:
        player1.movex(2)
    if keys_pressed[pygame.K_a]:
        player1.movex(-2)
    if keys_pressed[pygame.K_w]:
        player1.movey(-2)
    if keys_pressed[pygame.K_s]:
        player1.movey(2)
    
    for i in planets:
        for j in planets:
            i.sila(j)
        i.x+=i.vx*dt
        i.y+=i.vy*dt
       
        if i.x>=screen_w-i.r or i.x<=i.r:
            i.vx *= -0.8 #da ne bi pobegle iz ekrana
        if i.y>=screen_h-i.r or i.y<i.r:
            i.vy *= -0.8

        if (i.x-player1.x)**2+(i.y-player1.y)**2 < (i.r+r_igraca1)**2:
            if i.r>r_igraca1:
                i.r=(i.r**3+r_igraca1**3)**(1./3)
                winner="blue"
                game_over=True
                player1.visible=False
            elif i.r<r_igraca1:
                player1.eat(i)
                r_igraca1=player1.r
                planets.remove(i)

        if (i.x-player2.x)**2+(i.y-player2.y)**2 < (i.r+r_igraca2)**2:
            if i.r>r_igraca2:
                i.r=(i.r**3+r_igraca2**3)**(1./3)
                winner="red"
                player2.visible=False
                game_over=True
            elif i.r<r_igraca2:
                player2.eat(i)
                r_igraca2=player2.r
                planets.remove(i)
    if((player1.x-player2.x)**2+(player1.y-player2.y)**2 < (player1.r+player2.r)**2):
        if(player1.r<player2.r):
            player2.eat(player1)
            winner="blue"
            player1.visible=False
            game_over=True
        if(player1.r>player2.r):
            player1.eat(player2)
            winner="red"
            player2.visible=False
            game_over=True

    
    dis.fill(BLACK)
    player1.draw(dis)
    player2.draw(dis)

    for i in planets:
        i.draw(dis)

    pygame.display.update()

while True:
    dis.fill(BLACK)
    s= winner + " player won!"
    text = font.render(s, True, WHITE, BLACK)
    dis.blit(text, (screen_w // 2 - 100, screen_h // 2))
    for event in pygame.event.get():
        print(event)   
        if event.type == pygame.WINDOWCLOSE or event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()