import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK_GREY = (56, 56, 56)
GREY = (93, 93, 93)
DARK_RED = (169, 37, 37)
BROWN = (139, 69, 19)
RED = (236, 18, 18)
ROSE = (255, 127, 127)
ORANGE = (255, 165, 0)
GOLD = (255, 206, 0)
YELLOW = (255, 255, 0)
LIGHT_YELLOW = (255, 250, 205)
GREEN = (0, 128, 0)
LIME = (124, 252, 0)
TURQUOISE = (0, 206, 209)
LIGHT_TURQUOISE = (64, 224, 208)
BLUE = (0, 0, 205)
BLUE_GREY = (95, 158, 160)
PURPLE = (75, 0, 130)
LAVENDER = (189, 164, 208)

current_color = BLACK
thickness = 1

def Fill(surface, pos, color):
    color = surface.map_rgb(color)
    array = pygame.surfarray.pixels2d(surface)
    c_color = array[pos]
    
    front = [pos]
    while len(front) > 0:
        x, y = front.pop()
        try:
            if array[x, y] != c_color:
                continue
        except IndexError:
            continue
        array[x, y] = color
        front.append((x + 1, y))
        front.append((x - 1, y))
        front.append((x, y + 1))
        front.append((x, y - 1))

    pygame.surfarray.blit_array(surface, array)

class Bucket_Button:
    def __init__(self, x, y, a, b, color):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.color = color
        
    def clicked(self, x1, y1):
        if (x1 <= self.x + self.a and x1 >= self.x) and (y1 <= self.y + self.b and y1 >= self.y) and self.color == RED:
            self.color = GREEN
        elif (x1 <= self.x + self.a and x1 >= self.x) and (y1 <= self.y + self.b and y1 >= self.y) and self.color == GREEN:
            self.color = RED

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.a, self.b))
        pygame.draw.rect(surface, BLACK, (self.x, self.y, self.a, self.b), 1, border_radius = 1)

class Clear_Button:
    def __init__(self, x, y, a):
        self.x = x
        self.y = y
        self.a = a

    def clicked(self, x1, y1):
        if x1 <= self.x + self.a and x1 >= self.x and y1 <= self.y + self.a and y1 >= self.y:
            return True
        else:
            return False

    def draw(self, surface):
        pygame.draw.line(surface, RED, (self.x, self.y), (self.x + self.a, self.y + self.a), 3)
        pygame.draw.line(surface, RED, (self.x + self.a, self.y), (self.x, self.y + self.a), 3)

class Thickness_Plus:
    def __init__(self, x, y, a):
        self.x = x
        self.y = y
        self.a = a

    def clicked(self, x1, y1):
        if x1 <= self.x + self.a and x1 >= self.x and y1 <= self.y + self.a and y1 >= self.y:
            global thickness
            if thickness < 10:
                thickness += 1
            print(thickness)

    def draw(self, surface):
        pygame.draw.line(surface, BLACK, (self.x + self.a // 2, self.y), (self.x + self.a // 2, self.y + self.a), 3)
        pygame.draw.line(surface, BLACK, (self.x, self.y + self.a // 2), (self.x + self.a, self.y + self.a // 2), 3)

class Thickness_Minus:
    def __init__(self, x, y, a):
        self.x = x
        self.y = y
        self.a = a

    def clicked(self, x1, y1):
        if x1 <= self.x + self.a and x1 >= self.x and y1 <= self.y + self.a and y1 >= self.y:
            global thickness
            if thickness > 1:
                thickness -= 1
            print(thickness)

    def draw(self, surface):
        pygame.draw.line(surface, BLACK, (self.x, self.y + self.a // 2), (self.x + self.a, self.y + self.a // 2), 3)

class Black_Button:
    def __init__(self, x, y, a, color):
        self.x = x
        self.y = y
        self.a = a
        self.color = color

    def clicked(self, x1, y1):
        if x1 <= self.x + self.a and x1 >= self.x and y1 <= self.y + self.a and y1 >= self.y:
            global current_color
            current_color = BLACK
            self.color = YELLOW
        else:
            self.color = BLACK

    def draw(self, surface):
        pygame.draw.rect(surface, BLACK, (self.x, self.y, self.a, self.a))
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.a, self.a), 1, border_radius = 1)

class White_Button:
    def __init__(self, x, y, a, color):
        self.x = x
        self.y = y
        self.a = a
        self.color = color

    def clicked(self, x1, y1):
        if x1 <= self.x + self.a and x1 >= self.x and y1 <= self.y + self.a and y1 >= self.y:
            global current_color
            current_color = WHITE
            self.color = YELLOW
        else:
            self.color = BLACK

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, (self.x, self.y, self.a, self.a))
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.a, self.a), 1, border_radius = 1)
        
class Dark_Grey_Button:
    def __init__(self, x, y, a, color):
        self.x = x
        self.y = y
        self.a = a
        self.color = color

    def clicked(self, x1, y1):
        if x1 <= self.x + self.a and x1 >= self.x and y1 <= self.y + self.a and y1 >= self.y:
            global current_color
            current_color = DARK_GREY
            self.color = YELLOW
        else:
            self.color = BLACK

    def draw(self, surface):
        pygame.draw.rect(surface, DARK_GREY, (self.x, self.y, self.a, self.a))
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.a, self.a), 1, border_radius = 1)

