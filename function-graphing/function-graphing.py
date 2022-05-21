import pygame
import time
import random

screen_w = 1000
screen_h = 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY =  (192, 192, 192)
LIGHT_GRAY = (240, 240, 240)
RED = (255, 0, 0)
color = [(255, 0, 0),(0, 255, 0),(0, 0, 255),(255, 255, 0),(255, 0, 255),(0, 255, 255)]
BACKGROUND_COLOR = WHITE
XS = -10
XE = 10
YS = -8
YE = 8
Xs = XS
Xe = XE
Ys = YS
Ye = YE
BRx = 10
BRy = 8
ofsetx = 0
ofsety = 0
mistake = 0.04
mistake2 = 0.01
lk = []
le = []
lofset = []
lx = []
ly = []
llk = []
lle = []
pygame.init()
dis=pygame.display.set_mode((screen_w,screen_h))
pygame.display.update()
pygame.display.set_caption("GeoGebra2")
def input_and_calculate(lk, le):
    lk = [] 
    le = []
    polinom = input("unesi funkciju: ")
    polinom = "+"+polinom+"+"
    polinom = polinom.replace("=","")
    polinom = polinom.replace("y","")
    polinom = polinom.replace(" ","")
    polinom = polinom.replace("x","x^")
    polinom = polinom.replace("^^","^")
    polinom = polinom.replace("^+","^1+")
    polinom = polinom.replace("^-","^1-")
    polinom = polinom.replace("+x","+1x")
    polinom = polinom.replace("-x","-1x")
    ok = False
    br=0
    minus = False
    for i in range(len(polinom)):
        if polinom[i]>='0' and polinom[i]<='9':
            br=br*10+int(polinom[i])
        if polinom[i]=='^':
            if minus:
                br=-br
            lk.append(br)
            br=0
            ok=True
        if polinom[i]=='-' or polinom[i]=='+':
            if ok:
                le.append(br)
            else:
                if minus:
                    br=-br
                lk.append(br)
                le.append(0)
            br=0
            ok=False
        if polinom[i]=='-':
            minus = True
        if polinom[i]=='+':
            minus = False
    return lk, le
def make_ofsets(lofset):
    lofset = []
    ofset = 0.0000000001
    for i in range(100):
        lofset.append(ofset*1)
        lofset.append(ofset*2)
        lofset.append(ofset*5)
        ofset *= 10
    return lofset 
def moving_in_graph(Xs, Xe, Ys, Ye):
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_RIGHT]:
        dx= (Xe-Xs)*0.005
        Xe += dx
        Xs += dx
    if keys_pressed[pygame.K_LEFT]:
        dx= (Xe-Xs)*0.005
        Xe -= dx
        Xs -= dx
    if keys_pressed[pygame.K_UP]:
        dy= (Ye-Ys)*0.005
        Ye += dy
        Ys += dy
    if keys_pressed[pygame.K_DOWN]:
        dy= (Ye-Ys)*0.005
        Ye -= dy
        Ys -= dy
    if keys_pressed[pygame.K_1]:
        dx= (Xe-Xs)*0.005
        Xe -= dx
        Xs += dx
    if keys_pressed[pygame.K_2]:
        dx= (Xe-Xs)*0.005
        Xe += dx
        Xs -= dx
    if keys_pressed[pygame.K_3]:
        dy= (Ye-Ys)*0.005
        Ye -= dy
        Ys += dy
    if keys_pressed[pygame.K_4]:
        dy= (Ye-Ys)*0.005
        Ye += dy
        Ys -= dy
    if keys_pressed[pygame.K_5]:
        Xs = XS
        Xe = XE
        Ys = YS
        Ye = YE
    return Xs, Xe, Ys, Ye
def close_query():
    for event in pygame.event.get(): 
        if event.type == pygame.WINDOWCLOSE or event.type == pygame.QUIT:
            pygame.quit()
