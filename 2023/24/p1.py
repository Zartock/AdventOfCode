from ACutils.utils import read_input_to_list_of_strings, profiler, Pos3D, Pos2D

from typing import List
import numpy as np
from decimal import *


class Hail:
    def __init__(self, position: Pos2D, velocity: Pos2D):
        self.pos = position
        self.vel = velocity
        self.XYslope = Decimal('inf') if self.vel.x == 0 else self.vel.y / self.vel.x
    
    def intersectXY(self, other):
        # returns None, if parallel / intersect in a past
        if self.XYslope == other.XYslope:
            return None
        if self.XYslope == float('inf'): # self is vertical
            intX = self.pos.x
            intY = other.XYslope * (intX - other.pos.x) + other.py
        elif other.XYslope == float('inf'): # other is vertical
            intX = other.pos.x
            intY = self.XYslope * (intX - self.pos.x) + self.pos.y
        else:
            intX = (self.pos.y-other.pos.y  - self.pos.x*self.XYslope + other.pos.x*other.XYslope)/(other.XYslope-self.XYslope)
            intY = self.pos.y + self.XYslope*(intX-self.pos.x)
        #intX, intY = intX.quantize(Decimal(".1")), intY.quantize(Decimal(".1"))

        selfFuture = np.sign(intX-self.pos.x) == np.sign(self.vel.x)
        otherFuture = np.sign(intX-other.pos.x) == np.sign(other.vel.x)
        if not (selfFuture and otherFuture):
            return None
        return Pos2D(intX, intY)


def get_hails(input: List[str]):
    hails = []
    for line in input:
        lhs, rhs = line.split('@')
        left_numbers = [int(num) for num in lhs.split(',')]
        right_numbers = [int(num) for num in rhs.split(',')]
        pos = Pos2D(left_numbers[0], left_numbers[1])
        velo = Pos2D(right_numbers[0], right_numbers[1])
        hail = Hail(pos, velo)
        hails.append(hail)
    return hails


@profiler
def main():
    input = read_input_to_list_of_strings("input.txt")
    hails = get_hails(input)

    pMin = 200000000000000
    pMax = 400000000000000
    # pMin = 7
    # pMax = 27
    count = 0
    for idx, H1 in enumerate(hails):
        for H2 in hails[idx+1:]:
            p = H1.intersectXY(H2)
            if p is None:
                continue
            elif p.x >= pMin and p.x <= pMax and p.y >= pMin and p.y <= pMax:
                count += 1
    print(count)
                
main()