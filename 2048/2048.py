import pygame, sys, time
from pygame.locals import *
from pygame import mixer
from constants import *
from random import *

sirinaTable = 4
ukupnoPoena = 0
pocetniBrojPoena = 2

js = randint(30,50)
#js=5
jsBrojac=0

print(js)

pygame.init()
mixer.init()

displej = pygame.display.set_mode((400, 300), pygame.FULLSCREEN)
#displej = pygame.display.set_mode((400, 300))
pygame.display.set_caption("2048PFE")

#jedini font za sve
font = pygame.font.SysFont("Chiller", 40)
font1 = pygame.font.SysFont("Chiller", 20)

#inicijalizacija 4*4 matrice
matrica = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

mixer.music.load("caves-of-dawn-10376.mp3")
mixer.music.set_volume(0.4)
mixer.music.play()

#boje
crna=(0,0,0)
krv=(138,3,3)
boja2=(190,190,190)
boja4=(170,170,170)
boja8=(150,150,150)
boja16=(130,130,130)
boja32=(110,110,110)
boja64=(90,90,90)
boja128=(70,70,70)
boja256=(50,50,50)
boja512=(30,30,30)
boja1024=(10,10,10)
boja2048=(250,230,0)

boje = {
    0: crna,
    2: boja2,
    4: boja4,
    8: boja8,
    16: boja16,
    32: boja32,
    64: boja64,
    128: boja128,
    256: boja256,
    512: boja512,
    1024: boja1024,
    2048: boja2048
}
#Promena boja
#Provereno dobro!

# funkcija koja bira boju iz "recnika boja"
def getBoja(i):
    return boje[i]

image1 = pygame.image.load('horor1.jpeg')
image2 = pygame.image.load('horor2.jpg')
image3 = pygame.image.load('horor3.jpg')
image4 = pygame.image.load('horor4.jpeg')
image5 = pygame.image.load('horor5.jpg')

slike = {
    0: image1,
    1: image2,
    2: image3,
    3: image4,
    4: image5
}

# funkcija koja bira sliku
def getSlika(i):
    return slike[i]


#main, glavna funkcija
def main():

    staviRandomPolje()
    staviRandomPolje()
    ispisiMatricu()

    global jsBrojac

    #glavna while petlja

    #win demonstracija, odkomentarisi
    #win()

    while True:
        #da li smo izasli iz igrice?*
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            #da li je moguce pomeriti blokove?
            #ako je moguce, i ako je pritisnuta neka strelica, rotirati
            if mogucNastavak():
                if event.type == KEYDOWN:
                    if pritisnutaStrelica(event.key):
                        jsBrojac = jsBrojac + 1
                        jumpscare()
                        #аko je pritisnuta strelica, rotirati (getrotations se bavi time, koja je pritisnuta i kako ce se to odraziti na igricu)
                        rotations = getrotations(event.key)
                        #~~addToUnd
                        for i in range(0, rotations):
                            rotatematrixclockwise()

                        #ako se moze pomeriti,
                        if mogucePomeritiPolja():
                            #pomeriti polja
                            pomeriPolja()
                            #spojiti polja
                            mergetiles()
                            #staviti novo random polje
                            staviRandomPolje()

                        for j in range(0, (4 - rotations) % 4):
                            rotatematrixclockwise()

                        ispisiMatricu()
            else:
                #ako se ne moze nastaviti, igra je zavrsena
                gameover()

            if event.type == KEYDOWN:
                global sirinaTable

                #!!!napisi instrukcije!!!
                #Bbroj polja u redu/koloni se unosi po zavrsetku prve igre
                if event.key == pygame.K_r:
                    reset()
                if 50 < event.key and 56 > event.key:
                    sirinaTable = event.key - 48
                    reset()

        pygame.display.update()

#funkcija proverava da li je moguce pomeriti polja
def mogucePomeritiPolja():
    for i in range(0, sirinaTable):
        for j in range(1, sirinaTable):
            if matrica[i][j - 1] == 0 and matrica[i][j] > 0:
                return True
            elif (matrica[i][j - 1] == matrica[i][j]) and matrica[i][j - 1] != 0:
                return True
    return False

#pomeranje polja
#ovde moze nastati greska!
def pomeriPolja():
    for i in range(0, sirinaTable):
        for j in range(0, sirinaTable - 1):

            while matrica[i][j] == 0 and sum(matrica[i][j:]) > 0:
                for k in range(j, sirinaTable - 1):
                    matrica[i][k] = matrica[i][k + 1]
                matrica[i][sirinaTable - 1] = 0

#funkcija za spajanje (merging) polja
#nista posebno, samo sabira susedna polja, jedno brise, drugo udvostrucava
def mergetiles():
    global ukupnoPoena

    for i in range(0, sirinaTable):
        for k in range(0, sirinaTable - 1):
            if matrica[i][k] == matrica[i][k + 1] and matrica[i][k] != 0:
                matrica[i][k] = matrica[i][k] * 2
                matrica[i][k + 1] = 0
                ukupnoPoena += matrica[i][k]
                pomeriPolja()


