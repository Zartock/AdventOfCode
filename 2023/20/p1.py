from collections import defaultdict
from math import prod


modules = dict()
flips = defaultdict(int)
conjs = defaultdict(dict)

for line in open('input.txt'):
    tmp, _, *destination_modules = line.replace(',', '').split()
    prefix, module = (tmp[0], tmp[1:]) if tmp[0] in '%&' else ('', tmp)

    modules[module] = prefix, destination_modules

presses = 0
counts = [0, 0]

while True:
    if presses == 1000:
        print(prod(counts))
        break
    presses += 1

    queue = [(None, 'broadcaster', 0)]
    while queue:
        source, module, pulse_in = queue.pop(0)
        counts[pulse_in] += 1

        if module not in modules:
            continue
        type, nexts = modules[module]

        match type, pulse_in:
            case '', _:
                # broadcaster
                pulse_out = pulse_in
            case '%', 0:
                pulse_out = flips[module] = not flips[module]
            case '&', _:
                conjs[module][source] = pulse_in
                pulse_out = not all(conjs[module].values())
            case _, _:
                continue

        for n in nexts:
            queue.append((module, n, pulse_out))