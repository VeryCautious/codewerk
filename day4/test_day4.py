
from day4.day4_input_loader import get_puzzle_input, get_small_example
from day4.day4_solver import play


def test_smallInput_play_4512():
    expected = 4512
    games, values = get_small_example()
    actual = play(games, values)
    assert actual == expected

def test_puzzleInput_play_22680():
    expected = 22680
    games, values = get_puzzle_input()
    actual = play(games, values)
    assert actual == expected