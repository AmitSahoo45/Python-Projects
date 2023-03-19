import pygame
import sys
import numpy as np

pygame.init()

WIDTH, HEIGHT, LINE_WIDTH, COLOR, BAR_COLOR = 600, 600, 15, (
    238, 82, 83), (255, 255, 255)
BOARD_ROWS, BOARD_COLS = 3, 3
CROSS_COLOR = (241, 245, 248)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(COLOR)

board = np.zeros((BOARD_ROWS, BOARD_COLS))


def drawLines():
    # horizontal
    pygame.draw.line(screen, BAR_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    pygame.draw.line(screen, BAR_COLOR, (0, 400), (600, 400), LINE_WIDTH)
    # vertical
    pygame.draw.line(screen, BAR_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    pygame.draw.line(screen, BAR_COLOR, (400, 0), (400, 600), LINE_WIDTH)


def drawFigures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CROSS_COLOR, (int(
                    col * 200 + 100), int(row * 200 + 100)), 60, LINE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, BAR_COLOR, (col * 200 + 55, row * 200 + 155), (
                    col * 200 + 145, row * 200 + 45), LINE_WIDTH)
                pygame.draw.line(screen, BAR_COLOR, (col * 200 + 55, row * 200 + 45), (
                    col * 200 + 145, row * 200 + 155), LINE_WIDTH)


def mark_square(row, col, player):
    board[row][col] = player


def available_square(row, col):
    return board[row][col] == 0


def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True


def check_win():
    # horizontal win check
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True

    # vertical win check
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True

    # asc diagonal win check
    if board[2][0] == player[1][1] == board[0][2] == player:
        draw_asc_diagonal(player)
        return True

    # desc diagonal win check
    if board[0][0] == board[1][1] == board[2][2] == player:
        draw_desc_diagonal(player)
        return True

    return False


def draw_vertical_winning_line(col, player):
    posX = col * 200 + 100

    if player == 1:
        color = CROSS_COLOR
    elif player == 2:
        color = BAR_COLOR

    pygame.draw.line(screen, color, (posX, 15), (posX, HEIGHT - 15), 15)


def draw_horizontal_winning_line(row, player):
    posY = row * 200 + 100

    if player == 1:
        color = CROSS_COLOR
    elif player == 2:
        color = BAR_COLOR

    pygame.draw.line(screen, color, (15, posY), (WIDTH - 15, posY), 15)


def draw_asc_diagonal(player):
    if player == 1:
        color = CROSS_COLOR
    elif player == 2:
        color = BAR_COLOR

    pygame.draw.line(screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)


def draw_desc_diagonal(player):
    if player == 1:
        color = CROSS_COLOR
    elif player == 2:
        color = BAR_COLOR

    pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), 15)


def restart():
    screen.fill(COLOR)
    drawLines()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0


drawLines()

player = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)

            if available_square(clicked_row, clicked_col):
                if player == 1:
                    mark_square(clicked_row, clicked_col, 1)
                    check_win(player)
                    player = 2
                elif player == 2:
                    mark_square(clicked_row, clicked_col, 2)
                    check_win(player)
                    player = 1

                drawFigures()

            print(board)

    pygame.display.update()
