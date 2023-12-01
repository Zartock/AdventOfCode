from ACutils.utils import replace_text_with_digit_and_translate_text_to_digits, read_input_to_list_of_strings


def main():
    total = 0
    lines = read_input_to_list_of_strings("input.txt")
    for line in lines:
        new_line = replace_text_with_digit_and_translate_text_to_digits(line)
        if len(new_line) == 0:
            continue
        elif len(new_line) == 1:
            total += int(new_line + new_line)
        else:
            total += int(new_line[0] + new_line[-1])
    print("Result: {}".format(total))



main()