class Grey_Button:
    def __init__(self, x, y, a, color):
        self.x = x
        self.y = y
        self.a = a
        self.color = color

    def clicked(self, x1, y1):
        if x1 <= self.x + self.a and x1 >= self.x and y1 <= self.y + self.a and y1 >= self.y:
            global current_color
            current_color = GREY
            self.color = YELLOW
        else:
            self.color = BLACK

    def draw(self, surface):
        pygame.draw.rect(surface, GREY, (self.x, self.y, self.a, self.a))
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.a, self.a), 1, border_radius = 1)

class Dark_Red_Button:
    def __init__(self, x, y, a, color):
        self.x = x
        self.y = y
        self.a = a
        self.color = color

    def clicked(self, x1, y1):
        if x1 <= self.x + self.a and x1 >= self.x and y1 <= self.y + self.a and y1 >= self.y:
            global current_color
            current_color = DARK_RED
            self.color = YELLOW
        else:
            self.color = BLACK

    def draw(self, surface):
        pygame.draw.rect(surface, DARK_RED, (self.x, self.y, self.a, self.a))
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.a, self.a), 1, border_radius = 1)

class Brown_Button:
    def __init__(self, x, y, a, color):
        self.x = x
        self.y = y
        self.a = a
        self.color = color

    def clicked(self, x1, y1):
        if x1 <= self.x + self.a and x1 >= self.x and y1 <= self.y + self.a and y1 >= self.y:
            global current_color
            current_color = BROWN
            self.color = YELLOW
        else:
            self.color = BLACK

    def draw(self, surface):
        pygame.draw.rect(surface, BROWN, (self.x, self.y, self.a, self.a))
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.a, self.a), 1, border_radius = 1)

class Red_Button:
    def __init__(self, x, y, a, color):
        self.x = x
        self.y = y
        self.a = a
        self.color = color

    def clicked(self, x1, y1):
        if x1 <= self.x + self.a and x1 >= self.x and y1 <= self.y + self.a and y1 >= self.y:
            global current_color
            current_color = RED
            self.color = YELLOW
        else:
            self.color = BLACK

    def draw(self, surface):
        pygame.draw.rect(surface, RED, (self.x, self.y, self.a, self.a))
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.a, self.a), 1, border_radius = 1)

class Rose_Button:
    def __init__(self, x, y, a, color):
        self.x = x
        self.y = y
        self.a = a
        self.color = color

    def clicked(self, x1, y1):
        if x1 <= self.x + self.a and x1 >= self.x and y1 <= self.y + self.a and y1 >= self.y:
            global current_color
            current_color = ROSE
            self.color = YELLOW
        else:
            self.color = BLACK

    def draw(self, surface):
        pygame.draw.rect(surface, ROSE, (self.x, self.y, self.a, self.a))
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.a, self.a), 1, border_radius = 1)

