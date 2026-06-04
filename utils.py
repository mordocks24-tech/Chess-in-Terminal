
file_map = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}

def translate_coords(coord_string):
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
        
    for row in board:
        for sq in row:
            piece = sq.resident
            if piece is not None and sq.resident.team != team:
                king_indices = translate_coords(king_square.position)
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
                    

                    original_target_resident = board[tr][tc].resident
                    board[tr][tc].resident = piece
                    board[cr][cc].resident = None
                    piece.position = f"temp_pos" 

                    still_in_check = is_in_check(team, board)

                    board[cr][cc].resident = piece
                    board[tr][tc].resident = original_target_resident
                    piece.position = original_pos

                    if not still_in_check:
                        return False
                        
    return True