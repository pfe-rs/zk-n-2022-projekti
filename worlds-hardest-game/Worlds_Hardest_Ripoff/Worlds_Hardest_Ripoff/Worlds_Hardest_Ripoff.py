import pygame
import os

width = 800
height = 800

pygame.init()
dis=pygame.display.set_mode((width,height), 0, 32)
pygame.display.update()
pygame.display.set_caption('Worlds Hardest Ripoff')
game_over=False

imgWin = pygame.image.load("E:\\C#\\Worlds_Hardest_Ripoff\\IMG\\imgWin.png")
imgLose = pygame.image.load("E:\\C#\\Worlds_Hardest_Ripoff\\IMG\\imgLose.png")
imgNext = pygame.image.load("E:\\C#\\Worlds_Hardest_Ripoff\\IMG\\imgNext.png")



def citac(filename, w, h):                 # citanje nivoa

    cit = open(filename, "r")
       
    mat = []
    
    i = 0
    while(i < h / 10):

        x = cit.readline()                 #           -!-
            
        red = []
        j = 0
        while(j < w / 10):

            red.append(x[j])               #           -!-

            j+=1

        i+=1
        mat.append(red)
            
    cit.close()
    
    return mat



class PLAYER:
    def __init__(self, x, y, width, height):  # inicijalizacija
        self.x = width // 80 * x
        self.y = height // 80 * y
        self.h = 10
        self.clr = (60, 200, 100)

    def move(self, speed):                          # kretanje               -!-
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.x += speed

        if keys_pressed[pygame.K_LEFT]:
            self.x -= speed

        if keys_pressed[pygame.K_UP]:
            self.y -= speed

        if keys_pressed[pygame.K_DOWN]:
            self.y += speed                
     
    def draw(self, surf):                                           # crtanje           -!-
        pygame.draw.rect(surf, self.clr, (self.x, self.y, self.h, self.h))



class ZID:
    def __init__(self, x, y, width, height):  # inicijalizacija
        self.x = width // 80 * x
        self.y = height // 80 * y
        self.h = 10
        self.clr1 = (220, 140, 110)
        self.clr2 = (215, 110, 70)

    def draw(self, surf):                                           # crtanje           -!-
        pygame.draw.rect(surf, self.clr1, (self.x, self.y, self.h, self.h))
        pygame.draw.line(surf, self.clr2, (self.x, self.y), (self.x + self.h, self.y + self.h))
        pygame.draw.line(surf, self.clr2, (self.x + self.h, self.y), (self.x, self.y + self.h))

    def clch(self, xe, ye):                                                                     # colision check                -!-
        check1 = xe >= self.x and xe <= self.x + self.h and ye >= self.y and ye <= self.y + self.h
        check2 = xe + self.h >= self.x and xe + self.h <= self.x + self.h and ye + self.h >= self.y and ye + self.h <= self.y + self.h
        if check1 or check2:       # DISCLAMER: mora biti sazvano pri svakom move!
            #print('kolizija detektovana')
            #pygame.display.quit()
            return 0
        return currentLvl



