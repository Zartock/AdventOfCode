from ACutils.utils import read_input_to_list_of_strings

from typing import List, Dict, Tuple
from math import lcm

def get_formatted_input(input: List[str]) -> Dict[str, Tuple[str, str]]:
    result = {}
    for i in range(2, len(input)):
        tmp = input[i].split("=")
        tmp_tuple = tmp[1].replace("(","").replace(")","").replace(" ", "").split(',')
        result[tmp[0].strip()] = (tmp_tuple[0], tmp_tuple[1])
    return result


def get_index_for_instruction(instruction: str) -> int:
    if instruction == 'L':
        return 0
    else:
        return 1
    
def get_all_start_nodes(formatted_input: Dict[str, Tuple[str, str]]) -> List[str]:
    result = []
    for x in formatted_input:
        if x[2] == 'A':
            result.append(x)
    return result

def main():
    input = read_input_to_list_of_strings("input.txt")
    instructions = input[0]
    formatted_input = get_formatted_input(input)

    nodes = get_all_start_nodes(formatted_input)
    steps = []

    for node in nodes:
        curr_node = node
        found = False
        curr_steps = 0
        while not found:
            for c in instructions:
                curr_steps += 1
                curr_node = formatted_input[curr_node][get_index_for_instruction(c)]
                if curr_node.endswith('Z'):
                    found = True
                    steps.append(curr_steps)
                    break
    
    result = lcm(*( step for step in steps ))


    print("Result {}".format(result))
main()