class Orange_Button:
    def __init__(self, x, y, a, color):
        self.x = x
        self.y = y
        self.a = a
        self.color = color

    def clicked(self, x1, y1):
        if x1 <= self.x + self.a and x1 >= self.x and y1 <= self.y + self.a and y1 >= self.y:
            global current_color
            current_color = ORANGE
            self.color = YELLOW
        else:
            self.color = BLACK

    def draw(self, surface):
        pygame.draw.rect(surface, ORANGE, (self.x, self.y, self.a, self.a))
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.a, self.a), 1, border_radius = 1)

class Gold_Button:
    def __init__(self, x, y, a, color):
        self.x = x
        self.y = y
        self.a = a
        self.color = color

    def clicked(self, x1, y1):
        if x1 <= self.x + self.a and x1 >= self.x and y1 <= self.y + self.a and y1 >= self.y:
            global current_color
            current_color = GOLD
            self.color = YELLOW
        else:
            self.color = BLACK

    def draw(self, surface):
        pygame.draw.rect(surface, GOLD, (self.x, self.y, self.a, self.a))
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.a, self.a), 1, border_radius = 1)

class Yellow_Button:
    def __init__(self, x, y, a, color):
        self.x = x
        self.y = y
        self.a = a
        self.color = color

    def clicked(self, x1, y1):
        if x1 <= self.x + self.a and x1 >= self.x and y1 <= self.y + self.a and y1 >= self.y:
            global current_color
            current_color = YELLOW
            self.color = YELLOW
        else:
            self.color = BLACK

    def draw(self, surface):
        pygame.draw.rect(surface, YELLOW, (self.x, self.y, self.a, self.a))
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.a, self.a), 1, border_radius = 1)

class Light_Yellow_Button:
    def __init__(self, x, y, a, color):
        self.x = x
        self.y = y
        self.a = a
        self.color = color

    def clicked(self, x1, y1):
        if x1 <= self.x + self.a and x1 >= self.x and y1 <= self.y + self.a and y1 >= self.y:
            global current_color
            current_color = LIGHT_YELLOW
            self.color = YELLOW
        else:
            self.color = BLACK

    def draw(self, surface):
        pygame.draw.rect(surface, LIGHT_YELLOW, (self.x, self.y, self.a, self.a))
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.a, self.a), 1, border_radius = 1)

class Green_Button:
    def __init__(self, x, y, a, color):
        self.x = x
        self.y = y
        self.a = a
        self.color = color

    def clicked(self, x1, y1):
        if x1 <= self.x + self.a and x1 >= self.x and y1 <= self.y + self.a and y1 >= self.y:
            global current_color
            current_color = GREEN
            self.color = YELLOW
        else:
            self.color = BLACK

    def draw(self, surface):
        pygame.draw.rect(surface, GREEN, (self.x, self.y, self.a, self.a))
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.a, self.a), 1, border_radius = 1)

class Lime_Button:
    def __init__(self, x, y, a, color):
        self.x = x
        self.y = y
        self.a = a
        self.color = color

    def clicked(self, x1, y1):
        if x1 <= self.x + self.a and x1 >= self.x and y1 <= self.y + self.a and y1 >= self.y:
            global current_color
            current_color = LIME
            self.color = YELLOW
        else:
            self.color = BLACK

    def draw(self, surface):
        pygame.draw.rect(surface, LIME, (self.x, self.y, self.a, self.a))
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.a, self.a), 1, border_radius = 1)

class Turquoise_Button:
    def __init__(self, x, y, a, color):
        self.x = x
        self.y = y
        self.a = a
        self.color = color

    def clicked(self, x1, y1):
        if x1 <= self.x + self.a and x1 >= self.x and y1 <= self.y + self.a and y1 >= self.y:
            global current_color
            current_color = TURQUOISE
            self.color = YELLOW
        else:
            self.color = BLACK

    def draw(self, surface):
        pygame.draw.rect(surface, TURQUOISE, (self.x, self.y, self.a, self.a))
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.a, self.a), 1, border_radius = 1)

