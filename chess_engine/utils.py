
file_map = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}

def translate_indices(row, col):
    # Convert row index back to rank (8-0 -> '1'-'8')
    # Convert col index back to file (0-7 -> 'a'-'h')
    letter = chr(ord('a') + col)
    number = str(8 - row)
    return letter + number

def translate_coords(coord_string):
    if not isinstance(coord_string, str):
         raise ValueError(f"Expected string, got {type(coord_string)}: {coord_string}")
    if len(coord_string) < 2:
         raise ValueError(f"String too short: '{coord_string}'")
    if len(coord_string) != 2:
        raise ValueError("Invalid format, 2 characters please.")
    if not coord_string[0].isalpha():
        raise ValueError("First character must be a letter!")
    if not coord_string[1].isdigit():
        raise ValueError("Second character must be a number!")

    file_char = coord_string[0]
    col_index = file_map[file_char]
    
    rank_num = int(coord_string[1])
    row_index = rank_num - 1

    
    return row_index, col_index

def is_in_check(team, board):
    king_square = None
    for row in board:
        for sq in row:
            if sq.resident is not None and type(sq.resident).__name__ == "King" and sq.resident.team == team:
                king_square = sq
    
    if king_square is None:
        return False
    
    king_indices = translate_coords(king_square.position)
    
    for row in board:
        for sq in row:
            piece = sq.resident
            if piece is not None and piece.team != team:
                if king_indices in piece.get_valid_moves(board):
                    return True
    return False

def is_checkmate(team, board):
    if not is_in_check(team, board):
        return False

    for row in board:
        for sq in row:
            piece = sq.resident
            if piece is not None and piece.team == team:
                original_pos = piece.position
                valid_moves = piece.get_valid_moves(board)
                
                for move_coords in valid_moves:
                    tr, tc = move_coords
                    cr, cc = translate_coords(original_pos)

                    # 1. Save state
                    original_target_resident = board[tr][tc].resident
                    
                    # 2. Simulate move
                    board[tr][tc].resident = piece
                    board[cr][cc].resident = None
                    
                    # FIX: Set the piece's position to the actual destination string
                    piece.position = translate_indices(tr, tc) 

                    still_in_check = is_in_check(team, board)

                    # 3. Undo move (Restore state)
                    board[cr][cc].resident = piece
                    board[tr][tc].resident = original_target_resident
                    piece.position = original_pos

                    if not still_in_check:
                        return False
                        
    return True