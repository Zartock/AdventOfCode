from ACutils.utils import read_input_to_list_of_strings, Cardinal, CARDINALS

from collections.abc import Iterator

DIRECTIONS = {
    '>': [Cardinal.EAST.value],
    '<': [Cardinal.WEST.value],
    '^': [Cardinal.NORTH.value],
    'v': [Cardinal.SOUTH.value],
    '.': CARDINALS,
}


Pos = tuple[int, int]


def get_neighbors(position: Pos, trail_map: list[str]) -> Iterator[Pos]:
    width = len(trail_map[0])
    height = len(trail_map)
    x, y = position
    for dx, dy in DIRECTIONS[trail_map[y][x]]:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < width and 0 <= new_y < height and trail_map[new_y][new_x] != '#':
            yield new_x, new_y


def get_graph(trail_map: list[str]) -> dict[Pos, list[tuple[Pos, int]]]:
    vertices = [(1, 0)]
    visited = set()
    graph = {}
    while vertices:
        vertex = vertices.pop()
        if vertex in visited:
            continue
        graph[vertex] = []
        for next_step in get_neighbors(vertex, trail_map):
            length = 1
            prev = vertex
            position = next_step
            dead_end = False
            while True:
                neighbors = list(get_neighbors(position, trail_map))
                if neighbors == [prev] and trail_map[position[1]][position[0]] in '<>^v':
                    dead_end = True
                    break
                if len(neighbors) != 2:
                    break
                for neighbor in neighbors:
                    if neighbor != prev:
                        length += 1
                        prev = position
                        position = neighbor
                        break
            if dead_end:
                continue
            graph[vertex].append((position, length))
            vertices.append(position)
        visited.add(vertex)
    return graph


def iter_hike_lengths(graph: dict[Pos, list[tuple[Pos, int]]], goal: Pos) -> Iterator[int]:
    start = (1, 0)
    stack = [(start, 0, {start})]
    while stack:
        last, length, visited = stack.pop()
        if last == goal:
            yield length
            continue
        for new, edge_length in graph[last]:
            if new not in visited:
                stack.append((new, length + edge_length, visited | {new}))


def main():
    trail_map = read_input_to_list_of_strings("input.txt")
    goal = len(trail_map[0]) - 2, len(trail_map) - 1
    graph = get_graph(trail_map)
    print(max(iter_hike_lengths(graph, goal)))


main()