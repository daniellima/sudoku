# coding: utf-8
class Sudoku:

    SIZE = 3
    EMPTY = 0

    def __init__(self, puzzle):
        self.WIDTH = self.SIZE * self.SIZE
        #  "list" creates a copy of a list
        self.puzzle = list(puzzle)
        # vai ser usado depois para saber que trocas serão possíveis
        self.emptyIndexes = [i for i in range(len(self.puzzle)) if self.puzzle[i] == Sudoku.EMPTY]

    def get(self, line, column):
        return self.puzzle[line * self.WIDTH + column]

    def set(self, line, column, value):
        self.puzzle[line * self.WIDTH + column] = value

    def get_possible_swaps(self):
        swaps = []
        for i in range(len(self.emptyIndexes)):
            for j in range(i+1, len(self.emptyIndexes)):
                swaps.append([self.emptyIndexes[i], self.emptyIndexes[j]])

        return swaps

    def swap(self, this, that):
        temp = self.puzzle[that]
        self.puzzle[that] = self.puzzle[this]
        self.puzzle[this] = temp

    def get_line(self, line_index):
        line =[]
        for column in range(self.WIDTH):
            line.append(self.get(line_index, column))
        return line

    def get_column(self, column_index):
        column =[]
        for line in range(self.WIDTH):
            column.append(self.get(line, column_index))
        return column

    def get_block(self, block_index):
        block =[]

        init_for_range_line = (block_index // self.SIZE) * self.SIZE
        end_for_range_line = init_for_range_line + 3

        init_for_range_col = (block_index * self.SIZE) % 9
        end_for_range_col = init_for_range_col + self.SIZE
        for line_index in range(init_for_range_line, end_for_range_line):
            for column_index in range(init_for_range_col, end_for_range_col):
                block.append(self.get(line_index, column_index))
        return block

    def missing_numbers(self):
        # create a list with every possible number.
        # Ex: nine ones, nine twos, etc...
        all = []
        for n in range(self.WIDTH):
            i = [n+1] * self.WIDTH
            all.extend(i)

        for line in range(self.WIDTH):
            for column in range(self.WIDTH):
                if not self.get(line, column) == Sudoku.EMPTY:
                    all.remove(self.get(line, column))
        return all

    def random_fill_missing(self, missing):
        for line in range(self.WIDTH):
            for column in range(self.WIDTH):
                if self.get(line, column) == Sudoku.EMPTY:
                    self.set(line, column, missing.pop(0))

    def evaluate_line_errors(self):
        error_number_lines = 0
        for line_number in range(self.WIDTH):
            line = self.get_line(line_number)
            # to know how many different numbers there are in line list
            line_set = set(line)
            error_number = self.WIDTH - len(line_set)
            error_number_lines += error_number
        return error_number_lines

    def evaluate_column_errors(self):
        error_number_columns = 0
        for column_number in range(self.WIDTH):
            column = self.get_column(column_number)
            # to know how many different numbers there are in column list
            column_set = set(column)
            error_number = self.WIDTH - len(column_set)
            print(error_number)
            error_number_columns += error_number
        return error_number_columns

    def evaluate_block_errors(self):
        error_number_block = 0
        for block_number in range(self.WIDTH):
            block = self.get_block(block_number)
            # to know how many different numbers there are in  block list
            block_set = set(block)
            error_number = self.WIDTH - len(block_set)
            print(error_number)
            error_number_block += error_number
        return error_number_block

    def copy(self):
        return Sudoku(self.puzzle)

    def __str__(self):
        text = ""
        for line in range(self.WIDTH): # goes from 0 to self.WIDTH-1
            for column in range(self.WIDTH):
                el = self.get(line, column)
                if el == 0: el = '.'
                text += str(el) + " "
                if column % self.SIZE == self.SIZE - 1:
                    text += ' '
                if column == self.WIDTH-1:
                    text += '\n'
                if line % self.SIZE == self.SIZE - 1 and column == self.WIDTH-1:
                    text += "\n"

        return text