class Light_Turquoise_Button:
    def __init__(self, x, y, a, color):
        self.x = x
        self.y = y
        self.a = a
        self.color = color

    def clicked(self, x1, y1):
        if x1 <= self.x + self.a and x1 >= self.x and y1 <= self.y + self.a and y1 >= self.y:
            global current_color
            current_color = LIGHT_TURQUOISE
            self.color = YELLOW
        else:
            self.color = BLACK

    def draw(self, surface):
        pygame.draw.rect(surface, LIGHT_TURQUOISE, (self.x, self.y, self.a, self.a))
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.a, self.a), 1, border_radius = 1)

class Blue_Button:
    def __init__(self, x, y, a, color):
        self.x = x
        self.y = y
        self.a = a
        self.color = color

    def clicked(self, x1, y1):
        if x1 <= self.x + self.a and x1 >= self.x and y1 <= self.y + self.a and y1 >= self.y:
            global current_color
            current_color = BLUE
            self.color = YELLOW
        else:
            self.color = BLACK

    def draw(self, surface):
        pygame.draw.rect(surface, BLUE, (self.x, self.y, self.a, self.a))
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.a, self.a), 1, border_radius = 1)

class Blue_Grey_Button:
    def __init__(self, x, y, a, color):
        self.x = x
        self.y = y
        self.a = a
        self.color = color

    def clicked(self, x1, y1):
        if x1 <= self.x + self.a and x1 >= self.x and y1 <= self.y + self.a and y1 >= self.y:
            global current_color
            current_color = BLUE_GREY
            self.color = YELLOW
        else:
            self.color = BLACK

    def draw(self, surface):
        pygame.draw.rect(surface, BLUE_GREY, (self.x, self.y, self.a, self.a))
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.a, self.a), 1, border_radius = 1)

class Purple_Button:
    def __init__(self, x, y, a, color):
        self.x = x
        self.y = y
        self.a = a
        self.color = color

    def clicked(self, x1, y1):
        if x1 <= self.x + self.a and x1 >= self.x and y1 <= self.y + self.a and y1 >= self.y:
            global current_color
            current_color = PURPLE
            self.color = YELLOW
        else:
            self.color = BLACK

    def draw(self, surface):
        pygame.draw.rect(surface, PURPLE, (self.x, self.y, self.a, self.a))
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.a, self.a), 1, border_radius = 1)
        
class Lavender_Button:
    def __init__(self, x, y, a, color):
        self.x = x
        self.y = y
        self.a = a
        self.color = color

    def clicked(self, x1, y1):
        if x1 <= self.x + self.a and x1 >= self.x and y1 <= self.y + self.a and y1 >= self.y:
            global current_color
            current_color = LAVENDER
            self.color = YELLOW
        else:
            self.color = BLACK

    def draw(self, surface):
        pygame.draw.rect(surface, LAVENDER, (self.x, self.y, self.a, self.a))
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.a, self.a), 1, border_radius = 1)
          
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Paint') 
drawing = False
hold = True
hold1 = True
last_pos = None
right = False
left = False
screen_w = 1280
screen_h = 720
dis = pygame.display.set_mode((screen_w, screen_h), pygame.RESIZABLE)
pygame.display.update()
mouse_pos = (0, 0)
dis.fill(WHITE)
butt = Bucket_Button(20, 10, 101, 61, RED)
clear = Clear_Button(140, 10, 61)
plus = Thickness_Plus(640, 10, 61)
minus = Thickness_Minus(560, 10, 61)
black = Black_Button(720, 10, 41, YELLOW)
white = White_Button(720, 51, 41, BLACK)
dark_grey = Dark_Grey_Button(761, 10, 41, BLACK)
grey = Grey_Button(761, 51, 41, BLACK)
dark_red = Dark_Red_Button(802, 10, 41, BLACK)
brown = Brown_Button(802, 51, 41, BLACK)
red = Red_Button(843, 10, 41, BLACK)
rose = Rose_Button(843, 51, 41, BLACK)
orange = Orange_Button(884, 10, 41, BLACK)
gold = Gold_Button(884, 51, 41, BLACK)
yellow = Yellow_Button(925, 10, 41, BLACK)
light_yellow = Light_Yellow_Button(925, 51, 41, BLACK)
green = Green_Button(966, 10, 41, BLACK)
lime = Lime_Button(966, 51, 41, BLACK)
turquoise = Turquoise_Button(1007, 10, 41, BLACK)
light_turquoise = Light_Turquoise_Button(1007, 51, 41, BLACK)
blue = Blue_Button(1048, 10, 41, BLACK)
blue_grey = Blue_Grey_Button(1048, 51, 41, BLACK)
purple = Purple_Button(1089, 10, 41, BLACK)
lavender = Lavender_Button(1089, 51, 41, BLACK)

