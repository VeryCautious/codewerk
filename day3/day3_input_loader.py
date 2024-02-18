from pathlib import Path
from typing import List, Tuple


def get_small_example() -> Tuple[List[int], int]:
    lines = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]
    return (bin_strings_to_numbers(lines), 5)

def get_puzzle_input() -> Tuple[List[int], int]:
    lines = Path('./Day3/puzzle-input.txt').read_text().splitlines()
    return (bin_strings_to_numbers(lines), len(lines[0]))

def bin_strings_to_numbers(lines:List[str]) -> List[int]:
    return [int(line, 2) for line in lines]