def draw_main_lines():
    if Ys<=0 and Ye>=0:
        py = round(screen_h-((0-Ys)*screen_h)/(Ye-Ys))
        pygame.draw.line(dis, BLACK, (0, py),(screen_w, py), 1) 
    if Xs<=0 and Xe>=0:
        px = round((0-Xs)*screen_w/(Xe-Xs))
        pygame.draw.line(dis, BLACK, (px, 0),(px, screen_h), 1)    
def draw_small_lines():
    for px in range(screen_w):
        x = Xs+(px*(Xe-Xs))/screen_w
        if abs(round(x/ofsetx*5)-x/ofsetx*5) < mistake:
            pygame.draw.line(dis, LIGHT_GRAY, (px, 0),(px, screen_h), 1)
        px += 15
    for py in range(screen_h):
        y = Ys+(py*(Ye-Ys))/screen_h
        if abs(round(y/ofsety*5)-y/ofsety*5) < mistake:
            pygame.draw.line(dis, LIGHT_GRAY, (0, screen_h-py),(screen_w, screen_h-py), 1)
        py += 15
def convert_to_str(d, ofset):
    return str(round(round(d/ofset)*ofset,5))
def draw_other_lines():
    pygame.font.init()
    my_font = pygame.font.SysFont(None, 30, False)
    for px in range(screen_w):
        x = Xs+(px*(Xe-Xs))/screen_w
        if abs(round(x/ofsetx)-x/ofsetx) < mistake2:
            pygame.draw.line(dis, GRAY, (px, 0),(px, screen_h), 1)
            text_surface = my_font.render(convert_to_str(x, ofsetx), False, BLACK)
            if px <= 50:
                continue
            dis.blit(text_surface, (px,screen_h-20))
    for py in range(screen_h):
        y = Ys+(py*(Ye-Ys))/screen_h
        if abs(round(y/ofsety)-y/ofsety) < mistake2:
            pygame.draw.line(dis, GRAY, (0, screen_h-py),(screen_w, screen_h-py), 1)
            if py <= 50:
                continue
            text_surface = my_font.render(convert_to_str(y, ofsety), False, BLACK)
            dis.blit(text_surface, (0,screen_h-py))
def draw_on_graph(id, lx, ly, Xs, Xe, Ys, Ye):
    pygame.font.init()
    my_font = pygame.font.SysFont("Normal", 50, False)
    text_surface = my_font.render("AGeometry", False, BLACK)
    dis.blit(text_surface, (screen_w-200,0))
    for i in range(1,len(lx)):
        if((ly[i]>=0 and ly[i]<=screen_h) or (ly[i-1]>=0 and ly[i-1]<=screen_h)):
            pygame.draw.line(dis, color[id], (lx[i], ly[i]),(lx[i-1], ly[i-1]), 2)
def best_ofset(S, E, BR):
    mind = 1000000000
    ofset = 0
    for i in range(len(lofset)):
        if(abs((E-S)-(lofset[i]*BR))<mind):
            ofset = lofset[i]
            mind = abs((E-S)-(lofset[i]*BR))
    return ofset
def find_points(lx, ly, lk, le):
    lx = []
    ly = []
    for px in range(screen_w):
        x = Xs+(px*(Xe-Xs))/screen_w
        y = 0
        for i in range(len(lk)):
            y+=lk[i]*(x**le[i])
        py = screen_h-int((y-Ys)*screen_h)//(Ye-Ys)
        lx.append(px)
        ly.append(py)
    return lx, ly
lofset = make_ofsets(lofset)
n = int(input("unesi broj funkcija: "))
for i in range(n):
    lk, le = input_and_calculate(lk, le)
    llk.append(lk)
    lle.append(le)
while True:
    close_query()
    ofsetx = best_ofset(Xs, Xe, BRx)
    ofsety = best_ofset(Ys, Ye, BRy)
    dis.fill(BACKGROUND_COLOR)
    draw_small_lines()
    draw_other_lines()
    draw_main_lines()
    for i in range(n):
        lx, ly = find_points(lx, ly, llk[i], lle[i])
        draw_on_graph(i, lx, ly, Xs, Xe, Ys, Ye)
    Xs, Xe, Ys, Ye = moving_in_graph(Xs, Xe, Ys, Ye)
    pygame.display.update()
