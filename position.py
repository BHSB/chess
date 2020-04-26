class Position:

    def __init__(self, position=(0,0)):
        self.position = self.inside_board(position)


    def inside_board(self, position):
        if all(x >= 0 for x in position) and all(x <=7 for x in position):
            return (position)
        else:
            print("Position: Invalid move")

    def update_position(self, position):
        self.position = self.inside_board(position)
