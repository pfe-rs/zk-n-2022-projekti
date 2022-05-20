import pygame
import time
import math
import random
pygame.init()
screen_w = 1920//2
screen_h = 1080//2
dis=pygame.display.set_mode((screen_w,screen_h))
pygame.display.set_caption('Igra')

gameover=False
srce = pygame.image.load("Srce.jpg")
srce = pygame.transform.scale(srce,(50,50))
srce.set_colorkey((255,255,255))
srce=srce.convert_alpha()
font = pygame.font.Font('freesansbold.ttf', 50)

crno = (0, 0, 0)
belo = (255, 255, 255)
crveno=(255,0,0)
plavo=(0,0,255)
turn =0
boja={}
igrac={}
zgrade={}
Nz=0
boja[0]=(255,0,0)
boja[1]=(0,0,255)
boja[2]=(200,0,0)
boja[3]=(200,200,0)
boja[4]=(0,200,0)
black=(0,0,0)
xl=10000
xr=0
class objekat:
    def __init__(self,x,w,h,hp):
        self.x=x
        self.w=w
        self.h=h
        self.hp=hp
    def draw(self,gde):
        if(self.hp<=0):
            return
        oboj=(0,0,0)
        if self.hp<4:
            oboj=boja[self.hp+1]
        pygame.draw.rect(gde,oboj,(self.x,gde.get_height()-99-self.h,self.w,self.h))
        

class plrc:
    def __init__(self,x,y,xs,ys,boja):
        self.hp=3
        self.x=x
        self.y=y
        self.xs=xs
        self.ys=ys
        self.boja=boja
        self.dx=0
        self.dy=0
        self.brzina=100
    def nacrtaj(self,gde):
        pygame.draw.rect(gde, self.boja, (self.x, self.y, self.xs, self.ys))
    def pomeri(self,ekran,dt):
        self.x+=self.dx*dt*self.brzina
        if(abs(self.x+self.xs-xl)<1):
            self.x=min(self.x,xl-self.xs)
        if(abs(self.x-xr)<1):
            self.x=max(xr,self.x)
        self.x=max(self.x,0)
        self.x=min(self.x,ekran.get_width()-self.xs)
    def tasteri(self,w,s,a,d):
        self.dx=0
        self.dx+=a*-1
        self.dx+=d*1
        self.dy=0
        self.dy+=w*-1
        self.dy+=s*1
def getspeedfromdist():
    basespeed=300
    lower_bound=100
    upper_bound=500
    cx,cy = pygame.mouse.get_pos()
    ix=igrac[turn].x+igrac[turn].xs//2
    iy=igrac[turn].y+igrac[turn].ys//2
    dist=math.sqrt((cx-ix)*(cx-ix)+(cy-iy)*(cy-iy))
   # print(dist,math.sqrt(dist))
    newspeed=math.sqrt(dist)/15*basespeed
    newspeed=min(newspeed,upper_bound)
    newspeed=max(newspeed,lower_bound)
    return newspeed
def nacrtajsve(gde):
    gde.fill((200,200,200))
    cx,cy = pygame.mouse.get_pos()
    ix=igrac[turn].x+igrac[turn].xs//2
    iy=igrac[turn].y+igrac[turn].ys//2
    for i in range(1,Nz+1):
        zgrade[i].draw(gde)
    pygame.draw.line(gde,boja[turn],(ix,iy),(cx,cy),round(getspeedfromdist()*0.01))
    pygame.draw.rect(gde,(0,100,0),(0,gde.get_height()-99,gde.get_width(),gde.get_height()))
    igrac[0].nacrtaj(gde)
    igrac[1].nacrtaj(gde)
    for i in range(igrac[0].hp):
        gde.blit(srce, (10+i*60,10))
    for i in range(igrac[1].hp):
        gde.blit(srce, (gde.get_width()-60-i*60,10))
