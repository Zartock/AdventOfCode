from ACutils.utils import read_input_to_list_of_strings

from typing import List, Dict

def get_formatted_input(input: List[str]):
    result = {}
    for i in range(2, len(input)):
        tmp = input[i].split("=")
        tmp_tuple = tmp[1].replace("(","").replace(")","").replace(" ", "").split(',')
        result[tmp[0].strip()] = (tmp_tuple[0], tmp_tuple[1])
    return result


def get_index_for_instruction(instruction):
    if instruction == 'L':
        return 0
    else:
        return 1

def main():
    input = read_input_to_list_of_strings("input.txt")
    instructions = input[0]
    formatted_input = get_formatted_input(input)
    print(formatted_input)

    curr_node = "AAA"
    steps = 0
    found = False

    while not found:
        for c in instructions:
            steps += 1
            curr_node = formatted_input[curr_node][get_index_for_instruction(c)]
            if curr_node == "ZZZ":
                found = True
                break

    print("Result {}".format(steps))
main()