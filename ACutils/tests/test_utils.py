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


def test_replace_text_with_digit_and_translate_text_to_digits():
    test_string = "th1s_is_s0me_t3xt_with_sevenine_t3xt"
    assert replace_text_with_digit_and_translate_text_to_digits(test_string) == "103793"


def test_replace_text_with_digit():
    test_string = "ldksldskl6lskdldkls8lskdldksl3skdjkdjsk5"
    assert replace_text_with_digit(test_string) == "6835"