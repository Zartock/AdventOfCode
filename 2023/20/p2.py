from collections import defaultdict
from math import prod


modules = dict()
flips = defaultdict(int)
conjs = defaultdict(dict)

for line in open('input.txt'):
    tmp, _, *destination_modules = line.replace(',', '').split()
    prefix, module = (tmp[0], tmp[1:]) if tmp[0] in '%&' else ('', tmp)

    modules[module] = prefix, destination_modules

    for destination in destination_modules:
        conjs[destination][tmp] = 0
        if destination == 'rx': rx = tmp

rx_ins = {i: 0 for i in conjs[rx]}

presses = 0
counts = [0, 0]

while True:
    presses += 1

    if all(rx_ins.values()):
        print(prod(rx_ins.values()))
        break

    queue = [(None, 'broadcaster', 0)]
    while queue:
        source, mod, pulse_in = queue.pop(0)
        counts[pulse_in] += 1

        if mod not in modules: continue
        type, nexts = modules[mod]

        match type, pulse_in:
            case '', _:
                #brodcaster
                pulse_out = pulse_in
            case '%', 0:
                pulse_out = flips[mod] = not flips[mod]
            case '&', _:
                conjs[mod][source] = pulse_in
                pulse_out = not all(conjs[mod].values())

                if 'rx' in nexts:
                    for key, value in conjs[mod].items():
                        if value:
                            rx_ins[key] = presses
            case _,_: continue

        for n in nexts:
            queue.append((mod, n, pulse_out))