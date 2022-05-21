import pygame
import math

class Object(pygame.sprite.Sprite):
    def __init__(self,x,y,w,h,tex = None,angle = 0):
        super().__init__()
        if(tex == None):
            self.image = pygame.Surface([w, h])
            self.image.fill(RED)
            pygame.draw.rect(self.image, RED, pygame.Rect(0, 0, w, h))
            self.rect = self.image.get_rect()
        else:
            self.image_orig = pygame.image.load(tex).convert_alpha()
            self.image = pygame.transform.scale(self.image_orig,(w,h))
            self.image = pygame.transform.rotate(self.image,angle)
            self.rect = self.image_orig.get_rect()
        
        self.rect.x = x
        self.rect.y = y
    def getCoords(self):
        return (self.rect.x,self.rect.y,self.rect.width,self.rect.height)

class Player(pygame.sprite.Sprite):
    def __init__(self,velocity,rotation,max_speed,x,y,imgs):
        super().__init__()
        self.image_orig = pygame.image.load(imgs).convert_alpha()
        self.image = self.image_orig.copy()
        self.rect = self.image_orig.get_rect()
        self.velocity = velocity
        self.rotation = rotation
        self.max_speed = max_speed
        self.x = x
        self.y = y
        self.lap_count = 0
        self.colliding_x = False
        self.colliding_y = False
        self.dx = 0
        self.dy = 0
        self.mask = pygame.mask.from_surface(self.image)
        

    def reverse(self,a):
        if(-self.velocity <= self.max_speed):
            self.velocity -= a


    def move(self):
        
        self.x += self.velocity * math.cos(self.rotation)
        self.y += self.velocity * math.sin(self.rotation)

        self.rect.x = self.x
        self.rect.y = self.y

    def drift(self,a):
        self.x += self.dx
        self.y += self.dy

        if(self.dx > 0.2):
            self.dx -= 0.2
        if(self.dx < -0.2):
            self.dx += 0.2
        if(self.dx >= -0.2 and self.dx <= 0.2):
            self.dx = 0

        if(self.dy > 0.2):
            self.dy -= 0.1
        if(self.dy < -0.2):
            self.dy += 0.1
        if(self.dy >= -0.5 and self.dy <= 0.5):
            self.dy = 0
        
    def collideWithScreen(self):
        if(self.x <= 0 and self.velocity*math.cos(self.rotation) < 0):
            self.velocity = 0
        if(self.x >= screen_w-self.image.get_width() and self.velocity*math.cos(self.rotation) > 0):
            self.velocity = 0
        
        if(self.y <= 0 and self.velocity*math.sin(self.rotation) < 0):
            self.velocity = 0
        if(self.y >= screen_h-self.image.get_height() and self.velocity*math.sin(self.rotation) > 0):
            self.velocity = 0

    def trigger(self,obj):
        if(self.rect.x + self.rect.width > obj[0] and self.rect.x < obj[0]+obj[2] and self.rect.y + self.rect.height > obj[1] and self.rect.y < obj[1]+obj[3]):
            return True
    
    def boost(self,obj):
        collision = pygame.sprite.collide_mask(obj,self)
        
        if(collision != None):
            if(self.velocity > 0):
                self.velocity +=3

    def collide(self,obs):
        collision = pygame.sprite.collide_mask(obs,self)
        
        if(collision != None):
            x = collision[0]
            y = collision[1]
            if(x < obs.rect.width//2):
                if(self.velocity*math.cos(self.rotation) > 0):
                    self.velocity =  0
            elif(x > obs.rect.width//2):
                if(self.velocity*math.cos(self.rotation) < 0):
                    self.velocity =  0
            elif(y < obs.rect.height//2):
                if(self.velocity*math.sin(self.rotation) > 0):
                    self.velocity =  0
            elif(y > obs.rect.height//2):
                if(self.velocity*math.sin(self.rotation) < 0):
                    self.velocity =  0

    def collideCar(self,obj,pom):
        self.collide(pom)
            
    def accelerate(self,a):
        if(self.velocity <= self.max_speed):
            self.velocity += a
            
    def brakes(self,a):
        if(self.velocity > 0.1):
            self.velocity -= a
        if(self.velocity < -0.1):
            self.velocity += a
        if(self.velocity > self.max_speed + 0.5):
            self.velocity -= a*3
        
        if(self.velocity > -0.1 and self.velocity < 0.1):
            self.velocity = 0

    def slowdown(self,s):
        if(self.velocity > s and self.velocity):
            self.velocity -= 2

    def turn(self,angle):
        self.rotation += angle
        self.image = pygame.transform.rotate(self.image_orig,-self.rotation*180/math.pi)
        self.mask = pygame.mask.from_surface(self.image)

    def lapCounter(self,s1,s2):
        col1 = False
        col2 = False
        if(self.rect.x > s1[0]  and self.rect.y > s1[1] and self.rect.x < s1[0]+s1[2] and self.rect.y < s1[1] + s1[3]):
            col1 = True
        if(self.rect.x > s2[0]  and self.rect.y > s2[1] and self.rect.x < s2[0]+s2[2] and self.rect.y < s2[1] + s2[3]):
            col2 = True
        if col1 and self.lap_count % 2 == 0:
            self.lap_count +=1
        if col2 and self.lap_count % 2 == 1:
            self.lap_count += 1
      
WHITE = (255,255,255)        
BLACK = (0,0,0)
GRASS = (135, 255, 147, 255)
ASPHALT = (128, 129, 130, 255)
RED = (255,0,0)
pygame.init()
screen_w = 1800
screen_h = 1000
dis=pygame.display.set_mode((screen_w,screen_h))
pygame.display.update()
pygame.display.set_caption('PFE Race')

all_sprites_list = pygame.sprite.Group()


obstacles = []
o1 = Object(800,800,40,100)
o2 = Object(1200,700,40,100)
all_sprites_list.add(o1)
all_sprites_list.add(o2)
obstacles.append(o1)
obstacles.append(o2)

boosts = []
b1 = Object(700,100,40,40,'boost.png')
all_sprites_list.add(b1)
boosts.append(b1)
b2 = Object(900,150,40,40,'boost.png')
all_sprites_list.add(b2)
boosts.append(b2)
b3 = Object(1000,800,40,40,'boost.png',180)
all_sprites_list.add(b3)
boosts.append(b3)


player1_startx = 250
player1_starty = 80
player1_max_speed = 7
player1_turn_rate = 0.05
player1_acceleration = 0.6
slowdowncoeff = 5
player1 = Player(0,0,player1_max_speed,player1_startx,player1_starty,'player1.png')

all_sprites_list.add(player1)
clock = pygame.time.Clock()
playercnt = 0
menu = True




title = pygame.font.Font('freesansbold.ttf', 72)
font = pygame.font.Font('freesansbold.ttf', 42)
text = title.render('PFE Race', True, BLACK, WHITE)
text2 = font.render('Pritisni 1 ili 2 za broj igraca', True, BLACK, WHITE)
textRect = text.get_rect()
text2Rect = text2.get_rect()
textRect.center = (screen_w // 2, screen_h // 2 - 200)
text2Rect.center = (screen_w // 2, screen_h // 2)


f = (390,0,100,250)
c = (1150,400,650,200)

while menu:
    dis.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.WINDOWCLOSE or event.type == pygame.QUIT:
            pygame.quit()
    dis.blit(text, textRect)
    dis.blit(text2, text2Rect)
    keys_pressed = pygame.key.get_pressed()
    if(keys_pressed[pygame.K_1]):
        playercnt = 1
        menu = False
    elif(keys_pressed[pygame.K_2]):
        menu = False
        playercnt = 2
    pygame.display.flip()
    clock.tick(60)

if(playercnt == 2):
    player2_startx = 250
    player2_starty = 180
    player2_max_speed = 7
    player2_turn_rate = 0.05
    player2_acceleration = 0.6
    player2 = Player(0,0,player2_max_speed,player2_startx,player2_starty,'player2.png')
    all_sprites_list.add(player2)

bg = pygame.image.load('track2.png').convert()
bg = pygame.transform.scale(bg, (screen_w, screen_h))

winner = 0


stopwatch = pygame.time.Clock()
minutes = 0
seconds = 0
milliseconds = 0
    


while winner == 0:
    if milliseconds > 1000:
        seconds += 1
        milliseconds -= 1000

        pygame.display.update()

    if seconds > 60:
        minutes += 1
        seconds -= 60
    milliseconds += 16
    timelabel = font.render("{}:{}.{}".format(minutes, seconds,milliseconds), True, (0,0,0))
    timerect = timelabel.get_rect()
    timerect.bottomleft = (10,screen_h - 100)
    


    dis.blit(bg,(0,0))
    #pygame.draw.rect(dis,WHITE,f)
    #pygame.draw.rect(dis,WHITE,c)
    ree = 'Player 1: ' + str(player1.lap_count//2 +1) + '/3'
    lapCnt1 = font.render(ree, True, BLACK)
    lap1Rect = lapCnt1.get_rect()
    lap1Rect.bottomleft = (10,screen_h - 50)
    if(playercnt == 2):
        ree = 'Player 2: ' + str(player2.lap_count//2 +1) + '/3'
        lapCnt2 = font.render(ree, True, BLACK)
        lap2Rect = lapCnt2.get_rect()
        lap2Rect.bottomleft = (10,screen_h - 5)
        dis.blit(lapCnt2,lap2Rect)
    dis.blit(lapCnt1,lap1Rect)
    dis.blit(timelabel,timerect)
    for event in pygame.event.get():
        if event.type == pygame.WINDOWCLOSE or event.type == pygame.QUIT:
            pygame.quit()

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_w]:
        player1.accelerate(player1_acceleration)
    if keys_pressed[pygame.K_a] and abs(player1.velocity) > 1:
        player1.turn(-player1_turn_rate*player1.velocity/8)
    if keys_pressed[pygame.K_d] and abs(player1.velocity) > 1:
        player1.turn(player1_turn_rate*player1.velocity/8)
    if keys_pressed[pygame.K_s] and player1.velocity > 0:
        player1.brakes(player1_acceleration/2)
    if keys_pressed[pygame.K_s] and player1.velocity <= 0.2:
        player1.reverse(player1_acceleration/2)
    
    if(playercnt == 2):
        if keys_pressed[pygame.K_UP]:
            player2.accelerate(player2_acceleration)
        if keys_pressed[pygame.K_LEFT] and abs(player2.velocity) > 1:
            player2.turn(-player2_turn_rate*player2.velocity/8)
        if keys_pressed[pygame.K_RIGHT] and abs(player2.velocity) > 1:
            player2.turn(player2_turn_rate*player2.velocity/8)
        if keys_pressed[pygame.K_DOWN] and player2.velocity > 0:
            player2.brakes(player2_acceleration/2)
        if keys_pressed[pygame.K_DOWN] and player2.velocity <= 0.2:
            player2.reverse(player2_acceleration/2)
    player1.brakes(0.15)
    if(playercnt == 2):
        player2.brakes(0.15)

    player1.collideWithScreen()
    if(playercnt == 2):
        player2.collideWithScreen()

    
    matertial1 = bg.get_at((player1.rect.x+player1.rect.width//2, player1.rect.y+player1.rect.height//2))
    if matertial1 == GRASS:
        player1.slowdown(slowdowncoeff)

    player1.lapCounter(c,f)
    if player1.lap_count == 6:
        winner = 1

    if(playercnt == 2):
        matertial2 = bg.get_at((player2.rect.x+player2.rect.width//2, player2.rect.y+player2.rect.height//2))
        if matertial2 == GRASS:
            player2.slowdown(slowdowncoeff)
        player2.lapCounter(c,f)
        if player2.lap_count == 6:
            winner = 2

    if(playercnt == 2):
        player1.collideCar((player2.rect.x,player2.rect.y,player2.rect.width,player2.rect.height),player2)
        player2.collideCar((player2.rect.x,player2.rect.y,player2.rect.width,player2.rect.height),player1)
        player1.drift(0.2)
        player2.drift(0.2)
        for i in obstacles:
            player2.collide(i)
        for i in boosts:
            player2.boost(i)

    for i in obstacles:
        player1.collide(i)

    for i in boosts:
        player1.boost(i)

    player1.move()
    if(playercnt == 2):
        player2.move()
    all_sprites_list.update()
    all_sprites_list.draw(dis)

    pygame.display.flip()
    clock.tick(60)

endscreen = True

while endscreen:
    dis.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.WINDOWCLOSE or event.type == pygame.QUIT:
            pygame.quit()

    if(playercnt == 2):
        s = 'Pobedio je ' + str(winner) + ' igrač!'
    else:
        s = 'Čestitamo, vreme ti je'
    winnertext = title.render(s,True,BLACK,WHITE)
    winnerrect = winnertext.get_rect()
    winnerrect.center = (screen_w//2, screen_h//3)
    timet = title.render("{}:{}.{}".format(minutes, seconds,milliseconds), True, (0,0,0))
    timerect = timet.get_rect()
    timerect.center = (screen_w//2, screen_h//2)
    dis.blit(winnertext, winnerrect)
    dis.blit(timet, timerect)
    pygame.display.flip()