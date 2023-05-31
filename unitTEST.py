import pytest

# Import the function from the code file
from checkwin import check_win

def test_check_win_no_winner():
    board = [['X', 'O', 'X'],
             ['O', 'X', 'O'],
             ['O', 'X', 'O']]
    assert check_win(board) is None

def test_check_win_row_winner():
    board = [['X', 'X', 'X'],
             ['O', 'O', None],
             [None, 'O', None]]
    assert check_win(board) == 'X'

def test_check_win_column_winner():
    board = [['O', 'X', 'X'],
             ['O', 'X', 'O'],
             ['O', None, 'O']]
    assert check_win(board) == 'O'

def test_check_win_diagonal_winner():
    board = [['X', 'O', 'O'],
             [None, 'X', None],
             ['O', None, 'X']]
    assert check_win(board) == 'X'

def test_check_win_draw():
    board = [['X', 'O', 'X'],
             ['O', 'X', 'O'],
             ['O', 'X', 'O']]
    assert check_win(board) == 'DRAW'
