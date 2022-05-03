from math import inf as infinity
from random import choice

import numpy as np

HUMAN = -1
COMP = 1


def IA_play(board):
    depth = len(available_positions(board))
    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move, _ = minimax(board, depth, COMP)
        x, y = move[0], move[1]

    return x, y


def create_board():
    board = np.zeros((3, 3))
    return board


def available_positions(board):
    cells = []

    for x, row in enumerate(board):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])

    return cells


def wins(board, player):

    win_state = [
        list(board[0, :]),
        list(board[1, :]),
        list(board[2, :]),
        list(board[:, 0]),
        list(board[:, 1]),
        list(board[:, 2]),
        [board[0, 0], board[1, 1], board[2, 2]],
        [board[2, 0], board[1, 1], board[0, 2]],
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False


def evaluate(state):

    if wins(state, COMP):
        score = +1
    elif wins(state, HUMAN):
        score = -1
    else:
        score = 0

    return score


def game_over(board):

    return (
        wins(board, HUMAN) or wins(board, COMP) or len(available_positions(board)) == 0
    )


def minimax(board, depth, player):
    best_position = [-1, -1]

    if player == COMP:
        best = -infinity
    else:
        best = +infinity

    if depth == 0 or game_over(board):
        score = evaluate(board)
        return [-1, -1], score

    for position in available_positions(board):
        x, y = position[0], position[1]
        board[x][y] = player
        _, score = minimax(board, depth - 1, -player)
        board[x][y] = 0

        if player == COMP:
            if score > best:
                best = score  # max value
                best_position = [x, y]
        else:
            if score < best:
                best = score  # min value
                best_position = [x, y]

    return best_position, best
