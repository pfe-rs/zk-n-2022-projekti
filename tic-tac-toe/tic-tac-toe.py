import pygame,sys
import numpy

background=(137, 78, 204)
linecolor=(52, 19, 89)
line_width=10
d=10
sirina = 10
red=(255,255,255)

pygame.init()
screen_w = 600
screen_h = 600
dis=pygame.display.set_mode((screen_w,screen_h))
pygame.display.update()
pygame.display.set_caption(':)')
dis.fill(background)

board =numpy.zeros((3,3))

def mark(rows,columbs,player):
    board[rows][columbs]=player

def available_mark(rows,columbs):
    if board[rows][columbs]==0:
        return True
    else:
        return False

def is_board_full():
    for rows in range(3):
        for columbs in range(3):
            if board[rows][columbs]==0:
                return False
    return True

def figures():
    for rows in range(3):
        for columbs in range(3):
            #print(board[rows][columbs])
            if board[rows,columbs]==1:
                pygame.draw.circle(dis,red,(int(columbs*200+100),int(rows*200+100)),60,10)
            elif board[rows,columbs]==2:
                pygame.draw.line(dis,red,(columbs*200+40,rows*200+40),(columbs*200+200-40,rows*200+200-40),10)
                pygame.draw.line(dis,red,(columbs*200+200-40,rows*200+40),(columbs*200+40,rows*200+200-40),10)

def check_win(player):
    for columbs in range(3):
        if board[0][columbs]==player and board[1][columbs]==player and board[2][columbs]==player:
            draw_verticla_line(columbs)
            return True
    for rows in range(3):
        if board[rows][0]==player and board[rows][1]==player and board[rows][2]==player:
            draw_horisontal_line(rows)
            return True
    if board[0][2]==player and board[1][1]==player and board[2][0]==player:
        draw_desc_diagonal_line()
        return True
    if board[0][0]==player and board[1][1]==player and board[2][2]==player:
        draw_asc_diagonal_line()
        return True

def draw_verticla_line(columbs):
    posx=columbs*200+100
    pygame.draw.line(dis,red,(posx,0),(posx,600),sirina)
def draw_horisontal_line(rows):
    posy=rows*200+100
    pygame.draw.line(dis,red,(0,posy),(600,posy),sirina)
def draw_asc_diagonal_line():
    pygame.draw.line(dis,red,(0,0),(600,600),sirina)
def draw_desc_diagonal_line():
    pygame.draw.line(dis,red,(0,600),(600,0),sirina)

player=1
game_over=False

pygame.draw.line(dis,linecolor,(200,0),(200,600),10)
pygame.draw.line(dis,linecolor,(400,0),(400,600),10)
pygame.draw.line(dis,linecolor,(0,200),(600,200),10)
pygame.draw.line(dis,linecolor,(0,400),(600,400),10)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP and not game_over:
            mousex=event.pos[0]
            mousey=event.pos[1]
            click_row=int(mousey//200)
            click_columb=int(mousex//200)
            #print(click_row)
            #print(click_columb)
            if available_mark(click_row,click_columb):
                if player==1:
                    mark(click_row,click_columb,1)
                    if check_win(player):
                        game_over=True
                    player=2
                elif player==2:
                    mark(click_row,click_columb,2)
                    if check_win(player):
                        game_over=True
                    player=1
                figures()

    pygame.display.update()
