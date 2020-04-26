class Board:

    def __init__(self):
        self.board = [[0 for x in range(1,9)] for x in range(1,9)]

    def display_board(self):
        for row in self.board:
            print(row)
        print("*" * 10)

    def update_board(self, position, piece):
        self.display_board()
        if position != None:
            row, col = position
            self.board[row][col] = piece
            self.display_board()
        else:
            print("Board: Invalid move")


# board = Board()
# board.update_board((1,7), "King")
# board.update_board((7,1), "Queen")
