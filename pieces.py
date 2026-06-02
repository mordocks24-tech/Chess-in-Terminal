from board import translate_coords

class Piece:
    def __init__(self, position, team):
        self.position = position
        self.team = team
    def get_valid_moves(self, board):
        return
    def attempt_move(self, board, input):
        return

class Pawn(Piece):
    def __init__(self, position, team):
        super().__init__(position, team)
        self.symbol = "♟" if team == "white" else "♙"
    
    def get_valid_moves(self, position):
        if self.team == "white":
            forward_once = 1
        else:
            forward_once = -1



class Rook(Piece):
    def __init__(self, position, team):
        super().__init__(position, team)
        self.symbol = "♜" if team == "white" else "♖"
    
    def get_valid_moves(self, board):
        current_row, current_col = translate_coords(self.position)
        valid_moves = []
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        for rd, rc in directions:
            for i in range(1, 8):
                target_row = current_row + (rd * i)
                target_column = current_col + (rc * i)

                if 0 <= target_row <= 7 and 0 <= target_column <= 7:
                    target_square = board[target_row][target_column]

                    if target_square.resident == None:
                        valid_moves.append((target_row, target_column))
                    elif target_square.resident.team != self.team:
                        valid_moves.append((target_row, target_column))
                        break
                    elif target_square.resident.team == self.team:
                        break


class Bishop(Piece):
    def __init__(self, position, team):
        super().__init__(position, team)
        self.symbol = "♝" if team == "white" else "♗"
    
    def get_valid_moves(self, board):
        current_row, current_col = translate_coords(self.position)
        valid_moves = []
        directions = [(1, 1), (-1, -1), (1, -1), (-1, 1)]

        for rd, rc in directions:
            for i in range(1, 8):
                target_row = current_row + (rd * i)
                target_column = current_col + (rc * i)

                if 0 <= target_row <= 7 and 0 <= target_column <= 7:
                    target_square = board[target_row][target_column]

                    if target_square.resident == None:
                        valid_moves.append((target_row, target_column))
                    elif target_square.resident.team != self.team:
                        valid_moves.append((target_row, target_column))
                        break
                    elif target_square.resident.team == self.team:
                        break


class Knight(Piece):
    def __init__(self, position, team):
        super().__init__(position, team)
        self.symbol = "♞" if team == "white" else "♘"
    
    def get_valid_moves(self, board):
        current_row, current_col = translate_coords(self.position)
        valid_moves = []
        offsets = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

        for row, col in offsets:
            target_row = current_row + row
            target_column = current_col + col

            if 0 <= target_row <= 7 and 0 <= target_column <= 7:
                target_square = board[target_row][target_column]

                if target_square.resident is None or target_square.resident.team != self.team:
                    valid_moves.append((target_row, target_column))
            

class Queen(Piece):
    def __init__(self, position, team):
        super().__init__(position, team)
        self.symbol = "♛" if team == "white" else "♕"
    
    def get_valid_moves(self, board):
        current_row, current_col = translate_coords(self.position)
        valid_moves = []
        directions = [(1, 1), (-1, -1), (1, -1), (-1, 1), (1, 0), (-1, 0), (0, -1), (0, 1)]

        for rd, rc in directions:
            for i in range(1, 8):
                target_row = current_row + (rd * i)
                target_column = current_col + (rc * i)

                if 0 <= target_row <= 7 and 0 <= target_column <= 7:
                    target_square = board[target_row][target_column]

                    if target_square.resident == None:
                        valid_moves.append((target_row, target_column))
                    elif target_square.resident.team != self.team:
                        valid_moves.append((target_row, target_column))
                        break
                    elif target_square.resident.team == self.team:
                        break

class King(Piece):
    def __init__(self, position, team):
        super().__init__(position, team)
        self.symbol = "♚" if team == "white" else "♔"

    def get_valid_moves(self, board):
        current_row, current_col = translate_coords(self.position)
        valid_moves = []
        directions = [(1, 1), (-1, -1), (1, -1), (-1, 1), (1, 0), (-1, 0), (0, -1), (0, 1)]

        for rd, rc in directions:
            target_row = current_row + rd
            target_column = current_col + rc

            if 0 <= target_row <= 7 and 0 <= target_column <= 7:
                target_square = board[target_row][target_column]

                if target_square.resident == None:
                    valid_moves.append((target_row, target_column))
                elif target_square.resident.team != self.team:
                    valid_moves.append((target_row, target_column))
                    break
                elif target_square.resident.team == self.team:
                    break

