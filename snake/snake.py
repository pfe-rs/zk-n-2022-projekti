import pygame, sys
import random
import time
time.time()
pygame.init()
green=(0,255,0)
WHITE=(255,255,255)
cells=20
celln=30
score=0
apple=pygame.image.load
dis=pygame.display.set_mode((cells*celln+cells,cells*celln+cells))
pygame.display.set_caption('zmijica')
clock = pygame.time.Clock()
SCREEN_UPDATE=pygame.USEREVENT
t1=300
pygame.time.set_timer(SCREEN_UPDATE,t1)
class food:
    def __init__(self):
        self.x=random.randint(0,celln-1)
        self.y=random.randint(0,celln-1)
    def draw_food(self):
        food_rect = pygame.Rect(int(cells*self.x), int(cells*self.y),cells,cells)
        pygame.draw.rect(dis, (178,34,34),food_rect)
        #pygame.draw.circle(dis, (0,30,255),(int((cells*self.x)),int((cells*self.y))),sells,0)
class zmija():
    def __init__(self):
        self.telox=[5,6,7]
        self.teloy=[10,10,10]
        self.pomerajx=0
        self.pomerajy=1
        self.duzina=3
    def draw_snake(self):
        br=0
        while br<self.duzina:
            if br==0:
                deo = pygame.Rect(int(cells*self.telox[br]), int(cells*self.teloy[br]),cells,cells)
                pygame.draw.rect(dis,(202,255,112),deo)#0,154,205
            if br!=0 and br%2==0:
                deo = pygame.Rect(int(cells*self.telox[br]), int(cells*self.teloy[br]),cells,cells)
                pygame.draw.rect(dis,(255,130,71),deo)#0,154,205
            if br!=0 and br%2==1:
                deo = pygame.Rect(int(cells*self.telox[br]), int(cells*self.teloy[br]),cells,cells)
                pygame.draw.rect(dis,(99,184,255),deo)#0,154,205
            br+=1
    def pomeranje(self):
        if (self.pomerajx!=0 or self.pomerajy!=0) and started:
            self.telox=self.telox[:-1]
            self.teloy=self.teloy[:-1]
            self.telox.insert(0,self.telox[0]+self.pomerajx)
            self.teloy.insert(0,self.teloy[0]+self.pomerajy)
            
BLACK=(0,0,0)
voce=food()
z=zmija()
game_over=False
prethodni=4
started=False
#levo 1
#desno 2
#gore 3
#dole4
while not game_over:

    for event in pygame.event.get():
        if score%5==0 and score>0:
            if t1>100:
                t1-=4
            pygame.time.set_timer(SCREEN_UPDATE,t1)
        print(event)   
        if event.type == pygame.WINDOWCLOSE or event.type == pygame.QUIT:
            pygame.quit()
        if event.type == SCREEN_UPDATE:
            z.pomeranje()
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_SPACE]:
            started=True
        if keys_pressed[pygame.K_RIGHT]:#zmija se pomera u desno za velicinu kvadratica u mrezi
            if prethodni!=2 and prethodni !=1:
                z.pomerajx=1
                z.pomerajy=0
                z.pomeranje()
                prethodni=2
        if keys_pressed[pygame.K_LEFT]:#zmija se pomera u levo za velicinu kvadratica u mrezi
            if prethodni !=1 and prethodni !=2:
                z.pomerajx=-1
                z.pomerajy=0
                z.pomeranje()
                prethodni=1
        if keys_pressed[pygame.K_UP]:#zmija ide gore
            if prethodni!=3 and prethodni !=4:
                z.pomerajx=0
                z.pomerajy=-1
                z.pomeranje()
                prethodni=3
        if keys_pressed[pygame.K_DOWN]:#zmija ide dole
            if prethodni!=4 and prethodni !=3:
                z.pomerajx=0
                z.pomerajy=1
                z.pomeranje()
                prethodni=4
        if z.telox[0]==voce.x and z.teloy[0]==voce.y:
            z.teloy.append(z.teloy[z.duzina-1]+cells)
            z.telox.append(z.telox[z.duzina-1]+cells)
            z.duzina+=1
            score+=1
            voce.x=random.randint(0,celln-1)
            voce.y=random.randint(0,celln-1)
        if z.telox[0]*cells<0:
            game_over=True
        if z.telox[0]*cells> 600:
            game_over=True
        if z.teloy[0]*cells<0:
            game_over=True
        if z.teloy[0]*cells> 600:
            game_over=True
        pom=z.duzina-1
        while pom>0:
            if z.telox[pom]==z.telox[0] and z.teloy[0]==z.teloy[pom]:
                game_over=True
            pom=pom-1
    
    dis.fill((61,145,64))
    voce.draw_food()
    z.draw_snake()
    font = pygame.font.Font('freesansbold.ttf', 50)
    font1=pygame.font.Font('freesansbold.ttf', 20)
    text = font1.render(f"Score: {score}", True, WHITE, BLACK)
    dis.blit(text, (5, 5))
    pygame.display.update()
while True:
    dis.fill(BLACK)
    text = font.render("GAME OVER", True, WHITE, BLACK)
    dis.blit(text, (170, 300))
    for event in pygame.event.get():
        print(event)   
        if event.type == pygame.WINDOWCLOSE or event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()