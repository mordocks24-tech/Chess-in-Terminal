from board import 


class Piece:
    def __init__(self, position, team):
        self.position = position
        self.team = team


class Pawn(Piece):
    def __init__(self, position, team):
        super().__init__(position, team)
        self.symbol = "♙" if team == "white" else "♟"

class Rook(Piece):
    def __init__(self, position, team):
        super().__init__(position, team)
        self.symbol = "♖" if team == "white" else "♜"

class Bishop(Piece):
    def __init__(self, position, team):
        super().__init__(position, team)
        self.symbol = "♗" if team == "white" else "♝"

class Knight(Piece):
    def __init__(self, position, team):
        super().__init__(position, team)
        self.symbol = "♘" if team == "white" else "♞"

class Queen(Piece):
    def __init__(self, position, team):
        super().__init__(position, team)
        self.symbol = "♕" if team == "white" else "♛"

class King(Piece):
    def __init__(self, position, team):
        super().__init__(position, team)
        self.symbol = "♔" if team == "white" else "♚"
