from pathlib import Path
from typing import List, Tuple

from day4.game import Game


def get_small_example() -> Tuple[List[Game], List[int]]:
    lines = Path('./Day4/small-input.txt').read_text().splitlines()
    return parse_lines(lines)

def get_puzzle_input() -> Tuple[List[Game], List[int]]:
    lines = Path('./Day4/puzzle-input.txt').read_text().splitlines()
    return parse_lines(lines)

def parse_lines(lines: List[str]) -> Tuple[List[Game], List[int]]:
    lines.append('')
    values = [int(v) for v in lines[0].split(',')]
    games = list()

    currentGameLines = list()
    for line in lines[2:]:
        if(line == ''):
            games.append(Game(currentGameLines))
            currentGameLines = list()
            continue
        currentGameLines.append([int(number) for number in line.split(' ') if number != ''])
    
    return (games, values)
