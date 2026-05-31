from board import 


class Piece:
    def __init__(self, position, team):
        self.position = position
        self.team = team


class Pawn(Piece):
    def __init__(self, position, team):
        super().__init__(position, team)

class Rook(Piece):
    def __init__(self, position, team):
        super().__init__(position, team)

class Bishop(Piece):
    def __init__(self, position, team):
        super().__init__(position, team)

class Knight(Piece):
    def __init__(self, position, team):
        super().__init__(position, team)

class Queen(Piece):
    def __init__(self, position, team):
        super().__init__(position, team)

class King(Piece):
    def __init__(self, position, team):
        super().__init__(position, team)

