import os
from urllib.parse import urlparse

import fire
import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://adventofcode.com'

SOLUTION_FILE_CONTENT = """import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, 'input.txt')) as input_file:
    input_content = input_file.read()

print('Part One : ' + str(''))
print('Part Two : ' + str(''))
"""


class AdventOfCode(object):

    def __init__(self):
        if not os.environ.get('SESSION_ID'):
            print("""
            Get your session id by inspecting the session cookie content in your web browser
            while connected to adventofcode and add it to a local file .env like so:

            $ cat .env
            SESSION_ID=fe4d236f07d0482db2bd18a9ed49ca33
            """)
            raise Exception('SESSION_ID not found.')
        self.session = requests.Session()
        self.session.cookies.set(
            'session',
            os.environ['SESSION_ID'],
            domain=urlparse(BASE_URL).netloc
        )

    def init_day(self, year, day):
        year = int(year)
        day = int(day)
        day_str = str(day).rjust(2, '0')

        print(f'Initializing year: {year}, day: {day_str}')

        base_dir = f'{year}/{day_str}'
        if not os.path.exists(base_dir):
            os.mkdir(base_dir)

        input_file = f'{base_dir}/input.txt'
        if not os.path.exists(input_file):
            input_url = f'https://adventofcode.com/{year}/day/{day}/input'
            with open(input_file, 'w+') as f:
                f.write(self.session.get(input_url).text)

        puzzle_file = f'{base_dir}/puzzle.html'
        input_url = f'https://adventofcode.com/{year}/day/{day}'
        with open(puzzle_file, 'w+') as f:
            puzzle_content = self.session.get(input_url).text
            soup = BeautifulSoup(puzzle_content, features='html.parser')
            f.write('<p>'.join([str(i) for i in soup.find_all('article')]))

        solution_file = f'{base_dir}/solution.py'
        if not os.path.exists(solution_file):
            with open(solution_file, 'w+') as f:
                f.write(SOLUTION_FILE_CONTENT)

    def init_year(self, year):
        for day in range(1, 26):
            self.init_day(year=year, day=day)


if __name__ == '__main__':
    fire.Fire(AdventOfCode)
