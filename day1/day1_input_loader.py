from pathlib import Path
from typing import List

def get_puzzle_input() -> List[int]:
    lines = Path('./Day1/puzzle-input.txt').read_text().splitlines()
    return list(map(int, lines))

def get_small_input() -> List[int]:
    return [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]