import chess
import random
import piece_tables

from chessboard import display
from time import sleep

board = chess.Board()

def random_move(board):
    moves = list(board.legal_moves)
    move = random.choice(moves)
    return move

def evaluate_board(board):
    if board.is_checkmate():
        if board.turn:
            return -9999
        else:
            return 9999
    if board.is_stalemate():
        return 0
    if board.is_insufficient_material():
        return 0
    else:
        score = 0
        for i in range(8):
            for j in range(8):
                piece = board.piece_at(chess.square(i, j))
                if piece is not None:
                    if piece.color == chess.WHITE:
                        score += piece_tables.get_piece_value(piece, i, j)
                    else:
                        score -= piece_tables.get_piece_value(piece, i, j)
        return score
    
    
def minimax(board, depth, alpha, beta, white_to_play):
    if depth == 0:
        return evaluate_board(board), None
    if white_to_play:
        best_score = -9999
        best_move = None
        for move in board.legal_moves:
            board.push(move)
            score, _ = minimax(board, depth - 1, alpha, beta, False)
            board.pop()
            if score > best_score:
                best_score = score
                best_move = move
            alpha = max(alpha, best_score)
            if alpha >= beta:
                break
        return best_score, best_move
    else:
        best_score = 9999
        best_move = None
        for move in board.legal_moves:
            board.push(move)
            score, _ = minimax(board, depth - 1, alpha, beta, True)
            board.pop()
            if score < best_score:
                best_score = score
                best_move = move
            beta = min(beta, best_score)
            if alpha >= beta:
                break
        return best_score, best_move


def optimal_move(board, depth):
    white_to_play = board.turn
    best_score = -9999 if white_to_play else 9999
    best_move = random_move(board)
    for move in board.legal_moves:
        board.push(move)
        score, _ = minimax(board, depth - 1, -9999, 9999, not white_to_play)
        board.pop()
        if score > best_score and white_to_play:
            best_score = score
            best_move = move
        elif score < best_score and not white_to_play:
            best_score = score
            best_move = move
    return best_move


game_board = display.start(board.fen())
while not display.check_for_quit() and not (
    board.is_checkmate() or 
    board.is_stalemate() or 
    board.is_insufficient_material()
    ):
    move = optimal_move(board, 2)
    board.push(move)
    display.update(board.fen(), game_board)
#print(board)
#display.terminate()