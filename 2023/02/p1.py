from ACutils.utils import read_input_to_list_of_strings, extract_digits_from_string

from typing import List

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

def is_set_possible(sets: List[str]):
    for set in sets:
        number_colors = set.split(',')
        for cube_ammount in number_colors:
            tmp = cube_ammount.strip()
            number = extract_digits_from_string(tmp)
            if "blue" in tmp:
                if int(number) > MAX_BLUE:
                    return False
            if "red" in tmp:
                if int(number) > MAX_RED:
                    return False
            if "green" in tmp:
                if int(number) > MAX_GREEN:
                    return False
    return True


def main():
    input = read_input_to_list_of_strings("input.txt")
    total = 0
    for game in input:
        game_id = game.split(':')[0].replace("Game ", "")
        sets = game.split(':')[1].split(';')
        if is_set_possible(sets):
            total += int(game_id)
    print("Result: {}".format(total))


main()