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
            if d>=self.r+other.r:
                ax=G*other.m*(other.x-self.x)/(d**3) #a=Fg/m
                self.vx+=ax*dt
                ay=G*other.m*(other.y-self.y)/(d**3) #a=Fg/m
                self.vy+=ay*dt
            #if d <= self.r+other.r #sudaraju se
                #tu neka fizika


pygame.init()
screen_w = 900
screen_h = 720
dis=pygame.display.set_mode((screen_w,screen_h))
pygame.display.update()
pygame.display.set_caption('problem n tela')
game_over=False

planets = []
N=10
t=0

BLACK = (0, 0, 0)
WHITE = (255,255,255)


def random_color():
    levels = range(32,256,32)
    return tuple(random.choice(levels) for _ in range(3))
m=0
for i in range(N):
    r=random.randint(5,30)
    planets.append(Planeta(random.randint(r,screen_w-r),random.randint(r,screen_h-r),r,random_color()))
    m+=4*(r**3)*3.14/3

font = pygame.font.Font('freesansbold.ttf', 20)

while not game_over:
    for event in pygame.event.get():
        #print(event)   
        if event.type == pygame.WINDOWCLOSE or event.type == pygame.QUIT:
            pygame.quit()
    mrx=0
    mry=0
    for i in planets:
        for j in planets:
            i.sila(j)
        i.x+=i.vx*dt
        i.y+=i.vy*dt
        mrx+=i.m*i.x
        mry+=i.m*i.y
        #if i.x>=screen_w-i.r or i.x<=i.r:
            #i.vx *= -0.9 #da ne bi pobegle iz ekrana
        #if i.y>=screen_h-i.r or i.y<i.r:
            #i.vy *= -0.9
    t+=dt

    
    text = font.render(f"t: {t}", True, WHITE, BLACK)
    dis.fill(BLACK)
    for planet in planets:
        planet.draw(dis)
    dis.blit(text, (screen_w - 100, 50))
    pygame.display.update()

while True:
    dis.fill(BLACK)
    dis.blit(text, (screen_w // 2 - 100, screen_h // 2))
    for event in pygame.event.get():
        print(event)   
        if event.type == pygame.WINDOWCLOSE or event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
