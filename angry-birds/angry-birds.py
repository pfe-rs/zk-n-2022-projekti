
import math
import pygame

class Brick:
    def __init__(self, a, b, brick_h, brick_w, brick_color):
        self.a=a
        self.b=b
        self.brick_h=brick_h
        self.brick_w=brick_w
        self.brick_color=brick_color

    def drawBrick(self, surface):
        pygame.draw.rect(surface, self.brick_color, (self.a, self.b, self.brick_w, self.brick_h))

game_over= False
class Bird:
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x , self.y), self.r)

    def __init__ (self, x, y, r, color):
        self.x=x
        self.y=y
        self.r=r
        self.color=color
    
    @staticmethod
    def path(startx, starty, power, angle, time):
        vX=math.cos(angle) * power
        vY=math.sin(angle) * power
        disX= vX*time
        disY= (vY*time) + (-4.9 * (time**2)/2)

        newX=(startx+disX)
        newY=(starty-disY)

        return (newX, newY)

    def isColided(self,brick):
        global game_over
        if (brick.b - self.r)<int(self.y) and (brick.b + self.r+ brick.brick_h)>int(self.y):
            if (brick.a - self.r)<int(self.x) and (brick.a + self.r + brick.brick_w)>int(self.x):
                dis.fill(BLACK)
                pygame.display.update()
                text = font.render("GAME OVER", True, WHITE, BLACK)
                dis.blit(text, (screen_w // 2 - 100, screen_h // 2))
                game_over=True

       
def redrawWindow():
    if not game_over:

        dis.blit(bg, (0, 0))
        bird.draw(dis)
        brick.drawBrick(dis)
        pygame.draw.line(dis, RED, line[0], line [1], 3)
        pygame.display.update()
    if game_over:
        dis.fill(BLACK)
        text = font.render("GAME OVER", True, WHITE, BLACK)
        dis.blit(text, (screen_w // 2 - 100, screen_h // 2))


def findA (pos):
    sX=bird.x
    sY=bird.y
    try:
        angle=math.atan((sY - pos[1])/(sX - pos [0]))
    except:
        angle= math. pi/2

    if pos[1] < sY and pos[0] > sX:
        angle = abs(angle)
    if pos[1] < sY and pos [0] <sX:
        angle = math.pi - angle
    if pos[1] > sY and pos [0] <sX:
        angle = math.pi + abs(angle)
    if pos[1] > sY and pos [0] >sX:
        angle = (math.pi * 2) - angle
    
    return angle


menu= True


pygame.init()
width = 1200
height= 500
dis = pygame.display.set_mode ((width, height))
pygame.display.update()
pygame.display.set_caption('Angry Birds')
run=True

kraj = pygame.image.load("kraj.png")
bg1 = pygame.image.load("abab1.png")
bg = pygame.image.load("abab.png")
BLACK= (0, 0, 0)
RED= (255, 0, 0)
WHITE=(255, 255, 255)
BROWN= (92, 46, 6)
BLUE= (168, 224, 219)


screen_w = 1200
screen_h=500
bird_r=10
bird = Bird (150, 305, bird_r, RED)
brick = Brick (screen_w-200, 157, 150, 20, BROWN)
font = pygame.font.Font('freesansbold.ttf', 40)

menu= True
while menu:
    dis.blit(bg1, (0, 0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            menu = False

x=0
y=0
time = 0
power = 0
angle = 0
shoot = False
s = False
num = 0
while not game_over:
    if shoot:
        s = True
        if bird.y< 500 - bird.r:
            time += 0.3
            po = Bird.path(x, y, power, angle, time)
            bird.x= po [0]
            bird.y= po [1]
        else:
            shoot=False
            bird.y=305
    
    pos= pygame.mouse.get_pos()
    line= [ (bird.x, bird.y), pos]
    redrawWindow()
    bird.isColided(brick)
    
    
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            run=False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if shoot == False:
                shoot = True
                x = bird.x
                y = bird.y
                time = 0
                power = math.sqrt((line[1][1]-line[0][1])**2 + (line[1][0]-line[0][0])**2)/4
                angle = findA(pos)
                if y == 307:
                     if x<830 or x>850:
                        dis.fill(BLACK)
                        text = font.render("TRY AGAIN", True, WHITE, BLACK)
                        dis.blit(text, (screen_w // 2 - 100, screen_h // 2))
                        pygame.display.update()

while game_over:
    dis.blit(kraj, (0, 0))
    pygame.display.update()
                


   
        

