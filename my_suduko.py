import pygame
import random
import sudoku

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH, SCREEN_HEIGHT = 550, 550
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Sudoku')

# Define the Sudoku boarrd
puzzle = sudoku.generate_sudoku

# Print the Sudoku puzzle
sudoku.print_sudoku(puzzle)

# Fonts
font = pygame.font.Font(None, 36)

# Constants
GRID_SIZE = SCREEN_WIDTH // 9

# Functions
def draw_grid():
    for x in range(0, SCREEN_WIDTH, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, SCREEN_HEIGHT), 2)
    for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (SCREEN_WIDTH, y), 2)

def draw_numbers():
    for row in range(9):
        for col in range(9):
            if board[row][col] != 0:
                text = font.render(str(board[row][col]), True, BLACK)
                text_rect = text.get_rect(center=(col * GRID_SIZE + GRID_SIZE / 2, row * GRID_SIZE + GRID_SIZE / 2))
                screen.blit(text, text_rect)

def is_valid_move(row, col, num):
    # Check row and column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check 3x3 box
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[box_row + i][box_col + j] == num:
                return False

    return True

def solve_sudoku():
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid_move(row, col, num):
                        board[row][col] = num
                        if solve_sudoku():
                            return True
                        board[row][col] = 0
                return False
    return True

def main():
    clock = pygame.time.Clock()
    running = True
    selected = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row = y // GRID_SIZE
                col = x // GRID_SIZE
                selected = (row, col)

            if event.type == pygame.KEYDOWN and selected:
                if event.unicode.isnumeric():
                    num = int(event.unicode)
                    if is_valid_move(selected[0], selected[1], num):
                        board[selected[0]][selected[1]] = num

        screen.fill(WHITE)
        draw_grid()
        draw_numbers()
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    main()
