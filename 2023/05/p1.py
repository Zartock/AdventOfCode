from ACutils.utils import read_input_to_list_of_strings

from typing import List, Tuple, Dict

def contains_any_letters(s: str):
    return any(c.isalpha() for c in s)

def get_full_map(input: List[str]) -> Dict[str, List[Tuple[int, int, int]]]:
    result = {}
    current_map = ""
    for line in input:
        if not line:
            current_map = ""
            continue
        if contains_any_letters(line):
            current_map = line.split(' ')[0]
            continue
        numbers = line.split(' ')
        try:
            result[current_map].append((int(numbers[0]), int(numbers[1]), int(numbers[2])))
        except KeyError:
            result[current_map] = [(int(numbers[0]), int(numbers[1]), int(numbers[2]))]
    return result


def check_number_in_range(num: int, map_list: List[Tuple[int, int, int]]) -> bool:
    for mapping in map_list:
        if num in range(mapping[1], mapping[1] + mapping[2]):
            return True
    return False



def main():
    input = read_input_to_list_of_strings("input.txt")
    seeds = [int(seed) for seed in input[0].split(' ')[1:]]
    print(seeds)

    the_map = get_full_map(input)
    print("we got map ", the_map)

    for map_name, map_list in the_map.items():
        new_seeds = []

        for seed in seeds:
            if not check_number_in_range(seed, map_list):
                print(f"{seed} stayed {seed}")
                new_seeds.append(seed)
                continue

            for mapping in map_list:
                if seed not in range(mapping[1], mapping[1] + mapping[2]):
                    continue
                else:
                    diff = seed - mapping[1]
                    new_seed = mapping[0] + diff
                    print(f"{seed} became {new_seed}")
                    new_seeds.append(new_seed)
                    break

        seeds = new_seeds

    print(seeds)
    print(f"result: {min(seeds)}")


main()
