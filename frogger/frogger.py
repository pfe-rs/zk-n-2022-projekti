import pygame
import time
import random 


class frog:
    def __init__(self, x, y, str, color):
        self.x = x
        self.y = y
        self.str = str
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.str, self.str))

    def move(self, dx,dy):
        self.x += dx
        self.y += dy

class prepreka:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width ,self.height))

    def move(self, dx):
        self.x += dx
    def shift (self):
        self.y+=100




pygame.init()
screen_w = 1000
screen_h = 600
dis=pygame.display.set_mode((screen_w,screen_h))
pygame.display.update()
pygame.display.set_caption('Vipidipidijej')
klika_space=True
while(klika_space):
    game_over=False

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    YELLOW = (255,255,0)
    RED = (255,0,0)
    ORANGE = (255,165,0)
    BLUE = (0,0,255)
    GREEN = (0,255,0)

    P1=prepreka(0,500,120,50,BLACK)
    P2=prepreka(0,300,140,50,YELLOW)
    P3=prepreka(0,100,220,50,RED)
    P4=prepreka(900,400,100,50,ORANGE)
    P5=prepreka(880,200,120,50,BLUE)
    P6=prepreka(820,0,180,50,GREEN)

    parametri = [
        (0,500,100,50,BLACK),
        (0,300,120,50,YELLOW),
        (0,100,200,50,RED),
        (920,400,80,50,ORANGE),
        (900,200,100,50,BLUE),
        (840,0,160,50,GREEN)
    ]


    frog_str = 50

    player = frog(screen_w//2 - frog_str//2,screen_h - 50, frog_str, BLACK)

    rand_dx = random.random()
    rand_dy = random.random()

    step_x = screen_w // 16
    step_y = screen_h // 20

    BACKGROUND_COLOR = (201, 201, 201)

    font = pygame.font.Font('freesansbold.ttf', 20)
    click=False
    font2 = pygame.font.Font('freesansbold.ttf', 50)

    bodovi=0
    v1=0.8
    v2=1
    v3=0.4
    v4=-0.8
    v5=-1
    v6=-0.4

    while not game_over:
        for event in pygame.event.get():
            #print(event)   
            if event.type == pygame.WINDOWCLOSE or event.type == pygame.QUIT:
                pygame.quit()

        dis.fill(BACKGROUND_COLOR)
        player.draw(dis)
        P1.draw(dis)
        P2.draw(dis)
        P3.draw(dis)
        P4.draw(dis)
        P5.draw(dis)
        P6.draw(dis)
        
        P1.move(v1)
        P2.move(v2)
        P3.move(v3)
        P4.move(v4)
        P5.move(v5)
        P6.move(v6)

        keys_pressed = pygame.key.get_pressed()
        
        if keys_pressed[pygame.K_UP] and click==False :
            click=True
            bodovi+=1

            if(bodovi%20== 0 and bodovi!=0):
                v1+=0.02
                v2+=0.02
                v3+=0.02
                v4+=-0.02
                v5+=-0.02
                v6+=-0.02

            P1.y+=50
            P2.y+=50
            P3.y+=50
            P4.y+=50
            P5.y+=50
            P6.y+=50
            
            if (P1.y==600):
                P1=prepreka(*random.choice(parametri))
                P1.x=500
                P1.y=0
                P1.draw(dis)
            if (P2.y==600):
                P2=prepreka(*random.choice(parametri))
                P2.x=0
                P2.y=0
                P2.draw(dis)
            if (P3.y==600):
                P3=prepreka(*random.choice(parametri))
                P3.x=1000
                P3.y=0
                P3.draw(dis)
            if (P4.y==600):
                P4=prepreka(*random.choice(parametri))
                P4.x=0
                P4.y=0
                P4.draw(dis)
            if (P5.y==600):
                P5=prepreka(*random.choice(parametri))
                P5.x=500
                P5.y=0
                P5.draw(dis)
            if (P6.y==600):
                P6=prepreka(*random.choice(parametri))
                P6.x=1000
                P6.y=0
                P6.draw(dis)
        elif not  keys_pressed[pygame.K_UP] :
            click=False

        if keys_pressed[pygame.K_RIGHT]:
            player.move(1,0)
        if keys_pressed[pygame.K_LEFT]:
            player.move(-1,0)
        
        if P1.x+P1.width < 0:
            P1.x = 1000
        if P1.x > screen_w:
            P1.x = - P1.width
        
        if P2.x+P2.width < 0:
            P2.x = 1000
        if P2.x > screen_w:
            P2.x = - P2.width
        
        if P3.x+P3.width < 0:
            P3.x = 1000
        if P3.x > screen_w:
            P3.x = - P3.width

        if P4.x+P4.width < 0:
            P4.x = 1000
        if P4.x > screen_w:
            P4.x = - P4.width
        
        if P5.x+P5.width < 0:
            P5.x = 1000
        if P5.x > screen_w:
            P5.x = - P5.width
        
        if P6.x+P6.width < 0:
            P6.x = 1000
        if P6.x > screen_w:
            P6.x = - P6.width
        
        if player.x+player.str < 0:
            player.x = 1000
        if player.x > screen_w:
            player.x = - player.str
        
        # if(P1.y==500 and (P1.x>player.x-P1.width and P1.x<player.x+player.str)):
        #     if(click==True):
        #         game_over=True
        if(P1.y==550 and P1.x+P1.width>=player.x and P1.x<player.x+player.str):
            game_over=True
        # if(P2.y==500 and (P2.x>player.x-P2.width and P2.x<player.x+player.str)):
        #     if(click==True):
        #         game_over=True
        if (P2.y==550 and P2.x+P2.width>=player.x and P2.x<player.x+player.str):
            game_over=True
        # if(P3.y==500 and (P3.x>player.x-P3.width and P3.x<player.x+player.str)):
        #     if(click==True):
        #         game_over=True
        if(P3.y==550 and P3.x+P3.width>=player.x and P3.x<player.x+player.str):
            game_over=True
        # if(P4.y==500 and (P4.x>player.x-P4.width and P4.x<player.x+player.str)):
        #     if(click==True):
        #         game_over=True
        if(P4.y==550 and P4.x+P4.width>=player.x and P4.x<player.x+player.str):
            game_over=True
        # if(P5.y==500 and (P5.x>player.x-P5.width and P5.x<player.x+player.str)):
        #     if(click==True):
        #         game_over=True
        if(P5.y==550 and P5.x+P5.width>=player.x and P5.x<player.x+player.str):
            game_over=True
        # if(P6.y==500 and (P6.x>player.x-P6.width and P6.x<player.x+player.str)):
        #     if(click==True):
        #         game_over=True
        if(P6.y==550 and P6.x+P6.width>=player.x and P6.x<player.x+player.str):
            game_over=True

        poruka="BODOVI: " + str(bodovi)
        text=font2.render(poruka, True, BLACK, BACKGROUND_COLOR)
        dis.blit(text,(0, 40))

        

        pygame.display.update()

    nije_kliknuo_nista=True
    while nije_kliknuo_nista: 
        dis.fill(BLACK)
        poruka="BODOVI: " + str(bodovi)
        text1=font.render("OSVOJENI BODOVI: " + str(bodovi), True, WHITE, BLACK )
        dis.blit(text1,(screen_w // 2 - 140, screen_h // 2+50))            
        text = font2.render("GAME OVER", True, WHITE, BLACK)
        dis.blit(text, (screen_w // 2 - 180, screen_h // 2-20))
        text2=font.render("Za nastavak pritisni SPACE", True, WHITE, BLACK )
        dis.blit(text2,(screen_w // 2 - 160, screen_h // 2+80))            
        pygame.display.update()
        for event in pygame.event.get():
            print(event)   
            if event.type==pygame.KEYDOWN:
                nije_kliknuo_nista=False
            elif event.type == pygame.WINDOWCLOSE or event.type == pygame.QUIT:                    
                pygame.quit()
