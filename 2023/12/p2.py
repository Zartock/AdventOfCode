from ACutils.utils import read_input_to_list_of_strings


from functools import lru_cache
from typing import Tuple


@lru_cache
def find_potential_matches(springs: str, groups: Tuple[int]):
    if len(springs) == 0:
        if len(groups) == 0:
            return 1
        return 0
    if springs.startswith("."):
        # Be gone dots
        return find_potential_matches(springs.strip("."), groups)
    if springs.startswith("?"):
        # Test both options
        return find_potential_matches(springs.replace("?", ".", 1), groups) + find_potential_matches(springs.replace("?", "#", 1), groups)
    if springs.startswith("#"):
        if len(groups) == 0:
            # Nothing more to check
            return 0
        if len(springs) < groups[0]:
            # Can't possible be a match
            return 0
        if any(c == "." for c in springs[0:groups[0]]):
            # if there is a dot in the substring we check
            return 0
        if len(groups) > 1:
            if len(springs) < groups[0] + 1 or springs[groups[0]] == "#":
                return 0
            # group bigger than chunk or chunk to big
            return find_potential_matches(springs[groups[0] + 1:], groups[1:])
        else:
            return find_potential_matches(springs[groups[0]:], groups[1:])

def main():

    input = read_input_to_list_of_strings("input.txt")
    total_arrangements = 0
    for line in input:
        springs, numbers = line.split(" ")
        groups = tuple([int(x) for x in numbers.split(",")])

        springs = "?".join([springs] * 5)
        groups = groups * 5
        total_arrangements += find_potential_matches(springs, groups)
    print(total_arrangements)

main()
