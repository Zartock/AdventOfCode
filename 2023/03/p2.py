from ACutils.utils import read_input_to_list_of_strings, get_adjacent_values_in_matrix_for_range

import re


def digit_sequence_indices(s: str):
    pattern = r'\d+'
    return [(m.start(), m.end()-1) for m in re.finditer(pattern, s)]


def isSymbol(ch: str):
    return ch != '.'


def has_symbol_adj(sequence, idx, input):
    coord_range = [(idx, idx), (sequence[0], sequence[1])]
    adjacent_values = get_adjacent_values_in_matrix_for_range(input, coord_range)
    result = any(isSymbol(x) for x in adjacent_values)
    return result


def process_line(line_idx: int, input):
    res = 0
    digit_sequences = digit_sequence_indices(input[line_idx])
    for sequence in digit_sequences:
        if has_symbol_adj(sequence, line_idx, input):
            line = input[line_idx]
            start_idx = sequence[0]
            end_idx = sequence[1] + 1
            value_as_string = line[start_idx:end_idx]
            res += int(value_as_string)
    return res


def p1(input):
    total = 0
    for line_idx in range(0, len(input)):
        total += process_line(line_idx, input)
    return total


def main():
    input = read_input_to_list_of_strings("input.txt")
    print("total: ", p1(input))
    
# Facit
# Part 2: 82818007

main()
