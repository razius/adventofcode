import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, 'input.txt')) as input_file:
    input_content = input_file.read()

current_floor = 0
first_basement = 0
move_floor = lambda i: {'(': 1, ')': -1}.get(i, 0)
for index, char in enumerate(input_content, start=current_floor + 1):
    current_floor += move_floor(char)
    if current_floor < 0 and not first_basement:
        first_basement = index

print('Part One : ' + str(current_floor))
print('Part Two : ' + str(first_basement))
