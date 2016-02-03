# coding: utf-8
from __future__ import division
from sudoku import Sudoku

def get_initial_sudoku():
    _ = Sudoku.EMPTY
    sudoku = Sudoku([
        _, _, _,   7, _, _,   _, _, _,
        1, _, _,   _, _, _,   _, _, _,
        _, _, _,   4, 3, _,   2, _, _,

        _, _, _,   _, _, _,   _, _, 6,
        _, _, _,   5, _, 9,   _, _, _,
        _, _, _,   _, _, _,   4, 1, 8,

        _, _, _,   _, 8, 1,   _, _, _,
        _, _, 2,   _, _, _,   _, 5, _,
        _, 4, _,   _, _, _,   3, _, _
    ])
    return sudoku