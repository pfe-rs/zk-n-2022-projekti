from audioop import mul
import math
from operator import rshift
import pygame
import time
import random
import math


class Tile:
    def __init__(self, x, y, width, height, color, angle):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.angle = angle
        self.image = pygame.image.load("PlayerImage.png")
        self.rect = self.image.get_rect(center = (self.x,self.y))
        self.speed = (0, -1)
        self.deltax = 0
        self.deltay = 0
        self.collision = False
        self.fire = False

    def draw(self, surface):
        self.image.get_rect(center=(self.x, self.y))
        rot_image = pygame.transform.rotate(self.image, self.angle)
        image_rect = rot_image.get_rect()
        surface.blit(rot_image, (self.x - image_rect.width//2, self.y - image_rect.height//2))
        

    def rotate(self, ang):
        self.angle += ang
        if self.angle >= 360:
            self.angle = 0
        if self.angle < 0:
            self.angle = 360
        rad = ang*2*math.pi/360
        new_speed = (math.cos(rad)*self.speed[0] + math.sin(rad)*self.speed[1], -math.sin(rad)*self.speed[0] + math.cos(rad)*self.speed[1])
        self.speed = new_speed

    def move(self, mul):
        self.x += self.speed[0]*mul
        self.y += self.speed[1]*mul
        self.deltax = self.speed[0]*mul
        self.deltay = self.speed[1]*mul

    def print_speed(self):
        print(self.speed[0], ', ', self.speed[1])

    def friction(self, div):
        self.x += self.deltax/div
        self.y += self.deltay/div
        self.deltax = self.deltax/div
        self.deltay = self.deltay/div

    def edge(self):
        if self.x < 0:
            self.x = screen_w
        if self.x > screen_w:
            self.x = 0
        if self.y < 0:
            self.y = screen_h
        if self.y > screen_h:
            self.y = 0 

    def find_optimal_dot(self, ball):
        return max(self.x, min(ball.x, self.x + self.width)), max(self.y, min(ball.y, self.y + self.height))


#rsi - random speed factor
class Asteroid:
    def __init__(self, radius, color, rsf, same, x, y):
        if not same:
            self.x = random.randint(0, screen_w) # TO DO: Pazi da se ne stvori na igracu ili previse blizu njega
            self.y = random.randint(0, screen_h)
        else:
            self.x = x
            self.y = y
        self.radius = radius
        self.speed = (random.gauss(0, rsf), random.gauss(0, rsf))
        self.color = color
        #print(self.x)
        #print(self.y)
        #print(self.speed[0])
        #print(self.speed[1])
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
    def move(self, mul):
        self.x += self.speed[0]
        self.y += self.speed[1]
    def edge(self):
        if self.x < 0:
            self.x = screen_w
        if self.x > screen_w:
            self.x = 0
        if self.y < 0:
            self.y = screen_h
        if self.y > screen_h:
            self.y = 0 
    def isPointInCircle(self, point_x, point_y):
        return (point_x - self.x)**2 + (point_y - self.y)**2 < self.radius**2

    def tile_collision(self, other):
        optimal_x, optimal_y = other.find_optimal_dot(self)
        if self.isPointInCircle(optimal_x, optimal_y):
            return True
    def bulet_colision(self, other):
        if self.isPointInCircle(other.x, other.y):
            return True



class Bulet:
    def __init__(self, x, y, speed, color, radius, time):
        self.x = x
        self.y = y
        self.speed = speed
        self.color = color
        self.radius = radius
        self.time = time
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
    def move(self, mul):
        self.x += self.speed[0]*mul
        self.y += self.speed[1]*mul
    def edge(self):
        if self.x < 0:
            self.x = screen_w
        if self.x > screen_w:
            self.x = 0
        if self.y < 0:
            self.y = screen_h
        if self.y > screen_h:
            self.y = 0 
    def timer(self):
        self.time -= 1
        if(self.time <= 0):
            return True

pygame.init()
screen_w = 1000
screen_h = 800

lives = 3
score = 0
dis=pygame.display.set_mode((screen_w,screen_h))
pygame.display.update()
pygame.display.set_caption('Asteroidi')
game_over=False

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREY = (50, 50, 50)
BALL_TILE_COLOR = (255, 255, 255)
MOUSEX = 0
MOUSEY = 0
COL_STATE = 0

tile_w = 15
tile_h = 15
player = Tile(screen_w//2 - tile_w//2,screen_h - 200, tile_w, tile_h, BALL_TILE_COLOR, 0)
astNum = 5

BACKGROUND_COLOR = (0, 0, 0)


pygame.font.init()
my_font = pygame.font.SysFont('Ariel', 50)
go_font = pygame.font.SysFont('Ariel', 100)

asteroids = []
bulets = []

def game():
    global lives
    global score
    while lives > 0:
        for event in pygame.event.get():
            #print(event)   
            if event.type == pygame.WINDOWCLOSE or event.type == pygame.QUIT:
                pygame.quit()
            
            # prvobitno resenje - nije smooth
            ''' if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.move(20)
                if event.key == pygame.K_LEFT:
                    player.move(-20)
            '''

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            player.rotate(-2)
        if keys_pressed[pygame.K_LEFT]:
            player.rotate(2)
        if keys_pressed[pygame.K_UP]:
            player.move(2)
        #elif keys_pressed[pygame.K_DOWN]:
        #    player.move(-1)
        else:
            player.friction(1.005)
        if keys_pressed[pygame.K_SPACE]:
            if player.fire == False:
                bulets.append(Bulet(player.x, player.y, player.speed, player.color, 5, 100))
                player.fire = True
        else:
            player.fire = False

        player.edge()


        if len(asteroids) < astNum:
            multiply = random.randint(1, 5)
            asteroids.append(Asteroid(multiply*10, WHITE, 1, False, 0, 0))

        
        dis.fill(BACKGROUND_COLOR)
        player.draw(dis)
    
        for ast in  asteroids:
            if ast.radius < 10:
                asteroids.remove(ast)
            if ast.tile_collision(player):
                asteroids.remove(ast)
                lives -= 1
                player.x = screen_w//2 - tile_w//2
                player.y = screen_h - 200
                player.angle = 0
                player.speed = (0, -1)
            ast.move(1)
            ast.edge()
            ast.draw(dis)
        for bul in bulets:
            if(bul.timer()):
                bulets.remove(bul)
            bul.move(4)
            bul.edge()
            bul.draw(dis)
            for ast in asteroids:
                if ast.bulet_colision(bul):
                    radiusV = ast.radius
                    radiusV //= 2
                    asteroids.append(Asteroid(radiusV, WHITE, 1, True, ast.x, ast.y))
                    asteroids.append(Asteroid(radiusV, WHITE, 1, True, ast.x, ast.y))
                    asteroids.remove(ast)
                    bulets.remove(bul)
                    score += 10
        dis.blit(my_font.render('Score: ' + str(score), False, WHITE), (10, 10))
        dis.blit(my_font.render('Lives: ' + str(lives), False, WHITE), (10, 70))
        #player.print_speed()

        pygame.display.update()


    while lives <= 0:
        for event in pygame.event.get():
            #print(event)   
            if event.type == pygame.WINDOWCLOSE or event.type == pygame.QUIT:
                pygame.quit()
        dis.fill(BACKGROUND_COLOR)
        dis.blit(go_font.render('GAME OVER', False, WHITE), (screen_w//2-200, screen_h//2-100))
        dis.blit(go_font.render('Score: ' + str(score), False, WHITE), (screen_w//2-200, screen_h//2-200))
        pygame.draw.rect(dis, GREY, (screen_w//2-200, screen_h//2, 400, 100))
        dis.blit(go_font.render('RETRY', False, WHITE), (screen_w//2-115, screen_h//2+20))
        
        MOUSE_POS = pygame.mouse.get_pos()
        MOUSE_DOWN = pygame.mouse.get_pressed()
        if MOUSE_DOWN[0]:
            if MOUSE_POS[0] > screen_w//2-200:
                if MOUSE_POS[0] < screen_w//2-200 + 400:
                    if MOUSE_POS[1] > screen_h//2:
                        if MOUSE_POS[1] < screen_h//2+100:  
                            lives = 3
                            score = 0
                            game()
        pygame.display.update()

game()  