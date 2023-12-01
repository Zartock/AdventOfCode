from ACutils.utils import replace_text_with_digit, read_input_to_list_of_strings


def main():
    total = 0
    lines = read_input_to_list_of_strings()
    for line in lines:
        numbers = replace_text_with_digit(line)
        if len(numbers) == 0:
            continue
        elif len(numbers) == 1:
            total += int(numbers + numbers)
        else:
            total += int(numbers[0] + numbers[-1])
    print("Result: {}".format(total))

main()