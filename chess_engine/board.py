from .pieces import Pawn, Rook, Knight, King, Queen, Bishop

class square:
    def __init__(self, position, resident=None):
        self.position = position
        self.resident = resident

ranks = [1, 2, 3, 4, 5, 6, 7, 8]
files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


back_rank_pieces = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
front_rank_pieces = [Pawn] * 8

def create_and_set_board():
    board = []
    for rank in ranks:
        row = []
        for file in files:
            pos = f"{file}{rank}"
            row.append(square(pos))
        board.append(row)

    for i, piece_class in enumerate(back_rank_pieces):
        board[0][i].resident = piece_class(position=board[0][i].position, team="white")
        board[7][i].resident = piece_class(position=board[7][i].position, team="black")
        
    for i, piece_class in enumerate(front_rank_pieces):
        board[1][i].resident = piece_class(position=board[1][i].position, team="white")
        board[6][i].resident = piece_class(position=board[6][i].position, team="black")

    board[0][3].resident = Queen(position=board[0][3].position, team="white")
    board[7][3].resident = Queen(position=board[7][3].position, team="black")

    return board

