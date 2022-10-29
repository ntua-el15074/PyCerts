import pygame
from .constants import BLACK, RED, WIDTH, SQUARE_SIZE, MOUNT_SIZE
from .gear import Gear

class Board(pygame.sprite.Sprite):
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.red_left = self.blue_left = 12

    def draw_squares(self, win):
        win.fill(BLACK)
        pygame.draw.rect(win, RED, (WIDTH//2 - SQUARE_SIZE//2, 50, SQUARE_SIZE, SQUARE_SIZE))
        for square in range(3):
            pygame.draw.rect(win, RED, (WIDTH//2 - SQUARE_SIZE//2 - (square - 1)*SQUARE_SIZE, SQUARE_SIZE + 50, SQUARE_SIZE, SQUARE_SIZE))
        for square in range(5):
            pygame.draw.rect(win, RED, (WIDTH//2 - SQUARE_SIZE//2 - (square - 2)*SQUARE_SIZE, SQUARE_SIZE*2 + 50, SQUARE_SIZE, SQUARE_SIZE))
        for square in range(7):
            pygame.draw.rect(win, RED, (WIDTH//2 - SQUARE_SIZE//2 - (square - 3)*SQUARE_SIZE, SQUARE_SIZE*3 + 50, SQUARE_SIZE, SQUARE_SIZE))
        for square in range(9):
            pygame.draw.rect(win, RED, (WIDTH//2 - SQUARE_SIZE//2 - (square - 4)*SQUARE_SIZE, SQUARE_SIZE*4 + 50, SQUARE_SIZE, SQUARE_SIZE))
        for square in range(11):
            pygame.draw.rect(win, RED, (WIDTH//2 - SQUARE_SIZE//2 - (square - 5)*SQUARE_SIZE, SQUARE_SIZE*5 + 50, SQUARE_SIZE, SQUARE_SIZE))

        # for i in range(6):
        #     for r in range(1, 13, 2):
        #         pygame.draw.rect(win, RED, (WIDTH//2 - SQUARE_SIZE//2 - (r-i)*SQUARE_SIZE, SQUARE_SIZE*i + 50, SQUARE_SIZE, SQUARE_SIZE))

    def draw_gear_mounts(self, win):
        pygame.draw.circle(win, BLACK, (WIDTH//2 - SQUARE_SIZE//2 + 2*MOUNT_SIZE, 50 + 2*MOUNT_SIZE), MOUNT_SIZE)
        for square in range(3):
            pygame.draw.circle(win, BLACK, (WIDTH//2 - SQUARE_SIZE//2 - (square - 1)*SQUARE_SIZE+ 2*MOUNT_SIZE, SQUARE_SIZE+ 2*MOUNT_SIZE + 50), MOUNT_SIZE)
        for square in range(5):
            pygame.draw.circle(win, BLACK, (WIDTH//2 - SQUARE_SIZE//2 - (square - 2)*SQUARE_SIZE+ 2*MOUNT_SIZE, SQUARE_SIZE*2+ 2*MOUNT_SIZE + 50), MOUNT_SIZE)
        for square in range(7):
            pygame.draw.circle(win, BLACK, (WIDTH//2 - SQUARE_SIZE//2 - (square - 3)*SQUARE_SIZE+ 2*MOUNT_SIZE, SQUARE_SIZE*3+ 2*MOUNT_SIZE + 50), MOUNT_SIZE)
        for square in range(9):
            pygame.draw.circle(win, BLACK, (WIDTH//2 - SQUARE_SIZE//2 - (square - 4)*SQUARE_SIZE+ 2*MOUNT_SIZE, SQUARE_SIZE*4+ 2*MOUNT_SIZE + 50), MOUNT_SIZE)
        for square in range(11):
            pygame.draw.circle(win, BLACK, (WIDTH//2 - SQUARE_SIZE//2 - (square - 5)*SQUARE_SIZE+ 2*MOUNT_SIZE, SQUARE_SIZE*5+ 2*MOUNT_SIZE + 50), MOUNT_SIZE)

    def create_board(self):
        for row in range(6):
            self.board.append([])
            if row == 0:
                for col in range(row + 1):
                    self.board[row].append(Gear(row, col, 'green', 20, 20))
            elif row == 1:
                for col in range(row + 2):
                    self.board[row].append(Gear(row, col, 'green', 20, 20))
            else:
                for col in range(row + 3):
                    self.board[row].append(Gear(row, col, 'green', 20, 20))
                


board = Board()
board.create_board()
print(board.board)
board.board[1][1].make_jammed()
print(board.board)

    # def draw_squares(self, win):
    #     win.fill(BLACK)
    #     for row in range(ROWS):
    #         for col in range(row % 2, ROWS, 2):
    #             pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
