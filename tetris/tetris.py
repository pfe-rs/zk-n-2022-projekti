import pygame
import time
import random
pygame.init()
width = 10
height = 16
t = True
f = False
b_size = 50
OK = (220,85,57)
BLACK = (0, 0, 0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
#figura[rotacija][vertikalna kord][horizontalna kord]
# Indeksirano od 0
grid = [[f for i in range(0,20)] for j in range(0,20)]
square = [[[f,f,f,f],[f,t,t,f],[f,t,t,f],[f,f,f,f]],[[f,f,f,f],[f,t,t,f],[f,t,t,f],[f,f,f,f]],[[f,f,f,f],[f,t,t,f],[f,t,t,f],[f,f,f,f]],[[f,f,f,f],[f,t,t,f],[f,t,t,f],[f,f,f,f]]]
rectangle=[[[f,t,f,f],[f,t,f,f],[f,t,f,f],[f,t,f,f]],
[[f,f,f,f],[t,t,t,t],[f,f,f,f],[f,f,f,f]],
[[f,f,t,f],[f,f,t,f],[f,f,t,f],[f,f,t,f]],
[[f,f,f,f],[f,f,f,f],[t,t,t,t],[f,f,f,f]]]
Lshape=[[[f,f,f,f],[f,t,t,t],[f,t,f,f],[f,f,f,f]],
[[f,f,f,f],[f,t,t,f],[f,f,t,f],[f,f,t,f]],
[[f,f,f,f],[f,f,t,f],[t,t,t,f],[f,f,f,f]],
[[f,t,f,f],[f,t,f,f],[f,t,t,f],[f,f,f,f]]]
Z1=[[[f,f,f,f],[f,t,t,f],[f,f,t,t],[f,f,f,f]],
[[f,f,f,f],[f,f,t,f],[f,t,t,f],[f,t,f,f]],
[[f,f,f,f],[t,t,f,f],[f,t,t,f],[f,f,f,f]],
[[f,f,t,f],[f,t,t,f],[f,t,f,f],[f,f,f,f]]]
Z2=[[[f,f,f,f],[f,f,t,t],[f,t,t,f],[f,f,f,f]],
[[f,f,f,f],[f,t,f,f],[f,t,t,f],[f,f,t,f]],
[[f,f,f,f],[f,t,t,f],[t,t,f,f],[f,f,f,f]],
[[f,t,f,f],[f,t,t,f],[f,f,t,f],[f,f,f,f]]]
Tshape=[[[f,f,f,f],[f,t,f,f],[t,t,t,f],[f,f,f,f]],
[[f,t,f,f],[f,t,t,f],[f,t,f,f],[f,f,f,f]],
[[f,f,f,f],[f,t,t,t],[f,f,t,f],[f,f,f,f]],
[[f,f,f,f],[f,f,t,f],[f,t,t,f],[f,f,t,f]]]

typeList = [square,rectangle,Lshape,Z1,Z2,Tshape]
colorList = [WHITE, RED, GREEN , BLUE]
def placeable(x,y,tip,rot):
    for i in range(4):
        for j in range(4):
            if tip[rot][i][j]==f:
                continue
            if x+j<0:
                return False
            if y+i<0:
                return False
            if x+j>=width:
                return False
            if y+i>=height:
                return False
            if grid[y+i][x+j]==True:
                return False
    return True

class Block:
    def __init__(self,x,y,color,type,rotation):
        self.x = x
        self.y = y
        self.color = random.choice(colorList)
        self.type= type
        self.rotation = rotation
    
    def draw(self,surface):
        x=self.x
        y=self.y
        for i in range(4):
            for j in range(4):
                if self.type[self.rotation][i][j]:
                    pygame.draw.rect(surface, self.color, ((x+j)*b_size,(y+i)*b_size,b_size, b_size))
    def move(self, grid,r):
        if placeable(self.x+r,self.y,self.type,self.rotation):
            self.x +=r
    def drop(self, grid):
        if placeable(self.x,self.y+1,self.type,self.rotation):
            self.y += 1
    def rotate(self):
        if placeable(self.x,self.y,self.type,(self.rotation+1)%4):  
            self.rotation = (self.rotation+1)%4
def clearRow(y):
    global grid
    global score
    clear = t
    for jj in range(0,10):
        if not grid[y][jj]:
            clear = f
    if clear:
        for i in range(y,1,-1):
            for j in range(20):
                grid[i][j] = grid[i-1][j]
        score += 10
def appendToGrid(blok):
    global grid
    x = blok.x
    y = blok.y
    tip = blok.type
    for i in range(4):
        for j in range(4):
            if tip[blok.rotation][i][j]:
                grid[y+i][x+j] = t               
    
def drawGrid(grid,surface):
    for i in range(16):
        for j in range(10):
            if(grid[i][j]):
                pygame.draw.rect(surface,WHITE, (j*b_size,i*b_size,b_size,b_size))
    pygame.draw.rect(dis,OK,(500,0,400,800))
    pygame.draw.rect(dis,BLACK,(550,300,300,300))
dis=pygame.display.set_mode((900,800))
pygame.display.update()
pygame.display.set_caption('TETRIS')
gameOver = False
pocTip = random.choice(typeList)
kocka = Block(random.randrange(0,7),0,WHITE,pocTip,0) 
nextKocka = Block(12,7,WHITE,pocTip,0) 
kocka.draw(dis)
lastTick = 0
currTick = 0
dropTick = 0
score = 0
font = pygame.font.Font('freesansbold.ttf', 72)
text = font.render('Score:' + str(score), True, WHITE, BLACK)
pygame.draw.rect(dis,OK,(500,0,400,800))
clicked = f
dis.blit(text, ((550,50,300,100)))
pygame.display.update()
while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.WINDOWCLOSE or event.type == pygame.QUIT:
            pygame.quit()
    dropTick = time.time()
    if  dropTick - lastTick >=0.35 and not placeable(kocka.x, kocka.y+1,kocka.type, kocka.rotation):
        appendToGrid(kocka)
        clearRow(kocka.y)
        clearRow(kocka.y+1)
        clearRow(kocka.y+2)
        clearRow(kocka.y+3)
        pocTip = nextKocka.type
        kocka = Block(random.randrange(0,7),0,nextKocka.color,pocTip,0)
        nextKocka = Block(12,7,WHITE,random.choice(typeList),0) 
        if not placeable(kocka.x,kocka.y,kocka.type,kocka.rotation):
            gameOver=t
    dis.fill(BLACK)
    currTick = time.time()
    if currTick-lastTick>=0.35:
        kocka.drop(grid)
        lastTick = currTick

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_UP] and not clicked:
        clicked = t
        kocka.rotate()
    if keys_pressed[pygame.K_DOWN] and not clicked:
        clicked = t
        kocka.drop(grid)
    if keys_pressed[pygame.K_LEFT]and not clicked:
        clicked = t
        kocka.move(grid,-1)
    if keys_pressed[pygame.K_RIGHT]and not clicked:
        clicked = t
        kocka.move(grid,1)
    if not (keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_DOWN] ):
        clicked = f
    text = font.render("Score: " + str(score), True, WHITE, BLACK)
    dis.fill(BLACK)
    drawGrid(grid,dis)
    dis.blit(text, (550,50,300,100))
    kocka.draw(dis)
    nextKocka.draw(dis)
    pygame.display.update()
    print("Score" + str(score))