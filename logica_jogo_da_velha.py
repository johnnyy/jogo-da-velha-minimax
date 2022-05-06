from math import inf as infinity
from random import choice

import numpy as np

HUMAN = -1
COMP = 1


def IA_play(board, type_ia):
    # Funcao com a escolha da melhor jogada da IA
    depth = len(available_positions(board))
    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move, _ = minimax(board, depth, COMP, type_ia)
        x, y = move[0], move[1]

    return x, y


def create_board():
    # Criacao da matriz do tabuleiro
    board = np.zeros((3, 3))
    return board


def available_positions(board):
    # Posicoes disponiveis para jogadas
    cells = []

    for x, row in enumerate(board):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])

    return cells


def wins(board, player):
    # Situacoes de vitoria
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


def evaluate(state, type_ia):
    # Avaliacao de vitoria para retornar os scores recursivos do Minimax
    if wins(state, COMP):
        score = +1 * type_ia
    elif wins(state, HUMAN):
        score = -1 * type_ia
    else:
        score = 0

    return score


def game_over(board):
    # Verificacao de situacoes de game over
    return (
        wins(board, HUMAN) or wins(board, COMP) or len(available_positions(board)) == 0
    )


def minimax(board, depth, player, type_ia):
    # Execucao do minimax para selecionar a jogada
    best_position = [-1, -1]

    if player == COMP:
        best = -infinity
    else:
        best = +infinity

    if depth == 0 or game_over(board):
        score = evaluate(board, type_ia)
        return [-1, -1], score

    for position in available_positions(board):
        x, y = position[0], position[1]
        board[x][y] = player
        _, score = minimax(board, depth - 1, -player, type_ia)
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
