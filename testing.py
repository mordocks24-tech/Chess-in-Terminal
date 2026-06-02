from board import create_and_set_board, translate_coords
from visuals import print_board

def test_create_board():
    my_board = create_and_set_board()
    print_board(my_board)

def test_translate_coords():
    print(translate_coords("a1"))
    print(translate_coords("h5"))
    print(translate_coords("f8"))

test_translate_coords()