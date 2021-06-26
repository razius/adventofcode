import os
import itertools
from operator import mul
from functools import reduce

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, 'input.txt')) as input_file:
    input_content = input_file.read()

dimensions = [[int(j) for j in i.split('x')] for i in input_content.strip().split('\n')]

total_faces_surface = 0
total_ribbon_surface = 0
for sides in dimensions:
    l, w, h = sides
    surfaces = list(map(lambda side: mul(*side), itertools.combinations(sides, 2)))
    total_faces_surface += sum([mul(s, 2) for s in surfaces]) + min(surfaces)
    ribbon_surface = sum(sorted(sides)[:2]) * 2
    bow_surface = reduce(mul, sides)
    total_ribbon_surface += bow_surface + ribbon_surface

print('Part One : ' + str(total_faces_surface))
print('Part Two : ' + str(total_ribbon_surface))
