import pytest

@pytest.mark.parametrize("board, expected_winner", [
    ([
        ['X', 'X', 'X'],
        ['O', 'O', None],
        [None, None, None]
    ], 'X'),
    ([
        ['O', 'X', None],
        ['O', 'X', None],
        [None, 'X', None]
    ], 'X'),
    ([
        ['O', 'X', None],
        ['O', 'O', 'X'],
        ['X', None, 'O']
    ], 'O'),
    ([
        [None, 'X', 'O'],
        ['O', 'O', 'X'],
        ['O', None, 'X']
    ], 'O'),
    ([
        ['X', 'O', 'X'],
        ['O', 'O', 'X'],
        ['X', 'X', 'O']
    ], 'DRAW'),
    ([
        ['X', None, 'O'],
        ['O', 'O', 'X'],
        [None, None, 'X']
    ], None)
])
def test_check_win(board, expected_winner):
    assert check_win(board) == expected_winner
