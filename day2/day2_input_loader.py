from pathlib import Path
from typing import List

def get_small_input() -> List[str]:
    return [
        "forward 5",
        "down 5",
        "forward 8",
        "up 3",
        "down 8",
        "forward 2",
    ]

def get_puzzle_input() -> List[str]:
    return Path('./Day2/puzzle-input.txt').read_text().splitlines()