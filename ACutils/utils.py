import os
import inspect

DIGITS_TEXT_MAPPING = {"one": 1,
                       "two": 2,
                       "three": 3,
                       "four": 4,
                       "five": 5,
                       "six": 6,
                       "seven": 7,
                       "eight": 8,
                       "nine": 9}


def read_input_to_list_of_strings():
    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])
    dir_name = os.path.dirname(os.path.realpath(module.__file__))
    with open(dir_name + "/input.txt") as f:
        return f.readlines()

def replace_text_with_digit_and_translate_text_to_digits(line: str):
    new_line = ""
    for i in range(0, len(line)):
        if line[i].isdigit():
            new_line += line[i]
        else:
            for text_number in DIGITS_TEXT_MAPPING:
                if line[ i : i + len(text_number)] == text_number:
                    new_line += str(DIGITS_TEXT_MAPPING[text_number])
    return new_line


def replace_text_with_digit(text: str):
    x = filter(lambda x: x.isdigit(), text)
    numbers_as_string = "".join(x)
    return numbers_as_string
