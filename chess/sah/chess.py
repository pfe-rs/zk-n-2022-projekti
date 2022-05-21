import pygame
import sys

SCREEN_HEIGHT = 720
SCREEN_WIDTH = 720
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Chess')


pygame.font.init()

WHITE = (255,255,255)
GREEN = (0,200,150)
BLACK = (0,0,0)
BROWN = (47,79,80)
RED = (255,0,0)
GRAY = (0,128,128)
YELLOW = (30,144,255)
CYAN = (72,61,139)

img = pygame.image.load('images/white_king.png')
WHITE_KING = pygame.transform.scale(img, (70, 70))

img = pygame.image.load('images/white_queen.png')
WHITE_QUEEN = pygame.transform.scale(img, (70, 70))

img = pygame.image.load('images/white_bishop.png')
WHITE_BISHOP = pygame.transform.scale(img, (70, 70))

img = pygame.image.load('images/white_knight.png')
WHITE_KNIGHT = pygame.transform.scale(img, (70, 70))

img = pygame.image.load('images/white_rook.png')
WHITE_ROOK = pygame.transform.scale(img, (70, 70))

img = pygame.image.load('images/white_pawn.png')
WHITE_PAWN = pygame.transform.scale(img, (70, 70))


img = pygame.image.load('images/black_king.png')
BLACK_KING = pygame.transform.scale(img, (70, 70))

img = pygame.image.load('images/black_queen.png')
BLACK_QUEEN = pygame.transform.scale(img, (70, 70))

img = pygame.image.load('images/black_bishop.png')
BLACK_BISHOP = pygame.transform.scale(img, (70, 70))

img = pygame.image.load('images/black_knight.png')
BLACK_KNIGHT = pygame.transform.scale(img, (70, 70))

img = pygame.image.load('images/black_rook.png')
BLACK_ROOK = pygame.transform.scale(img, (70, 70))

img = pygame.image.load('images/black_pawn.png')
BLACK_PAWN = pygame.transform.scale(img, (70, 70))



class Piece :
    def __init__(self, pos) :
        self.name = None
        self.color = None
        self.img = None
        self.pos = pos

        self.first_move = True
        self.check = False

