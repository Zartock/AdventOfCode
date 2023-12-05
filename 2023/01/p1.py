from ACutils.utils import extract_digits_from_string, read_input_to_list_of_strings


def main():
    total = 0
    lines = read_input_to_list_of_strings("input.txt")
    for line in lines:
        numbers = extract_digits_from_string(line)
        if len(numbers) == 0:
            continue
        elif len(numbers) == 1:
            total += int(numbers + numbers)
        else:
            total += int(numbers[0] + numbers[-1])
    print("Result: {}".format(total))

main()