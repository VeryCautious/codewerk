from day1.day1_solver import count_depth_increases, count_tripple_depth_increases
from day1.day1_input_loader import get_puzzle_input, get_small_input

### Part 1

def test_smallInput_CountDepthIncreases_7():
    expected = 7
    acctual = count_depth_increases(get_small_input())
    assert acctual == expected

def test_puzzleInput_CountDepthIncreases_1616():
    expected = 1616
    acctual = count_depth_increases(get_puzzle_input())
    assert acctual == expected

### Part 2

def test_smallInput_CountTrippleDepthIncreases_5():
    expected = 5
    acctual = count_tripple_depth_increases(get_small_input())
    assert acctual == expected

def test_puzzleInput_CountTrippleDepthIncreases_1645():
    expected = 1645
    acctual = count_tripple_depth_increases(get_puzzle_input())
    assert acctual == expected