class ChessBoard :
    def __init__(self) :
        self.board = [[Piece((i, j)) for j in range(8)] for i in range(8)]
        self.width = 80

        self.set_pieces()
        self.white_king_pos = (7, 4)
        self.black_king_pos = (0, 4)

    def set_pieces(self) :
        white_king = self.board[7][4]
        white_king.name = 'K'
        white_king.color = 'W'
        white_king.img = WHITE_KING

        white_queen = self.board[7][3]
        white_queen.name = 'Q'
        white_queen.color = 'W'
        white_queen.img = WHITE_QUEEN

        white_bishop = self.board[7][2]
        white_bishop.name = 'B'
        white_bishop.color = 'W'
        white_bishop.img = WHITE_BISHOP

        white_bishop = self.board[7][5]
        white_bishop.name = 'B'
        white_bishop.color = 'W'
        white_bishop.img = WHITE_BISHOP

        white_knight = self.board[7][1]
        white_knight.name = 'N'
        white_knight.color = 'W'
        white_knight.img = WHITE_KNIGHT

        white_knight = self.board[7][6]
        white_knight.name = 'N'
        white_knight.color = 'W'
        white_knight.img = WHITE_KNIGHT

        white_rook = self.board[7][0]
        white_rook.name = 'R'
        white_rook.color = 'W'
        white_rook.img = WHITE_ROOK

        white_rook = self.board[7][7]
        white_rook.name = 'R'
        white_rook.color = 'W'
        white_rook.img = WHITE_ROOK

        for j in range(8) :
            white_pawn = self.board[6][j]
            white_pawn.name = 'P'
            white_pawn.color = 'W'
            white_pawn.img = WHITE_PAWN


        black_king = self.board[0][4]
        black_king.name = 'K'
        black_king.color = 'B'
        black_king.img = BLACK_KING

        black_queen = self.board[0][3]
        black_queen.name = 'Q'
        black_queen.color = 'B'
        black_queen.img = BLACK_QUEEN

        black_bishop = self.board[0][2]
        black_bishop.name = 'B'
        black_bishop.color = 'B'
        black_bishop.img = BLACK_BISHOP

        black_bishop = self.board[0][5]
        black_bishop.name = 'B'
        black_bishop.color = 'B'
        black_bishop.img = BLACK_BISHOP

        black_knight = self.board[0][1]
        black_knight.name = 'N'
        black_knight.color = 'B'
        black_knight.img = BLACK_KNIGHT

        black_knight = self.board[0][6]
        black_knight.name = 'N'
        black_knight.color = 'B'
        black_knight.img = BLACK_KNIGHT

        black_rook = self.board[0][0]
        black_rook.name = 'R'
        black_rook.color = 'B'
        black_rook.img = BLACK_ROOK

        black_rook = self.board[0][7]
        black_rook.name = 'R'
        black_rook.color = 'B'
        black_rook.img = BLACK_ROOK

        for j in range(8) :
            black_pawn = self.board[1][j]
            black_pawn.name = 'P'
            black_pawn.color = 'B'
            black_pawn.img = BLACK_PAWN

    def show(self) :
        for i in range(8) :
            for j in range(8) :

                if (i + j) % 2 == 0 :
                    cell_color = WHITE
                else :
                    cell_color = BROWN

                pygame.draw.rect(win, cell_color, (j * self.width + 40, i * self.width + 40, self.width, self.width))

        font = pygame.font.SysFont('Consolas', 30)
        for i in range(8) :
            text = font.render(str(i + 1), True, WHITE)
            win.blit(text, (12, (8 - i) * self.width - 18))
            

        for j in range(8) :
            text = font.render(chr(65 + j), True, WHITE)
            
            win.blit(text, ((j + 1) * self.width - 8, 685))

        for i in range(8) :
            for j in range(8) :
                piece = self.board[i][j]
                if piece.name is not None :
                    if piece.check :
                        pygame.draw.rect(win, RED, (j * self.width + 40, i * self.width + 40, self.width, self.width))

                    win.blit(self.board[i][j].img, (j * self.width + 43, i * self.width + 43))

    def show_options(self, i, j, move_color, select = True) :
        piece = self.board[i][j]
        
        if piece.name is None :
            return []

        if select :
            pygame.draw.rect(win, YELLOW, (j * self.width + 40, i * self.width + 40, self.width, self.width))
            win.blit(self.board[i][j].img, (j * self.width + 43, i * self.width + 43))

        options = []

        if move_color != piece.color :
            return []

        if piece.name == 'P' :
            
            if piece.color == 'W' :
                d = -1
            else :
                d = 1

            if 0 <= i + d < 8:
                if 0 <= j + d < 8 :
                    enemy = self.board[i + d][j + d] 
                    if enemy.name is not None :
                        if enemy.color != piece.color :
                            options.append((i + d, j + d))
                
                if 0 <= j - d < 8 :
                    enemy = self.board[i + d][j - d] 
                    if enemy.name is not None :
                        if enemy.color != piece.color :
                            options.append((i + d, j - d))
        
                if self.board[i + d][j].name is None : 
                    options.append((i + d, j))

            
            if piece.first_move :
                if 0 <= i + 1 * d < 8 :
                    if self.board[i + 1 * d][j].name is None :
                        if 0 <= i + 2 * d < 8 :
                            enemy = self.board[i + 2 * d][j]
                            if enemy.name is None :
                                options.append((i + 2 * d, j))

        if piece.name == 'B' or piece.name == 'Q' :

            for k1 in range(-1, 2, 2) :
                for k2 in range(-1, 2, 2) :
                    for d in range(1, 8) :
                        if 0 <= i - k1 * d < 8 and 0 <= j - k2 * d < 8 :
                            enemy = self.board[i - k1 * d][j - k2 * d]

                            if enemy.name is not None :
                                if enemy.color == piece.color :
                                    break

                            options.append((i - k1 * d, j - k2 * d))

                            if enemy.name is not None :
                                break

        if piece.name == 'R' or piece.name == 'Q':
            
            for k1 in range(-1, 2, 2) :
                for d in range(1, 8) :
                    if 0 <= i - k1 * d < 8  :
                        enemy = self.board[i - k1 * d][j]

                        if enemy.name is not None :
                            if enemy.color == piece.color :
                                break

                        options.append((i - k1 * d, j))

                        if enemy.name is not None :
                            break
            for k2 in range(-1, 2, 2) :
                for d in range(1, 8) :
                    if 0 <= j - k2 * d < 8  :
                        enemy = self.board[i][j - k2 * d]

                        if enemy.name is not None :
                            if enemy.color == piece.color :
                                break

                        options.append((i, j - k2 * d))

                        if enemy.name is not None :
                            break

        if piece.name == 'K' :
            
            for d1 in range(-1, 2) :
                for d2 in range(-1, 2) :
                    if d1 == 0 and d2 == 0 :
                        continue
                    
                    if 0 <= i + d1 < 8 and 0 <= j + d2 < 8 :
                        enemy = self.board[i + d1][j + d2]

                        if enemy.name is not None :
                            if enemy.color == piece.color :
                                continue

                        options.append((i + d1, j + d2))

           
            if piece.first_move :
                rook1 = self.board[i][j + 3]
                if rook1.name == 'R' and rook1.color == piece.color:
                    if rook1.first_move :
                        if self.board[i][j + 1].name is None and self.board[i][j + 2].name is None :
                            if not self.in_check(self.black_king_pos) :
                                options.append((i, j + 2))

                rook2 = self.board[i][j - 4]
                if rook2.name == 'R' and rook2.color == piece.color and rook2.first_move :
                    if self.board[i][j - 1].name is None and self.board[i][j - 2].name is None and self.board[i][j - 3].name is None :
                        options.append((i, j - 2)) 

        if piece.name == 'N' :

            for d1 in range(-2, 3) :
                for d2 in range(-2, 3) :
                    if abs(d1) + abs(d2) == 3 :

                        if 0 <= i + d1 < 8 and 0 <= j + d2 < 8 :
                            enemy = self.board[i + d1][j + d2]

                            if enemy.name is not None :
                                if enemy.color == piece.color :
                                    continue

                            options.append((i + d1, j + d2)) 

        return options

    def move(self, prev_i, prev_j, new_i, new_j) :
        piece = self.board[prev_i][prev_j]
        piece.first_move = False

        
        if piece.name == 'K' :
            if new_j == prev_j + 2 :
                self.board[new_i][new_j - 1] = self.board[prev_i][prev_j + 3]
                self.board[prev_i][prev_j + 3] = Piece((prev_i, prev_j + 3))
            elif new_j == prev_j - 2 :
                self.board[new_i][new_j + 1] = self.board[prev_i][prev_j - 4]
                self.board[prev_i][prev_j - 4] = Piece((prev_i, prev_j - 4))

       
        if piece.name == 'P' :
            if new_i == 0 or new_i == 7 :
                piece = Piece((new_i, new_j))

                valid = False
                while not valid :
                    done = False
                    while not done :
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_q:
                                    ch = 'q'
                                elif event.key == pygame.K_r:
                                    ch = 'r'
                                elif event.key == pygame.K_b:
                                    ch = 'b'
                                elif event.key == pygame.K_n:
                                    ch = 'n'
                                elif event.key == pygame.K_RETURN :
                                    done = True
                    
                    ch = ch.upper()

                    if ch in ['Q', 'R', 'B', 'N'] :
                        valid = True

                        piece.name = ch

                        if new_i == 0 :
                            piece.color = 'W'
                        else :
                            piece.color = 'B'    

                        if ch == 'Q' :
                            if piece.color == 'W' :
                                piece.img = WHITE_QUEEN
                            else :
                                piece.img = BLACK_QUEEN

                        elif ch == 'R' :
                            if piece.color == 'W' :
                                piece.img = WHITE_ROOK
                            else :
                                piece.img = BLACK_ROOK

                        elif ch == 'B' :
                            if piece.color == 'W' :
                                piece.img = WHITE_BISHOP
                            else :
                                piece.img = BLACK_BISHOP

                        elif ch == 'N' :
                            if piece.color == 'W' :
                                piece.img = WHITE_KNIGHT
                            else :
                                piece.img = WHITE_KNIGHT

        if piece.name == 'K' :
            if piece.color == 'W' :
                self.white_king_pos = (new_i, new_j)
            else :
                self.black_king_pos = (new_i, new_j)

        self.board[new_i][new_j] = piece
        self.board[prev_i][prev_j] = Piece((prev_i, prev_j))

    def temp_move(self, prev_i, prev_j, new_i, new_j) :
        piece = self.board[prev_i][prev_j]
        temp = self.board[new_i][new_j] 

        self.board[new_i][new_j] = piece
        self.board[prev_i][prev_j] = Piece((prev_i, prev_j))

        if piece.name == 'K' :
            if piece.color == 'W' :
                self.white_king_pos = (new_i, new_j)
            else :
                self.black_king_pos = (new_i, new_j)

        return temp    

    def rev_temp_move(self, prev_i, prev_j, new_i, new_j, temp) :
        piece = self.board[new_i][new_j]
        self.board[prev_i][prev_j] = self.board[new_i][new_j]
        self.board[new_i][new_j] = temp

        if piece.name == 'K' :
            if piece.color == 'W' :
                self.white_king_pos = (prev_i, prev_j)
            else :
                self.black_king_pos = (prev_i, prev_j)

    def in_check(self, pos) :
        i = pos[0]
        j = pos[1]
        check = False
        king = self.board[i][j]
        if king.name == 'K' :
            
            for k1 in range(-1, 2, 2) :
                for d in range(1, 8) :
                    if 0 <= i - k1 * d < 8  :
                        enemy = self.board[i - k1 * d][j]
                        if enemy.name is None :
                            continue
                        else :
                            if enemy.color != king.color :
                                if enemy.name == 'R' or enemy.name == 'Q' :
                                    check = True
                            break

            for k2 in range(-1, 2, 2) :
                for d in range(1, 8) :
                    if 0 <= j - k2 * d < 8  :
                        enemy = self.board[i][j - k2 * d]
                        if enemy.name is None :
                            continue
                        else :
                            if enemy.color != king.color :
                                if enemy.name == 'R' or enemy.name == 'Q' :
                                    check = True
                            break 

            for k1 in range(-1, 2, 2) :
                for k2 in range(-1, 2, 2) :
                    for d in range(1, 8) :
                        if 0 <= i - k1 * d < 8 and 0 <= j - k2 * d < 8 :
                            enemy = self.board[i - k1 * d][j - k2 * d]
                            if enemy.name is None :
                                continue
                            else :
                                if enemy.color != king.color :
                                    if enemy.name == 'B' or enemy.name == 'Q' :
                                        check = True
                                break     
            
            for d1 in range(-2, 3) :
                for d2 in range(-2, 3) :
                    if abs(d1) + abs(d2) == 3 :
                        if 0 <= i + d1 < 8 and 0 <= j + d2 < 8 :
                            enemy = self.board[i + d1][j + d2]
                            if enemy.name is None :
                                continue
                            else :
                                if enemy.color != king.color :
                                    if enemy.name == 'N' :
                                        check = True
                                break

            if king.color == 'W' :
                if i - 1 >= 0 :
                    if j + 1 < 8 :
                        enemy = self.board[i - 1][j + 1] 
                        if enemy.name == 'P' and enemy.color != king.color :
                            check = True
                        
                    if j - 1 >= 0 :
                        enemy = self.board[i - 1][j - 1] 
                        if enemy.name == 'P' and enemy.color != king.color :
                            check = True

            else :
                if i + 1 < 8 :
                    if j + 1 < 8 :
                        enemy = self.board[i + 1][j + 1] 
                        if enemy.name == 'P' and enemy.color != king.color :
                            check = True
                        
                    if j - 1 >= 0 :
                        enemy = self.board[i + 1][j - 1] 
                        if enemy.name == 'P' and enemy.color != king.color :
                            check = True

            if check == True :
                return True

        return False

