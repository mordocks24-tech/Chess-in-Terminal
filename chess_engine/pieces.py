from .utils import translate_coords, is_in_check


class Piece:
    def __init__(self, position, team):
        self.position = position
        self.team = team
    def get_valid_moves(self, board):
        return
    def attempt_move(self, board, targeted_coord_string):
        target_row, target_col = translate_coords(targeted_coord_string)
        current_row, current_col = translate_coords(self.position)

        if (target_row, target_col) not in self.get_valid_moves(board):
            print("Illegal Move!")
            return False

        original_target_resident = board[target_row][target_col].resident

        board[target_row][target_col].resident = self
        board[current_row][current_col].resident = None

        original_pos_string = self.position
        self.position = targeted_coord_string

        if is_in_check(self.team, board):
            board[current_row][current_col].resident = self
            board[target_row][target_col].resident = original_target_resident
            self.position = original_pos_string
            print("You cannot leave your King in check!")
            return False

        return True

class Pawn(Piece):
    def __init__(self, position, team):
        super().__init__(position, team)
        self.symbol = "♟" if team == "white" else "♙"
    
    def get_valid_moves(self, board):
        current_row, current_column = translate_coords(self.position)
        valid_moves = []
        direction = 1 if self.team == "white" else -1
        target_row = current_row + direction

        # moves forward once 
        if 0 <= target_row <= 7:
            if board[target_row][current_column].resident is None:
                valid_moves.append((target_row, (current_column)))
        # moves forward twice
                start_row = 1 if self.team == "white" else 6
                if current_row == start_row:
                    double_target = current_row + (direction * 2)
                    if board[double_target][current_column].resident is None:
                        valid_moves.append((double_target, current_column))
        #capture diagonally
        for cap in [-1, 1]:
            target_column = current_column + cap
            if 0 <= target_row <= 7 and 0 <= target_column <= 7:
                diagonal_square = board[target_row][target_column]
                if diagonal_square.resident != None and diagonal_square.resident.team != self.team:
                    valid_moves.append((target_row, target_column))
        return valid_moves

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
        return valid_moves

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
        return valid_moves

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
        return valid_moves           

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
        return valid_moves

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
        return valid_moves