while True:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            if drawing:
                if last_pos is not None:
                    if right:
                        pygame.draw.line(dis, current_color, last_pos, mouse_pos, thickness)
                    elif left:
                        pygame.draw.line(dis, WHITE, last_pos, mouse_pos, 5)
                last_pos = mouse_pos
        if event.type == pygame.MOUSEBUTTONUP:
            last_pos = None
            drawing = False
            hold = True
            hold1 = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            if event.button == 1:
                right = True
                left = False
            elif event.button == 3:
                left = True
                right = False
            if hold and mouse_pos[0] >= 560 and mouse_pos[0] < 720 and mouse_pos[1] < 90:
                plus.clicked(mouse_pos[0], mouse_pos[1])
                minus.clicked(mouse_pos[0], mouse_pos[1])
            elif hold and mouse_pos[0] >=720 and mouse_pos[1] < 90:
                black.clicked(mouse_pos[0], mouse_pos[1])
                white.clicked(mouse_pos[0], mouse_pos[1])
                dark_grey.clicked(mouse_pos[0], mouse_pos[1])
                grey.clicked(mouse_pos[0], mouse_pos[1])
                dark_red.clicked(mouse_pos[0], mouse_pos[1])
                brown.clicked(mouse_pos[0], mouse_pos[1])
                red.clicked(mouse_pos[0], mouse_pos[1])
                rose.clicked(mouse_pos[0], mouse_pos[1])
                orange.clicked(mouse_pos[0], mouse_pos[1])
                gold.clicked(mouse_pos[0], mouse_pos[1])
                yellow.clicked(mouse_pos[0], mouse_pos[1])
                light_yellow.clicked(mouse_pos[0], mouse_pos[1])
                green.clicked(mouse_pos[0], mouse_pos[1])
                lime.clicked(mouse_pos[0], mouse_pos[1])
                turquoise.clicked(mouse_pos[0], mouse_pos[1])
                light_turquoise.clicked(mouse_pos[0], mouse_pos[1])
                blue.clicked(mouse_pos[0], mouse_pos[1])
                blue_grey.clicked(mouse_pos[0], mouse_pos[1])
                purple.clicked(mouse_pos[0], mouse_pos[1])
                lavender.clicked(mouse_pos[0], mouse_pos[1])
                hold = False
            elif hold and mouse_pos[0] < 560 and mouse_pos[1] < 90:
                butt.clicked(mouse_pos[0], mouse_pos[1])
                if clear.clicked(mouse_pos[0], mouse_pos[1]):
                    dis.fill(WHITE)
                hold = False
            if butt.color == GREEN and hold1 and mouse_pos[1] > 90:
                Fill(dis, mouse_pos, current_color)
                hold1 = False

    pygame.draw.rect(dis, WHITE, (0, 0, 1280, 91))
    pygame.draw.line(dis, BLACK, (0, 91), (1280, 91))
    butt.draw(dis)
    clear.draw(dis)
    plus.draw(dis)
    minus.draw(dis)
    black.draw(dis)
    white.draw(dis)
    dark_grey.draw(dis)
    grey.draw(dis)
    dark_red.draw(dis)
    brown.draw(dis)
    red.draw(dis)
    rose.draw(dis)
    orange.draw(dis)
    gold.draw(dis)
    yellow.draw(dis)
    light_yellow.draw(dis)
    green.draw(dis)
    lime.draw(dis)
    turquoise.draw(dis)
    light_turquoise.draw(dis)
    blue.draw(dis)
    blue_grey.draw(dis)
    purple.draw(dis)
    lavender.draw(dis)
    #pygame.draw.rect(dis, BLACK, (680, 20, 411, 82), 1, border_radius = 1)
    pygame.display.update()
    clock.tick(60)
