import chess
import random

from chessboard import display
from time import sleep

board = chess.Board()

def random_move(board):
    moves = list(board.legal_moves)
    move = random.choice(moves)
    return move

game_board = display.start(board.fen())
while not display.check_for_quit():
    move = random_move(board)
    board.push(move)
    display.update(board.fen(), game_board)
#print(board)
display.terminate()