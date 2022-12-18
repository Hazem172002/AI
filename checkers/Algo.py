from copy import deepcopy
import pygame
RED = (255,0,0)
WHITE = (255, 255, 255)

def minimax(position, depth, max_player, game, cond=float(
    'inf')):
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position

    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_temp_board(position, WHITE, game):
            evaluation = minimax(move, depth - 1, False, game, maxEval)[
                0]
            if evaluation >= cond:
                break
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move

        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_temp_board(position, RED, game):
            evaluation = minimax(move, depth - 1, True, game, minEval)[0]
            if evaluation <= cond:
                break
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move

        return minEval, best_move

def simulate_move(piece, move, board, game,
                  skip):  # trying to make valid moves of this piece in temp board with his skipped
    board.move(piece, move[0], move[1])  # move piece to row,col
    if skip:
        board.remove(skip)

    return board


def get_temp_board(board, color, game):  # get temp board after moves
    boards = []  # list of all temp boards

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(
            piece)
        for move, skip in valid_moves.items():
            temp_board = deepcopy(board)  # copy of the current board
            temp_piece = temp_board.get_piece(piece.row, piece.col)  # put pieces in temp board
            new_board = simulate_move(temp_piece, move, temp_board, game,
                                      skip)  # is new board after do the valid move and skippe
            boards.append(new_board)  # add this board to list

    return boards
