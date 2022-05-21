from inspect import currentframe
import pygame
import queue
pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 751

GRID_SIZE_X = 750
GRID_SIZE_Y = 750
CELL_SIZE = 25
LINE_THICKNESS = 1

WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

EMPTY_CELL_COLOR = BLACK
GRID_COLOR = GRAY
BEGINNING_CELL_COLOR = GREEN
DESTINATION_CELL_COLOR = RED
WALL_CELL_COLOR = BLUE

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze")
font = pygame.font.SysFont('Verdana.ttf', 30)


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
matrix = []
for i in range(0, GRID_SIZE_X, CELL_SIZE):
    row = []
    for i in range(0, GRID_SIZE_Y, CELL_SIZE):
        row.append('E')
    matrix.append(row)

class CellSelectionData:
    def __init__(self, position, already_selected, coordinates):
        self.position = position
        self.already_selected = already_selected
        self.coordinates = coordinates


class Smth:
    def __init__(self, queue, len):
        self.queue = queue
        self.len = len

def draw_grid():
    for i in range(0, GRID_SIZE_X + 1, CELL_SIZE):
        pygame.draw.line(window, GRID_COLOR, (i, 0), (i, GRID_SIZE_Y), LINE_THICKNESS)
    for i in range(0, GRID_SIZE_Y + 1, CELL_SIZE):
        pygame.draw.line(window, GRID_COLOR, (0, i), (GRID_SIZE_X, i), LINE_THICKNESS)


beginning_cell = CellSelectionData(Position(-1, -1), False, Position(-1, -1))