def staviRandomPolje():
    c = 0
    for i in range(0, sirinaTable):
        for j in range(0, sirinaTable):
            if matrica[i][j] == 0:
                c += 1

    k = floor(random() * sirinaTable * sirinaTable)
    print("click")

    while matrica[floor(k / sirinaTable)][k % sirinaTable] != 0:
        k = floor(random() * sirinaTable * sirinaTable)

    matrica[floor(k / sirinaTable)][k % sirinaTable] = 2

#funkcija vraca ceo deo broja
def floor(n):
    return int(n - (n % 1 ))

#ispis polja matrica, mozda je doslo do greske
def ispisiMatricu():
    displej.fill(crna)
    global sirinaTable
    global ukupnoPoena

    for i in range(0, sirinaTable):
        for j in range(0, sirinaTable):
            pygame.draw.rect(displej, getBoja(matrica[i][j]), (
            120 + i * (400 / sirinaTable), j * (400 / sirinaTable) + 80, 400 / sirinaTable, 400 / sirinaTable))
            label = font.render(str(matrica[i][j]), 1, krv)
            label2 = font.render("Broj poena:" + str(ukupnoPoena), 1, krv)
            displej.blit(label, (120 + i * (400 / sirinaTable) + 20, j * (400 / sirinaTable) + 130))
            displej.blit(label2, (130, 20))

def jumpscare():

    global js
    global jsBrojac

    #ispisati sliku
    print(jsBrojac, js)
    if jsBrojac == js:
        # pustiti zvuk

        mixer.music.load("scream14-6918.mp3")
        mixer.music.set_volume(1)
        mixer.music.play()

        time.sleep(0.5)

        DEFAULT_IMAGE_SIZE = (displej.get_width(), displej.get_height())
        image = pygame.transform.scale(getSlika(js % 5), DEFAULT_IMAGE_SIZE)
        displej.blit(image, (0, 0))
        # displej.fill((255,255,255))
        pygame.display.update()

        time.sleep(2)

        mixer.music.load("caves-of-dawn-10376.mp3")
        mixer.music.set_volume(0.4)
        mixer.music.play()

        #promeniti brojace
        js = randint(10, 40)
        jsBrojac = 0

        print("js i js brojac: ")
        print(js, jsBrojac)


def win():
    global ukupnoPoena

    time.sleep(0.7)

    mixer.music.load("general-logo-13395.mp3")
    mixer.music.set_volume(0.7)
    mixer.music.play()

    displej.fill(boja2048)

    label = font1.render("Čestitam!! Pobeda!!!", 1, (0,0,0))
    label2 = font1.render("Poeni : " + str(ukupnoPoena), 1, (0,0,0))
    label3 = font1.render("Pritisni 'R' za ponovnu igru", 1, (0,0,0))

    displej.blit(label, (50, 100))
    displej.blit(label2, (50, 200))
    displej.blit(label3, (50, 300))


#da li se moze naciniti sledeci potez? tj. da li je kraj igrice
#ako je moguce napraviti bar jedan potez, igrica se moze nastaviti
def mogucNastavak():
    for i in range(0, sirinaTable ** 2):
        if matrica[floor(i / sirinaTable)][i % sirinaTable] == 0:
            return True


    for i in range(0, sirinaTable):
        for j in range(0, sirinaTable - 1):
            if matrica[i][j]==2048 or matrica[i][j+1]==2048:
                win()
            if matrica[i][j] == matrica[i][j + 1]:
                return True
            elif matrica[j][i] == matrica[j + 1][i]:
                return True
    return False

#funkcija koja matricu rotira za 90 stepeni udesno - koristi se da bi se pomerila polja pomocu svih 4 strelica
#pomeranje se posmatra kao
def rotatematrixclockwise():
    for i in range(0, int(sirinaTable / 2)):
        for k in range(i, sirinaTable - i - 1):
            temp1 = matrica[i][k]
            temp2 = matrica[sirinaTable - 1 - k][i]
            temp3 = matrica[sirinaTable - 1 - i][sirinaTable - 1 - k]
            temp4 = matrica[k][sirinaTable - 1 - i]

            matrica[sirinaTable - 1 - k][i] = temp1
            matrica[sirinaTable - 1 - i][sirinaTable - 1 - k] = temp2
            matrica[k][sirinaTable - 1 - i] = temp3
            matrica[i][k] = temp4


def gameover():
    global ukupnoPoena

    displej.fill(crna)

    label = font1.render("Igrica je završena!", 1, (255, 255, 255))
    label2 = font1.render("Poeni : " + str(ukupnoPoena), 1, (255, 255, 255))

    displej.blit(label, (50, 100))
    displej.blit(label2, (50, 200))


def reset():
    global ukupnoPoena
    global matrica

    ukupnoPoena = 0
    displej.fill(crna)
    matrica = [[0 for i in range(0, sirinaTable)] for j in range(0, sirinaTable)]
    main()


def pritisnutaStrelica(k):
    return (k == pygame.K_UP or k == pygame.K_DOWN or k == pygame.K_LEFT or k == pygame.K_RIGHT)

#funkcija koja prepoznaje strelice tj. svakoj dodeljuje broj, za koliko ce se rotirati matrica
def getrotations(k):
    if k == pygame.K_UP:
        return 0
    elif k == pygame.K_DOWN:
        return 2
    elif k == pygame.K_LEFT:
        return 1
    elif k == pygame.K_RIGHT:
        return 3

main()