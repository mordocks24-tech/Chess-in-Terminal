from board import create_and_set_board, square
from utils import translate_coords, is_in_check, is_checkmate
from visuals import print_board

my_board = create_and_set_board()

def swap_turn(current_turn):
    if current_turn == "black":
        return "white"
    else:
        return "black"

def main():

    current_turn = "white"
    next_turn = "black"

    while True:

        print_board(my_board)

        if is_in_check(current_turn, my_board):
            print("CHECK!")

        #try to get starting square, and continue if not valid
        print(f"{current_turn.capitalize()}'s turn!")
        print("Which piece to move?")
        try:
            s1, s2 = translate_coords(input())
        except Exception:
            print("Please enter a valid coordinate like 'e4'")
            continue
        start_square = my_board[s1][s2]


        if start_square.resident is not None and start_square.resident.team == current_turn:
            #try to get target square, and continue if not valid
            print("Moving where?")
            try:
                target_square_string = input()
            except Exception:
                print("Please enter a valid coordinate like 'e4'")
                continue

            if start_square.resident.attempt_move(my_board, target_square_string) == True:
                if is_checkmate(next_turn, my_board):
                    print(f"CHECKMATE! {current_turn.capitalize()} wins!")
                    break
                current_turn = swap_turn(current_turn)
                next_turn = swap_turn(next_turn)
        else:
            print("Invalid Move!")






main()