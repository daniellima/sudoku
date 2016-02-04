# coding: utf-8
import time
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

TIMES = []


def timing(f):
    def wrap(*args):
        global TIMES
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        thistime = (time2-time1)*1000.0
        print('%s function took %0.3f ms' % (f.__name__, thistime))
        TIMES.append(thistime)
        return ret
    return wrap


def avg_times():
    if len(TIMES) == 0:
        return 0

    return sum(TIMES)/len(TIMES)


def reset_times():
    global TIMES
    TIMES = []
