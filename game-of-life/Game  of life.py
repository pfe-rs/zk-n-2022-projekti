import time
from random import randint

import pygame_textinput
import pygame
pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
GRAY = (100,100,100)
n = 1000
# Create TextInput-object
textinput = pygame_textinput.TextInputVisualizer(None,None,None,WHITE,300,3,WHITE)





players = [[randint(0,4)//4%2 for y in range(n)]   for x in range(n)]
screen = pygame.display.set_mode((740,740))


color_light = (170,170,170)
color_dark = (100,100,100)
width = 740
height = 740
smallfont = pygame.font.SysFont('Corbel',35)
text = smallfont.render('random',True , WHITE)
text1 = smallfont.render('choose',True, WHITE)
ntext = smallfont.render('n:',True, WHITE)
Izabran = False
Izaberi = False
clock = pygame.time.Clock()
textRect = pygame.Rect(100,100,160,60)
time_before = time.time()
while not Izabran and  not Izaberi:
	events = pygame.event.get()
	screen.fill(BLACK)
	textinput.update(events)
	screen.blit(textinput.surface, (10, 100))
	screen.blit(ntext,(10,60))
	for ev in events:
		if ev.type == pygame.QUIT:
			pygame.quit()
		if ev.type == pygame.MOUSEBUTTONDOWN:
			if width/2 <= mouse[0] <= width/2+140 and height/2-20 <= mouse[1] <= height/2-20+40:
				Izabran = True
				if textinput._manager.value.isdigit():
					n = int(textinput._manager.value)
				else:
					n = 40
			if width/2 >= mouse[0] >= width/2-140 and height/2-20 <= mouse[1] <= height/2-20+40:
				Izaberi = True
				if textinput._manager.value.isdigit():
					n = int(textinput._manager.value)
				else:
					n = 40
	mouse = pygame.mouse.get_pos()
	if width/2 <= mouse[0] <= width/2+140 and height/2-20 <= mouse[1] <= height/2-20+40:
		pygame.draw.rect(screen,color_light,[width/2,height/2-20,140,40])
	else:
		pygame.draw.rect(screen,color_dark,[width/2,height/2-20,140,40])
	screen.blit(text , (width/2+25,height/2-10))
	if width/2 >= mouse[0] >= width/2-140 and height/2-20 <= mouse[1] <= height/2+20:
		pygame.draw.rect(screen,color_light,[width/2-140,height/2-20,140,40])
	else:
		pygame.draw.rect(screen,color_dark,[width/2-140,height/2-20,140,40])
	screen.blit(text1 , (width/2-100,height/2-10))
	pygame.display.update()
	clock.tick(30)
def cellInfo(it,jt):
    br = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if(not (i==0 and  j== 0)):
                a = i + it
                b = j + jt
                if(b == -1):
                    b = n-1
                if b == n:
                    b = 0
                if(a == -1):
                    a = n-1
                if a == n:
                    a = 0
                if players[a][b] == 1:
                    br = br+1
    return br
def cellUpdate(i,j):
    l = array[i][j]
    if(players[i][j] == 1):
        if not(l>1 and l<4):
            players[i][j] = 0
    else:
        if(l==3):
            players[i][j] = 1
array = [[0 for y in range(n)]   for x in range(n)]
def updateTable():
    for i in range(n):
        for j in range(n):
            array[i][j] = cellInfo(i,j)
    for i in range(n):
        for j in range(n):
            cellUpdate(i,j)

def drawTable():
    for i in range(n):
        for j in range(n):
            if(players[i][j] == 1):
                pygame.draw.rect(screen,WHITE,pygame.Rect(width//n*i,width//n*j,width//n,width//n))
            else:
                pygame.draw.line(screen,GRAY,(width//n*i,0),(width//n*i,width))
                pygame.draw.line(screen,GRAY,(0,width//n*j),(width,width//n*j))
if Izaberi:
    for i in range(0,n):
        for j in range(0,n):
            players[i][j] = 0
while Izaberi:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            x  = mouse_pos[0]//(width//n)
            y = mouse_pos[1]//(width//n)
            if(players[x][y]):
                players[x][y] = 0
            else:
                players[x][y] = 1
    drawTable()
    keyPressed = pygame.key.get_pressed();
    if keyPressed[pygame.K_SPACE]:
        Izaberi = False
    pygame.display.update()
while True:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    drawTable()
    updateTable()
    pygame.display.update()

