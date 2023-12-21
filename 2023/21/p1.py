from ACutils.utils import read_input_to_string
cardinal_directions = (1, -1, 1j, -1j)
class Grid:
    def __init__(self, input: str):
        self.size = len(input.splitlines())
        self.grid = set()
        self.positions = set()
        for y, l in enumerate(input.splitlines()):
            for x, v in enumerate(l):
                if v == '#':
                    self.grid.add(complex(x, y))
                if v == 'S':
                    self.positions.add(complex(x, y))
    
    def step(self):
        new_positions = set()
        for position in self.positions:
            for direction in cardinal_directions:
                if position + direction not in self.grid:
                    new_positions.add(position + direction)
        self.positions = new_positions

def main():
    input = read_input_to_string("input.txt")
    g = Grid(input)
    for step in range(64):
        g.step()

    print(len(g.positions))

main()



