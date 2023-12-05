import sys
sys.path.append("..") # Adds higher directory to python modules path.

from utils import *

import pytest


def test_read_input_to_list_of_strings():
    lines = read_input_to_list_of_strings("test_input.txt")

    assert len(lines) == 3
    assert lines[0] == "this_is_some_test_input_in_a_file_1"
    assert lines[1] == "this_is_some_test_input_in_a_file_2"
    assert lines[2] == "this_is_some_test_input_in_a_file_3"


def test_extract_digits_from_string_and_translate_text_to_digits():
    test_string = "th1s_is_s0me_t3xt_with_sevenine_t3xt"
    assert extract_digits_from_string_and_translate_text_to_digits(test_string) == "103793"


def test_extract_digits_from_string():
    test_string = "ldksldskl6lskdldkls8lskdldksl3skdjkdjsk5"
    assert extract_digits_from_string(test_string) == "6835"


def test_get_adjecant_matrix():
    matrix = [[1,  2,  3,  4,  5],
              [6,  7,  8,  9,  10],
              [11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25]]
    coord_range = [(1,1),(1,3)]
    expected_result = [1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15]
    result = get_adjacent_values_in_matrix_for_range(matrix, coord_range)
    assert result == expected_result

    # (row, col) in on of the adds will be same as coord_range[0]
    # There was a bug and this was used for TDD
    input = read_input_to_list_of_strings("test_input_matrix.txt")
    row = 90
    column_start = 87
    column_end = 89
    coord_range = ((row, row), (column_start, column_end))
    result = get_adjacent_values_in_matrix_for_range(input, coord_range)

    assert '%' in result
