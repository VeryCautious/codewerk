from day3.day3_input_loader import get_puzzle_input, get_small_example
from day3.day3_solver import analyze_data, get_masks


def test_3_getMasks_masks():
    masks = get_masks(3)
    assert masks == [4, 2, 1]

def test_smallExample_getMostCommonBit_198():
    expected = 198
    data, length = get_small_example()
    epsilon, gamma = analyze_data(data, length)
    actual = epsilon * gamma
    assert expected == actual

def test_puzzleInput_getMostCommonBit_3242606():
    expected = 3242606
    data, length = get_puzzle_input()
    epsilon, gamma = analyze_data(data, length)
    actual = epsilon * gamma
    assert expected == actual