import os 

from ACutils.utils import replace_text_with_digit

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
        numbers = replace_text_with_digit(line)
        if len(numbers) == 0:
            continue
        elif len(numbers) == 1:
            total += int(numbers + numbers)
        else:
            first_number = numbers[0]
            last_number = numbers[-1]
            tmp = first_number + last_number
            total += int(tmp)
    print("Result: {}".format(total))

main()