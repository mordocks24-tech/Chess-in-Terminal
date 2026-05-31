

class square:
    def __init__(self, position, resident):
    self.position = position
    self.resident = resident

ranks = [1, 2, 3, 4, 5, 6, 7, 8]
files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

board = []
for rank in ranks:
    row = []
    for file in files:
        row.append(square(file, rank))
    board.append(row)


def set_board(board):