def select_beginning_cell():
    cursor_position = Position(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    beginning_cell_data = CellSelectionData(Position(0,0), False, Position(-1, -1))

    for i in range(0, GRID_SIZE_Y, CELL_SIZE):
        beginning_cell_data.position.x = 0
        for j in range(0, GRID_SIZE_X, CELL_SIZE):
            if i <= cursor_position.x <= i + CELL_SIZE and j <= cursor_position.y <= j + CELL_SIZE:
                if window.get_at(pygame.mouse.get_pos()) == EMPTY_CELL_COLOR:
                    pygame.draw.rect(window, BEGINNING_CELL_COLOR, (i + LINE_THICKNESS, j + LINE_THICKNESS, CELL_SIZE - LINE_THICKNESS, CELL_SIZE - LINE_THICKNESS))

                    beginning_cell_data.already_selected = True
                    beginning_cell_data.coordinates.x = i
                    beginning_cell_data.coordinates.y = j

                    return beginning_cell_data

            beginning_cell_data.position.x += 1
        beginning_cell_data.position.y += 1

    return CellSelectionData(Position(-1, -1), False, Position(-1, -1))


destination_cell = CellSelectionData(Position(-1, -1), False, Position(-1, -1))


def select_destination_cell():
    cursor_position = Position(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    destination_cell_data = CellSelectionData(Position(0, 0), False, Position(-1, -1))

    for i in range(0, GRID_SIZE_Y, CELL_SIZE):
        destination_cell_data.position.x = 0
        for j in range(0, GRID_SIZE_X, CELL_SIZE):
            if i <= cursor_position.x <= i + CELL_SIZE and j <= cursor_position.y <= j + CELL_SIZE:
                if window.get_at(pygame.mouse.get_pos()) == EMPTY_CELL_COLOR:
                        pygame.draw.rect(window, DESTINATION_CELL_COLOR, (i + LINE_THICKNESS, j + LINE_THICKNESS, CELL_SIZE - LINE_THICKNESS, CELL_SIZE - LINE_THICKNESS))

                        destination_cell_data.already_selected = True
                        destination_cell_data.coordinates.x = i
                        destination_cell_data.coordinates.y = j

                        return destination_cell_data

            destination_cell_data.position.x += 1
        destination_cell_data.position.y += 1

    return CellSelectionData(Position(-1, -1), False, Position(-1, -1))


wall_cell = CellSelectionData(Position(-1, -1), False, Position(-1, -1))


def select_wall_cell():
    cursor_position = Position(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    wall_cell_data = CellSelectionData(Position(0, 0), False, Position(-1, -1))

    for i in range(0, GRID_SIZE_Y, CELL_SIZE):
        wall_cell_data.position.x = 0
        for j in range(0, GRID_SIZE_X, CELL_SIZE):
            if i <= cursor_position.x <= i + CELL_SIZE and j <= cursor_position.y <= j + CELL_SIZE:
                if window.get_at(pygame.mouse.get_pos()) == EMPTY_CELL_COLOR:
                    pygame.draw.rect(window, WALL_CELL_COLOR, (i + LINE_THICKNESS, j + LINE_THICKNESS, CELL_SIZE - LINE_THICKNESS, CELL_SIZE - LINE_THICKNESS))

                    return wall_cell_data

            wall_cell_data.position.x += 1
        wall_cell_data.position.y += 1

    return CellSelectionData(Position(-1, -1), False, Position(-1, -1))



def move_is_valid(x, y, move):
    if move == "U":
        x -= 1

    elif move == "D":
        x += 1

    elif move == "L":
        y -= 1

    elif move == "R":
        y += 1

    if not(0 <= y < len(matrix[0]) and 0 <= x < len(matrix)):
        return (False, x, y)
    elif (matrix[x][y] == "W"):
        return (False, x, y)
    return (True, x, y)

def breadth_first_search(beginning_cell):
    nums = queue.Queue()
    bili = set()
    add = ("", beginning_cell.position.x, beginning_cell.position.y)
    nums.put(add)
    while not matrix[add[1]][add[2]] == 'D': 
        add = nums.get()
        put, x, y = add
        bili.add((x, y))
        ### # ISPIS # ###
        ##pygame.draw.rect(window, (34, 150, 200), (y * CELL_SIZE + 1, x * CELL_SIZE + 1, CELL_SIZE - LINE_THICKNESS, CELL_SIZE - LINE_THICKNESS))
        ##pygame.display.update()
        for j in ["L", "R", "U", "D"]:
            noviput = put + j
            moze, novo_x, novo_y = move_is_valid(x, y, j)
            if moze:
                nums.put((noviput, novo_x, novo_y))
    return add[0]

path = ""

draw_grid()
while True:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.WINDOWCLOSE or event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if pygame.mouse.get_pressed()[0] and beginning_cell.already_selected == False:
        beginning_cell = select_beginning_cell()
        if beginning_cell.position.x >= 0 and beginning_cell.position.y >= 0:
            matrix[beginning_cell.position.x][beginning_cell.position.y] = 'B'

    if pygame.mouse.get_pressed()[0] and destination_cell.already_selected == False and beginning_cell.already_selected == True:
        destination_cell = select_destination_cell()
        if destination_cell.position.x >= 0 and destination_cell.position.y >= 0:
            matrix[destination_cell.position.x][destination_cell.position.y] = 'D'

    if pygame.mouse.get_pressed()[0] and wall_cell.already_selected == False:
        wall_cell = select_wall_cell()
        if wall_cell.position.x >= 0 and wall_cell.position.y >= 0:
            matrix[wall_cell.position.x][wall_cell.position.y] = 'W'

    if pygame.key.get_pressed()[pygame.K_SPACE] and wall_cell.already_selected == False:
        wall_cell.already_selected = True
        path = breadth_first_search(beginning_cell)
        print(path)
        posit = beginning_cell.position
        for i in range(len(path) - 1):
            if path[i] == "U":
                posit.x -= 1

            elif path[i] == "D":
                posit.x += 1

            elif path[i] == "L":
                posit.y -= 1

            elif path[i] == "R":
                posit.y += 1
            pygame.draw.rect(window, (150, 23, 200), (posit.y * CELL_SIZE + 1, posit.x * CELL_SIZE + 1, CELL_SIZE - LINE_THICKNESS, CELL_SIZE - LINE_THICKNESS))
            pygame.display.update()

    elif pygame.key.get_pressed()[pygame.K_BACKSPACE]:
        for i in range(0, int(GRID_SIZE_Y / CELL_SIZE)):
            for j in range(0, int(GRID_SIZE_X / CELL_SIZE)):
                matrix[i][j] = 'E'
        window.fill(EMPTY_CELL_COLOR)
        draw_grid()

        beginning_cell.already_selected = False
        destination_cell.already_selected = False
        wall_cell.already_selected = False

    pygame.display.update()