class ZLI:
    
    def __init__(self, x, y, width, height, prav):  # inicijalizacija
        self.x = width // 80 * x
        self.y = height // 80 * y
        self.h = 10

        self.cap = 20
        self.brojac = 0
        self.prav = prav
        self.tri = 18

        self.clr1 = (255, 0, 0)
        self.clr2 = (80, 50, 50)

    def draw(self, surf):                                           # crtanje           -!-
        pygame.draw.rect(surf, self.clr1, (self.x, self.y, self.h, self.h))
        pygame.draw.circle(surf, self.clr2, (self.x + self.h//2, self.y + self.h//2), self.h // 2, self.h)

    def clch(self, xe, ye):                                                                     # colision check                -!-
        check1 = xe >= self.x and xe <= self.x + self.h and ye >= self.y and ye <= self.y + self.h
        check2 = xe + self.h >= self.x and xe + self.h <= self.x + self.h and ye + self.h >= self.y and ye + self.h <= self.y + self.h
        if check1 or check2:       # DISCLAMER: mora biti sazvano pri svakom move!
            #print('kolizija detektovana')
            #pygame.display.quit()
            return 0  
        return currentLvl

    def move(self, speed):                          # kretanje               -!-        
        if self.cap == self.brojac:
            if self.prav == 0:
                self.y -= speed
                self.brojac = -1
                self.tri -= 1

            if self.prav == 1:
                self.x += speed
                self.brojac = -1
                self.tri -= 1

            if self.prav == 2:
                self.y += speed
                self.brojac = -1
                self.tri -= 1

            if self.prav == 3:
                self.x -= speed
                self.brojac = -1
                self.tri -= 1

        self.brojac += 1

        if self.tri == 0:
            if self.prav == 0:
                self.prav = 2               
            else:
                if self.prav == 2:
                    self.prav = 0
                else:               
                    if self.prav == 1:
                        self.prav = 3
                    else:
                        if self.prav == 3:
                            self.prav = 1               #                -!- -!- -!-
            self.tri = 18



class EXIT:
    def __init__(self, x, y, width, height):  # inicijalizacija
        self.x = width // 80 * x
        self.y = height // 80 * y
        self.h = 10
        self.clr1 = (60, 200, 230)
        self.clr2 = (20, 20, 70)       

        self.lock = False
        if coinCnt > 0:
            self.lock = True

    def draw(self, surf):                                           # crtanje           -!-
        pygame.draw.rect(surf, self.clr1,( self.x, self.y, self.h, self.h))
        if not self.lock:
            self.clr2 = (150, 200, 250)
        pygame.draw.rect(surf, self.clr2, (self.x + self.h // 5, self.y + self.h // 5, self.h // 5 * 3, self.h // 5 * 3))

    def clch(self, xe, ye, coinCnt):                                                                     # colision check                -!-
        check1 = xe >= self.x and xe <= self.x + self.h and ye >= self.y and ye <= self.y + self.h
        check2 = xe + self.h >= self.x and xe + self.h <= self.x + self.h and ye + self.h >= self.y and ye + self.h <= self.y + self.h 
        if coinCnt == 0:
            self.lock = False
        if (check1 or check2) and not self.lock:       # DISCLAMER: mora biti sazvano pri svakom move!
            #print('kolizija detektovana')
            return True  # win
        return False
                            


class COIN:
    def __init__(self, x, y, width, height):  # inicijalizacija
        self.x = width // 80 * x
        self.y = height // 80 * y
        self.h = 10
        self.clr1 = (240, 240, 60)
        self.clr2 = (230, 190, 50)

        self.col = False

    def draw(self, surf):                                           # crtanje           -!-
        if not self.col: 
            pygame.draw.circle(surf, self.clr2, (self.x + self.h // 2, self.y + self.h // 2), self.h // 2, self.h)
            pygame.draw.circle(surf, self.clr1, (self.x + self.h // 2, self.y + self.h // 2), self.h // 2 // 5 * 3, self.h // 5 * 3)
            pygame.draw.line(surf, self.clr2, (self.x + self.h // 2, self.y), (self.x + self.h // 2, self.y + self.h))

    def clch(self, xe, ye):                                                                     # colision check                -!-
        check1 = xe >= self.x and xe <= self.x + self.h and ye >= self.y and ye <= self.y + self.h
        check2 = xe + self.h >= self.x and xe + self.h <= self.x + self.h and ye + self.h >= self.y and ye + self.h <= self.y + self.h
        if check1 or check2:       # DISCLAMER: mora biti sazvano pri svakom move!
            #print('kolizija detektovana')
            self.col = True
            return 1   # fali totalCoinCount
        return 0
            



lvlNum = len(os.listdir("E:\\C#\\Worlds_Hardest_Ripoff\\LVL"))

currentLvl = 1
cheat = '' # tajni kod za EASY MODE

while currentLvl < lvlNum // 2 + 1:
    nivo1 = citac("E:\\C#\\Worlds_Hardest_Ripoff\\LVL\\lvl{}{}.txt".format(currentLvl, cheat), width, height)   

    coinCnt = 0

    coinList: list[COIN] = []
    zliList: list[ZLI] = []
    zidList: list[ZID] = []


    player1 = PLAYER(0, 0, width, height)
    ex = 79
    ey = 79

    for i in range(height // 10):
    
        for j in range(width // 10):

            if nivo1[j][i] == "1":
                player1 = PLAYER(i, j, width, height)

            if nivo1[j][i] == "2": 
                zidList.append(ZID(i, j, width, height))

            if nivo1[j][i] == "3":
                zliList.append(ZLI(i, j, width, height, 0))

            if nivo1[j][i] == "4":
                zliList.append(ZLI(i, j, width, height, 1))

            if nivo1[j][i] == "5":
                zliList.append(ZLI(i, j, width, height, 2))

            if nivo1[j][i] == "6":
                zliList.append(ZLI(i, j, width, height, 3))

            if nivo1[j][i] == "7":
                ex = i
                ey = j

            if nivo1[j][i] == "8":
                coinList.append(COIN(i, j, width, height))
                coinCnt += 1

    exit1 = EXIT(ex, ey, width, height)

    lvlNext = False

    while not game_over:                        # ovo je UKRADENO od nasih dragih profa.      -!-
        for event in pygame.event.get():  
            if event.type == pygame.WINDOWCLOSE or event.type == pygame.QUIT:
                pygame.quit()
                exit() 
            
        dis.fill((200, 255, 240))               # pozadina je neka minti
    

        ###
    
    

        player1.draw(dis)
        player1.move(1)

        for i in range(len(zidList)):
            zidList[i].draw(dis)
            currentLvl = zidList[i].clch(player1.x, player1.y)

        for i in range(len(zliList)):
            zliList[i].draw(dis)
            zliList[i].move(1)
            currentLvl = zliList[i].clch(player1.x, player1.y)

        for i in range(len(coinList)):
            coinList[i].draw(dis)
            coinCnt -= coinList[i].clch(player1.x, player1.y)
        
        exit1.draw(dis)
        lvlNext = exit1.clch(player1.x, player1.y, coinCnt)


        if lvlNext:
            print("You win!")
            currentLvl += 1
            for x in range(1024):
                dis.blit(imgNext, (0 , 0))
                pygame.display.update()
            break

        if currentLvl == 0:
            for x in range(1024):
                dis.blit(imgLose, (0 , 0))
                pygame.display.update()
            currentLvl = 1
            break

        ###


        pygame.display.update()                 # updater. izmedju ovoga i pozadine ide sam kod po frame-u

    continue

for x in range(1024):
    dis.blit(imgWin, (0 , 0))
    pygame.display.update()

pygame.display.quit()
pygame.quit()
exit() 




