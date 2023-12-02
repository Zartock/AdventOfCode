from ACutils.utils import read_input_to_list_of_strings, replace_text_with_digit

from typing import List

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

def get_power(sets: List[str]) -> int:
    min_red = 0
    min_green = 0
    min_blue = 0
    for set in sets:
        number_colors = set.split(',')
        for cube_ammount in number_colors:
            tmp = cube_ammount.strip()
            number = int(replace_text_with_digit(tmp))
            if "blue" in tmp:
                min_blue = max(min_blue, number)
            if "red" in tmp:
                min_red = max(min_red, number)
            if "green" in tmp:
                min_green = max(min_green, number)

    return int(min_red * min_green * min_blue)


def main():
    input = read_input_to_list_of_strings("input.txt")
    total = 0
    for game in input:
        sets = game.split(':')[1].split(';')
        total += int(get_power(sets))
    print("Result: {}".format(total))


main()