chess = ChessBoard()

touched_piece = False
showing_options = False
options = []
new_options = []
i = 0
j = 0
move_color = 'W'

run = True
while run :

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False

    win.fill(BROWN) 

    chess.show()

    king_i, king_j = chess.white_king_pos
    if chess.in_check(chess.white_king_pos) :
        chess.board[king_i][king_j].check = True 

        total = 0
        for ii in range(8) :
            for jj in range(8) :
                if total > 0 :
                    break
                
                piece = chess.board[ii][jj]
                if piece.name is None or piece.color == 'B' :
                    continue

                opt = chess.show_options(ii, jj, 'W', False)

                new_opt = []
                for pos in opt :
                    new_i = pos[0]
                    new_j = pos[1]

                    temp = chess.temp_move(ii, jj, new_i, new_j) 

                    if not chess.in_check(chess.white_king_pos) :
                        new_opt.append(pos) 

                    chess.rev_temp_move(ii, jj, new_i, new_j, temp)

                total += len(new_opt)

        if total == 0 :
            font = pygame.font.SysFont('Consolas', 50)
            text = font.render('SAHMAT,CRNI JE POBIJEDIO', True, CYAN)
            win.blit(text, (75, 300))

    else :
        chess.board[king_i][king_j].check = False

    king_i, king_j = chess.black_king_pos
    if chess.in_check(chess.black_king_pos) :
        chess.board[king_i][king_j].check = True 

        total = 0
        for ii in range(8) :
            for jj in range(8) :
                if total > 0 :
                    break
                
                piece = chess.board[ii][jj]
                if piece.name is None or piece.color == 'W' :
                    continue

                opt = chess.show_options(ii, jj, 'B', False)
                new_opt = []
                for pos in opt :
                    new_i = pos[0]
                    new_j = pos[1]

                    temp = chess.temp_move(ii, jj, new_i, new_j) 

                    if not chess.in_check(chess.black_king_pos) :
                        new_opt.append(pos)

                    chess.rev_temp_move(ii, jj, new_i, new_j, temp)

                total += len(new_opt)

        if total == 0 :
            font = pygame.font.SysFont('Consolas', 30)
            text = font.render('SAHMAT,BIJELI JE POBIJEDIO', True, WHITE)
            win.blit(text, (200, 5))

    else :
        chess.board[king_i][king_j].check = False 

    prev_i, prev_j = i, j
    
    if pygame.mouse.get_pressed() != (0, 0, 0) :
        pygame.time.delay(50)
        touched_piece = True

        curr_pos = pygame.mouse.get_pos()

        i = (curr_pos[1] - 40) // 80
        j = (curr_pos[0] - 40) // 80

        if len(options) > 0 :
            if (i, j) in options :
                chess.move(prev_i, prev_j, i, j) 
                touched_piece = False
                options = []
                pygame.time.delay(50)

                if move_color == 'W' :
                    move_color = 'B'
                else :
                    move_color = 'W'

    if touched_piece :
        if 0 <= i < 8 and 0 <= j < 8 :

            options = chess.show_options(i, j, move_color)
            new_options = []
            for pos in options :
                new_i = pos[0]
                new_j = pos[1]

                temp = chess.temp_move(i, j, new_i, new_j) 

                if move_color == 'W' :
                    if not chess.in_check(chess.white_king_pos) :
                        new_options.append(pos) 
                else :
                    if not chess.in_check(chess.black_king_pos) :
                        new_options.append(pos)

                chess.rev_temp_move(i, j, new_i, new_j, temp)

            options = new_options.copy()

            for pos in options :
                new_i = pos[0]
                new_j = pos[1]

                pygame.draw.circle(win, (0,0,139), ((new_j + 1) * chess.width, (new_i + 1) * chess.width), 12)

                 
    pygame.display.update()
    for ii in range(8) :
        sol = []
        for jj in range(8) :
            piece = chess.board[ii][jj]
            if piece.name is None:
                if len(sol) == 0:
                    sol.append('1')
                    continue
                if ord(sol[len(sol)-1])>=ord('0') and ord(sol[len(sol)-1])<=ord('9'):
                    sol[len(sol)-1]=chr(ord(sol[len(sol)-1])+1)
                    
                else: 
                    sol.append('1')
                    
            if piece.name == 'R':
                sol.append('R')
            elif piece.name == 'N':
                sol.append('N') 
                
            if  piece.name == 'B':
                sol.append('B')  
                
            if  piece.name == 'Q':
                sol.append('Q')
                
            if  piece.name == 'K':
                sol.append('K') 
                
            if  piece.name == 'P':
                sol.append('P') 
        print(sol)
pygame.quit()