def simuliraj(ekran,xp,yp,xd,yd):
    global gameover
    brzina=getspeedfromdist()
    g=200
    xv=brzina*xd/math.sqrt(xd*xd+yd*yd)
    yv=brzina*yd/math.sqrt(xd*xd+yd*yd)
    t=time.time()
    while yp<ekran.get_height()-99 and xp<ekran.get_width() and xp>=0 and yp>=0:
        for event in pygame.event.get():  
            if event.type == pygame.WINDOWCLOSE or event.type == pygame.QUIT:
                pygame.quit()
        dt=time.time()-t
        t=time.time()
        xp+=xv*dt
        yp+=yv*dt
        yv+=g*dt
        ox=max(igrac[turn^1].x, min(xp, igrac[turn^1].x + igrac[turn^1].xs))
        oy=max(igrac[turn^1].y, min(yp, igrac[turn^1].y + igrac[turn^1].ys))
        if((ox-xp)*(ox-xp)+(oy-yp)*(oy-yp)<=5):
            igrac[turn^1].hp-=1
            if igrac[turn^1].hp==0:
                gameover=True
                text = font.render("GAME OVER", True, boja[turn])
                nacrtajsve(ekran)
                ekran.blit(text, (screen_w // 2 -200, screen_h // 2 - 50))
                pygame.display.update()
                time.sleep(3)
            return
        for i in range(1,Nz+1):
            if(zgrade[i].hp<=0):
                continue
            ox=max(zgrade[i].x, min(xp, zgrade[i].x + zgrade[i].w))
            oy=max(ekran.get_height()-99-zgrade[i].h, min(yp, ekran.get_height()-99))
            if((ox-xp)*(ox-xp)+(oy-yp)*(oy-yp)<=5):
                zgrade[i].hp-=1
                global xl,xr
                xl=10000
                xr=0
                for i in range(1,Nz+1):
                    if(zgrade[i].hp==0):
                        continue
                    xl=min(xl,zgrade[i].x)
                    xr=max(xr,zgrade[i].x+zgrade[i].w)
                return
        nacrtajsve(ekran)
        pygame.draw.circle(ekran,boja[turn],(xp,yp),5)
        pygame.display.update()
    nacrtajsve(ekran)
    pygame.display.update()
def setup(gde):
    global Nz
    global gameover
    igrac[0]=plrc(30,screen_h-118,50,20,boja[0])
    igrac[1]=plrc(screen_w-80,screen_h-118,50,20,boja[1])
    dt=0
    pt=time.time()
    gameover=False
    Nz=0
    xo=100
    while True:
        if min(100,(screen_w-100)//2-10-xo)<15:
            break
        zgrada=objekat(xo,random.randint(15,min(100,(screen_w-100)//2-10-xo)),random.randint(10,200),random.randint(1,3))
        xo+=zgrada.w 
        xo+=random.randint(1,50)
        Nz+=1
        zgrade[Nz]=zgrada
        if xo>(screen_w-100)//2-10:
            break
    zgrada=objekat(screen_w//2-5,10,15,1e18)
    Nz+=1
    pok=Nz-1
    zgrade[Nz]=zgrada
    while pok>0:
        Nz+=1
        zgrade[Nz]=objekat(zgrade[pok].x,zgrade[pok].w,zgrade[pok].h,zgrade[pok].hp)
        zgrade[Nz].x=zgrade[pok].x+2*(screen_w//2-zgrade[pok].x)-zgrade[pok].w
        pok-=1
    global xl,xr
    xl=10000
    xr=0
    for i in range(1,Nz+1):
        if(zgrade[i].hp==0):
            continue
        xl=min(xl,zgrade[i].x)
        xr=max(xr,zgrade[i].x+zgrade[i].w)
    nacrtajsve(gde)
    
setup(dis)
pt=time.time()
turn = 0
while True:
    dt=time.time()-pt
    pt=time.time()
    for event in pygame.event.get():  
        if event.type == pygame.WINDOWCLOSE or event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONUP:
            cx,cy = pygame.mouse.get_pos()
            simuliraj(dis,igrac[turn].x+igrac[turn].xs//2,igrac[turn].y+igrac[turn].ys//2,cx-(igrac[turn].x+igrac[turn].xs//2),cy-(igrac[turn].y+igrac[turn].ys//2))
            turn^=1
            dt=0
            pt=time.time()
    if gameover==True:
        setup(dis)
        continue
    nacrtajsve(dis)
    pygame.display.update()
    keys_pressed = pygame.key.get_pressed()
    igrac[turn].tasteri( keys_pressed[pygame.K_UP], keys_pressed[pygame.K_DOWN], keys_pressed[pygame.K_LEFT], keys_pressed[pygame.K_RIGHT])
    igrac[turn].pomeri(dis,dt)