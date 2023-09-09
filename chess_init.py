import chess
import chess.svg
import chess.pgn
import chess.engine
import datetime

import movement

from chessboard import display
from IPython.display import SVG
from time import sleep

count = 0
movehistory = []
game = chess.pgn.Game()
board = chess.Board()

game_board = display.start(board.fen())
while not board.is_game_over(claim_draw=True):
    if board.turn:
        count += 1
        #print(f'\n{count}]\n')
        # high depth takes too long
        move = movement.optimal_move(board, 2)
        board.push(move)
        display.update(board.fen(), game_board)
        movehistory.append(move)
        #print(board)
        #print()
    else:
        move = movement.optimal_move(board, 2)
        board.push(move)
        display.update(board.fen(), game_board)
        movehistory.append(move)
        #print(board)
        
game.add_line(movehistory)
game.headers["Date"] = str(datetime.datetime.now().date())
game.headers["Round"] = 1
game.headers["White"] = "PsAi"
game.headers["Black"] = "PsAi2"
game.headers["Result"] = str(board.result(claim_draw=True))
print(game)
SVG(chess.svg.board(board=board,size=400))
#display.terminate()