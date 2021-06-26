import os
from dataclasses import dataclass, field
from collections import Counter
from functools import reduce
from operator import and_, or_

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, 'input.txt')) as input_file:
    input_content = input_file.read()

@dataclass
class Coordinate:
    x: int
    y: int

    def __add__(self, other):
        return Coordinate(x=self.x + other.x, y=self.y + other.y)

    def __eq__(self, other):
        if other.__class__ == self.__class__:
            return self.x == other.x and self.y == other.y
        raise NotImplemented

    def __hash__(self):
        return hash(f'{self.x}:{self.y}')

    def __str__(self):
        return f'{self.x}:{self.y}'

@dataclass
class Santa:
    _current_position: Coordinate = field(default_factory=lambda: Coordinate(0, 0))
    visited_positions: list = field(default_factory=lambda: [])

    @property
    def current_position(self) -> Coordinate:
        return self._current_position

    @current_position.setter
    def current_position(self, position: Coordinate) -> None:

        self._current_position = position
        self.visited_positions.append(position)

movements = {
    '^': Coordinate(0, 1),
    'v': Coordinate(0, -1),
    '>': Coordinate(1, 0),
    '<': Coordinate(-1, 0),
}
get_movement = lambda i: movements.get(i, Coordinate(0, 0))


def get_visited_unique_positions(num_santas):
    santas = [Santa() for i in range(num_santas)]
    for index, movement in enumerate(input_content, start=1):
        santa = santas[index % num_santas]
        santa.current_position += get_movement(movement)
    return reduce(or_, [set(i.visited_positions) for i in santas])

print('Part One : ' + str(len(get_visited_unique_positions(num_santas=1))))
print('Part Two : ' + str(len(get_visited_unique_positions(num_santas=2))))
