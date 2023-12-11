from ACutils.utils import read_input_to_list_of_strings

from typing import List, Tuple

def get_galaxies(input: List[str]) -> List[Tuple[int, int]]:
    result = []
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == '#':
                result.append((j, i))
    return result


def distance(a, b, doublewide, doublehigh):
    dist = abs(a[0] - b[0]) + abs(a[1] - b[1])
    for x in doublewide:
        if a[0] < x < b[0] or b[0] < x < a[0]:
            dist += 1
    for y in doublehigh:
        if a[1] < y < b[1] or b[1] < y < a[1]:
            dist += 1
    return dist

def main():
    input = read_input_to_list_of_strings("input.txt")
    input = input.split('\n')
    width = len(input[0])
    height = len(input)

    galaxies = get_galaxies(input)
    print(width)
    print(height)
    print(len(galaxies))

    gx = set([x for x, _ in galaxies])
    gy = set([y for _, y in galaxies])

    doublewide = [x for x in range(width) if x not in gx]
    doublehigh = [y for y in range(height) if y not in gy]

    dist = 0
    for i in range(len(galaxies)):
        for j in range(i + 1,len(galaxies)):
            dist += distance(galaxies[i], galaxies[j], doublewide, doublehigh)

    print("Result: ", dist)


main()
