from ACutils.utils import read_input_to_grid_2d


from typing import Tuple, List


def fire(input: List[str], beam: Tuple[Tuple[int, int], Tuple[int, int]]) -> int:
    energized = set()
    beams = [beam]

    while any(beams):
        for i, beam in enumerate(beams):
            if not beam:
                continue
            (x, y), (dx, dy) = beam
            if beam in energized:
                del beams[i]
            else:
                energized.add(beam)
                x += dx
                y += dy
                if min(x, y) < 0 or y >= len(input) or x >= len(input[0]):
                    # out of bounds
                    del beams[i]
                    continue
                cell = input[y][x]
                if cell == '/':
                    dx, dy = -dy, -dx
                elif cell == '\\':
                    dx, dy = dy, dx
                elif cell == '-' and dy:
                    dx, dy = 1, 0
                    beams.append(((x, y), (-1, 0)))
                elif cell == '|' and dx:
                    dx, dy = 0, 1
                    beams.append(((x, y), (0, -1)))
                beams[i] = (x, y), (dx, dy)

    return len({p for p, _ in energized}) - 1


def main():


    input = read_input_to_grid_2d("input.txt")
    print('Result ', fire(input, ((-1, 0), (1, 0))))


main()
