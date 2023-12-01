from ACutils.utils import replace_text_with_digit_and_translate_text_to_digits
import os




def read_from_file():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    lines = []
    with open(dir_path + "/input.txt") as f:
        lines = [line for line in f]
    return lines


def main():
    total = 0
    lines = read_from_file()
    for line in lines:
        new_line = replace_text_with_digit_and_translate_text_to_digits(line)
        if len(new_line) == 0:
            continue
        elif len(new_line) == 1:
            total += int(new_line + new_line)
        else:
            first_number = new_line[0]
            last_number = new_line[-1]
            tmp = first_number + last_number
            total += int(tmp)
    print("Result: {}".format(total))



main()