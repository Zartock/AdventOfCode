import os
import inspect
from typing import List, Tuple

DIGITS_TEXT_MAPPING = {"one": 1,
                       "two": 2,
                       "three": 3,
                       "four": 4,
                       "five": 5,
                       "six": 6,
                       "seven": 7,
                       "eight": 8,
                       "nine": 9}


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
