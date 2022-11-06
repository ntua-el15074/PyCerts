import pygame
from .constants import BLACK, RED, WIDTH, SQUARE_SIZE, MOUNT_SIZE, ROWS
from .gear import Gear

class Board(pygame.sprite.Sprite):
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.green_left = self.blue_left = 12

    def draw_squares(self, win):
        for row in range(ROWS):
            for col in range(row + 1):
                if row != 0:
                    pygame.draw.rect(win, RED, (WIDTH//2 - SQUARE_SIZE//2 - (row - col)*SQUARE_SIZE + (SQUARE_SIZE//2)*row, SQUARE_SIZE*row + 50, SQUARE_SIZE, SQUARE_SIZE))
                else:
                    pygame.draw.rect(win, RED, (WIDTH//2 - SQUARE_SIZE//2 - (row - col)*SQUARE_SIZE, SQUARE_SIZE*row + 50, SQUARE_SIZE, SQUARE_SIZE))


    def draw_gear_mounts(self, win):
        for row in range(ROWS):
            for col in range(row + 1):
                if row != 0:
                    pygame.draw.circle(win, BLACK, (WIDTH//2 - SQUARE_SIZE//2 - (row - col)*SQUARE_SIZE + 2*MOUNT_SIZE + (SQUARE_SIZE//2)*row, SQUARE_SIZE*row + 2*MOUNT_SIZE + 50), MOUNT_SIZE)
                else:
                    pygame.draw.circle(win, BLACK, (WIDTH//2 - SQUARE_SIZE//2 - (row - col)*SQUARE_SIZE + 2*MOUNT_SIZE, SQUARE_SIZE*row + 2*MOUNT_SIZE + 50), MOUNT_SIZE)

    def create_board(self, win):
        for row in range(ROWS):
            self.board.append([])
            for col in range(row + 1):
                if row != 0:
                    new_gear = Gear(row, col, 'transparent', WIDTH//2 - SQUARE_SIZE//2 - (row - col)*SQUARE_SIZE + 2*MOUNT_SIZE + (SQUARE_SIZE//2)*row,  SQUARE_SIZE*row + 2*MOUNT_SIZE + 50)
                else:
                    new_gear = Gear(row, col, 'transparent', WIDTH//2 - SQUARE_SIZE//2 - (row - col)*SQUARE_SIZE + 2*MOUNT_SIZE,  SQUARE_SIZE*row + 2*MOUNT_SIZE + 50)
                self.board[row].append(new_gear)
                new_gear.draw(win)
