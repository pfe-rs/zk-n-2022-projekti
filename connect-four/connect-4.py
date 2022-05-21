mport numpy as np
import pygame
import sys
import math

BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

ROW = 6
COLUMN = 7


def create_board():
    matrix = np.zeros((6, 7))
    return matrix


def is_valid(matrix, cols):
    if cols < 0 or cols > 6:
        return False
    elif matrix[0][cols] == 0:
        return True


def drop_piece(matrix, rows, cols):
    for r in range(rows - 1, -1, -1):
        if matrix[r][cols] == 0:
            return r


def check(matrix, piece):
    for c in range(COLUMN - 3):
        for r in range(ROW):
            if matrix[r][c] == piece and matrix[r][c + 1] == piece and matrix[r][c + 2] == piece and \
                    matrix[r][c + 3] == piece:
                return True

    for c in range(COLUMN):
        for r in range(ROW - 3):
            if matrix[r][c] == piece and matrix[r + 1][c] == piece and matrix[r + 2][c] == piece and\
                    matrix[r + 3][c] == piece:
                return True

    for c in range(COLUMN - 3):
        for r in range(ROW - 3):
            if matrix[r][c] == piece and matrix[r + 1][c + 1] == piece and matrix[r + 2][c + 2] == piece and\
                    matrix[r + 3][c + 3] == piece:
                return True

    for c in range(COLUMN - 3):
        for r in range(3, ROW):
            if matrix[r][c] == piece and matrix[r - 1][c + 1] == piece and matrix[r - 2][c + 2] == piece and\
                    board[r - 3][c + 3] == piece:
                return True


def draw_board(matrix):
    for c in range(COLUMN):
        for r in range(ROW-1, -1, -1):
            pygame.draw.rect(screen, BLUE, (c * square, r * square + square, square, square))
            pygame.draw.circle(screen, YELLOW, (int(c * square + square / 2), int(r * square + square + square / 2)), RADIUS)

    for c in range(COLUMN):
        for r in range(ROW-1, -1, -1):
            if matrix[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c * square + square / 2), int((r+1) * square + square / 2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, GREEN, (int(c * square + square / 2), int((r+1) * square + square / 2)), RADIUS)
    pygame.display.update()


board = create_board()
print(board)
print("\n")
game_over = False
turn = 0
pygame.init()
square = 100
width = COLUMN * square
height = (ROW + 1) * square
size = (width, height)
RADIUS = int(square / 2 - 5)
screen = pygame.display.set_mode(size)
screen.fill(YELLOW)
draw_board(board)
pygame.display.update()

mf = pygame.font.SysFont("monospace", 50)

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, YELLOW, (0, 0, width, square))
            x = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (x, int(square / 2)), RADIUS)
            else:
                pygame.draw.circle(screen, GREEN, (x, int(square / 2)), RADIUS)

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, YELLOW, (0, 0, width, square))
            if turn == 0:
                x = event.pos[0]
                col = int(math.floor(x / square))
                if is_valid(board, col):
                    row = drop_piece(board, ROW, col)
                    board[row][col] = 1
                    if check(board, 1):
                        label = mf.render("The winner is player 1", 1, RED)
                        screen.blit(label, (30, 10))
                        game_over = True

            else:
                x = event.pos[0]
                col = int(math.floor(x / square))
                if is_valid(board, col):
                    row = drop_piece(board, ROW, col)
                    board[row][col] = 2
                    if check(board, 2):
                        label = mf.render("The winner is player 2!", 1, GREEN)
                        screen.blit(label, (30, 10))
                        game_over = True

            print(board)
            print('\n')

            turn += 1
            turn = turn % 2
        draw_board(board)
        pygame.display.update()
        if game_over:
            pygame.time.wait(3000)
