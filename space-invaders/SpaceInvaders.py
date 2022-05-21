import pygame
from sys import exit
from random import seed
from random import randint

WHITE = (255,255,255)
seed(1)

###Funkcija koja se zove na kraju igre:
###text - Poruka koja se ispisuje igracu
def game_over(surface, text):
    surface.fill(WHITE)
    font = pygame.font.SysFont("Liberation Serif", 30)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_ESCAPE]:
            exit()
        
        ispis = font.render('Kraj igre! Pritisnite ESCAPE za izlazak', False, (0, 0, 0))
        dis.blit(ispis, (screen_w // 2 - 200, screen_h // 2))
        ispis = font.render(text, False, (0,0,0))
        dis.blit(ispis, (screen_w // 2 - 200, screen_h // 2 + 50))
        pygame.display.flip()

###Klasa Projektil:
##Clan klase Igrac
class Projektil:
    def __init__(self, x, y, color, Igrac, direction):
        self.x = x
        self.y = y
        self.color = color
        self.parent = Igrac
        self.direction = direction

    ###Funkcija za ispis projektila na ekranu
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, 2, 2))
    ###Funkcija za pomeranje projektila za a mesta na dole/gore. Return vrednost True/False - da li je projektil izasao sa ekrana
    def move(self, a):
        self.y += a
        if self.y > screen_h or self.y < 0:
            return False
        return True
    ###Da li su se ovaj projektil i dati Igrac sudarili (True/False)
    def collide(self, Igrac):
        if self.x >= Igrac.x and self.x <= (Igrac.x + Igrac.width) and self.y >= Igrac.y and self.y <= (Igrac.y + Igrac.height):
            return True
        return False

###Klasa Igraca/Invader-a
class Igrac:
    def __init__(self, x, y, width, height, color, direction):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.pogodjen = False
        self.direction = direction
        self.projektil = Projektil(self.x + (self.width // 2), self.y + 2, WHITE, self, self.direction)
    
    ###Funkcija za ispis ovog igraca na ekran
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
    
    ###Funkcija za pomeranje Igraca/Invader-a
    ##nesto - odredjuje da li se funkcija ponasa u skladu sa pomeranjem igraca ili pomeranjem invader-a
    #0 - Invader
    #1 - Igrac
    def move(self, dx, dy, nesto, nesto1):
        #self.y += dy       #Dozvoljava pomeranje gore-dole i za Invader-e i za igraca

        #Sinhronizovano kretanje:
        self.direction = invaders[nesto1].direction

        ###Pomeranje Invader-a
        if nesto == 0:
            self.y += dy    #Dozvoljava pomeranje gore-dole samo za Invader-a
            self.x += dx * self.direction
            ##Pomeranje projektila tako da prati smer Invader-a po x osi
            self.projektil.x += dx * self.projektil.direction
            ##Ako je izadjeno na desnu stranu ekrana, (vrati se skroz levo) odbij se od ivice
            if self.x > screen_w - self.width:
                #self.x = 0
                #self.projektil.x = self.width // 2
                self.x = screen_w - self.width
                self.direction *= -1
            #Ako je izadjeno na levu stranu ekrana, (vrati se skroz desno) odbij se od ivice
            if self.x < 0:
                #self.x = screen_w
                #self.projektil.x = self.width // 2
                self.x = 0
                self.direction *= -1

        ###Pomeranje igraca
        if nesto == 1:
            self.x += dx
            #Ogranicenje za izlazak sa ekrana po x osi
            if self.x + self.width > screen_w or self.x < 0:
                self.x -= dx
            #Ogranicenje za izlazak sa ekrana po y osi
            if self.y + self.height > screen_h or self.y < 0:
                self.y -= dy
        #Sinhronizovano kretanje:
        invaders[nesto1].direction = self.direction

    #Funkcija za pomeranje projektila po y osi za b pixela. NE PROVERAVA DA LI JE PROJEKTIL IZASAO SA MAPE
    def pucaj(self, surface, b):
        self.projektil.move(b)
        self.projektil.draw(surface)

#PyGame Inicijalizacija
pygame.init()
screen_w = 1000
screen_h = 800
dis = pygame.display.set_mode((screen_w, screen_h))
dis.fill(WHITE)
pygame.display.update()
pygame.display.set_caption("SpaceInvaders Game")
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255, 0, 0)

#Inicijalizacija pocetnog ekrana
pygame.font.init()
my_font = pygame.font.SysFont("Liberation Serif", 30)

menu = True
while menu == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_ESCAPE]:
        menu = False

    text_surface = my_font.render('Dobrodosli u Space Invaders', False, (0, 0, 0))
    dis.blit(text_surface, (screen_w // 2 - 200, screen_h // 2))
    text_surface = my_font.render("Pritisnite ESCAPE za pocetak", False, (0,0,0))
    dis.blit(text_surface, (screen_w // 2 - 200, screen_h // 2 + 50))
    pygame.display.flip()


#Deklarisanje igraca i liste Invaders-a
player = Igrac(screen_w // 2 - 50, screen_h - 55, 25, 25, GREEN, 0)
player.projektil.y = -1

invaders = []
a = 110
k = a
brojLetelica = 18

smer1 = 1
for i in range(0, brojLetelica // 2):
    #smer = randint(0,1)
    #if smer == 0:
    #    smer = -1
    invader = Igrac(k, 51, 25, 25, RED, smer1)
    invaders.append(invader)
    k+= a
k = a - 40
smer2 = -1
for i in range(brojLetelica // 2, brojLetelica):
    #smer = randint(0,1)
    #if smer == 0:
    #    smer = -1
    invader = Igrac(k, 102, 25, 25, RED, smer2)
    invaders.append(invader)
    k+= a


###Pocetak igre
while True:
    dis.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #User Input za igraca
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_RIGHT]:
        player.move(2,0, 1, 0)
    if key_pressed[pygame.K_LEFT]:
        player.move(-2,0, 1, 0)
    if key_pressed[pygame.K_UP]:
        player.move(0,-2, 1, 0)
    if key_pressed[pygame.K_DOWN]:
        player.move(0,2, 1, 0)
    if key_pressed[pygame.K_SPACE]:
        #Kada je SPACE pritisnut, vrati projektil dole kod igraca
        player.projektil.y = player.y + 2
        player.projektil.x = player.x + (player.width // 2)
    #Igrac sve vreme salje projektil za 5 pixela na gore
    player.pucaj(dis, -5)
    #sviGotovi - Da li su svi Invader-i unisteni
    sviGotovi = True
    #broj - random integer koji odredjuje koji Invader trenutno puca.
    broj = randint(0, brojLetelica*10)
    for i in range(0, brojLetelica):
        if invaders[i].pogodjen == False:
            #Unosenje nasumicnosti pomeranja medju Invader-e
            jedan = randint(1,10)
            dva = randint(1,10)
            if jedan > dva:
                vece = jedan
                manje = dva
            else:
                vece = dva
                manje = jedan
            #Pomeranje Invader-a
            if i < brojLetelica // 2:
                invaders[i].move(manje/vece, 0.05, 0, 0)
            else:
                invaders[i].move(manje/vece, 0.05, 0, brojLetelica//2)
            #Dodato: Ako je Invader dodatao dno ekrana, proglasi kraj igre
            if invaders[i].y > screen_h - 55:
                game_over(dis, "Invader dosao do kraja!")
            #Nacrtaj Invader-a
            invaders[i].draw(dis)
            #Ako je igracev projektil pogodio i-tog Invader-a, podesi njegovu 'pogodjen' varijablu na True
            if player.projektil.collide(invaders[i]) == True:
                invaders[i].pogodjen = True
            #Ako neki od Invader-a jos uvek nije pogodjen, stavi sviGotovi na False
            if invaders[i].pogodjen == False:
                sviGotovi = False

            #Pomeri Invader-ov projektil za 2 na dole ako nije pogodjen(***)
            a = invaders[i].projektil.move(1)
            #  Ako je i-ti Invader Invader koji treba da puca(i == broj), taj Invader nije pogodjen i njegov projektil je
            #  van ekrana(a == False), vrati njegov projektil kod Invader-a tako da on nastavi da ide na dole
            if(a == False and i == broj and invaders[i].pogodjen == False):
                invaders[i].projektil.y = invaders[i].y + 2
                invaders[i].projektil.x = invaders[i].x + (invaders[i].width // 2)
        #Pomeri metak za jos 1 ako je Invader nepogodjen ili samo za 1 ako je pogodjen(***)
        invaders[i].pucaj(dis, 1)
        #Ako se projektil bilo kog Invader-a sudario sa igracem, proglasi kraj igre
        if invaders[i].projektil.collide(player) == True:
            game_over(dis, "Tvoj brod je pogodjen!")

    #Ako su svi Invader-i gotovi, proglasi kraj igre
    if sviGotovi == True:
        game_over(dis, "Igrac je pobedio sve invadere!")

    #Nacrtaj igraca i azuriraj ekran
    player.draw(dis)
    pygame.display.update()
