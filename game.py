from board import Board
from position import Position

board = Board()
pos = Position()

pos.update_position((0,5))
board.update_board(pos.position,"King")
pos.update_position((6,3))
board.update_board(pos.position,"Queen")
pos.update_position((5,8))
board.update_board(pos.position,"Rook")
