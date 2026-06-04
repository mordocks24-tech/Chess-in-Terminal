from .board import create_and_set_board, square

def print_board(board):
    for row in reversed(board): # Reverse so Rank 8 is at the top
        row_string = ""
        for square in row:
            if square.resident:
                row_string += f" {square.resident.symbol} "
            else:
                row_string += " . " # Use a dot for empty squares
        print(row_string)