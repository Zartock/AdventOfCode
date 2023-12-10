from ACutils.utils import read_input_to_grid_2d

from enum import Enum

from matplotlib.path import Path

class Relativecurr_pos(Enum):
    ABOVE = (0, -1)
    RIGHT = (1, 0)
    BELOW = (0, 1)
    LEFT = (-1, 0)



# def find_start(input: List[str]) -> Tuple[int, int]:
#     char = 'S'
#     for i, row in enumerate(input):
#         for j, col in enumerate(row):
#             if col == char:
#                 return i, j



def main():
    input = read_input_to_grid_2d("input.txt")
    start = (110, 107) # Hard coded x, y
    visited = [start]

    curr_pos = [start[0], start[1] - 1]
    last_move = Relativecurr_pos.ABOVE
    while input[curr_pos[1]][curr_pos[0]] != 'S':
        visited.append([*curr_pos])
        tile = input[curr_pos[1]][curr_pos[0]]
        if tile == "|":
            if last_move == Relativecurr_pos.BELOW:
                curr_pos[1] += 1
            elif last_move == Relativecurr_pos.ABOVE:
                curr_pos[1] -= 1
        elif tile == "-":
            if last_move == Relativecurr_pos.RIGHT:
                curr_pos[0] += 1
            elif last_move == Relativecurr_pos.LEFT:
                curr_pos[0] -= 1
        elif tile == "7":
            if last_move == Relativecurr_pos.RIGHT:
                curr_pos[1] += 1
                last_move = Relativecurr_pos.BELOW
            elif last_move == Relativecurr_pos.ABOVE:
                curr_pos[0] -= 1
                last_move = Relativecurr_pos.LEFT
        elif tile == "J":
            if last_move == Relativecurr_pos.RIGHT:
                curr_pos[1] -= 1
                last_move = Relativecurr_pos.ABOVE
            elif last_move == Relativecurr_pos.BELOW:
                curr_pos[0] -= 1
                last_move = Relativecurr_pos.LEFT
        elif tile == "L":
            if last_move == Relativecurr_pos.LEFT:
                curr_pos[1] -= 1
                last_move = Relativecurr_pos.ABOVE
            elif last_move == Relativecurr_pos.BELOW:
                curr_pos[0] += 1
                last_move = Relativecurr_pos.RIGHT
        elif tile == "F":
            if last_move == Relativecurr_pos.LEFT:
                curr_pos[1] += 1
                last_move = Relativecurr_pos.BELOW
            elif last_move == Relativecurr_pos.ABOVE:
                curr_pos[0] += 1
                last_move = Relativecurr_pos.RIGHT
        else:
            print("HOW DID WE GET HERE!?!?!?!?")
            break
            
    print(len(visited)//2)

    count = 0
    p = Path(visited)
    for y in range(len(input)):
        for x in range(len(input[0])):
            if [x, y] in visited:
                continue
            if p.contains_point((x, y)):
                #print(input[y][x])
                count += 1

    print(len(visited), len(p))
    print(count - 1) # start is not concidered part of the poly, so subtract 1



main()


