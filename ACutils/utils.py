import os
import inspect
from typing import List, Tuple
from enum import Enum
from time import perf_counter


DIGITS_TEXT_MAPPING = {"one": 1,
                       "two": 2,
                       "three": 3,
                       "four": 4,
                       "five": 5,
                       "six": 6,
                       "seven": 7,
                       "eight": 8,
                       "nine": 9}

class Cardinal(Enum):
    __order__ = 'WEST EAST NORTH SOUTH'
    WEST = (-1, 0)
    EAST = (1, 0)
    NORTH = (0, -1)
    SOUTH = (0, 1) 

CARDINALS = [x.value for x in Cardinal]


def profiler(method):
    def wrapper_method(*arg, **kw):
        t = perf_counter()
        ret = method(*arg, **kw)
        print("Method " + method.__name__ + " took : " + "{:2.5f}".format(perf_counter() - t) + " sec")
        return ret

    return wrapper_method


def read_input_to_list_of_strings(file_name: str) -> List[str]: 
    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])
    dir_name = os.path.dirname(os.path.realpath(module.__file__))
    with open("{directory_name}/{name_of_file}".format(directory_name=dir_name, name_of_file=file_name)) as f:
        return f.read().splitlines()
    
def read_input_to_string(file_name: str) -> str: 
    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])
    dir_name = os.path.dirname(os.path.realpath(module.__file__))
    with open("{directory_name}/{name_of_file}".format(directory_name=dir_name, name_of_file=file_name)) as f:
        return f.read()


def read_input_to_grid_2d(file_name: str):
    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])
    dir_name = os.path.dirname(os.path.realpath(module.__file__))
    with open("{directory_name}/{name_of_file}".format(directory_name=dir_name, name_of_file=file_name)) as f:
        return [list(line.strip()) for line in f.readlines()] 


def extract_digits_from_string_and_translate_text_to_digits(line: str) -> str:
    new_line = ""
    for i in range(0, len(line)):
        if line[i].isdigit():
            new_line += line[i]
        else:
            for text_number in DIGITS_TEXT_MAPPING:
                if line[ i : i + len(text_number)] == text_number:
                    new_line += str(DIGITS_TEXT_MAPPING[text_number])
    return new_line


def extract_digits_from_string(text: str) -> str:
    x = filter(lambda x: x.isdigit(), text)
    numbers_as_string = "".join(x)
    return numbers_as_string


# coord_range must only contain 2 values
def get_adjacent_values_in_matrix_for_range(matrix: List[List[str]], coord_range: Tuple[Tuple[int, int], Tuple[int, int]]) -> List[str]:
    row_start, row_end = coord_range[0]
    col_start, col_end = coord_range[1]
    adjacent_values = []
    for row in range(row_start - 1, row_end + 2):
        for col in range(col_start - 1, col_end + 2):
            if row >= 0 and col >= 0 and row < len(matrix) and col < len(matrix[0]):
                if row == row_start - 1 or row == row_end + 1 or col == col_start - 1 or col == col_end + 1:
                    value_to_add = matrix[row][col]
                    adjacent_values.append(value_to_add)
    return adjacent_values

def in_range(i, j, max_i, max_j):
    return i >= 0 and j >= 0 and i < max_i and j < max_j

def neighbors_helper(max_i, max_j, candidates):
    if max_j is None and isinstance(max_i, list):
        max_j = len(max_i[0])
        max_i = len(max_i)
    return [(i, j) for i, j in candidates if in_range(i, j, max_i, max_j)]

def cardinal_neighbors(i, j, max_i, max_j=None):
    return neighbors_helper(
        max_i, max_j, [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    )

def all_neighbors(i, j, max_i, max_j=None):
    return neighbors_helper(
        max_i,
        max_j,
        [
            (i - 1, j),
            (i + 1, j),
            (i, j - 1),
            (i, j + 1),
            (i - 1, j - 1),
            (i - 1, j + 1),
            (i + 1, j - 1),
            (i + 1, j + 1),
        ],
    )