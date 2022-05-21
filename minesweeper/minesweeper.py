import sys
import pygame
import random
import time
game_over = False
otvoreni = 0
win = False

class Polje:
    otvoreno = False
    vrednost = 0
    mina = False
    obelezeno = False

    def Otvori(self, klik):
        global game_over
        global otvoreni
        global win

        if(klik==0):
            if(self.mina):
                game_over=True
            elif(not self.otvoreno):
                self.otvoreno = True
                otvoreni +=1
        elif(klik==1):
            if(not self.otvoreno):
                self.obelezeno = not self.obelezeno 


pygame.init()

blockSize = 50
dimenzija = 9
screen_d = blockSize*dimenzija
brojMina = 10
dis=pygame.display.set_mode((screen_d,screen_d))
pygame.display.update()
pygame.display.set_caption('Minotragac')

font2 = pygame.font.SysFont("Segoe UI", 40)
font = pygame.font.Font('freesansbold.ttf', 20)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
OZNAKA = (168, 224, 227)
IVICA = (214, 200, 219)
NEOTVORENO = (195, 163, 209)
x = 50
y = 50
rect = pygame.Rect(x, y, blockSize, blockSize)
pygame.draw.rect(dis, WHITE, rect, 1)

matrica = [[Polje() for x in range(dimenzija)]for y in range(dimenzija)]


def OtvoriNulu(x, y):
    global otvoreni
    if(not matrica[x][y].otvoreno):
        matrica[x][y].otvoreno = True
        otvoreni+=1
    for i in range(x-1, x+2):
        if (i >= 0 and i < dimenzija):
            if (y-1 >= 0 ):
                if(not matrica[i][y-1].otvoreno):
                    OtvoriPolje(0, i, y-1)
            if (y+1 < dimenzija ):
                if( not matrica[i][y+1].otvoreno):
                    OtvoriPolje(0, i, y+1)
    if (x-1 >= 0):
        if(not matrica[x-1][y]):
            OtvoriPolje(0, x-1, y)

    if (x+1 < dimenzija ): 
        if(not matrica[x+1][y]):
            OtvoriPolje(0, x+1, y)
   
 


def drawGrid():
    for x in range(0, screen_d, blockSize):
        for y in range(0, screen_d, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            if (matrica[x//blockSize][y//blockSize].otvoreno): #ako je polje otvoreno
                pygame.draw.rect(dis, WHITE, rect)
                if(not matrica[x//blockSize][y//blockSize].vrednost == 0): #ako je nula
                    text = font.render(str(matrica[x//blockSize][y//blockSize].vrednost), True, BLACK, WHITE)
                    dis.blit(text, (x+blockSize/2-5, y+blockSize/2-5))
            elif (matrica[x//blockSize][y//blockSize].obelezeno): #u suprotnom ako je obelezeno
                    pygame.draw.rect(dis, OZNAKA, rect) #crveno
            else:
                pygame.draw.rect(dis, NEOTVORENO, rect)
            pygame.draw.rect(dis, IVICA, rect, 1)
            

def OtvoriPolje(klik, x, y):
    if(matrica[x][y].vrednost==0 and klik==0):
        OtvoriNulu(x,y)
    else:
        matrica[x][y].Otvori(klik)
    

for f in range(brojMina):

    x = random.randint(0, dimenzija-1)
    y = random.randint(0, dimenzija-1)

    if (not matrica[x][y].mina):
        matrica[x][y].mina = True
        matrica[x][y].vrednost = -1
        for i in range(x-1, x+2):
            if (i >= 0 and i < dimenzija):
                if (y-1 >= 0 and not matrica[i][y-1].mina):
                    matrica[i][y-1].vrednost += 1
                if (y+1 < dimenzija and not matrica[i][y+1].mina):
                    matrica[i][y+1].vrednost += 1
        if (x-1 >= 0 and not matrica[x-1][y].mina):
            matrica[x-1][y].vrednost += 1
        if (x+1 < dimenzija and not matrica[x+1][y].mina):
            matrica[x+1][y].vrednost += 1   

trenutnoVreme = time.time()

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.WINDOWCLOSE or event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if(not game_over):
        drawGrid()

    if(time.time()- trenutnoVreme > 0.1):
        if (pygame.mouse.get_pressed()[0]):
            x, y = pygame.mouse.get_pos()
            OtvoriPolje(0, x//blockSize, y//blockSize)
        trenutnoVreme = time.time()

    if (pygame.mouse.get_pressed()[2]):
        x, y = pygame.mouse.get_pos()
        OtvoriPolje(1, x//blockSize, y//blockSize)
    
    if(otvoreni==(dimenzija*dimenzija)-brojMina):
        dis.fill(BLACK)
        text = font2.render("BRAVO!!!", True, WHITE, BLACK)
        dis.blit(text, (screen_d / 2 -70, screen_d / 2-70))
        win = True

    pygame.display.update()    


while True:

    if(game_over):
        if(not win):
            dis.fill(BLACK)
            text = font2.render("UZASS!!!", True, WHITE, BLACK)
            dis.blit(text, (screen_d / 2-70 , screen_d / 2-70))

        
    for event in pygame.event.get():
        if event.type == pygame.WINDOWCLOSE or event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    pygame.display.update()